%bcond_with     static_libs     # static library
%define _pkgconfigdir	%{_libdir}/pkgconfig

Summary:	Nettle - a cryptographic library
Name:		nettle
Version:	2.7.1
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz
# Source0-md5:	003d5147911317931dd453520eb234a5
Patch0:		%{name}-2.4-makefile.patch
URL:		http://www.lysator.liu.se/~nisse/nettle/
BuildRequires:	gmp-devel >= 3.1
BuildRequires:	m4
Requires:	gmp

%description
Nettle is a cryptographic library that is designed to fit easily in
more or less any context: In crypto toolkits for object-oriented
languages (C++, Python, Pike, ...), in applications like LSH or GNUPG,
or even in kernel space. Nettle does only one thing, the low-level
crypto stuff, providing simple but general interface to it. In
particular, Nettle doesn't do algorithm selection. It doesn't do
memory allocation. It doesn't do any I/O. All these is up to
application.

%package devel
Summary:	Header files for nettle library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nettle library.

%package static
Summary:	Static nettle library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nettle library.

%prep
%setup -q
%patch0 -p1

%build
LIBS="-lgmp" %configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-openssl-compatibility \
	--disable-rpath \
	%{?with_static_libs:--enable-static} \
	--disable-guile \
	--disable-valgrind-tests \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%post	devel -p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

#%postun	devel -p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/nettle-hash
%attr(755,root,root) %{_bindir}/nettle-lfib-stream
%attr(755,root,root) %{_bindir}/pkcs1-conv
%attr(755,root,root) %{_bindir}/sexp-conv
%attr(755,root,root) %{_libdir}/libhogweed.so.*.*
%attr(755,root,root) %{_libdir}/libhogweed.so.2
%attr(755,root,root) %{_libdir}/libnettle.so.*.*
%attr(755,root,root) %{_libdir}/libnettle.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhogweed.so
%attr(755,root,root) %{_libdir}/libnettle.so
%{_includedir}/nettle
%{_pkgconfigdir}/hogweed.pc
%{_pkgconfigdir}/nettle.pc
%{_infodir}/nettle.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libhogweed.a
%{_libdir}/libnettle.a
%endif

%changelog
