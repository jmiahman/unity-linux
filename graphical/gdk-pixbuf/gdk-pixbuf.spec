#
# Conditional build:
%bcond_with	gnome1		# build with libgnomecanvaspixbuf (which requires GNOME)
%bcond_with	static_libs	# don't build static libraries
#
Summary:	Image loading library used with GNOME
Name:		gdk-pixbuf
Version:	2.33.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/2.33/%{name}-%{version}.tar.xz
URL:		http://developer.gnome.org/arch/imaging/gdkpixbuf.html
%{?with_gnome1:BuildRequires:	gnome-libs-devel}
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	rpm-build
BuildRequires:	libxt-devel

%description
The GdkPixBuf library provides a number of features:
 - image loading facilities,
 - rendering of a GdkPixBuf into various formats: drawables (windows,
   pixmaps), GdkRGB buffers,
 - a cache interface.

%package devel
Summary:	Include files for the gdk-pixbuf
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Include files for the gdk-pixbuf.

%package static
Summary:	Static gdk-pixbuf libraries
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gdk-pixbuf libraries.

%package gnome
Summary:	GNOME part of gdk-pixbuf library
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME part of gdk-pixbuf library.

%package gnome-devel
Summary:	GNOME part of gdk-pixbuf library - development files
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description gnome-devel
GNOME part of gdk-pixbuf library - development files.

%package gnome-static
Summary:	GNOME part of gdk-pixbuf library - static version
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}

%description gnome-static
GNOME part of gdk-pixbuf library - static version.

%prep
%setup -q

%build
%configure \
	--disable-gtk-doc \
	--with-x11 \
	--sysconfdir=/etc \
	%{!?with_static_libs:--disable-static} \
	%{!?with_gnome1:--without-gnome} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

# resolve conflict with gtk+2-devel
#%{__mv} $RPM_BUILD_ROOT%{_gtkdocdir}/gdk-pixbuf{,-1.0}

%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf/loaders/lib*.a
%endif

# cleanup non-gnome build
%if %{without gnome}
#%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnomecanvaspixbufConf.sh
#%{__rm} $RPM_BUILD_ROOT%{_gtkdocdir}/gdk-pixbuf-1.0/gnomecanvaspixbuf.html
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	gnome -p /sbin/ldconfig
%postun	gnome -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/gdk-pixbuf-pixdata
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-query-loaders
%attr(755,root,root) %{_libdir}/libgdk_pixbuf-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgdk_pixbuf-2.0.so.*
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib-2.0.so.*
%dir %{_libdir}/gdk-pixbuf-2.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-*.so

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/gdk-pixbuf-2.0
%dir %{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf
%{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf/*.h
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib-2.0.so
%attr(755,root,root) %{_libdir}/libgdk_pixbuf-2.0.so
%attr(755,root,root) %{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir

#%dir %{_gtkdocdir}/gdk-pixbuf-1.0
#%{_gtkdocdir}/gdk-pixbuf-1.0/a*.html
#%{_gtkdocdir}/gdk-pixbuf-1.0/compiling.html
#%{_gtkdocdir}/gdk-pixbuf-1.0/extra-configuration-options.html
#%{_gtkdocdir}/gdk-pixbuf-1.0/gdk-pixbuf-*.html
#%{_gtkdocdir}/gdk-pixbuf-1.0/gdkpixbufloader.html
#%{_gtkdocdir}/gdk-pixbuf-1.0/index.html
#%{_gtkdocdir}/gdk-pixbuf-1.0/license.html
#%{_gtkdocdir}/gdk-pixbuf-1.0/r*.html
#%{_gtkdocdir}/gdk-pixbuf-1.0/x*.html

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdk_pixbuf.a
%{_libdir}/libgdk_pixbuf_xlib.a
%endif

%if %{with gnome1}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecanvaspixbuf.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnomecanvaspixbuf.so.1

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnomecanvaspixbufConf.sh
%attr(755,root,root) %{_libdir}/libgnomecanvaspixbuf.so
%{_libdir}/libgnomecanvaspixbuf.la
%{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf/gnome-canvas-pixbuf.h
#%{_gtkdocdir}/gdk-pixbuf-1.0/gnomecanvaspixbuf.html

%if %{with static_libs}
%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libgnomecanvaspixbuf.a
%endif
%endif
