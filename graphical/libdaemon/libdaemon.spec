#
# Conditional build:
%bcond_with	static_libs	# don't build static library
#
Summary:	Lightweight C library which eases the writing of UNIX daemons
Name:		libdaemon
Version:	0.14
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz

Patch0:		fix-includes.patch

URL:		http://0pointer.de/lennart/projects/libdaemon/
BuildRequires:	libtool

%description
libdaemon is a lightweight C library which eases the writing of UNIX
daemons.

%package devel
Summary:	Header files and development documentation for libdaemon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains Header files and development documentation for
libdaemon.

%package static
Summary:	Static libdaemon library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libdaemon library.

%prep
%setup -q
%patch0 -p1
%build
%configure \
	--disable-silent-rules \
	--prefix=/usr \
	--localstatedir=/var \
	--disable-lynx \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libdaemon.so.*.*.*
%attr(755,root,root) %{_libdir}/libdaemon.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdaemon.so
%{_libdir}/libdaemon.la
%{_includedir}/%{name}
%{_libdir}/pkgconfig/libdaemon.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdaemon.a
%endif
