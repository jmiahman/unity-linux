%bcond_with     static_libs     # don't build static library
%define 	_sysconfdir	/etc

Summary:	Abstraction layer for touchscreen panel event
Name:		tslib
Version:	1.1
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	https://github.com/kergoth/tslib/archive/%{version}/%{name}-%{version}.tar.gz
URL:		http://tslib.berlios.de/
BuildRequires:	libtool

%description
tslib is an abstraction layer for touchscreen panel events, as well as
a filter stack for the manipulation of those events. It was created by
Russell King, of arm.linux.org.uk. Examples of implemented filters
include jitter smoothing and the calibration transform.

tslib is generally used on embedded devices to provide a common user
space interface to touchscreen functionality. It is supported by
Kdrive (aka TinyX) and OPIE as well as being used on a number of
commercial Linux devices including the Nokia 770.

%package devel
Summary:	Header files for tslib library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tslib library.

%package static
Summary:	Static tslib library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tslib library.

%prep
%setup -q

%build
%{__libtoolize}
aclocal -I m4/internal
%{__autoconf}
%{__autoheader}
automake --add-missing
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ts/*.*a
# obsoleted by pkg-config, but keep for now for other existing *.la
#%{__rm} $RPM_BUILD_ROOT%{_libdir}/libts.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ts_calibrate
%attr(755,root,root) %{_bindir}/ts_harvest
%attr(755,root,root) %{_bindir}/ts_print
%attr(755,root,root) %{_bindir}/ts_print_raw
%attr(755,root,root) %{_bindir}/ts_test
%attr(755,root,root) %{_libdir}/libts-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libts-1.0.so.0
%dir %{_libdir}/ts
%attr(755,root,root) %{_libdir}/ts/*.so
%config(noreplace) %{_sysconfdir}/ts.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libts.so
%{_libdir}/libts.la
%{_includedir}/tslib.h
%{_libdir}/pkgconfig/tslib.pc
%{_libdir}/pkgconfig/tslib-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libts.a
%endif

%changelog
