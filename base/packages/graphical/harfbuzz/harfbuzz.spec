#
# Conditional build:
%bcond_with	tests		# "make check" call

Summary:	HarfBuzz - internationalized text shaping library
Name:		harfbuzz
Version:	1.0.5
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/harfbuzz/release/%{name}-%{version}.tar.bz2
URL:		http://www.freedesktop.org/wiki/HarfBuzz
BuildRequires:	cairo-devel
BuildRequires:	freetype-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	graphite2-devel
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool 
BuildRequires:	pkgconfig
BuildRequires:	sed
Requires:	freetype
Requires:	glib

%description
Internationalized OpenType text layout and rendering library.

%package devel
Summary:	Header files for HarfBuzz library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel
Requires:	glib-devel
Requires:	graphite2-devel
Requires:	libstdc++-devel

%description devel
Header files for HarfBuzz library.

%package gobject
Summary:	Harfbuzz GObject interface
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gobject
Harfbuzz GObject interface.

%description gobject -l pl.UTF-8
Interfejs GObject do biblioteki Harfbuzz.

%package gobject-devel
Summary:	Header files for Harfbuzz GObject interface
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gobject = %{version}-%{release}
Requires:	glib-devel

%description gobject-devel
This is the package containing the header files for Harfbuzz GObject
interface.

%package icu
Summary:	HarfBuzz text shaping library - ICU integration
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description icu
HarfBuzz text shaping library - ICU integration.

%package icu-devel
Summary:	Header file for HarfBuzz ICU library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-icu = %{version}-%{release}
Requires:	libicu-devel

%description icu-devel
Header file for HarfBuzz ICU library.

%package progs
Summary:	HarfBuzz command-line utilities
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo 

%description progs
HarfBuzz command-line utilities.

%prep
%setup -q

# missing dependencies
cat >> src/harfbuzz.pc.in <<EOF
Requires.private: glib-2.0 freetype2 graphite2
EOF

%build
%configure \
	--disable-silent-rules \
	--with-cairo \
	--with-freetype \
	--with-glib \
	--with-gobject \
	--with-graphite2 \
	--with-icu \
	--disable-gtk-doc
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gobject -p /sbin/ldconfig
%postun	gobject -p /sbin/ldconfig

%post	icu -p /sbin/ldconfig
%postun	icu -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libharfbuzz.so.*.*.*
%attr(755,root,root) %{_libdir}/libharfbuzz.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz.so
%dir %{_includedir}/harfbuzz
%{_includedir}/harfbuzz/hb.h
%{_includedir}/harfbuzz/hb-blob.h
%{_includedir}/harfbuzz/hb-buffer.h
%{_includedir}/harfbuzz/hb-common.h
%{_includedir}/harfbuzz/hb-deprecated.h
%{_includedir}/harfbuzz/hb-face.h
%{_includedir}/harfbuzz/hb-font.h
%{_includedir}/harfbuzz/hb-ft.h
%{_includedir}/harfbuzz/hb-glib.h
%{_includedir}/harfbuzz/hb-graphite2.h
%{_includedir}/harfbuzz/hb-ot-font.h
%{_includedir}/harfbuzz/hb-ot-layout.h
%{_includedir}/harfbuzz/hb-ot-shape.h
%{_includedir}/harfbuzz/hb-ot-tag.h
%{_includedir}/harfbuzz/hb-ot.h
%{_includedir}/harfbuzz/hb-set.h
%{_includedir}/harfbuzz/hb-shape-plan.h
%{_includedir}/harfbuzz/hb-shape.h
%{_includedir}/harfbuzz/hb-unicode.h
%{_includedir}/harfbuzz/hb-version.h
%{_libdir}/pkgconfig/harfbuzz.pc

%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-gobject.so.*.*.*
%attr(755,root,root) %{_libdir}/libharfbuzz-gobject.so.0
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib

%files gobject-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-gobject.so
%{_includedir}/harfbuzz/hb-gobject.h
%{_includedir}/harfbuzz/hb-gobject-enums.h
%{_includedir}/harfbuzz/hb-gobject-structs.h
%{_libdir}/pkgconfig/harfbuzz-gobject.pc
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir

%files icu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-icu.so.*.*.*
%attr(755,root,root) %{_libdir}/libharfbuzz-icu.so.0

%files icu-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-icu.so
%{_includedir}/harfbuzz/hb-icu.h
%{_libdir}/pkgconfig/harfbuzz-icu.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hb-ot-shape-closure
%attr(755,root,root) %{_bindir}/hb-shape
%attr(755,root,root) %{_bindir}/hb-view

%changelog
