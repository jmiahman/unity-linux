# Conditional build:
%bcond_with	tests		# build without tests (tests fail mostly)
%bcond_with	qt4		# build without Qt4
%bcond_with	qt5		# build without Qt5

Summary:	A lightweight display manager
Name:		lightdm
# Odd versions are development, use only Even versions here (1.x = x odd/even)
Version:	1.16.4
Release:	1
# library/bindings are LGPLv2 or LGPLv3, the rest GPLv3+
License:	(LGPLv2 or LGPLv3) and GPLv3+
Group:		X11/Applications
Source0:	https://launchpad.net/lightdm/1.16/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	830662050f576e60acf29fa9b8ca4ada
Source1:	%{name}.pamd
Source2:	%{name}-autologin.pamd
Source3:	%{name}-greeter.pamd
Source4:	%{name}.init
Source5:	%{name}-tmpfiles.conf
Patch0:		config.patch
Patch2:		%{name}-nodaemon_option.patch
Patch3:		%{name}-qt5.patch
URL:		http://www.freedesktop.org/wiki/Software/LightDM
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-xml
BuildRequires:	gettext
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	libxklavier-devel
BuildRequires:	linux-pam-devel
BuildRequires:	perl-xml-parser
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	rpm-build
BuildRequires:	tar
BuildRequires:	libx11-devel
BuildRequires:	libxdmcp-devel
BuildRequires:	xz
%if %{with qt4}
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	qt5-build
%endif
Requires:	/usr/bin/X
Requires:	dbus-x11
Requires:	lightdm-greeter
Requires:	xinitrc-ng 
Provides:	XDM
Provides:	group(xdm)
Provides:	user(xdm)

%define bashdir %{_sysconfdir}/bash_completion.d

%description
An X display manager that:
 - Has a lightweight codebase
 - Is standards compliant (PAM, ConsoleKit, etc)
 - Has a well defined interface between the server and user interface
 - Fully themeable (easiest with the webkit interface)
 - Cross-desktop (greeters can be written in any toolkit)

%package libs-gobject
Summary:	LightDM GObject client library
Group:		Libraries
Obsoletes:	lightdm-libs < 1.7.0-0.6

%description libs-gobject
This package contains a GObject based library for LightDM clients to
use to interface with LightDM.

%package libs-gobject-devel
Summary:	Development files for %{name}-gobject
Group:		Development/Libraries
Group:		Libraries
Requires:	%{name}-libs-gobject = %{version}-%{release}

%description libs-gobject-devel
This package contains development files for a GObject based library
for LightDM clients to use to interface with LightDM.

%package libs-qt4
Summary:	LightDM Qt4 client library
Group:		Libraries
Obsoletes:	lightdm-libs-qt
Conflicts:	lightdm-libs < 1.7.0-0.6

%description libs-qt4
This package contains a Qt4 based library for LightDM clients to use
to interface with LightDM.

%package libs-qt4-devel
Summary:	Development files for %{name}-qt4
Group:		Development/Libraries
Requires:	%{name}-libs-qt4 = %{version}-%{release}
Obsoletes:	lightdm-libs-qt-devel

%description libs-qt4-devel
This package contains development files for a Qt4 based library for
LightDM clients to use to interface with LightDM.

%package libs-qt5
Summary:	LightDM Qt5 client library
Group:		Libraries

%description libs-qt5
This package contains a Qt5 based library for LightDM clients to use
to interface with LightDM.

%package libs-qt5-devel
Summary:	Development files for %{name}-qt5
Group:		Development/Libraries
Requires:	%{name}-libs-qt5 = %{version}-%{release}

%description libs-qt5-devel
This package contains development files for a Qt5 based library for
LightDM clients to use to interface with LightDM.

%package init
Summary:	Init script for Lightdm
Summary(pl.UTF-8):	Skrypt init dla Lightdm-a
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires(post,postun):	systemd-units >= 38
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts >= 0.4.3.0
Requires:	systemd-units >= 38
Obsoletes:	lightdm-upstart < 1.7.12-6

%description init
Init script for Lightdm.

%description init -l pl.UTF-8
Skrypt init dla Lightdm-a.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p0

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	%{__enable tests} \
	--enable-liblightdm-gobject \
	%{?with_qt4:--enable-liblightdm-qt} \
	%{?with_qt5:--enable-liblightdm-qt5} \
	--disable-gtk-doc \
	--with-greeter-session=lightdm-gtk-greeter \
	--with-greeter-user=xdm
%{__make}
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL='install -p' \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{pam.d,security,rc.d/init.d,dbus-1/system.d} \
	$RPM_BUILD_ROOT%{bashdir} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf.d \
	$RPM_BUILD_ROOT/home/services/xdm \
	$RPM_BUILD_ROOT%{_datadir}/xgreeters \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{remote-sessions,%{name}.conf.d} \
	$RPM_BUILD_ROOT%{systemdunitdir} \
	$RPM_BUILD_ROOT/var/lib/%{name}-data \
	$RPM_BUILD_ROOT/var/{log,cache}/%{name}

install -d $RPM_BUILD_ROOT{/var/run/lightdm,%{systemdtmpfilesdir}}
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/lightdm.conf

# initscripts
install -p %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
ln -s /dev/null $RPM_BUILD_ROOT%{systemdunitdir}/%{name}.service

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/%{name}
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/lightdm-autologin
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/lightdm-greeter
touch $RPM_BUILD_ROOT/etc/security/blacklist.%{name}

# We don't ship AppAmor
rm -rv $RPM_BUILD_ROOT/etc/apparmor.d

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{lb,wae}

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/bash-completion
cp -p data/bash-completion/{dm-tool,lightdm} $RPM_BUILD_ROOT%{bashdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 55 -r -f xdm
%useradd -u 55 -r -d /home/services/xdm -s /bin/false -c "X Display Manager" -g xdm xdm

%postun
if [ "$1" = "0" ]; then
	%userremove xdm
	%groupremove xdm
fi

%post	libs-gobject -p /sbin/ldconfig
%postun	libs-gobject -p /sbin/ldconfig

%post	libs-qt4 -p /sbin/ldconfig
%postun	libs-qt4 -p /sbin/ldconfig

%post	libs-qt5 -p /sbin/ldconfig
%postun	libs-qt5 -p /sbin/ldconfig

%post init
/sbin/chkconfig --add %{name}
%service -n %{name} restart
%systemd_reload

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del %{name}
	%service %{name} stop
fi

%postun init

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{name}.conf.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/keys.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/users.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/lightdm-autologin
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/lightdm-greeter
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.%{name}
/etc/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%attr(755,root,root) %{_bindir}/dm-tool
%attr(755,root,root) %{_sbindir}/lightdm
%attr(755,root,root) %{_libdir}/lightdm-guest-session
%{_libdir}/girepository-1.0/LightDM-1.typelib
%{systemdtmpfilesdir}/lightdm.conf
%dir %{_datadir}/xgreeters
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/remote-sessions
%dir %{_datadir}/%{name}/%{name}.conf.d
%{_mandir}/man1/dm-tool.1*
%{_mandir}/man1/%{name}.1*
%dir %attr(710,root,root) /var/cache/%{name}
%dir %attr(710,root,root) /var/log/%{name}
%dir %attr(770,root,root) /var/run/%{name}
%dir %attr(700,root,root) /var/lib/%{name}-data
%dir %attr(750,xdm,xdm) /home/services/xdm

%files libs-gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblightdm-gobject-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblightdm-gobject-1.so.0

%if %{with qt4}
%files libs-qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblightdm-qt-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblightdm-qt-3.so.0

%files libs-qt4-devel
%defattr(644,root,root,755)
%{_libdir}/liblightdm-qt-3.la
%attr(755,root,root) %{_libdir}/liblightdm-qt-3.so
%{_includedir}/lightdm-qt-3
%{_pkgconfigdir}/liblightdm-qt-3.pc
%endif

%if %{with qt5}
%files libs-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblightdm-qt5-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblightdm-qt5-3.so.0

%files libs-qt5-devel
%defattr(644,root,root,755)
%{_libdir}/liblightdm-qt5-3.la
%attr(755,root,root) %{_libdir}/liblightdm-qt5-3.so
%{_includedir}/lightdm-qt5-3
%{_pkgconfigdir}/liblightdm-qt5-3.pc
%endif

%files libs-gobject-devel
%defattr(644,root,root,755)
%{_datadir}/gir-1.0/LightDM-1.gir
%{_includedir}/lightdm-gobject-1
%{_pkgconfigdir}/liblightdm-gobject-1.pc
%{_libdir}/liblightdm-gobject-1.la
%attr(755,root,root) %{_libdir}/liblightdm-gobject-1.so
# -vala
#%{_datadir}/vala/vapi/liblightdm-gobject-1.vapi
#%{_datadir}/vala/vapi/liblightdm-gobject-1.deps

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%{systemdunitdir}/%{name}.service

