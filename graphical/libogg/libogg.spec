#
# Conditional build:
%bcond_with	static_libs	# don't build static library
#
Summary:	Ogg Bitstream Library
Name:		libogg
Version:	1.3.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.xz
URL:		http://www.xiph.org/ogg/
BuildRequires:	libtool
BuildRequires:	tar
BuildRequires:	xz

%description
Libogg is a library for manipulating Ogg bitstreams. It handles both
making Ogg bitstreams and getting packets from Ogg bitstreams.

%package devel
Summary:	Ogg Bitstream Library Development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%package static
Summary:	Ogg Bitstream Static Library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The libogg-static package contains the static libraries of libogg.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_datadir}/aclocal

mv -f $RPM_BUILD_ROOT%{_datadir}/doc/%{name} devel-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING README
%attr(755,root,root) %{_libdir}/libogg.so.*.*.*
%attr(755,root,root) %{_libdir}/libogg.so.0

%files devel
%defattr(644,root,root,755)
%doc devel-docs/*
%attr(755,root,root) %{_libdir}/libogg.so
%{_libdir}/libogg.la
%{_includedir}/ogg
%{_datadir}/aclocal/ogg.m4
%{_libdir}/pkgconfig/ogg.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libogg.a
%endif
