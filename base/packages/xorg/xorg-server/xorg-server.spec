# Conditional builds:
%bcond_with	dbus		# D-BUS support for configuration (if no udev)
%bcond_without	udev		# UDEV support for configuration
%bcond_without	dri2		# DRI2 extension
%bcond_without	record		# RECORD extension
%bcond_with	xcsecurity	# XC-SECURITY extension (deprecated)
%bcond_with	xf86bigfont	# XF86BigFont extension
%bcond_without	dmx		# DMX DDX (Xdmx server)
%bcond_without	wayland		# Wayland DDX (Xwayland server)
%bcond_with	glamor		# glamor dix module
%bcond_with	systemtap	# systemtap/dtrace probes
%bcond_with	libunwind	# use libunwind for backtracing
#
# ABI versions, see hw/xfree86/common/xf86Module.h
%define	xorg_xserver_server_ansic_abi		0.4
%define	xorg_xserver_server_extension_abi	9.0
%define	xorg_xserver_server_font_abi		0.6
%define	xorg_xserver_server_videodrv_abi	19.0
%define	xorg_xserver_server_xinput_abi		21.0

%define _fontsdir %{_datadir}/fonts

%define	pixman_ver	0.30.0

%ifarch x32
%undefine	with_libunwind
%endif

Summary:	X.org server
Name:		xorg-server
Version:	1.17.2
Release:	1
License:	MIT
Group:		X11/Servers
Source0:	http://xorg.freedesktop.org/releases/individual/xserver/xorg-server-%{version}.tar.bz2
# Source0-md5:	397e405566651150490ff493e463f1ad
Source1:	10-quirks.conf
Source2:	xserver.pamd
#Source10:	%{name}-Xvfb.init
#Source11:	%{name}-Xvfb.sysconfig
Source11:	20-modules.conf
Source12:	xvfb-run.sh

#Patch0:		%{name}-xwrapper.patch
#Patch1:		%{name}-pic-libxf86config.patch
#Patch2:		dtrace-link.patch

#Patch4:		%{name}-builtin-SHA1.patch

#Patch6:		110_nvidia_slowdow_fix.patch
#Patch7:		%{name}-include-defs.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	mesa-libgl-devel
%{?with_dri2:BuildRequires:	mesa-libgl-devel}
%{?with_glamor:BuildRequires:	mesa-libgbm-devel}
# for glx headers
BuildRequires:	opengl-glx-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	docbook-xml
#BuildRequires:	doxygen >= 1.6.1
BuildRequires:	libdrm-devel 
%if %{with glamor} || %{with wayland}
BuildRequires:	libepoxy-devel
%endif
BuildRequires:	libtool 
%{?with_libunwind:BuildRequires:	libunwind-devel}
BuildRequires:	libxcb-devel >= 1.6
BuildRequires:	linux-pam-devel
BuildRequires:	perl
BuildRequires:	pixman-devel >= %{pixman_ver}
BuildRequires:	pkgconfig
%{?with_systemtap:BuildRequires:	systemtap-sdt-devel}
BuildRequires:	eudev-devel
# wayland-client
%{?with_wayland:BuildRequires:	wayland-devel >= 1.3.0}
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xmlto 
BuildRequires:	mkfontscale
BuildRequires:	libx11-devel
BuildRequires:	font-util
BuildRequires:	libxau-devel
%{?with_dmx:BuildRequires:	libxaw-devel}
BuildRequires:	libxdamage-devel
BuildRequires:	libxdmcp
BuildRequires:	libxext-devel 
BuildRequires:	libxfixes-devel
BuildRequires:	libxfont-devel
BuildRequires:	libxi-devel
%{?with_dmx:BuildRequires:	libxmu-devel}
%{?with_dmx:BuildRequires:	libxpm-devel}
BuildRequires:	libxrender-devel
BuildRequires:	libxres-devel
%{?with_dmx:BuildRequires:	libxt-devel}
BuildRequires:	libxtst-devel
BuildRequires:	libxv-devel
BuildRequires:	libxxf86dga-devel
BuildRequires:	libxxf86misc-devel
BuildRequires:	libxxf86vm-devel
%{?with_dmx:BuildRequires:	libdmx-devel}
BuildRequires:	libfontenc-devel
BuildRequires:	libpciaccess-devel
BuildRequires:	libxkbfile-devel
BuildRequires:	libxshmfence-devel
BuildRequires:	xtrans
BuildRequires:	bigreqsproto
BuildRequires:	compositeproto
BuildRequires:	damageproto
%{?with_dmx:BuildRequires:	dmxproto}
%{?with_dri2:BuildRequires:	dri2proto}
BuildRequires:	dri3proto
BuildRequires:	fixesproto
BuildRequires:	fontcacheproto
BuildRequires:	fontsproto
BuildRequires:	glproto
BuildRequires:	inputproto
BuildRequires:	kbproto
BuildRequires:	presentproto
BuildRequires:	printproto
BuildRequires:	randrproto
%{?with_record:BuildRequires:	recordproto}
BuildRequires:	renderproto
BuildRequires:	resourceproto
BuildRequires:	scrnsaverproto
BuildRequires:	videoproto
BuildRequires:	xcmiscproto
BuildRequires:	xextproto 
%{?with_xf86bigfont:BuildRequires:	xf86bigfontproto}
BuildRequires:	xf86dgaproto
BuildRequires:	xf86driproto
BuildRequires:	xf86miscproto
BuildRequires:	xf86vidmodeproto
BuildRequires:	xineramaproto
BuildRequires:	xproto
#BuildRequires:	xorg-sgml-doctools
BuildRequires:	util-macros
#BR: tslib (for KDRIVE only)
Requires(triggerpostun):	sed
%{?with_glamor:Requires:	mesa-libgbm}
Requires:	libdrm 
Requires:	pixman >= %{pixman_ver}
Requires:	eudev
Requires:	xkeyboard-config
Requires:	xkbcomp
Requires:	libxfont
Requires:	libpciaccess
Requires:	libxshmfence
Suggests:	xkeyboard-config
# Usual desktop setups need least one video driver to run, see xorg.log which one exactly
Suggests:	xorg-driver-video

# avoid self-dependencies on included modules
%define		_noautoreq	libscanpci.so libxf1bpp.so

%description
Xorg server is a generally used X server which uses display hardware.
It requires proper driver for your display hardware.

%package xdmx
Summary:	Xdmx - distributed multi-head X server
Group:		X11/Servers
Requires:	pixman >= %{pixman_ver}
Requires:	libx11
Requires:	libxext
Requires:	libxfont
Requires:	libxi
Requires:	libdmx

%description xdmx
Xdmx - distributed multi-head X server.

%package xnest
Summary:	Xnest - nested X server
Group:		X11/Servers
Requires:	pixman >= %{pixman_ver}
Requires:	libxext 
Requires:	libxfont

%description xnest
Xnest is an X Window System server which runs in an X window. Xnest is
a 'nested' window server, actually a client of the real X server,
which manages windows and graphics requests for Xnest, while Xnest
manages the windows and graphics requests for its own clients.

%package xephyr
Summary:	Xephyr - nested X server
Group:		X11/Servers
Requires:	mesa-libgl
Requires:	libxcb
Requires:	pixman >= %{pixman_ver}
Requires:	libxfont

%description xephyr
Xephyr is a kdrive server that outputs to a window on a pre-existing
'host' X display. Think Xnest but with support for modern extensions
like composite, damage and randr.

Unlike Xnest which is an X proxy, i.e. limited to the capabilities of
the host X server, Xephyr is a real X server which uses the host X
server window as "framebuffer" via fast SHM XImages.

It also has support for 'visually' debugging what the server is
painting.

%package xfbdev
Summary:	Xfbdev - Linux framebuffer device X server
Group:		X11/Servers
Requires:	pixman >= %{pixman_ver}
Requires:	libxfont >= 1.4.2

%description xfbdev
Xfbdev is a Linux framebuffer device X server based on the kdrive X
server.

%package xvfb
Summary:	Xvfb - virtual framebuffer X server
Group:		X11/Servers
Requires:	mesa-libgl >= 7.1.0
Requires:	pixman >= %{pixman_ver}
Requires:	util-linux
Requires:	xkeyboard-config
Requires:	xauth
Requires:	xkbcomp
Requires:	libxfont

%description xvfb
Xvfb (X Virtual Frame Buffer) is an X Window System server that is
capable of running on machines with no display hardware and no
physical input devices. Xvfb emulates a dumb framebuffer using virtual
memory. Xvfb doesn't open any devices, but behaves otherwise as an X
display. Xvfb is normally used for testing servers. Using Xvfb, the
mfb or cfb code for any depth can be exercised without using real
hardware that supports the desired depths. Xvfb has also been used to
test X clients against unusual depths and screen configurations, to do
batch processing with Xvfb as a background rendering engine, to do
load testing, to help with porting an X server to a new platform, and
to provide an unobtrusive way of running applications which really
don't need an X server but insist on having one.

#%package xvfb-init
#Summary:	Init scripts for Xvfb
#Group:		X11/Servers
#Requires:	xorg-xserver-xvfb

#%description xvfb-init
#This package contains init scripts for Xvfb and registers Xvfb as
#system service.

%package xwayland
Summary:	Xwayland - X server integrated into a Wayland window system
Group:		X11/Servers
Requires:	pixman >= %{pixman_ver}
Requires:	libx11
Requires:	libxext
Requires:	libxfont
Requires:	libxi

%description xwayland
Xwayland - server integrated into a Wayland window system.

%package devel
Summary:	Header files for X.org server
Group:		X11/Development/Libraries
Requires:	mesa-libgl-devel >= 7.8.0
Requires:	libdrm-devel >= 2.4.46
Requires:	pixman-devel >= %{pixman_ver}
Requires:	libpciaccess-devel >= 0.12.901
Requires:	libxkbfile-devel
%{?with_dri2:Requires:	dri2proto}
Requires:	dri3proto
Requires:	fontsproto
Requires:	glproto
Requires:	inputproto
Requires:	kbproto
Requires:	presentproto
Requires:	randrproto
Requires:	renderproto
Requires:	resourceproto
Requires:	scrnsaverproto
Requires:	videoproto
Requires:	xextproto
Requires:	xf86driproto
Requires:	xineramaproto
Requires:	xproto

%description devel
Header files for X.org server.

%package source
Summary:	X.org server source code
Group:		X11/Development/Libraries

%description source
X.org server source code.

%package libglx
Summary:	GLX extension library for X.org server
Group:		X11/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	mesa-libgl
%{?with_dri2:Requires:	mesa-libgl}
# Mesa version glapi tables in glx/ dir come from
Provides:	xorg-xserver-libglx(glapi)
Provides:	xorg-xserver-module(glx)

%description libglx
GLX extension library for X.org server.

%prep
%setup -q -n xorg-server-%{version}
#%patch0 -p0
#%patch1 -p1
#%patch2 -p1

#%patch4 -p1

#%patch6 -p1

#unfortunately breaks build
#patch7 -p1

# Fix dbus config path
sed -i -e 's/\$(sysconfdir)/\/etc/' config/Makefile.*
sed -i -e 's/termio.h/termios.h/' hw/xfree86/os-support/xf86_OSlib.h

# xserver uses pixman-1 API/ABI so put that explictly here
sed -i -e 's#<pixman\.h#<pixman-1/pixman.h#g' ./fb/fb.h ./include/miscstruct.h ./render/picture.h

# support __filemansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__filemansuffix__/,.so man5/,' hw/xfree86/man/*.man

%build
API=$(awk '/#define ABI_ANSIC_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_ansic_abi} ]; then
	echo "Set %%define xorg_xserver_server_ansic_abi to $API and rerun."
	exit 1
fi

API=$(awk '/#define ABI_EXTENSION_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_extension_abi} ]; then
	echo "Set %%define xorg_xserver_server_extension_abi to $API and rerun."
	exit 1
fi

API=$(awk '/#define ABI_FONT_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_font_abi} ]; then
	echo "Set %%define xorg_xserver_server_font_abi to $API and rerun."
	exit 1
fi
API=$(awk '/#define ABI_VIDEODRV_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_videodrv_abi} ]; then
	echo "Set %%define xorg_xserver_server_videodrv_abi to $API and rerun."
	exit 1
fi
API=$(awk '/#define ABI_XINPUT_VERSION/ { split($0,A,/[(,)]/); printf("%d.%d",A[2], A[3]); }' hw/xfree86/common/xf86Module.h)
if [ $API != %{xorg_xserver_server_xinput_abi} ]; then
	echo "Set %%define xorg_xserver_server_xinput_abi to $API and rerun."
	exit 1
fi

%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

# xorg modules does not work with the -z now and it seems like we
# cannot pass over the linker flag to .so files. so we tweak the
# gcc specs.
export CFLAGS="$CFLAGS -D_GNU_SOURCE"
export CFLAGS="$CFLAGS -D__gid_t=gid_t -D__uid_t=uid_t"
export LDFLAGS="$LDFLAGS -Wl,-z,lazy"
%configure \
	--prefix=/usr \
	--with-os-name="Unity/Linux" \
	--with-os-vendor="Unity/Team" \
	--with-fontrootdir=%{_fontsdir} \
	--with-log-dir=/var/log \
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--with-xkb-output=/var/lib/xkb \
	--disable-linux-acpi \
	--disable-linux-apm \
	--enable-aiglx \
	%{?with_dbus:--enable-config-dbus} \
	--enable-config-udev%{!?with_udev:=no} \
	--enable-dga \
	%{?with_dmx:--enable-dmx} \
	--enable-dri2%{!?with_dri2:=no} \
	%{?with_glamor:--enable-glamor} \
	--enable-glx-tls \
	--enable-install-libxf86config \
	--enable-kdrive \
	%{?with_libunwind:--enable-libunwind} \
	%{?with_record:--enable-record} \
	%{?with_xcsecurity:--enable-xcsecurity} \
	--enable-xephyr \
	%{?with_xf86bigfont:--enable-xf86bigfont} \
	--disable-xfake \
	--enable-xfbdev \
	--disable-xselinux \
	%{?with_wayland:--enable-xwayland} \
	%{!?with_systemtap:--without-dtrace} \
	--without-fop \
	--disable-systemd-logind \
	--without-systemd-daemon \

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%if "%{_libdir}" != "%{_exec_prefix}/lib"
install -d $RPM_BUILD_ROOT%{_exec_prefix}/lib/xorg/modules/dri
%endif

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -Dp %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/xserver
install -d $RPM_BUILD_ROOT/etc/security/console.apps
install -d $RPM_BUILD_ROOT/etc/X11/xorg.conf.d
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/dri
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/input


install -d $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
install -p %{SOURCE12} $RPM_BUILD_ROOT%{_bindir}/xvfb-run

:> $RPM_BUILD_ROOT/etc/security/console.apps/xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xserver

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/10-quirks.conf
cp -p %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/20-modules.conf

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/etc/sysconfig
#install -p %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/Xvfb
#cp -p %{SOURCE11} $RPM_BUILD_ROOT/etc/sysconfig/Xvfb

# prepare source package
install -d $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
cp -a * $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
cd $RPM_BUILD_ROOT%{_usrsrc}/%{name}-%{version}
%{__make} distclean
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f
find -name '*.h' | xargs chmod a-x

%if %{with systemtap}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/xorg-server/Xserver-DTrace.*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- xorg-xserver < 1.5.0
if [ -f /etc/X11/xorg.conf ]; then
	sed -i -e 's/^\s*RgbPath.*$/#& # obsolete option/' /etc/X11/xorg.conf
	sed -i -e 's/^\s*Load\s*"type1".*$/#& # obsolete module/' /etc/X11/xorg.conf
%if %{without record}
	sed -i -e 's/^\s*Load\s*"record".*$/#& # module disabled in this build/' /etc/X11/xorg.conf
%endif
	sed -i -e 's/^\s*Load\s*"xtrap".*$/#& # obsolete module/' /etc/X11/xorg.conf
fi

#%post xvfb-init
#/sbin/chkconfig --add Xvfb
#%service Xvfb restart

#%preun xvfb-init
#if [ "$1" = "0" ]; then
#	%service -q Xvfb stop
#	/sbin/chkconfig --del Xvfb
#fi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/X
%attr(755,root,root) %{_bindir}/Xorg
#%attr(4755,root,root) %{_bindir}/Xwrapper
%attr(755,root,root) %{_bindir}/cvt
%attr(755,root,root) %{_bindir}/gtf
%dir %{_libdir}/xorg
%dir /etc/X11
%{_libdir}/xorg/protocol.txt
%dir %{_libdir}/xorg/modules
%attr(755,root,root) %{_libdir}/xorg/modules/libexa.so
%attr(755,root,root) %{_libdir}/xorg/modules/libfb.so
%attr(755,root,root) %{_libdir}/xorg/modules/libfbdevhw.so
%{?with_glamor:%attr(755,root,root) %{_libdir}/xorg/modules/libglamoregl.so}
%attr(755,root,root) %{_libdir}/xorg/modules/libint10.so
%attr(755,root,root) %{_libdir}/xorg/modules/libshadow.so
%attr(755,root,root) %{_libdir}/xorg/modules/libshadowfb.so
%attr(755,root,root) %{_libdir}/xorg/modules/libvbe.so
%attr(755,root,root) %{_libdir}/xorg/modules/libvgahw.so
%attr(755,root,root) %{_libdir}/xorg/modules/libwfb.so
%dir %{_libdir}/xorg/modules/dri
%dir %{_libdir}/xorg/modules/drivers
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/modesetting_drv.so
%dir %{_libdir}/xorg/modules/extensions
%dir %{_libdir}/xorg/modules/input
%if "%{_libdir}" != "%{_exec_prefix}/lib"
%dir %{_exec_prefix}/lib/xorg
%dir %{_exec_prefix}/lib/xorg/modules
%dir %{_exec_prefix}/lib/xorg/modules/dri
%endif
%dir /var/lib/xkb
/var/lib/xkb/README.compiled
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%dir /etc/security/console.apps
%config(missingok) /etc/security/console.apps/xserver
%{?with_dbus:/etc/dbus-1/system.d/xorg-server.conf}
%dir /etc/X11/xorg.conf.d
%dir %{_datadir}/X11/xorg.conf.d
# overwrite these settings with local configs in /etc/X11/xorg.conf.d
%verify(not md5 mtime size) %{_datadir}/X11/xorg.conf.d/10-evdev.conf
%verify(not md5 mtime size) %{_datadir}/X11/xorg.conf.d/10-quirks.conf
%verify(not md5 mtime size) %{_datadir}/X11/xorg.conf.d/20-modules.conf
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man1/cvt.1*
%{_mandir}/man1/gtf.1*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/modesetting.4*
%{_mandir}/man5/xorg.conf.5*
%{_mandir}/man5/xorg.conf.d.5*

%if %{with dmx}
%files xdmx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xdmx
%attr(755,root,root) %{_bindir}/dmxaddinput
%attr(755,root,root) %{_bindir}/dmxaddscreen
%attr(755,root,root) %{_bindir}/dmxinfo
%attr(755,root,root) %{_bindir}/dmxreconfig
%attr(755,root,root) %{_bindir}/dmxresize
%attr(755,root,root) %{_bindir}/dmxrminput
%attr(755,root,root) %{_bindir}/dmxrmscreen
%attr(755,root,root) %{_bindir}/dmxtodmx
%attr(755,root,root) %{_bindir}/dmxwininfo
%attr(755,root,root) %{_bindir}/vdltodmx
%attr(755,root,root) %{_bindir}/xdmxconfig
%{_mandir}/man1/Xdmx.1*
%{_mandir}/man1/dmxtodmx.1*
%{_mandir}/man1/vdltodmx.1*
%{_mandir}/man1/xdmxconfig.1*
%endif

%files xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%files xephyr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xephyr
%{_mandir}/man1/Xephyr.1*

%files xfbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xfbdev

%files xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%attr(755,root,root) %{_bindir}/xvfb-run
%{_mandir}/man1/Xvfb.1*

#%files xvfb-init
#%defattr(644,root,root,755)
#%attr(754,root,root) /etc/rc.d/init.d/Xvfb
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/Xvfb

%if %{with wayland}
%files xwayland
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xwayland
%endif

%files devel
%defattr(644,root,root,755)
%doc doc/{Xinput,Xserver-spec}.html %{?with_systemtap:doc/dtrace/Xserver-DTrace.html}
%{_includedir}/xorg
%{_libdir}/libxf86config.a
%{_libdir}/libxf86config.la
%{_datadir}/aclocal/xorg-server.m4
%{_libdir}/pkgconfig/xorg-server.pc

%files source
%defattr(644,root,root,755)
# keep file perms from install time, but have default defattr to keep adapter happy
%defattr(-,root,root,755)
%{_usrsrc}/%{name}-%{version}

%files libglx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libglx.so

%changelog
