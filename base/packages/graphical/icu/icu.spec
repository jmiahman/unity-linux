#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%define _pkgconfigdir %{_libdir}/pkgconfig

%define		ver	%(echo %{version} | tr . _)
Summary:	International Components for Unicode
Name:		icu
Version:	55.1
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	http://download.icu-project.org/files/icu4c/%{version}/%{name}4c-%{ver}-src.tgz

Patch1:		CVE-2015-1270.patch 
Patch2:		icu-timezone.patch
Patch3:		ac264-hack.patch

URL:		http://www.icu-project.org/
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
Requires:	libicu = %{version}-%{release}

%description
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides
calendar support, conversions for many character sets, language
sensitive collation, date and time formatting, support for many
locales, message catalogs and resources, message formatting,
normalization, number and currency formatting, time zones support,
transliteration, word, line and sentence breaking, etc.

This package contains the Unicode character database and derived
properties, along with converters and time zones data.

%package -n libicu
Summary:	International Components for Unicode (libraries)
Group:		Libraries

%description -n libicu
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the runtime
libraries for ICU. It does not contain any of the data files needed at
runtime and present in the `icu' package.

%package -n libicu-devel
Summary:	International Components for Unicode (development files)
Group:		Development/Libraries
Requires:	libicu = %{version}-%{release}

%description -n libicu-devel
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the development
files for ICU.

%package -n libicu-static
Summary:	International Components for Unicode (static libraries)
Group:		Development/Libraries
Requires:	libicu-devel = %{version}-%{release}

%description -n libicu-static
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the static 
libraries for ICU.

%prep
%setup -q -n %{name}
%patch1 -p0
%patch2 -p0
%patch3 -p1

%build
cd source
%{__autoconf}
%configure \
	--sbindir=%{_bindir} \
	--with-data-packaging=library \
	%{?with_static_libs:--enable-static} \
	--disable-samples

%{__make} \
	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT

for f in icu-i18n icu-io icu-le icu-lx icu-uc ; do
sed -i \
	-e 's/\$(THREADSCXXFLAGS)//' \
	-e 's/\$(THREADSCFLAGS)//' \
	-e 's/\$(THREADSCPPFLAGS)/-D_REENTRANT/' $RPM_BUILD_ROOT%{_pkgconfigdir}/${f}.pc
done

# help rpm to generate deps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

# rpm is too stupid sometimes and fails on symlinks to symlinked resources
# (reporting unresolved dependency at install time)
for f in Makefile.inc pkgdata.inc ; do
	ln -sf %{version}/${f} $RPM_BUILD_ROOT%{_libdir}/%{name}/${f}
done

%{__rm} $RPM_BUILD_ROOT%{_datadir}/icu/%{version}/license.html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libicu -p /sbin/ldconfig
%postun	-n libicu -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc license.html readme.html
%attr(755,root,root) %{_bindir}/derb
%attr(755,root,root) %{_bindir}/gen*
%attr(755,root,root) %{_bindir}/icuinfo
%attr(755,root,root) %{_bindir}/icupkg
%attr(755,root,root) %{_bindir}/makeconv
%attr(755,root,root) %{_bindir}/pkgdata
%attr(755,root,root) %{_bindir}/uconv
%{_mandir}/man1/derb.1*
%{_mandir}/man1/gen*.1*
%{_mandir}/man1/makeconv.1*
%{_mandir}/man1/pkgdata.1*
%{_mandir}/man1/uconv.1*
%{_mandir}/man8/gen*.8*
%{_mandir}/man8/icupkg.8*

%files -n libicu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libicu*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libicu*.so.55

%files -n libicu-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/icu-config
%attr(755,root,root) %{_libdir}/libicu*.so
%{_pkgconfigdir}/icu-i18n.pc
%{_pkgconfigdir}/icu-io.pc
%{_pkgconfigdir}/icu-le.pc
%{_pkgconfigdir}/icu-lx.pc
%{_pkgconfigdir}/icu-uc.pc
%{_includedir}/unicode
%{_includedir}/layout
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.inc
%dir %{_libdir}/%{name}/current
%dir %{_libdir}/%{name}/%{version}
%{_libdir}/%{name}/%{version}/*.inc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/config
%attr(755,root,root) %{_datadir}/%{name}/%{version}/install-sh
%attr(755,root,root) %{_datadir}/%{name}/%{version}/mkinstalldirs
%{_mandir}/man1/icu-config.1*

%if %{with static_libs}
%files -n libicu-static
%defattr(644,root,root,755)
%{_libdir}/libicu*.a
%endif
