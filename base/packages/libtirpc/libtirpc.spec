%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64
%define _lib /lib64

Summary:	Transport Independent RPC Library
Name:		libtirpc
Version:	0.3.2
Release:	0
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libtirpc/%{name}-%{version}.tar.bz2
Source1:	nis.h
Patch0:		musl-fixes.patch

URL:		http://sourceforge.net/projects/libtirpc/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	musl-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	musl

%description
This package contains SunLib's implementation of transport-independent
RPC (TI-RPC) documentation. This library forms a piece of the base of
Open Network Computing (ONC), and is derived directly from the Solaris
2.3 source.

TI-RPC is an enhanced version of TS-RPC that requires the UNIX System
V Transport Layer Interface (TLI) or an equivalent X/Open Transport
Interface (XTI). TI-RPC is on-the-wire compatible with the TS-RPC,
which is supported by almost 70 vendors on all major operating
systems. TS-RPC source code (RPCSRC 4.0) remains available from
several Internet sites.

%package devel
Summary:	Development files for the TI-RPC library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	musl-devel

%description devel
This package includes header files necessary for developing programs
which use the TI-RPC library.

%package static
Summary:	Static TI-RPC library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package includes static TI-RPC library.

%prep
%setup -q
%patch0 -p1

%build
mkdir src/rpcsvc
cp %{SOURCE1} src/rpcsvc/
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-gssapi \
	--disable-static \
	--sysconf=/etc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sysconfdir}
install -d $RPM_BUILD_ROOT/%{_lib}
install -d $RPM_BUILD_ROOT/%{_mandir}/man3
install -d $RPM_BUILD_ROOT/%{_mandir}/man5
install -d $RPM_BUILD_ROOT/%{_includedir}/rpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C doc install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libtirpc.so.* $RPM_BUILD_ROOT/%{_lib}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtirpc.so
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib}; echo lib*.so.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libtirpc.so

# Provide rpc/rpc.h
ln -sf %{_includedir}/tirpc/rpc/*.h $RPM_BUILD_ROOT%{_includedir}/rpc/
ln -sf %{_includedir}/tirpc/netconfig.h $RPM_BUILD_ROOT%{_includedir}/

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtirpc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/netconfig
%attr(755,root,root) /%{_lib}/libtirpc.so.*.*
%attr(755,root,root) /%{_lib}/libtirpc.so.1
%{_mandir}/man5/netconfig.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtirpc.so
%{_includedir}/netconfig.h
%{_includedir}/tirpc
%{_includedir}/rpc
%{_libdir}/pkgconfig/libtirpc.pc
%{_mandir}/man3/bindresvport.3t*
%{_mandir}/man3/des_crypt.3t*
%{_mandir}/man3/getnet*.3t*
%{_mandir}/man3/getrpc*.3t*
%{_mandir}/man3/rpc*.3t*
%{_mandir}/man3/rtime.3t*

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libtirpc.a

%changelog
