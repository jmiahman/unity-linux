%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
#%{!?python3_sitearch: %global python3_sitearch %(python3 -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
# TODO
# - finish with_apidocs
# - qt and Qt packages make file collisions on case insensitive filesystems,
#   consider adding version suffix to either of the pckages
#
# Conditional build:
%bcond_with	apidocs		# build API documentation
%bcond_with	dotnet		# build without dotnet bindings
%bcond_with	gtk		# build without GTK+
%bcond_with	gtk3		# build without GTK+3
%bcond_with	pygtk		# build without PyGTK
%bcond_with	qt		# build without (any) qt bindings
%bcond_with	qt3		# build without qt3 bindings
%bcond_with	qt4		# build without qt4 bindings

%define _pkgconfigdir %{_libdir}/pkgconfig
%define _sysconfdir	/etc
%define _pixmapsdir	%{_datadir}/pixmaps

%ifnarch %{ix86} %{x8664} alpha arm hppa ia64 mips ppc s390 s390x sparc sparcv9
%undefine with_dotnet
%endif
%ifarch i386
%undefine with_dotnet
%endif

%if %{without qt}
%undefine	with_qt3
%undefine	with_qt4
%endif

# see http://lists.pld-linux.org/mailman/pipermail/pld-devel-pl/2012-October/155984.html
%undefine _ssp_cflags

%{?with_dotnet:%include /usr/lib/rpm/macros.mono}
Summary:	Free mDNS/DNS-SD/Zeroconf implementation
Name:		avahi
Version:	0.6.31
Release:	1
License:	LGPL v2.1+
Group:		Applications
Source0:	http://avahi.org/download/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Patch0:	%{name}-musl-fix.patch
Patch1:	%{name}-initscripts.patch
URL:		http://avahi.org/
BuildRequires:	autoconf
BuildRequires:	automake 
BuildRequires:	dbus-devel
%if %{with apidocs}
BuildRequires:	doxygen
# for the 'dot' tool used by doxygen
BuildRequires:	graphviz
%endif
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
%if %{with gtk}
BuildRequires:	glib-devel
BuildRequires:	gtk+2-devel
%endif
%if %{with gtk3}
BuildRequires:	glib-devel
BuildRequires:	gtk+3-devel
%endif
BuildRequires:	intltool
BuildRequires:	libcap-devel
BuildRequires:	libdaemon-devel
BuildRequires:	libtool
%if %{with dotnet}
BuildRequires:	dotnet-gtk-sharp2-devel 
BuildRequires:	mono-csharp
BuildRequires:	monodoc
%endif
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-dbus
%{?with_pygtk:BuildRequires:	python-pygtk-devel}
%if %{with qt3}
BuildRequires:	qt-devel
%endif
%if %{with qt4}
BuildRequires:	QtCore-devel
BuildRequires:	qt4-build
%endif
BuildRequires:	rpm-build
#Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
Requires:	libdaemon
#Requires:	rc-scripts
#Suggests:	nss_mdns
Provides:	group(avahi)
Provides:	user(avahi)

%description
Avahi is an implementation the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing. It uses D-BUS for communication
between user applications and a system daemon.

%package libs
Summary:	Avahi client, common and core libraries
Group:		Libraries

%description libs
Avahi client, common and core libraries.

%package devel
Summary:	Header files for Avahi library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-devel
Requires:	expat-devel

%description devel
This is the package containing the header files for Avahi library.

%package static
Summary:	Static Avahi library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Avahi library.

%package ui
Summary:	Avahi UI library
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2 

%description ui
Common GTK+ UI support library for Avahi.

%package ui-devel
Summary:	Header files for Avahi UI library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ui = %{version}-%{release}
Requires:	%{name}-ui-devel-common = %{version}-%{release}
Requires:	gtk+2-devel

%description ui-devel
Header files for Avahi UI library.

%package ui-static
Summary:	Static Avahi UI library
Group:		X11/Development/Libraries
Requires:	%{name}-ui-devel = %{version}-%{release}

%description ui-static
Static Avahi UI library.

%package ui-devel-common
Summary:	Header files for Avahi UI library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description ui-devel-common
Header files for Avahi UI library.

%package ui-gtk3
Summary:	Avahi UI library - GTK+ 3.x version
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description ui-gtk3
Common GTK+ 3.x UI support library for Avahi.

%package ui-gtk3-devel
Summary:	Header files for Avahi UI library - GTK+ 3.x version
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ui-devel-common = %{version}-%{release}
Requires:	%{name}-ui-gtk3 = %{version}-%{release}

%description ui-gtk3-devel
Header files for Avahi GTK+ 3.x UI library.

%package ui-gtk3-static
Summary:	Static Avahi UI library - GTK+ 3.x version
Group:		X11/Development/Libraries
Requires:	%{name}-ui-gtk3-devel = %{version}-%{release}

%description ui-gtk3-static
Static Avahi GTK+ 3.x UI library.

%package compat-libdns_sd
Summary:	Avahi Bonjour compat library
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Provides:	mdns-bonjour

%description compat-libdns_sd
Avahi Bonjour compat library.

%package compat-libdns_sd-devel
Summary:	Header files for Avahi Bonjour compat library
Group:		Development/Libraries
Requires:	%{name}-compat-libdns_sd = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description compat-libdns_sd-devel
Header files for Avahi Bonjour compat library.

%package compat-libdns_sd-static
Summary:	Static Avahi Bonjour compat library
Group:		Development/Libraries
Requires:	%{name}-compat-libdns_sd-devel = %{version}-%{release}

%description compat-libdns_sd-static
Static Avahi Bonjour compat library.

%package compat-howl
Summary:	Avahi Howl compat library
Group:		Libraries
Provides:	mdns-howl-libs

%description compat-howl
Avahi Howl compat library.

%package compat-howl-devel
Summary:	Header files for Avahi Howl compat library
Group:		Development/Libraries
Requires:	%{name}-compat-howl = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Provides:	mdns-howl-devel
Obsoletes:	howl-devel

%description compat-howl-devel
Header files for Avahi Howl compat library.

%package compat-howl-static
Summary:	Static Avahi Howl compat library
Group:		Development/Libraries
Requires:	%{name}-compat-howl-devel = %{version}-%{release}
Provides:	mdns-howl-static

%description compat-howl-static
Static Avahi Howl compat library.

%package glib
Summary:	Avahi GLib library bindings
Group:		Libraries

%description glib
Avahi GLib library bindings.

%package glib-devel
Summary:	Header files for Avahi GLib library bindings
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
Requires:	glib-devel

%description glib-devel
This is the package containing the header files for Avahi-glib
library.

%package glib-static
Summary:	Static Avahi GLib library
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static Avahi GLib library.

%package gobject
Summary:	Avahi GObject interface
Group:		Libraries

%description gobject
Avahi GObject interface.

%package gobject-devel
Summary:	Header files for Avahi GObject interface
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gobject = %{version}-%{release}
Requires:	glib-devel

%description gobject-devel
This is the package containing the header files for Avahi GObject
interface.

%package gobject-static
Summary:	Static Avahi GObject library
Group:		Development/Libraries
Requires:	%{name}-gobject-devel = %{version}-%{release}

%description gobject-static
Static Avahi GObject library.

%package qt3
Summary:	Avahi Qt 3 library bindings
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	avahi-qt3

%description qt3
Avahi Qt 3 library bindings.

%package qt3-devel
Summary:	Header files for Avahi Qt 3 library bindings
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt3 = %{version}-%{release}
Requires:	qt3-devel 

%description qt3-devel
Header files for Avahi Qt 3 library bindings.

%package qt3-static
Summary:	Static Avahi Qt 3 library
Group:		Development/Libraries
Requires:	%{name}-qt3-devel = %{version}-%{release}

%description qt3-static
Static Avahi Qt 3 library.

%package qt4
Summary:	Avahi Qt 4 library bindings
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description qt4
Avahi Qt 4 library bindings.

%package qt4-devel
Summary:	Header files for Avahi Qt 4 library bindings
Group:		Development/Libraries
Requires:	%{name}-qt4 = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description qt4-devel
Header files for Avahi Qt 4 library bindings.

%package qt4-static
Summary:	Static Avahi Qt 4 library
Group:		Development/Libraries
Requires:	%{name}-qt4-devel = %{version}-%{release}

%description qt4-static
Static Avahi Qt 4 library.

%package -n python-avahi
Summary:	Avahi Python bindings
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-dbus

%description -n python-avahi
Avahi Python bindings.

%package -n dotnet-avahi
Summary:	Avahi MONO bindings
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description -n dotnet-avahi
Avahi MONO bindings.

%package -n dotnet-avahi-devel
Summary:	Development files for MONO Avahi bindings
Group:		Development/Libraries
Requires:	dotnet-avahi = %{version}-%{release}
Requires:	monodoc

%description -n dotnet-avahi-devel
Development files for MONO Avahi bindings.

%package -n dotnet-avahi-ui
Summary:	Avahi UI MONO bindings
Group:		X11/Libraries
Requires:	%{name}-ui = %{version}-%{release}
Requires:	dotnet-avahi = %{version}-%{release}

%description -n dotnet-avahi-ui
Avahi UI MONO bindings.

%package -n dotnet-avahi-ui-devel
Summary:	Development files for MONO Avahi UI bindings
Group:		X11/Development/Libraries
Requires:	dotnet-avahi-ui = %{version}-%{release}
Requires:	monodoc >= 2.6

%description -n dotnet-avahi-ui-devel
Development files for MONO Avahi UI bindings.

%package bookmarks
Summary:	Miniature web server
Group:		Applications

%description bookmarks
A Python based miniature web server that browses for mDNS/DNS-SD
services of type '_http._tcp' (i.e. web sites) and makes them
available as HTML links on http://localhost:8080/.

%package discover
Summary:	Avahi Zeroconf browser
Group:		Applications
Requires:	python-avahi = %{version}-%{release}
Requires:	python-pygtk-glade

%description discover
A tool for enumerating all available services on the local LAN
(python-pygtk implementation).

%package discover-standalone
Summary:	Avahi Zeroconf browser
Group:		Applications
Requires:	%{name}-glib = %{version}-%{release}

%description discover-standalone
GTK+ tool for enumerating all available services on the local LAN.

%package utils
Summary:	Avahi CLI utilities
Group:		Applications

%description utils
Command line utilities using avahi-client.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--disable-autoipd \
	%{!?with_apidocs:--disable-doxygen-doc} \
	%{!?with_gtk:--disable-gtk} \
	%{!?with_gtk3:--disable-gtk3} \
	%{!?with_pygtk:--disable-pygtk} \
	%{!?with_qt3:--disable-qt3} \
	%{!?with_qt4:--disable-qt4} \
	%{!?with_dotnet:--disable-mono} \
	%{!?with_dotnet:--disable-monodoc} \
	--disable-doxygen-doc \
	--disable-xmltoman \
	--enable-compat-libdns_sd \
	--enable-compat-howl \
	--enable-python \
	--with-distro="gentoo" \
	--with-systemdsystemunitdir=/lib/systemd/system \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share/dbus-1/system-services
install -d $RPM_BUILD_ROOT/%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{python_sitearch}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%{?with_gtk:%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/bvnc.1}
%if %{with gtk}
echo '.so bssh.1' > $RPM_BUILD_ROOT%{_mandir}/man1/bvnc.1
echo '.so bssh.1' > $RPM_BUILD_ROOT%{_mandir}/man1/bshell.1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -g 165 -r -f avahi

if id -u avahi >/dev/null 2>&1; then
        echo "user exists"
	exit 0
else
	/usr/sbin/useradd -u 165 -r -d -f /usr/share/empty -s /bin/false -c "Avahi daemon" -g avahi avahi
fi

%post
#/sbin/chkconfig --add %{name}-daemon
#/sbin/service %{name}-daemon restart
#/sbin/chkconfig --add %{name}-dnsconfd
#/sbin/service %{name}-dnsconfd restart

%preun
if [ "$1" = "0" ]; then
	/sbin/service -q %{name}-dnsconfd stop
#	/sbin/chkconfig --del %{name}-dnsconfd
	/sbin/service -q %{name}-daemon stop
#	/sbin/chkconfig --del %{name}-daemon
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/userdel avahi
	/usr/sbin/groupdel avahi
fi

%triggerpostun -- avahi < 0.6.30-7

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	ui -p /sbin/ldconfig
%postun	ui -p /sbin/ldconfig

%post	ui-gtk3 -p /sbin/ldconfig
%postun	ui-gtk3 -p /sbin/ldconfig

%post	compat-libdns_sd -p /sbin/ldconfig
%postun	compat-libdns_sd -p /sbin/ldconfig

%post	compat-howl -p /sbin/ldconfig
%postun	compat-howl -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	gobject -p /sbin/ldconfig
%postun	gobject -p /sbin/ldconfig

%post	qt3 -p /sbin/ldconfig
%postun	qt3 -p /sbin/ldconfig

%post	qt4 -p /sbin/ldconfig
%postun	qt4 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/COMPAT-LAYERS docs/NEWS docs/README docs/TODO

%dir %{_sysconfdir}/avahi
%dir %{_sysconfdir}/avahi/services
%attr(755,root,root) %{_sysconfdir}/avahi/avahi-dnsconfd.action
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/avahi-daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/hosts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/services/ssh.service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/services/sftp-ssh.service
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/avahi-dbus.conf

%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service

%attr(755,root,root) %{_bindir}/avahi-set-host-name

%attr(755,root,root) %{_sbindir}/avahi-daemon
%attr(755,root,root) %{_sbindir}/avahi-dnsconfd
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/service-types.db
%{_datadir}/%{name}/avahi-service.dtd
%{_datadir}/%{name}/service-types
%dir %{_datadir}/dbus-1/interfaces
%{_datadir}/dbus-1/interfaces/org.freedesktop.Avahi.*.xml

%{_mandir}/man1/avahi-set-host-name.1*
%{_mandir}/man5/avahi-daemon.conf.5*
%{_mandir}/man5/avahi.hosts.5*
%{_mandir}/man5/avahi.service.5*
%{_mandir}/man8/avahi-daemon.8*
%{_mandir}/man8/avahi-dnsconfd.8*
%{_mandir}/man8/avahi-dnsconfd.action.8*

%attr(754,root,root) /etc/init.d/%{name}-daemon
%attr(754,root,root) /etc/init.d/%{name}-dnsconfd

%files libs 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-client.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-client.so.3
%attr(755,root,root) %{_libdir}/libavahi-common.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-common.so.3
%attr(755,root,root) %{_libdir}/libavahi-core.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-core.so.7
# common for -discover*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/interfaces

%files devel
%defattr(644,root,root,755)
%doc docs/API-CHANGES-0.6 docs/DBUS-API docs/HACKING docs/MALLOC
%attr(755,root,root) %{_libdir}/libavahi-client.so
%attr(755,root,root) %{_libdir}/libavahi-common.so
%attr(755,root,root) %{_libdir}/libavahi-core.so
%{_includedir}/avahi-client
%{_includedir}/avahi-common
%{_includedir}/avahi-core
%{_pkgconfigdir}/avahi-client.pc
%{_pkgconfigdir}/avahi-core.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libavahi-client.a
%{_libdir}/libavahi-common.a
%{_libdir}/libavahi-core.a

%if %{with gtk}
%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-ui.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-ui.so.0
%if %{without gtk3}
%attr(755,root,root) %{_bindir}/bshell
%attr(755,root,root) %{_bindir}/bssh
%attr(755,root,root) %{_bindir}/bvnc
%{_mandir}/man1/bshell.1*
%{_mandir}/man1/bssh.1*
%{_mandir}/man1/bvnc.1*
%{_desktopdir}/bssh.desktop
%{_desktopdir}/bvnc.desktop
%endif

%files ui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-ui.so
%{_pkgconfigdir}/avahi-ui.pc

%files ui-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-ui.a
%endif

%if %{with gtk} || %{with gtk3}
%files ui-devel-common
%defattr(644,root,root,755)
%{_includedir}/avahi-ui
%endif

%if %{with gtk3}
%files ui-gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bshell
%attr(755,root,root) %{_bindir}/bssh
%attr(755,root,root) %{_bindir}/bvnc
%attr(755,root,root) %{_libdir}/libavahi-ui-gtk3.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-ui-gtk3.so.0
%{_mandir}/man1/bshell.1*
%{_mandir}/man1/bssh.1*
%{_mandir}/man1/bvnc.1*
%{_desktopdir}/bssh.desktop
%{_desktopdir}/bvnc.desktop

%files ui-gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-ui-gtk3.so
%{_pkgconfigdir}/avahi-ui-gtk3.pc

%files ui-gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-ui-gtk3.a
%endif

%files compat-libdns_sd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdns_sd.so.*.*.*
%attr(755,root,root) %{_libdir}/libdns_sd.so.1

%files compat-libdns_sd-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdns_sd.so
%{_includedir}/avahi-compat-libdns_sd
%{_pkgconfigdir}/avahi-compat-libdns_sd.pc

%files compat-libdns_sd-static
%defattr(644,root,root,755)
%{_libdir}/libdns_sd.a

%files compat-howl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhowl.so.*.*.*
%attr(755,root,root) %{_libdir}/libhowl.so.0

%files compat-howl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhowl.so
%{_includedir}/avahi-compat-howl
%{_pkgconfigdir}/avahi-compat-howl.pc

%files compat-howl-static
%defattr(644,root,root,755)
%{_libdir}/libhowl.a

%files -n python-avahi
%defattr(644,root,root,755)
%{python_sitearch}/avahi

%if %{with dotnet}
%files -n dotnet-avahi
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/avahi-sharp

%files -n dotnet-avahi-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/avahi-sharp
%{_prefix}/lib/monodoc/sources/avahi-sharp-docs.*
%{_pkgconfigdir}/avahi-sharp.pc

%files -n dotnet-avahi-ui
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/avahi-ui-sharp

%files -n dotnet-avahi-ui-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/avahi-ui-sharp
%{_prefix}/lib/monodoc/sources/avahi-ui-sharp-docs.*
%{_pkgconfigdir}/avahi-ui-sharp.pc
%endif

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-glib.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-glib.so.1

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-glib.so
%{_includedir}/avahi-glib
%{_pkgconfigdir}/avahi-glib.pc

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-glib.a

%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-gobject.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-gobject.so.0
%{_libdir}/girepository-1.0/Avahi-0.6.typelib
%{_libdir}/girepository-1.0/AvahiCore-0.6.typelib

%files gobject-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-gobject.so
%{_includedir}/avahi-gobject
%{_pkgconfigdir}/avahi-gobject.pc
%{_datadir}/gir-1.0/Avahi-0.6.gir
%{_datadir}/gir-1.0/AvahiCore-0.6.gir

%files gobject-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-gobject.a

%if %{with qt3}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-qt3.so.1

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so
%{_includedir}/avahi-qt3
%{_pkgconfigdir}/avahi-qt3.pc

%files qt-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-qt3.a
%endif

%if %{with qt4}
%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt4.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-qt4.so.1

%files qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt4.so
%{_includedir}/avahi-qt4
%{_pkgconfigdir}/avahi-qt4.pc

%files qt4-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-qt4.a
%endif

%files bookmarks
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-bookmarks
%{_mandir}/man1/avahi-bookmarks.1*

%if %{with pygtk}
%files discover
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-discover
%{python_sitearch}/avahi_discover
%{_datadir}/%{name}/interfaces/avahi-discover.ui
%{_desktopdir}/avahi-discover.desktop
%{_pixmapsdir}/avahi.png
%{_mandir}/man1/avahi-discover.1*
%endif

%if %{with gtk}
%files discover-standalone
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-discover-standalone
%{_datadir}/%{name}/interfaces/avahi-discover-standalone.glade
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-browse
%attr(755,root,root) %{_bindir}/avahi-browse-domains
%attr(755,root,root) %{_bindir}/avahi-publish
%attr(755,root,root) %{_bindir}/avahi-publish-address
%attr(755,root,root) %{_bindir}/avahi-publish-service
%attr(755,root,root) %{_bindir}/avahi-resolve
%attr(755,root,root) %{_bindir}/avahi-resolve-address
%attr(755,root,root) %{_bindir}/avahi-resolve-host-name
%{_mandir}/man1/avahi-browse.1*
%{_mandir}/man1/avahi-browse-domains.1*
%{_mandir}/man1/avahi-publish.1*
%{_mandir}/man1/avahi-publish-address.1*
%{_mandir}/man1/avahi-publish-service.1*
%{_mandir}/man1/avahi-resolve.1*
%{_mandir}/man1/avahi-resolve-address.1*
%{_mandir}/man1/avahi-resolve-host-name.1*

%changelog
