%define         _pkgconfigdir   %{_libdir}/pkgconfig
%define         _aclocaldir     %{_datadir}/aclocal
%define		_sysconfdir	/etc
#
# Conditional build:
%bcond_with	apidocs		# gtk-doc build
%bcond_with	cloudprint	# cloudprint print backend
%bcond_with	cups		# CUPS print backend
%bcond_with	papi		# PAPI print backend
%bcond_with	broadway	# Broadway target
%bcond_with	mir		# Mir target
%bcond_without	wayland		# Wayland target
%bcond_with	static_libs	# static library build

Summary:	The GIMP Toolkit
Name:		gtk+3
Version:	3.18.4
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk+/3.18/gtk+-%{version}.tar.xz
#Patch0:		%{name}-papi.patch
URL:		http://www.gtk.org/
BuildRequires:	at-spi2-atk-devel
BuildRequires:	atk-devel 
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-gobject-devel
#BuildRequires:	colord-devel
%if %{with cups} || %{with papi}
BuildRequires:	cups-devel
%endif
BuildRequires:	docbook-xml
BuildRequires:	docbook-xsl
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
%if %{with apidocs}
BuildRequires:	gtk-doc
BuildRequires:	gtk-doc-automake
%endif
%{?with_cloudprint:BuildRequires:	json-glib-devel}
BuildRequires:	libepoxy-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2
BuildRequires:	libxslt
%{?with_mir:BuildRequires:	mir-devel}
BuildRequires:	pango-devel
%{?with_papi:BuildRequires:	papi-devel}
BuildRequires:	perl
BuildRequires:	pkgconfig
%{?with_cloudprint:BuildRequires:	rest-devel}
#BuildRequires:	rpm-pythonprov
BuildRequires:	rpm-build
BuildRequires:	sqlite-devel
BuildRequires:	tar
BuildRequires:	libx11-devel >= 1.5.0
BuildRequires:	libxcomposite-devel
BuildRequires:	libxcursor-devel
BuildRequires:	libxdamage-devel
BuildRequires:	libxext-devel
BuildRequires:	libxfixes-devel
BuildRequires:	libxft-devel
BuildRequires:	libxi-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxrender-devel
BuildRequires:	xz
%{?with_broadway:BuildRequires:	zlib-devel}
%if %{with wayland}
# wayland-client, wayland-cursor
BuildRequires:	wayland-devel
BuildRequires:	libxkbcommon-devel >= 0.2.0
%endif
Requires:	libx11
Requires(post,postun):	glib
Requires:	atk 
Requires:	cairo-gobject
Requires:	gdk-pixbuf
Requires:	glib
Requires:	libepoxy
Requires:	pango
Requires:	libxi
Requires:	libxrandr
%if %{with wayland}
Requires:	libwayland-server
Requires:	libxkbcommon
%endif
%if %{with cups}
Suggests:	%{name}-cups = %{version}-%{release}
%endif

%define		abivers	3.0.0

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		pqext		-%{libext}
%else
%define		pqext		%{nil}
%endif

%description
GTK+, which stands for the GIMP ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach. GDK (part of GTK+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and GTK is a widget set for
creating user interfaces.

%package -n gtk-update-icon-cache
Summary:	Utility to update icon cache used by GTK+ library
Group:		Applications/System
Requires:	gdk-pixbuf
Requires:	glib

%description -n gtk-update-icon-cache
Utility to update icon cache used by GTK+ library.

%package devel
Summary:	GTK+ header files and development documentation
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	at-spi2-atk-devel
Requires:	atk-devel
Requires:	cairo-gobject-devel
Requires:	gdk-pixbuf-devel
Requires:	glib-devel
Requires:	pango-devel

%description devel
Header files and development documentation for the GTK+ libraries.

%package static
Summary:	GTK+ static libraries
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GTK+ static libraries.

%package apidocs
Summary:	GTK+ API documentation
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
GTK+ API documentation.

%package examples
Summary:	GTK+ - example programs
Group:		X11/Development/Libraries
Requires(post,postun):	glib
Requires:	%{name}-devel = %{version}-%{release}

%description examples
GTK+ - example programs.

%package cloudprint
Summary:	Cloudprint printing module for GTK+
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description cloudprint
Cloudprint printing module for GTK+.

%package cups
Summary:	CUPS printing module for GTK+
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description cups
CUPS printing module for GTK+.

%package papi
Summary:	PAPI printing module for GTK+
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	papi

%description papi
PAPI printing module for GTK+.

%prep
%setup -q -n gtk+-%{version}
#%patch0 -p1

# for packaging clean examples
# TODO: add am patch to do it like demos/gtk-demo via some configurable dir
# NOTE: make install so far installs only demos/gtk-demo
install -d _examples
cp -a demos examples _examples

# upstream used too new wayland for make dist in 3.10.6 - force regeneration
touch gdk/wayland/protocol/gtk-shell.xml

%build
CPPFLAGS="%{?with_papi: -I/usr/include/papi}"
%{?with_apidocs:%{__gtkdocize}}
%configure \
	--disable-silent-rules \
	%{!?with_cloudprint:--disable-cloudprint} \
	%{!?with_cups:--disable-cups} \
	%{!?with_papi:--disable-papi} \
	%{?debug:--enable-debug=yes} \
	%{!?with_apidocs:--disable-gtk-doc --disable-man} \
	%{!?with_static:--disable-static-libs} \
	%{?with_broadway:--enable-broadway-backend} \
	%{?with_mir:--enable-mir-backend} \
	%{?with_wayland:--enable-wayland-backend} \
	--enable-x11-backend \
	--enable-xinerama \
	--enable-xkb \
	--with-html-dir=%{_gtkdocdir}

sed -i 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
%{__make} \
#	democodedir=%{_examplesdir}/%{name}-%{version}/demos/gtk-demo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{abivers}/engines
install -d $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{abivers}/theming-engines

%{__make} install \
	democodedir=%{_examplesdir}/%{name}-%{version}/demos/gtk-demo \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{abivers}/gtk.immodules
install -d $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/modules

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a _examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# shut up check-files (static modules and *.la for modules)
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{abivers}/*/*.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{abivers}/*/*.a}

%if "%{_lib}" != "lib"
# We need to have 32-bit and 64-bit binaries as they have hardcoded LIBDIR.
# (needed when multilib is used)
mv $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-3.0{,%{pqext}}
%endif

%{__mv} $RPM_BUILD_ROOT%{_localedir}/sr@ije \
	$RPM_BUILD_ROOT%{_localedir}/sr@ijekavian
# unsupported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/io

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%{!?with_apidocs:%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}/gdk3}
%{!?with_apidocs:%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}/gtk3}

%clean
rm -rf $RPM_BUILD_ROOT

%post
#/sbin/ldconfig
#%glib_compile_schemas
#umask 022
#%{_bindir}/gtk-query-immodules-3.0%{pqext} --update-cache
#exit 0

%postun
#/sbin/ldconfig
#if [ "$1" != "0" ]; then
#	umask 022
#	%{_bindir}/gtk-query-immodules-3.0%{pqext} --update-cache
#else
#	%glib_compile_schemas
#fi
#exit 0

%post examples
#%glib_compile_schemas

%postun examples
#%glib_compile_schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{?with_broadway:%attr(755,root,root) %{_bindir}/broadwayd}
%attr(755,root,root) %{_bindir}/gtk-launch
%attr(755,root,root) %{_bindir}/gtk-query-immodules-3.0%{pqext}
%attr(755,root,root) %{_libdir}/libgailutil-3.so.*.*.*
%attr(755,root,root) %{_libdir}/libgailutil-3.so.0
%attr(755,root,root) %{_libdir}/libgdk-3.so.*.*.*
%attr(755,root,root) %{_libdir}/libgdk-3.so.0
%attr(755,root,root) %{_libdir}/libgtk-3.so.*.*.*
%attr(755,root,root) %{_libdir}/libgtk-3.so.0

%dir %{_libdir}/gtk-3.0
%dir %{_libdir}/gtk-3.0/modules
%dir %{_libdir}/gtk-3.0/%{abivers}
%dir %{_libdir}/gtk-3.0/%{abivers}/engines
%dir %{_libdir}/gtk-3.0/%{abivers}/theming-engines
%dir %{_libdir}/gtk-3.0/%{abivers}/immodules
%dir %{_libdir}/gtk-3.0/%{abivers}/printbackends
%{_libdir}/gtk-3.0/%{abivers}/gtk.immodules
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/printbackends/libprintbackend-file.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/printbackends/libprintbackend-lpr.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-am-et.so
%{?with_broadway:%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-broadway.so}
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-cedilla.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-cyrillic-translit.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-inuktitut.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-ipa.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-multipress.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-thai.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-ti-er.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-ti-et.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-viqr.so
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/immodules/im-xim.so
%{_libdir}/girepository-1.0/Gdk-3.0.typelib
%{_libdir}/girepository-1.0/GdkX11-3.0.typelib
%{_libdir}/girepository-1.0/Gtk-3.0.typelib

%dir %{_sysconfdir}/gtk-3.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk-3.0/im-multipress.conf
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%dir %{_datadir}/themes
%dir %{_datadir}/themes/Default
%dir %{_datadir}/themes/Default/gtk-3.0
%{_datadir}/themes/Default/gtk-3.0/gtk-keys.css
%dir %{_datadir}/themes/Emacs
%dir %{_datadir}/themes/Emacs/gtk-3.0
%{_datadir}/themes/Emacs/gtk-3.0/gtk-keys.css
%{?with_broadway:%{_mandir}/man1/broadwayd.1*}
%{_mandir}/man1/gtk-launch.1*
%{_mandir}/man1/gtk-query-immodules-3.0.1*

%files -n gtk-update-icon-cache
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk-encode-symbolic-svg
%attr(755,root,root) %{_bindir}/gtk-update-icon-cache
%{_mandir}/man1/gtk-encode-symbolic-svg.1*
%{_mandir}/man1/gtk-update-icon-cache.1*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/gtk-builder-tool
%attr(755,root,root) %{_libdir}/libgailutil-3.so
%attr(755,root,root) %{_libdir}/libgdk-3.so
%attr(755,root,root) %{_libdir}/libgtk-3.so
%{_includedir}/gail-3.0
%{_includedir}/gtk-3.0
%{_aclocaldir}/gtk-3.0.m4
%{_pkgconfigdir}/gail-3.0.pc
%{_pkgconfigdir}/gdk-3.0.pc
%{_pkgconfigdir}/gdk-x11-3.0.pc
%{_pkgconfigdir}/gtk+-3.0.pc
%{_pkgconfigdir}/gtk+-unix-print-3.0.pc
%{_pkgconfigdir}/gtk+-x11-3.0.pc
%if %{with broadway}
%{_pkgconfigdir}/gdk-broadway-3.0.pc
%{_pkgconfigdir}/gtk+-broadway-3.0.pc
%endif
%if %{with mir}
%{_pkgconfigdir}/gdk-mir-3.0.pc
%{_pkgconfigdir}/gtk+-mir-3.0.pc
%endif
%if %{with wayland}
%{_pkgconfigdir}/gdk-wayland-3.0.pc
%{_pkgconfigdir}/gtk+-wayland-3.0.pc
%endif
%{_datadir}/gtk-3.0
%{_datadir}/gir-1.0/Gdk-3.0.gir
%{_datadir}/gir-1.0/GdkX11-3.0.gir
%{_datadir}/gir-1.0/Gtk-3.0.gir
%{_mandir}/man1/gtk-builder-tool.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgailutil-3.a
%{_libdir}/libgdk-3.a
%{_libdir}/libgtk-3.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gail-libgail-util3
%{_gtkdocdir}/gdk3
%{_gtkdocdir}/gtk3
%endif

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk3-demo
%attr(755,root,root) %{_bindir}/gtk3-demo-application
%attr(755,root,root) %{_bindir}/gtk3-icon-browser
%attr(755,root,root) %{_bindir}/gtk3-widget-factory
%{_datadir}/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml
%{_desktopdir}/gtk3-demo.desktop
%{_desktopdir}/gtk3-icon-browser.desktop
%{_desktopdir}/gtk3-widget-factory.desktop
%{_iconsdir}/hicolor/*/apps/gtk3-demo-symbolic.symbolic.png
%{_iconsdir}/hicolor/*/apps/gtk3-demo.png
%{_iconsdir}/hicolor/*/apps/gtk3-widget-factory-symbolic.symbolic.png
%{_iconsdir}/hicolor/*/apps/gtk3-widget-factory.png
%{_mandir}/man1/gtk3-demo.1*
%{_mandir}/man1/gtk3-demo-application.1*
%{_mandir}/man1/gtk3-icon-browser.1*
%{_mandir}/man1/gtk3-widget-factory.1*
%{_examplesdir}/%{name}-%{version}

%if %{with cloudprint}
%files cloudprint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/printbackends/libprintbackend-cloudprint.so
%endif

%if %{with cups}
%files cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/printbackends/libprintbackend-cups.so
%endif

%if %{with papi}
%files papi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/%{abivers}/printbackends/libprintbackend-papi.so
%endif
