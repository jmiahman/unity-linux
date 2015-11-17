# TODO: clutter (requires .pc: clutter-1.0 clutter-imcontext-0.1)
#
# Conditional build:
%bcond_with	gtk2ui		# build GTK+ 2.x based gtkutils and setup
%bcond_with	clutter		# Clutter IMModule
%bcond_with	gtk2		# GTK+ 2.x IMModule
%bcond_with	qt3		# Qt 3.x IMModule
%bcond_with	qt4		# Qt 4.x IMModule
#
Summary:	Smart Common Input Method
Name:		scim
Version:	1.4.14
Release:	3
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	495fbd080d9d6189e7eb67fd61097324
Source1:	%{name}.xinputd
Patch0:		%{name}-config.patch
URL:		http://www.scim-im.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
%{?with_clutter:BuildRequires:	clutter-devel >= 1.0.0}
%{?with_clutter:BuildRequires:	clutter-imcontext-devel >= 0.1}
BuildRequires:	gettext >= 0.14.1
BuildRequires:	gdk-pixbuf-devel >= 2.4.0
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.4.0}
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2.0
BuildRequires:	pango-devel >= 1.1.0
BuildRequires:	pkgconfig
%{?with_qt3:BuildRequires:	qt-devel >= 3}
BuildRequires:	xorg-lib-libX11-devel
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4.0
BuildRequires:	QtGui-devel >= 4.0
BuildRequires:	qt4-build >= 4.0
%endif
Requires:	%{name}-libs = %{version}-%{release}
Requires:	im-chooser
Requires:	imsettings

%define		abiver		1.4.0
%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		gtk2confdir	%{_sysconfdir}/gtk%{libext}-2.0
%define		gtkpqext	-%{libext}
%else
%define		gtk2confbase	%{_sysconfdir}/gtk-2.0
%define		gtkpqext	%{nil}
%endif

%description
scim is the core package of the SCIM project, which provides the
fundamental routines and data types. A GTK+ 2 based Panel (User
Interface) and setup dialog are also shipped within this package.

%package libs
Summary:	Smart Common Input Method libraries
Group:		X11/Libraries
Requires:	gtk+2 >= 2:2.4.0
Requires:	pango >= 1.1.0

%description libs
Smart Common Input Method libraries.

%description libs -l pl.UTF-8
Biblioteki Smart Common Input Method.

%package devel
Summary:	Header files for SCIM libraries
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for SCIM libraries.

%package static
Summary:	Static SCIM libraries
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SCIM libraries.

%package clutter
Summary:	Smart Common Input Method Clutter IM module
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description clutter
This package provides a Clutter input method module for SCIM.

%package gtk2
Summary:	Smart Common Input Method GTK+ 2.x IM module
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2
Requires(post,postun):	gtk+2

%description gtk2
This package provides a GTK+ 2.x input method module for SCIM.

%package gtk3
# or -n gtk+3-im-scim?
Summary:	Smart Common Input Method GTK+ 3.x IM module
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3
Requires(post,postun):	gtk+3

%description gtk3
This package provides a GTK+ 3.x input method module for SCIM.

%package qt3
# or -n qt-plugin-im-scim?
Summary:	Smart Common Input Method Qt 3.x IM module
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	qt >= 3

%description qt3
This package provides a Qt 3.x input method module for SCIM.

%package qt4
# or -n qt4-plugin-im-scim?
Summary:	Smart Common Input Method Qt 4.x IM module
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui >= 4

%description qt4
This package provides a Qt 4.x input method module for SCIM.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_clutter:--disable-clutter-immodule} \
	%{!?with_gtk2:--disable-gtk2-immodule} \
	--enable-ld-version-script \
	%{!?with_qt3:--disable-qt3-immodule} \
	%{!?with_qt4:--disable-qt4-immodule} \
	%{?with_gtk2ui:--with-gtk-version=2} \
	%{?with_qt3:--with-qt3-im-module-dir=%{_libdir}/qt/plugins-mt/inputmethods}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -e 's|@@LIB@@|%{_lib}|g' %{SOURCE1} >$RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/scim.conf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.{la,a}
%{?with_clutter:%{__rm} $RPM_BUILD_ROOT%{_libdir}/clutter-imcontext/immodules/im-scim.{la,a}}
%{?with_gtk2:%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/immodules/im-scim.{la,a}}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/*/immodules/im-scim.{la,a}
%{?with_qt3:%{__rm} $RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/inputmethods/im-scim.{la,a}}
%{?with_qt4:%{__rm} $RPM_BUILD_ROOT%{_libdir}/qt4/plugins/inputmethods/im-scim.{la,a}}

# obsolete GNOME2 file
%{__rm} $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets/scim-setup.desktop


%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post gtk2
%{_bindir}/gtk-query-immodules-2.0%{gtkpqext} > %{gtk2confdir}/gtk.immodules

%postun gtk2
%{_bindir}/gtk-query-immodules-2.0%{gtkpqext} > %{gtk2confdir}/gtk.immodules

%post gtk3
%{_bindir}/gtk-query-immodules-3.0%{gtkpqext} --update-cache

%postun gtk3
%{_bindir}/gtk-query-immodules-3.0%{gtkpqext} --update-cache

%files 
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%dir %{_sysconfdir}/scim
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/scim/config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/scim/global
%{_sysconfdir}/X11/xinit/xinput.d/scim.conf
%attr(755,root,root) %{_bindir}/scim
%attr(755,root,root) %{_bindir}/scim-config-agent
%attr(755,root,root) %{_bindir}/scim-im-agent
%attr(755,root,root) %{_bindir}/scim-setup
%dir %{_libdir}/scim-1.0/%{abiver}/Filter
%dir %{_libdir}/scim-1.0/%{abiver}/FrontEnd
%dir %{_libdir}/scim-1.0/%{abiver}/Helper
%dir %{_libdir}/scim-1.0/%{abiver}/SetupUI
%attr(755,root,root) %{_libdir}/scim-1.0/%{abiver}/Filter/*.so
%attr(755,root,root) %{_libdir}/scim-1.0/%{abiver}/FrontEnd/*.so
%attr(755,root,root) %{_libdir}/scim-1.0/%{abiver}/Helper/*.so
%attr(755,root,root) %{_libdir}/scim-1.0/%{abiver}/SetupUI/*.so
%attr(755,root,root) %{_libdir}/scim-1.0/scim-helper-launcher
%attr(755,root,root) %{_libdir}/scim-1.0/scim-helper-manager
%attr(755,root,root) %{_libdir}/scim-1.0/scim-launcher
%attr(755,root,root) %{_libdir}/scim-1.0/scim-panel-gtk
%{_datadir}/scim
%{_desktopdir}/scim-setup.desktop
%{_pixmapsdir}/scim-setup.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libscim-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libscim-1.0.so.8
%attr(755,root,root) %{_libdir}/libscim-gtkutils-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libscim-gtkutils-1.0.so.8
%attr(755,root,root) %{_libdir}/libscim-x11utils-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libscim-x11utils-1.0.so.8
%dir %{_libdir}/scim-1.0
%dir %{_libdir}/scim-1.0/%{abiver}
%dir %{_libdir}/scim-1.0/%{abiver}/Config
%dir %{_libdir}/scim-1.0/%{abiver}/IMEngine
%attr(755,root,root) %{_libdir}/scim-1.0/%{abiver}/Config/*.so
%attr(755,root,root) %{_libdir}/scim-1.0/%{abiver}/IMEngine/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libscim-1.0.so
%attr(755,root,root) %{_libdir}/libscim-gtkutils-1.0.so
%attr(755,root,root) %{_libdir}/libscim-x11utils-1.0.so
%dir %{_includedir}/scim-1.0
%{_includedir}/scim-1.0/scim*.h
%{_includedir}/scim-1.0/gtk
%{_includedir}/scim-1.0/x11
%{_pkgconfigdir}/scim.pc
%{_pkgconfigdir}/scim-gtkutils.pc
%{_pkgconfigdir}/scim-x11utils.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libscim-1.0.a
%{_libdir}/libscim-gtkutils-1.0.a
%{_libdir}/libscim-x11utils-1.0.a

%if %{with clutter}
%files clutter
%defattr(644,root,root,755)
# TODO: move these dirs to clutter-imcontext when other modules appear
%dir %{_libdir}/clutter-imcontext
%dir %{_libdir}/clutter-imcontext/immodules
%attr(755,root,root) %{_libdir}/clutter-imcontext/immodules/im-scim.so
%endif

%if %{with gtk2}
%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/immodules/im-scim.so
%endif

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/3.*/immodules/im-scim.so

%if %{with qt3}
%files qt3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt/plugins-mt/inputmethods/im-scim.so
%endif

%if %{with qt4}
%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/inputmethods/im-scim.so
%endif
