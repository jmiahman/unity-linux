#
# Conditional build:
%bcond_with	apidocs		# disable gtk-doc
%bcond_with	libthai		# don't build thai-lang module
%bcond_with	static_libs	# don't build static library
#
Summary:	System for layout and rendering of internationalized text
Name:		pango
Version:	1.38.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pango/1.38/%{name}-%{version}.tar.xz
URL:		http://www.pango.org/
BuildRequires:	cairo-devel
BuildRequires:	cairo-gobject-devel
BuildRequires:	docbook-xml
BuildRequires:	docbook-xsl
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	glib-devel 
BuildRequires:	gobject-introspection-devel
%if %{with apidocs}
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	gtk-doc-automake >= 1.8
%endif
BuildRequires:	harfbuzz-devel >= 0.9.30
%{?with_libthai:BuildRequires:	libthai-devel}
BuildRequires:	libtool
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	rpm-build
BuildRequires:	tar
BuildRequires:	libx11-devel
BuildRequires:	libxft-devel
BuildRequires:	xz
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	glib 
Requires:	harfbuzz

%description
System for layout and rendering of internationalized text.

%package view
Summary:	Pango text viewer
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description view
Pango text viewer.

%package devel
Summary:	Header files for Pango libraries
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel
Requires:	fontconfig-devel
Requires:	freetype-devel
Requires:	glib-devel
Requires:	harfbuzz-devel
%{?with_libthai:Requires:	libthai-devel}
Requires:	libx11-devel
Requires:	libxft-devel >= 2.1.0

%description devel
Header files for Pango libraries.

%package static
Summary:	Static pango libraries
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pango libraries.

%package modules
Summary:	Pango modules for various scripts
Group:		X11/Development/Libraries
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
%{?with_libthai:Requires:	libthai >= 0.1.9}

%description modules
Pango is a system for layout and rendering of internationalized text.

This package contains pango modules for: arabic, bengali, devanagari,
gujarati, gurmukhi, hangul, hebrew, indic, myanmar, tamil, thai.

%package apidocs
Summary:	Pango API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Pango API documentation.

%package examples
Summary:	pango - example programs
Group:		X11/Development/Libraries

%description examples
pango - example programs.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--enable-debug=%{?debug:yes}%{!?debug:minimum} \
	--disable-gtk-docs \
	--disable-static \
	--with-included-modules=basic-fc \
	--localstatedir=/var \

# some generator script requires access to newely created .pc files
export PKG_CONFIG_PATH="$PWD"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

cp examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/pango}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS
%attr(755,root,root) %{_libdir}/libpango-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libpango-1.0.so.0
%attr(755,root,root) %{_libdir}/libpangocairo-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libpangocairo-1.0.so.0
%attr(755,root,root) %{_libdir}/libpangoft2-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libpangoft2-1.0.so.0
%attr(755,root,root) %{_libdir}/libpangoxft-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libpangoxft-1.0.so.0
%{_libdir}/girepository-1.0/Pango*-1.0.typelib

%files view
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pango-view
%{_mandir}/man1/pango-view.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpango-1.0.so
%attr(755,root,root) %{_libdir}/libpangocairo-1.0.so
%attr(755,root,root) %{_libdir}/libpangoft2-1.0.so
%attr(755,root,root) %{_libdir}/libpangoxft-1.0.so
%{_libdir}/libpango-1.0.la
%{_libdir}/libpangocairo-1.0.la
%{_libdir}/libpangoft2-1.0.la
%{_libdir}/libpangoxft-1.0.la
%{_pkgconfigdir}/pango.pc
%{_pkgconfigdir}/pangocairo.pc
%{_pkgconfigdir}/pangoft2.pc
%{_pkgconfigdir}/pangoxft.pc
%{_includedir}/pango-1.0
%{_datadir}/gir-1.0/Pango*-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpango-1.0.a
%{_libdir}/libpangocairo-1.0.a
%{_libdir}/libpangoft2-1.0.a
%{_libdir}/libpangoxft-1.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pango
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
