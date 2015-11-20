# TODO: verify install time dependencies
#
# Conditonal build:
%bcond_with	systemd		# systemd (user session) support
%bcond_without	wayland		# Wayland clients in composite module
%bcond_with	wayland_egl	# Wayland clients EGL rendering
#
%define		efl_ver		1.16.0
%define		elementary_ver	1.16.0
%define         _pkgconfigdir   %{_libdir}/pkgconfig
%define         _desktopdir     %{_datadir}/applications/
%undefine       __cxx
%define         basearch        %(echo %{_target_platform} | cut -d- -f1)
%define         arch_tag        linux%{_gnu}-%{basearch}-ver-serious-0.19
%define		_sysconfdir	/etc

Summary:	Enlightenment Window Manager
Name:		enlightenment
Version:	0.19.13
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	http://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.xz
Source1:	%{name}-xsession.desktop
URL:		http://enlightenment.org/
BuildRequires:	alsa-lib-devel >= 1.0.8
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.11
#BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	ecore-con-devel >= %{efl_ver}
BuildRequires:	ecore-devel >= %{efl_ver}
BuildRequires:	ecore-evas-devel >= %{efl_ver}
BuildRequires:	ecore-file-devel >= %{efl_ver}
BuildRequires:	ecore-input-devel >= %{efl_ver}
BuildRequires:	ecore-input-evas-devel >= %{efl_ver}
BuildRequires:	ecore-ipc-devel >= %{efl_ver}
BuildRequires:	ecore-x-devel >= %{efl_ver}
BuildRequires:	edje >= %{efl_ver}
BuildRequires:	edje-devel >= %{efl_ver}
BuildRequires:	eet-devel >= %{efl_ver}
BuildRequires:	eeze-devel >= %{efl_ver}
BuildRequires:	efreet-devel >= %{efl_ver}
BuildRequires:	eina-devel >= %{efl_ver}
BuildRequires:	eio-devel >= %{efl_ver}
BuildRequires:	eldbus-devel >= %{efl_ver}
BuildRequires:	elementary-devel >= %{elementary_ver}
BuildRequires:	emotion-devel >= %{efl_ver}
BuildRequires:	evas-devel >= %{efl_ver}
BuildRequires:	gettext >= 0.17
BuildRequires:	libtool >= 2
BuildRequires:	libxcb-devel
BuildRequires:	linux-pam-devel
BuildRequires:	pkgconfig
%{?with_systemd:BuildRequires:	systemd-units >= 192}
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xkeyboard-config
%if %{with wayland}
%{?with_wayland_egl:BuildRequires:	Mesa-libEGL-devel >= 7.10}
BuildRequires:	pixman-devel >= 0.3
# wayland-server
BuildRequires:	wayland-devel >= 1.3.0
BuildRequires:	libxkbcommon-devel >= 0.3.0
%endif
Requires:	alsa-lib >= 1.0.8
Requires:	ecore >= %{efl_ver}
Requires:	ecore-con >= %{efl_ver}
Requires:	ecore-evas >= %{efl_ver}
Requires:	ecore-file >= %{efl_ver}
Requires:	ecore-input >= %{efl_ver}
Requires:	ecore-input-evas >= %{efl_ver}
Requires:	ecore-ipc >= %{efl_ver}
Requires:	ecore-x >= %{efl_ver}
Requires:	edje-libs >= %{efl_ver}
Requires:	eet >= %{efl_ver}
Requires:	eeze >= %{efl_ver}
Requires:	efreet >= %{efl_ver}
Requires:	eina >= %{efl_ver}
Requires:	eio >= %{efl_ver}
Requires:	eldbus >= %{efl_ver}
Requires:	elementary >= %{elementary_ver}
Requires:	emotion >= %{efl_ver}
Requires:	evas >= %{efl_ver}
Requires:	evas-engine-software_x11 >= %{efl_ver}
Requires:	evas-loader-jpeg >= %{efl_ver}
Requires:	evas-loader-png >= %{efl_ver}
Requires:	ecore-con >= %{efl_ver}
Requires:	ecore-drm >= %{efl_ver}  
Requires:	ecore-sdl >= %{efl_ver}  
Requires:	ecore-wayland >= %{efl_ver}  
Requires:	ecore-x >= %{efl_ver}   
Requires:	eet >= %{efl_ver}   
Requires:	elementary-libs >= %{efl_ver}  
Requires:	evas >= %{efl_ver}  
Requires:	emile >= %{efl_ver}
Requires:	ector >= %{efl_ver}
Requires:	harfbuzz  
Requires:	libinput
Requires:	mesa-libgbm
Requires:	libxcursor
Requires:	libxcomposite
Requires:	libxinerama
Requires:	libxscrnsaver
Requires:	libwayland-client
Requires:	libwayland-cursor
Requires:	setxkbmap
Requires:	xcb-util-keysyms
Requires:	tslib
Requires:	graphite2
Requires:	sdl2

%{?with_systemd:Requires:	systemd-units >= 1:192}
%if %{with wayland}
%{?with_wayland_egl:Requires:	Mesa-libEGL >= 7.10}
Requires:	pixman >= 0.3
Requires:	libwayland-server >= 1.3.0
Requires:	libxkbcommon >= 0.3.0
%endif
#Suggests:	vfmg >= 0.9.95

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%package module-cpufreq-freqset
Summary:	CPU speed management binary
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description module-cpufreq-freqset
freqset makes you able to change CPU frequency using cpufreq module.

It contains SUID binary.

%package devel
Summary:	Development headers for Enlightenment
Group:		Development/Libraries
# doesn't require base
Requires:	ecore-devel >= %{efl_ver}
Requires:	ecore-con-devel >= %{efl_ver}
Requires:	ecore-evas-devel >= %{efl_ver}
Requires:	ecore-file-devel >= %{efl_ver}
Requires:	ecore-input-devel >= %{efl_ver}
Requires:	ecore-input-evas-devel >= %{efl_ver}
Requires:	ecore-ipc-devel >= %{efl_ver}
Requires:	ecore-x-devel >= %{efl_ver}
Requires:	edje-devel >= %{efl_ver}
Requires:	eet-devel >= %{efl_ver}
Requires:	eeze-devel >= %{efl_ver}
Requires:	efreet-devel >= %{efl_ver}
Requires:	eina-devel >= %{efl_ver}
Requires:	eio-devel >= %{efl_ver}
Requires:	eldbus-devel >= %{efl_ver}
Requires:	elementary-devel >= %{elementary_ver}
Requires:	emotion-devel >= %{efl_ver}
Requires:	evas-devel >= %{efl_ver}

%description devel
Development headers for Enlightenment.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	%{!?with_systemd:--disable-systemd} \
	%{?with_wayland:--enable-wayland-clients} \
	%{?with_wayland_egl:--enable-wayland-egl} \
	--with-profile=SLOW_PC
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

# recheck: still valid for E18?
install -d $RPM_BUILD_ROOT%{_libdir}/enlightenment/modules_extra
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/config-apps

find $RPM_BUILD_ROOT%{_libdir}/enlightenment -name '*.la' | xargs %{__rm}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
/etc/xdg/menus/e-applications.menu
%dir %{_sysconfdir}/enlightenment
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/enlightenment/sysactions.conf
%attr(755,root,root) %{_bindir}/enlightenment
%attr(755,root,root) %{_bindir}/enlightenment_filemanager
%attr(755,root,root) %{_bindir}/enlightenment_imc
%attr(755,root,root) %{_bindir}/enlightenment_open
%attr(755,root,root) %{_bindir}/enlightenment_remote
%attr(755,root,root) %{_bindir}/enlightenment_start
%if %{with systemd}
%{_prefix}/lib/systemd/user/e18.service
%endif
%dir %{_libdir}/enlightenment
%dir %{_libdir}/enlightenment/modules
%dir %{_libdir}/enlightenment/modules_extra
#
#%dir %{_libdir}/enlightenment/modules/access
#%dir %{_libdir}/enlightenment/modules/access/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/access/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/access/module.desktop
#
%dir %{_libdir}/enlightenment/modules/appmenu
%{_libdir}/enlightenment/modules/appmenu/e-module-appmenu.edj
%dir %{_libdir}/enlightenment/modules/appmenu/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/appmenu/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/appmenu/module.desktop
#
%dir %{_libdir}/enlightenment/modules/backlight
%{_libdir}/enlightenment/modules/backlight/e-module-backlight.edj
%dir %{_libdir}/enlightenment/modules/backlight/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/backlight/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/backlight/module.desktop
#
%dir %{_libdir}/enlightenment/modules/battery
%{_libdir}/enlightenment/modules/battery/e-module-battery.edj
%dir %{_libdir}/enlightenment/modules/battery/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/battery/%{arch_tag}/batget
%attr(755,root,root) %{_libdir}/enlightenment/modules/battery/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/battery/module.desktop
#
%dir %{_libdir}/enlightenment/modules/bluez4
%{_libdir}/enlightenment/modules/bluez4/e-module-bluez4.edj
%dir %{_libdir}/enlightenment/modules/bluez4/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/bluez4/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/bluez4/module.desktop
#
%dir %{_libdir}/enlightenment/modules/clock
%{_libdir}/enlightenment/modules/clock/e-module-clock.edj
%dir %{_libdir}/enlightenment/modules/clock/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/clock/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/clock/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf
%{_libdir}/enlightenment/modules/conf/e-module-conf.edj
%dir %{_libdir}/enlightenment/modules/conf/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_applications
%{_libdir}/enlightenment/modules/conf_applications/e-module-conf_applications.edj
%dir %{_libdir}/enlightenment/modules/conf_applications/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_applications/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_applications/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_bindings
%dir %{_libdir}/enlightenment/modules/conf_bindings/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_bindings/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_bindings/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/conf_comp
#%dir %{_libdir}/enlightenment/modules/conf_comp/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_comp/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/conf_comp/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_dialogs
%{_libdir}/enlightenment/modules/conf_dialogs/e-module-conf_dialogs.edj
%dir %{_libdir}/enlightenment/modules/conf_dialogs/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_dialogs/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_dialogs/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_display
%dir %{_libdir}/enlightenment/modules/conf_display/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_display/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_display/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_interaction
%{_libdir}/enlightenment/modules/conf_interaction/e-module-conf_interaction.edj
%dir %{_libdir}/enlightenment/modules/conf_interaction/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_interaction/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_interaction/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_intl
%dir %{_libdir}/enlightenment/modules/conf_intl/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_intl/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_intl/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_menus
%{_libdir}/enlightenment/modules/conf_menus/e-module-conf_menus.edj
%dir %{_libdir}/enlightenment/modules/conf_menus/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_menus/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_menus/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_paths
%{_libdir}/enlightenment/modules/conf_paths/e-module-conf_paths.edj
%dir %{_libdir}/enlightenment/modules/conf_paths/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_paths/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_paths/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_performance
%{_libdir}/enlightenment/modules/conf_performance/e-module-conf_performance.edj
%dir %{_libdir}/enlightenment/modules/conf_performance/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_performance/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_performance/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_randr
%{_libdir}/enlightenment/modules/conf_randr/e-module-conf_randr.edj
%dir %{_libdir}/enlightenment/modules/conf_randr/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_randr/linux-*/module.so
%{_libdir}/enlightenment/modules/conf_randr/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_shelves
%{_libdir}/enlightenment/modules/conf_shelves/e-module-conf_shelves.edj
%dir %{_libdir}/enlightenment/modules/conf_shelves/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_shelves/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_shelves/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_theme
%dir %{_libdir}/enlightenment/modules/conf_theme/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_theme/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_theme/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/conf_wallpaper2
#%dir %{_libdir}/enlightenment/modules/conf_wallpaper2/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_wallpaper2/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/conf_wallpaper2/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_manipulation
%dir %{_libdir}/enlightenment/modules/conf_window_manipulation/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_window_manipulation/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_window_manipulation/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_remembers
%{_libdir}/enlightenment/modules/conf_window_remembers/e-module-conf_window_remembers.edj
%dir %{_libdir}/enlightenment/modules/conf_window_remembers/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_window_remembers/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_window_remembers/module.desktop
#
%dir %{_libdir}/enlightenment/modules/connman
%{_libdir}/enlightenment/modules/connman/e-module-connman.edj
%dir %{_libdir}/enlightenment/modules/connman/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/connman/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/connman/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/contact
#%{_libdir}/enlightenment/modules/contact/e-module-contact.edj
#%dir %{_libdir}/enlightenment/modules/contact/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/contact/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/contact/module.desktop
#
%dir %{_libdir}/enlightenment/modules/cpufreq
%{_libdir}/enlightenment/modules/cpufreq/e-module-cpufreq.edj
%dir %{_libdir}/enlightenment/modules/cpufreq/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/cpufreq/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/cpufreq/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything
%{_libdir}/enlightenment/modules/everything/e-module-everything-start.edj
%{_libdir}/enlightenment/modules/everything/e-module-everything.edj
%dir %{_libdir}/enlightenment/modules/everything/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/everything/module.desktop
#
%dir %{_libdir}/enlightenment/modules/fileman
%{_libdir}/enlightenment/modules/fileman/e-module-fileman.edj
%dir %{_libdir}/enlightenment/modules/fileman/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/fileman/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/fileman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/fileman_opinfo
%{_libdir}/enlightenment/modules/fileman_opinfo/e-module-fileman_opinfo.edj
%dir %{_libdir}/enlightenment/modules/fileman_opinfo/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/fileman_opinfo/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/fileman_opinfo/module.desktop
#
%dir %{_libdir}/enlightenment/modules/gadman
%{_libdir}/enlightenment/modules/gadman/e-module-gadman.edj
%dir %{_libdir}/enlightenment/modules/gadman/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/gadman/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/gadman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/ibar
%{_libdir}/enlightenment/modules/ibar/e-module-ibar.edj
%dir %{_libdir}/enlightenment/modules/ibar/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/ibar/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/ibar/module.desktop
#
%dir %{_libdir}/enlightenment/modules/ibox
%{_libdir}/enlightenment/modules/ibox/e-module-ibox.edj
%dir %{_libdir}/enlightenment/modules/ibox/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/ibox/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/ibox/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume-bluetooth
#%{_libdir}/enlightenment/modules/illume-bluetooth/e-module-illume-bluetooth.edj
#%dir %{_libdir}/enlightenment/modules/illume-bluetooth/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-bluetooth/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume-bluetooth/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume-home
#%{_libdir}/enlightenment/modules/illume-home/e-module-illume-home.edj
#%dir %{_libdir}/enlightenment/modules/illume-home/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-home/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume-home/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume-home-toggle
#%{_libdir}/enlightenment/modules/illume-home-toggle/e-module-illume-home-toggle.edj
#%dir %{_libdir}/enlightenment/modules/illume-home-toggle/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-home-toggle/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume-home-toggle/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume-indicator
#%{_libdir}/enlightenment/modules/illume-indicator/e-module-illume-indicator.edj
#%dir %{_libdir}/enlightenment/modules/illume-indicator/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-indicator/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume-indicator/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume-kbd-toggle
#%{_libdir}/enlightenment/modules/illume-kbd-toggle/e-module-illume-kbd-toggle.edj
#%dir %{_libdir}/enlightenment/modules/illume-kbd-toggle/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-kbd-toggle/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume-kbd-toggle/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume-keyboard
#%dir %{_libdir}/enlightenment/modules/illume-keyboard/dicts
#%{_libdir}/enlightenment/modules/illume-keyboard/dicts/*.dic
#%{_libdir}/enlightenment/modules/illume-keyboard/e-module-illume-keyboard.edj
#%dir %{_libdir}/enlightenment/modules/illume-keyboard/keyboards
#%{_libdir}/enlightenment/modules/illume-keyboard/keyboards/ignore_built_in_keyboards
#%{_libdir}/enlightenment/modules/illume-keyboard/keyboards/*.kbd
#%{_libdir}/enlightenment/modules/illume-keyboard/keyboards/*.png
#%dir %{_libdir}/enlightenment/modules/illume-keyboard/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-keyboard/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume-keyboard/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume-mode-toggle
#%{_libdir}/enlightenment/modules/illume-mode-toggle/e-module-illume-mode-toggle.edj
#%dir %{_libdir}/enlightenment/modules/illume-mode-toggle/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-mode-toggle/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume-mode-toggle/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume-softkey
#%{_libdir}/enlightenment/modules/illume-softkey/e-module-illume-softkey.edj
#%dir %{_libdir}/enlightenment/modules/illume-softkey/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-softkey/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume-softkey/module.desktop
#
#%dir %{_libdir}/enlightenment/modules/illume2
#%{_libdir}/enlightenment/modules/illume2/e-module-illume2.edj
#%dir %{_libdir}/enlightenment/modules/illume2/keyboards
#%{_libdir}/enlightenment/modules/illume2/keyboards/ignore_built_in_keyboards
#%dir %{_libdir}/enlightenment/modules/illume2/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume2/%{arch_tag}/module.so
#%{_libdir}/enlightenment/modules/illume2/module.desktop
#%dir %{_libdir}/enlightenment/modules/illume2/policies
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume2/policies/illume.so
#%attr(755,root,root) %{_libdir}/enlightenment/modules/illume2/policies/tablet.so
#
%dir %{_libdir}/enlightenment/modules/mixer
%{_libdir}/enlightenment/modules/mixer/e-module-mixer.edj
%dir %{_libdir}/enlightenment/modules/mixer/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/mixer/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/mixer/module.desktop
#
%dir %{_libdir}/enlightenment/modules/msgbus
%{_libdir}/enlightenment/modules/msgbus/e-module-msgbus.edj
%dir %{_libdir}/enlightenment/modules/msgbus/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/msgbus/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/msgbus/module.desktop
#
%dir %{_libdir}/enlightenment/modules/music-control
%{_libdir}/enlightenment/modules/music-control/e-module-music-control.edj
%dir %{_libdir}/enlightenment/modules/music-control/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/music-control/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/music-control/module.desktop
#
%dir %{_libdir}/enlightenment/modules/notification
%{_libdir}/enlightenment/modules/notification/e-module-notification.edj
%dir %{_libdir}/enlightenment/modules/notification/linux-*
%attr(755,root,root)  %{_libdir}/enlightenment/modules/notification/linux-*/module.so
%{_libdir}/enlightenment/modules/notification/module.desktop
#
%dir %{_libdir}/enlightenment/modules/pager
%{_libdir}/enlightenment/modules/pager/e-module-pager.edj
%dir %{_libdir}/enlightenment/modules/pager/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/pager/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/pager/module.desktop
#
%dir %{_libdir}/enlightenment/modules/quickaccess
%{_libdir}/enlightenment/modules/quickaccess/e-module-quickaccess.edj
%dir %{_libdir}/enlightenment/modules/quickaccess/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/quickaccess/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/quickaccess/module.desktop
#
%dir %{_libdir}/enlightenment/modules/shot
%{_libdir}/enlightenment/modules/shot/e-module-shot.edj
%dir %{_libdir}/enlightenment/modules/shot/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/shot/linux-*/module.so
%{_libdir}/enlightenment/modules/shot/module.desktop
#
%dir %{_libdir}/enlightenment/modules/start
%{_libdir}/enlightenment/modules/start/e-module-start.edj
%dir %{_libdir}/enlightenment/modules/start/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/start/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/start/module.desktop
#
%dir %{_libdir}/enlightenment/modules/syscon
%{_libdir}/enlightenment/modules/syscon/e-module-syscon.edj
%dir %{_libdir}/enlightenment/modules/syscon/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/syscon/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/syscon/module.desktop
#
%dir %{_libdir}/enlightenment/modules/systray
%{_libdir}/enlightenment/modules/systray/e-module-systray.edj
%dir %{_libdir}/enlightenment/modules/systray/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/systray/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/systray/module.desktop
#
%dir %{_libdir}/enlightenment/modules/tasks
%{_libdir}/enlightenment/modules/tasks/e-module-tasks.edj
%dir %{_libdir}/enlightenment/modules/tasks/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/tasks/linux-*/module.so
%{_libdir}/enlightenment/modules/tasks/module.desktop
#
%dir %{_libdir}/enlightenment/modules/teamwork
%{_libdir}/enlightenment/modules/teamwork/e-module-teamwork.edj
%dir %{_libdir}/enlightenment/modules/teamwork/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/teamwork/linux-*/module.so
%{_libdir}/enlightenment/modules/teamwork/module.desktop
#
%dir %{_libdir}/enlightenment/modules/temperature
%{_libdir}/enlightenment/modules/temperature/e-module-temperature.edj
%dir %{_libdir}/enlightenment/modules/temperature/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/temperature/%{arch_tag}/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/temperature/%{arch_tag}/tempget
%{_libdir}/enlightenment/modules/temperature/module.desktop
#
%dir %{_libdir}/enlightenment/modules/tiling
%{_libdir}/enlightenment/modules/tiling/e-module-tiling.edj
%dir %{_libdir}/enlightenment/modules/tiling/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/tiling/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/tiling/module.desktop
#
%dir %{_libdir}/enlightenment/modules/winlist
%{_libdir}/enlightenment/modules/winlist/e-module-winlist.edj
%dir %{_libdir}/enlightenment/modules/winlist/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/winlist/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/winlist/module.desktop
#
%dir %{_libdir}/enlightenment/modules/wizard
%dir %{_libdir}/enlightenment/modules/wizard/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wizard/%{arch_tag}/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/wizard/%{arch_tag}/page_*.so
%{_libdir}/enlightenment/modules/wizard/def-ibar.txt
%{_libdir}/enlightenment/modules/wizard/desktop
#
#%if %{with wayland}
#%dir %{_libdir}/enlightenment/modules/wl_desktop_shell
#%dir %{_libdir}/enlightenment/modules/wl_desktop_shell/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/%{arch_tag}/module.so
#%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/module.desktop
#%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/*.edj
#%dir %{_libdir}/enlightenment/modules/wl_screenshot
#%dir %{_libdir}/enlightenment/modules/wl_screenshot/%{arch_tag}
#%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_screenshot/%{arch_tag}/module.so
#%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_screenshot/module.desktop
#%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_screenshot/*.edj
#%endif
#
%dir %{_libdir}/enlightenment/modules/xkbswitch
%{_libdir}/enlightenment/modules/xkbswitch/e-module-xkbswitch.edj
%dir %{_libdir}/enlightenment/modules/xkbswitch/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/xkbswitch/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/xkbswitch/module.desktop
#
%dir %{_libdir}/enlightenment/utils
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_alert
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_backlight
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_fm
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_fm_op
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_static_grabber
# SETUID root: allows rebooting, hibernating and shuting system down
%attr(4755,root,root) %{_libdir}/enlightenment/utils/enlightenment_sys
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_thumb
%{_datadir}/enlightenment
%{_desktopdir}/enlightenment_filemanager.desktop
%{_datadir}/xsessions/enlightenment.desktop

%files module-cpufreq-freqset
%defattr(644,root,root,755)
# what group should it be ?
%attr(4754,root,sys) %{_libdir}/enlightenment/modules/cpufreq/%{arch_tag}/freqset

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/enlightenment
%{_includedir}/enlightenment/e.h
%{_includedir}/enlightenment/e_*.h
%{_includedir}/enlightenment/evry_*.h
%{_pkgconfigdir}/enlightenment.pc
%{_pkgconfigdir}/everything.pc
