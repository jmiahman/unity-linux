#
# Conditional build:
%bcond_with	static_libs	# don't build static library
#
Summary:	C library for executing name service queries asynchronously
Name:		libasyncns
Version:	0.8
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libasyncns/%{name}-%{version}.tar.gz
URL:		http://0pointer.de/lennart/projects/libasyncns/
BuildRequires:	libtool

%description
libasyncns is a C library for Linux/Unix for executing name service
queries asynchronously. It is an asynchronous wrapper around
getaddrinfo(3) and getnameinfo(3) from the libc.

In contrast to GNU's asynchronous name resolving API getaddrinfo_a(),
libasyncns does not make use of UNIX signals for reporting completion
of name queries. Instead, the API exports a standard UNIX file
descriptor which may be integerated cleanly into custom main loops.

%package devel
Summary:	Header files for libasyncns library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libasyncns library.

%package static
Summary:	Static libasyncns library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libasyncns library.

%prep
%setup -q

%build
%configure \
	--disable-lynx \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libasyncns.so.*.*.*
%attr(755,root,root) %{_libdir}/libasyncns.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasyncns.so
%{_libdir}/libasyncns.la
%{_includedir}/asyncns.h
%{_libdir}/pkgconfig/libasyncns.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libasyncns.a
%endif

%changelog
