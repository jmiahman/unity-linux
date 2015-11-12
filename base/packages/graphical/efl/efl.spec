# TODO:
# - Xpresent
# - use system liblinebreak?
# - eio-devel conflicts with libeio-devel
#	file /usr/lib64/libeio.so from install of eio-devel-0.1.0.65643-1.x86_64 conflicts with file from package libeio-devel-1.0-1.x86_64
#
# Conditional build:
%bcond_without	drm		# DRM engine
%bcond_without	egl		# EGL rendering support
%bcond_without	fb		# Linux FrameBuffer support
%bcond_without	gstreamer	# GStreamer support
%bcond_with	gesture		# Xgesture support in Ecore_X
%bcond_without	harfbuzz	# HarfBuzz complex text shaping and layouting support
%bcond_with	ibus		# IBus input module
%bcond_without	luajit		# LuaJIT as Lua engine (Lua 5.1 interpreter if disabled)
%bcond_with	pixman		# pixman for software rendering
%bcond_without	scim		# SCIM input module
%bcond_without	sdl		# SDL support
%bcond_with	systemd		# systemd journal support in Eina, daemon support in Ecore
%bcond_without	wayland		# Wayland display server support
%bcond_with	wayland_egl	# Wayland display server support [only with GLES instead of GL]
%bcond_with	xcb		# use XCB API instead of Xlib
%bcond_with	xine		# Xine support
%bcond_with	gnutls		# use GnuTLS as crypto library (default is OpenSSL)
%bcond_with	static_libs	# static libraries build
#
%ifnarch %{ix86} %{x8664} arm mips ppc
%undefine	with_luajit
%endif
%define 	_pkgconfigdir	%{_libdir}/pkgconfig
Summary:	EFL - The Enlightenment Foundation Libraries
Name:		efl
Version:	1.10.3
Release:	1
License:	LGPL v2.1+, BSD (depends on component)
Group:		Libraries
Source0:	https://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.bz2
URL:		https://www.enlightenment.org/docs/efl/start
%{?with_egl:BuildRequires:	egl-devel}
BuildRequires:	mesa-libgl
%{?with_sdl:BuildRequires:	sdl-devel}
BuildRequires:	avahi-devel
BuildRequires:	bullet-devel
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gettext
BuildRequires:	giflib-devel
BuildRequires:	glib-devel
%{?with_gnutls:BuildRequires:	gnutls-devel}
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
%endif
%{?with_harfbuzz:BuildRequires:	harfbuzz-devel}
%{?with_ibus:BuildRequires:	ibus-devel}
%{?with_drm:BuildRequires:	libdrm-devel}
%{?with_gnutls:BuildRequires:	libgcrypt-devel}
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libmount-devel
BuildRequires:	libpng-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwebp-devel
%{!?with_luajit:BuildRequires:	lua51 >= 5.1.0}
%{?with_luajit:BuildRequires:	luajit >= 2.0.0}
BuildRequires:	libtool
BuildRequires:	openjpeg-devel >= 2
%{!?with_gnutls:BuildRequires:	openssl-devel}
%if %{with pixman} || %{with xcb}
BuildRequires:	pixman-devel
%endif
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
%{?with_scim:BuildRequires:	scim}
%{?with_systemd:BuildRequires:	systemd-devel}
BuildRequires:	tslib-devel
BuildRequires:	eudev-devel
%{?with_xine:BuildRequires:	xine-lib-devel >= 1.1.1}
%{?with_gesture:BuildRequires:	libxgesture-devel}
%if %{with drm} || %{with wayland}
BuildRequires:	libxkbcommon-devel
%endif
BuildRequires:	zlib-devel
%if %{with xcb}
BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel
%else
BuildRequires:	libx11-devel
BuildRequires:	libxscrnsaver-devel
BuildRequires:	libxcomposite-devel
BuildRequires:	libxcursor-devel
BuildRequires:	libxdamage-devel
BuildRequires:	libxext-devel
BuildRequires:	libxfixes-devel
BuildRequires:	libxi-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxp-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxrender-devel
BuildRequires:	libxtst-devel
%endif
%if %{with wayland}
%{?with_wayland_egl:BuildRequires:	mesa-libegl-devel}
%{?with_wayland_egl:BuildRequires:	mesa-libwayland-egl-devel}
BuildRequires:	wayland-devel
%endif
# svg tests - exist in m4, but not called from configure
#BuildRequires:	esvg-devel >= 0.0.18
#BuildRequires:	ender-devel >= 0.0.6

# it used to be linux-gnu-ARCH before...
%define		arch_tag	v-1.10

%description
EFL - The Enlightenment Foundation Libraries.

%package -n ecore
Summary:	Enlightened Core event abstraction library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	eina = %{version}-%{release}
Requires:	eo = %{version}-%{release}
%{?with_systemd:Requires:	systemd-libs >= 1:192}
Obsoletes:	ecore-config
Obsoletes:	ecore-config-devel
Obsoletes:	ecore-config-static
Obsoletes:	ecore-directfb
Obsoletes:	ecore-directfb-devel
Obsoletes:	ecore-directfb-static
Obsoletes:	ecore-desktop
Obsoletes:	ecore-job
Obsoletes:	ecore-libs
Obsoletes:	ecore-txt

%description -n ecore
Ecore is the event/X abstraction layer that makes doing selections,
Xdnd, general X stuff, event loops, timeouts and idle handlers fast,
optimized, and convenient. It's a separate library so anyone can make
use of the work put into Ecore to make this job easy for applications.

%package -n ecore-devel
Summary:	Header files for Ecore library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eina-devel = %{version}-%{release}
Requires:	eo-devel = %{version}-%{release}
Requires:	glib2-devel >= 2.0
%{?with_systemd:Requires:	systemd-devel >= 1:192}

%description -n ecore-devel
Header files for Ecore library.

%package -n ecore-static
Summary:	Static Ecore library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-devel = %{version}-%{release}

%description -n ecore-static
Static Ecore library.

%package -n ecore-cxx-devel
Summary:	C++ API for Ecore library
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-devel = %{version}-%{release}
Requires:	eina-cxx-devel = %{version}-%{release}
Requires:	eo-cxx-devel = %{version}-%{release}

%description -n ecore-cxx-devel
C++ API for Ecore library.

%package -n ecore-system-systemd
Summary:	systemd system module for Ecore library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}

%description -n ecore-system-systemd
systemd system module for Ecore library.

%package -n ecore-system-upower
Summary:	UPower system module for Ecore library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}

%description -n ecore-system-upower
UPower system module for Ecore library.

%package -n ecore-audio
Summary:	Ecore Audio library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eet = %{version}-%{release}

%description -n ecore-audio
Ecore Audio Library.

%package -n ecore-audio-devel
Summary:	Header file for Ecore Audio library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-audio = %{version}-%{release}
Requires:	ecore-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	libsndfile-devel
Requires:	pulseaudio-devel

%description -n ecore-audio-devel
Header file for Ecore Audio library.

%package -n ecore-audio-static
Summary:	Static Ecore Audio library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-audio-devel = %{version}-%{release}

%description -n ecore-audio-static
Static Ecore Audio library.

%package -n ecore-audio-cxx-devel
Summary:	C++ API for Ecore Audio library
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-audio-devel = %{version}-%{release}
Requires:	eo-cxx-devel = %{version}-%{release}

%description -n ecore-audio-cxx-devel
C++ API for Ecore Audio library.

%package -n ecore-avahi
Summary:	Ecore Avahi integration library
License:	unknown
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eina = %{version}-%{release}
Requires:	eo = %{version}-%{release}

%description -n ecore-avahi
Ecore Avahi integration library.

%package -n ecore-avahi-devel
Summary:	Header file for Ecore Avahi library
License:	unknown
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	avahi-devel
Requires:	ecore-avahi = %{version}-%{release}
Requires:	ecore-devel = %{version}-%{release}
Requires:	eina-devel = %{version}-%{release}
Requires:	eo-devel = %{version}-%{release}

%description -n ecore-avahi-devel
Header file for Ecore Avahi library.

%package -n ecore-avahi-static
Summary:	Static Ecore Avahi library
License:	unknown
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-avahi-devel = %{version}-%{release}

%description -n ecore-avahi-static
Static Ecore Avahi library.

%package -n ecore-con
Summary:	Ecore Con(nection) library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eet = %{version}-%{release}
%{?with_gnutls:Requires:	gnutls}
%{?with_gnutls:Requires:	libgcrypt}

%description -n ecore-con
Ecore Con(nection) Library.

%package -n ecore-con-devel
Summary:	Header file for Ecore Con library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con = %{version}-%{release}
Requires:	ecore-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
%{?with_gnutls:Requires:	gnutls-devel}
%{?with_gnutls:Requires:	libgcrypt-devel}
%{!?with_gnutls:Requires:	openssl-devel}

%description -n ecore-con-devel
Header file for Ecore Con(nection) library.

%package -n ecore-con-static
Summary:	Static Ecore Con library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con-devel = %{version}-%{release}

%description -n ecore-con-static
Static Ecore Con(nection) library.

%package -n ecore-drm
Summary:	Ecore DRM library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}
Requires:	libdrm
Requires:	eudev-libs
Requires:	libxkbcommon

%description -n ecore-drm
Ecore DRM library.

%package -n ecore-drm-devel
Summary:	Header file for Ecore DRM library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-drm = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	libdrm-devel
Requires:	eudev-devel
Requires:	libxkbcommon-devel

%description -n ecore-drm-devel
Header file for Ecore DRM (frame buffer system functions) library.

%package -n ecore-drm-static
Summary:	Static Ecore DRM library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-drm-devel = %{version}-%{release}

%description -n ecore-drm-static
Static Ecore DRM (frame buffer system functions) library.

%package -n ecore-evas
Summary:	Ecore Evas library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
%{?with_drm:Requires:	ecore = %{version}-%{release}}
Requires:	ecore-input = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	evas = %{version}-%{release}

%description -n ecore-evas
Ecore Evas library.

%package -n ecore-evas-devel
Summary:	Header file for Ecore Evas library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-devel = %{version}-%{release}
%{?with_drm:Requires:	ecore-drm = %{version}-%{release}}
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-input-evas-devel = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n ecore-evas-devel
Header file for Ecore Evas library.

%package -n ecore-evas-static
Summary:	Static Ecore Evas library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas-devel = %{version}-%{release}

%description -n ecore-evas-static
Static Ecore Evas library.

%package -n ecore-evas-engine-drm
Summary:	DRM engine module for Ecore Evas library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	evas-engine-drm = %{version}-%{release}

%description -n ecore-evas-engine-drm
DRM engine module for Ecore Evas library.

%package -n ecore-evas-engine-extn
Summary:	extn engine module for Ecore Evas library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-ipc = %{version}-%{release}

%description -n ecore-evas-engine-extn
extn engine module for Ecore Evas library.

%package -n ecore-evas-engine-fb
Summary:	Framebuffer engine module for Ecore Evas library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-fb = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	evas-engine-fb = %{version}-%{release}

%description -n ecore-evas-engine-fb
Framebuffer engine module for Ecore Evas library.

%package -n ecore-evas-engine-sdl
Summary:	SDL engine module for Ecore Evas library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	ecore-sdl = %{version}-%{release}
Requires:	evas-engine-gl_sdl = %{version}-%{release}

%description -n ecore-evas-engine-sdl
SDL engine module for Ecore Evas library.

%package -n ecore-evas-engine-wayland
Summary:	Wayland engine module for Ecore Evas library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	ecore-wayland = %{version}-%{release}
Requires:	evas-engine-wayland_egl = %{version}-%{release}
Requires:	evas-engine-wayland_shm = %{version}-%{release}

%description -n ecore-evas-engine-wayland
Wayland engine module for Ecore Evas library.

%package -n ecore-evas-engine-x
Summary:	X engine module for Ecore Evas library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
Requires:	evas-engine-gl_x11 = %{version}-%{release}
Requires:	evas-engine-software_x11 = %{version}-%{release}

%description -n ecore-evas-engine-x
X engine module for Ecore Evas library.

%package -n ecore-fb
Summary:	Ecore FB (frame buffer system functions) library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}

%description -n ecore-fb
Ecore FB (frame buffer system functions) library.

%package -n ecore-fb-devel
Summary:	Header file for Ecore FB library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-fb = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	tslib-devel

%description -n ecore-fb-devel
Header file for Ecore FB (frame buffer system functions) library.

%package -n ecore-fb-static
Summary:	Static Ecore FB library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-fb-devel = %{version}-%{release}

%description -n ecore-fb-static
Static Ecore FB (frame buffer system functions) library.

%package -n ecore-file
Summary:	Ecore File library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con = %{version}-%{release}

%description -n ecore-file
Ecore File library.

%package -n ecore-file-devel
Summary:	Header file for Ecore File library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con-devel = %{version}-%{release}
Requires:	ecore-file = %{version}-%{release}

%description -n ecore-file-devel
Header file for Ecore File library.

%package -n ecore-file-static
Summary:	Static Ecore File library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-file-devel = %{version}-%{release}

%description -n ecore-file-static
Static Ecore File library.

%package -n ecore-imf
Summary:	Ecore IMF library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}

%description -n ecore-imf
Ecore IMF library.

%package -n ecore-imf-devel
Summary:	Header file for Ecore IMF library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-imf = %{version}-%{release}

%description -n ecore-imf-devel
Header file for Ecore IMF library.

%package -n ecore-imf-static
Summary:	Static Ecore IMF library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf-devel = %{version}-%{release}

%description -n ecore-imf-static
Static Ecore IMF library.

%package -n ecore-imf-module-ibus
Summary:	Ecore IMF IBus input method module
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-imf = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
Requires:	ibus 
Obsoletes:	ecore-module-ibus

%description -n ecore-imf-module-ibus
Ecore IMF IBus input method module.

%package -n ecore-imf-module-scim
Summary:	Ecore IMF SCIM input method module
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-imf = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
Requires:	scim
Obsoletes:	ecore-module-scim

%description -n ecore-imf-module-scim
Ecore IMF SCIM input method module.

%package -n ecore-imf-module-wayland
Summary:	Ecore IMF Wayland input method module
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-imf = %{version}-%{release}
Requires:	ecore-wayland = %{version}-%{release}

%description -n ecore-imf-module-wayland
Ecore IMF Wayland input method module.

%package -n ecore-imf-module-xim
Summary:	Ecore IMF XIM input method module
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
Obsoletes:	ecore-module-xim

%description -n ecore-imf-module-xim
Ecore IMF XIM input method module.

%package -n ecore-imf-evas
Summary:	Ecore IMF Evas library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf = %{version}-%{release}
Requires:	evas = %{version}-%{release}

%description -n ecore-imf-evas
Ecore IMF Evas library.

%package -n ecore-imf-evas-devel
Summary:	Header file for Ecore IMF Evas library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf-devel = %{version}-%{release}
Requires:	ecore-imf-evas = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n ecore-imf-evas-devel
Header file for Ecore IMF Evas library.

%package -n ecore-imf-evas-static
Summary:	Static Ecore IMF Evas library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf-evas-devel = %{version}-%{release}

%description -n ecore-imf-evas-static
Static Ecore IMF Evas library.

%package -n ecore-input
Summary:	Ecore Input library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}

%description -n ecore-input
Ecore Input library.

%package -n ecore-input-devel
Summary:	Header file for Ecore Input library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-devel = %{version}-%{release}
Requires:	ecore-input = %{version}-%{release}

%description -n ecore-input-devel
Header file for Ecore Input library.

%package -n ecore-input-static
Summary:	Static Ecore Input library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-devel = %{version}-%{release}

%description -n ecore-input-static
Static Ecore Input library.

%package -n ecore-input-evas
Summary:	Ecore Input Evas extension library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}
Requires:	evas = %{version}-%{release}

%description -n ecore-input-evas
Ecore Input Evas extension library.

%package -n ecore-input-evas-devel
Summary:	Header file for Ecore Input Evas extension library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n ecore-input-evas-devel
Header file for Ecore Input Evas extension library.

%package -n ecore-input-evas-static
Summary:	Static Ecore Input Evas extension library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-evas-devel = %{version}-%{release}

%description -n ecore-input-evas-static
Static Ecore Input Evas extension library.

%package -n ecore-ipc
Summary:	Ecore IPC (inter-process communication functions) library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con = %{version}-%{release}

%description -n ecore-ipc
Ecore IPC (inter-process communication functions) library.

%package -n ecore-ipc-devel
Summary:	Header file for Ecore IPC library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con-devel = %{version}-%{release}
Requires:	ecore-ipc = %{version}-%{release}

%description -n ecore-ipc-devel
Header file for Ecore IPC (inter-process communication functions)
library.

%package -n ecore-ipc-static
Summary:	Static Ecore IPC library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-ipc-devel = %{version}-%{release}

%description -n ecore-ipc-static
Static Ecore IPC (inter-process communication functions) library.

%package -n ecore-sdl
Summary:	Ecore SDL library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}
Requires:	SDL >= 1.2.0

%description -n ecore-sdl
Ecore SDL library.

%package -n ecore-sdl-devel
Summary:	Header file for Ecore SDL library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-sdl = %{version}-%{release}
Requires:	SDL-devel >= 1.2.0

%description -n ecore-sdl-devel
Header file for Ecore SDL library.

%package -n ecore-sdl-static
Summary:	Static Ecore SDL library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-sdl-devel = %{version}-%{release}

%description -n ecore-sdl-static
Static Ecore SDL library.

%package -n ecore-wayland
Summary:	Ecore Wayland library
Group:		Libraries
Requires:	ecore = %{version}-%{release}
Requires:	ecore-input = %{version}-%{release}
Requires:	wayland 
Requires:	libxkbcommon

%description -n ecore-wayland
Ecore Wayland library.

%package -n ecore-wayland-devel
Summary:	Header file for Ecore Wayland library
Group:		Development/Libraries
Requires:	ecore-devel = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-wayland = %{version}-%{release}
Requires:	wayland-devel
Requires:	libxkbcommon-devel

%description -n ecore-wayland-devel
Header file for Ecore Wayland library.

%package -n ecore-wayland-static
Summary:	Static Ecore Wayland library
Group:		Development/Libraries
Requires:	ecore-wayland-devel = %{version}-%{release}

%description -n ecore-wayland-static
Static Ecore Wayland library.

%package -n ecore-x
Summary:	Ecore X (functions for dealing with the X Window System) library
Group:		X11/Libraries
Requires:	ecore = %{version}-%{release}
Requires:	ecore-input = %{version}-%{release}
%if %{with xcb}
Requires:	xcb-util
Requires:	xcb-util-image
Requires:	xcb-util-keysyms
Requires:	xcb-util-wm
%else
Requires:	libxi
Requires:	libxrandr
%endif

%description -n ecore-x
Ecore X (functions for dealing with the X Window System) library.

%package -n ecore-x-devel
Summary:	Header files for Ecore X library
Group:		Development/Libraries
Requires:	ecore-devel = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
%if %{with xcb}
Requires:	libxcb-devel
Requires:	pixman-devel
Requires:	xcb-util-devel
Requires:	xcb-util-image-devel
Requires:	xcb-util-keysyms-devel
Requires:	xcb-util-wm-devel
%else
Requires:	libx11-devel
Requires:	libxscrnsaver-devel
Requires:	libxcomposite-devel
Requires:	libxcursor-devel
Requires:	libxdamage-devel
Requires:	libxext-devel
Requires:	libxfixes-devel
Requires:	libxi-devel 
Requires:	libxinerama-devel
Requires:	libxp-devel
Requires:	libxrandr-devel
Requires:	libxrender-devel
Requires:	libxtst-devel
%endif

%description -n ecore-x-devel
Header files for Ecore X (functions for dealing with the X Window
System) library.

%package -n ecore-x-static
Summary:	Static Ecore X library
Group:		Development/Libraries
Requires:	ecore-x-devel = %{version}-%{release}

%description -n ecore-x-static
Static Ecore X (functions for dealing with the X Window System)
library.

%package -n edje
Summary:	Complex Graphical Design/Layout Engine
License:	BSD (library), GPL v2 (epp)
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	edje-libs = %{version}-%{release}
Requires:	evas-loader-png = %{version}-%{release}

%description -n edje
Edje is a complex graphical design and layout engine. It provides a
mechanism for allowing configuration data to define visual elements in
terms of layout, behavior, and appearance. Edje allows for multiple
collections of layouts in one file, allowing a complete set of images,
animations, and controls to exist as a unified whole.

Edje separates the arrangement, appearance, and behavior logic into
distinct independent entities. This allows visual objects to share
image data and configuration information without requiring them to do
so. This separation and simplistic event driven style of programming
can produce almost any look and feel one could want for basic visual
elements. Anything more complex is likely the domain of an application
or widget set that may use Edje as a convenient way of being able to
configure parts of the display.

%package -n edje-libs
Summary:	Edje library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	ecore-audio = %{version}-%{release}
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-file = %{version}-%{release}
Requires:	ecore-imf-evas = %{version}-%{release}
Requires:	eina = %{version}-%{release}
Requires:	eio = %{version}-%{release}
Requires:	eet = %{version}-%{release}
Requires:	embryo = %{version}-%{release}
Requires:	ephysics = %{version}-%{release}
%{!?with_luajit:Requires:	lua51 >= 5.1.0}
%{?with_luajit:Requires:	luajit >= 2.0.0}

%description -n edje-libs
Edje library.

%package -n edje-devel
Summary:	Edje header files
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	ecore-audio-devel = %{version}-%{release}
Requires:	ecore-evas-devel = %{version}-%{release}
Requires:	ecore-file-devel = %{version}-%{release}
Requires:	ecore-imf-evas-devel = %{version}-%{release}
Requires:	edje-libs = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	eio-devel = %{version}-%{release}
Requires:	embryo-devel = %{version}-%{release}
Requires:	ephysics-devel = %{version}-%{release}
%{!?with_luajit:Requires:	lua51-devel >= 5.1.0}
%{?with_luajit:Requires:	luajit-devel >= 2.0.0}

%description -n edje-devel
Header files for Edje.

%package -n edje-static
Summary:	Static Edje library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	edje-devel = %{version}-%{release}

%description -n edje-static
Static Edje library.

%package -n edje-cxx-devel
Summary:	C++ API for Edje library
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	edje-devel = %{version}-%{release}
Requires:	eo-cxx-devel = %{version}-%{release}

%description -n edje-cxx-devel
C++ API for Edje library.

%package -n edje-module-emotion
Summary:	Emotion module for Edje library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	edje-libs = %{version}-%{release}
Requires:	emotion = %{version}-%{release}

%description -n edje-module-emotion
Emotion module for Edje library.

%package -n eet
Summary:	Library for speedy data storage, retrieval, and compression
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eet
Requires:	eina = %{version}-%{release}
%{?with_gnutls:Requires:	gnutls}
%{?with_gnutls:Requires:	libgcrypt}
Requires:	zlib

%description -n eet
Eet is a tiny library designed to write an arbitary set of chunks of
data to a file and optionally compress each chunk (very much like a
zip file) and allow fast random-access reading of the file later on.
It does not do zip as a zip itself has more complexity than is needed,
and it was much simpler to implement this once here.

It also can encode and decode data structures in memory, as well as
image data for saving to eet files or sending across the network to
other machines, or just writing to arbitary files on the system. All
data is encoded in a platform independant way and can be written and
read by any architecture.

%package -n eet-devel
Summary:	Header files for Eet library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eet
Requires:	eet = %{version}-%{release}
Requires:	eina-devel = %{version}-%{release}
%{?with_gnutls:Requires:	gnutls-devel}
%{?with_gnutls:Requires:	libgcrypt-devel}
%{!?with_gnutls:Requires:	openssl-devel}
Requires:	libjpeg-devel
Requires:	zlib-devel

%description -n eet-devel
Header files for Eet library.

%package -n eet-static
Summary:	Static Eet library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eet
Requires:	eet-devel = %{version}-%{release}

%description -n eet-static
Static Eet library.

%package -n eet-cxx-devel
Summary:	C++ API for Eet library
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eet
Requires:	eet-devel = %{version}-%{release}
Requires:	eina-cxx-devel = %{version}-%{release}
Requires:	eo-cxx-devel = %{version}-%{release}

%description -n eet-cxx-devel
C++ API for Eet library.

%package -n eeze
Summary:	Library for manipulating devices through udev
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eeze
Requires:	ecore-file = %{version}-%{release}
Requires:	eet = %{version}-%{release}
Requires:	libmount 
Requires:	eudev-libs
Obsoletes:	enlightenment-utils-eeze

%description -n eeze
Eeze is a library for manipulating devices through udev with a simple
and fast API. It interfaces directly with libudev, avoiding such
middleman daemons as udisks/upower or hal, to immediately gather
device information the instant it becomes known to the system. This
can be used to determine such things as:
 - If a CD-ROM has a disk inserted
 - The temperature of a cpu core
 - The remaining power left in a battery
 - The current power consumption of various parts
 - Monitor in realtime the status of peripheral devices.
  
Each of the above examples can be performed by using only a single
eeze function, as one of the primary focuses of the library is to
reduce the complexity of managing devices.

%package -n eeze-devel
Summary:	Eeze header files
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eeze
Requires:	eeze = %{version}-%{release}
Requires:	ecore-file-devel = %{version}-%{release}
Requires:	libmount-devel
Requires:	eudev-devel

%description -n eeze-devel
Header files for Eeze.

%package -n eeze-static
Summary:	Static Eeze library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eeze
Requires:	eeze-devel = %{version}-%{release}

%description -n eeze-static
Static Eeze library.

%package -n efreet
Summary:	freedesktop.org standards implementation for the EFL
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Efreet
Requires:	dbus
Requires:	efreet-libs = %{version}-%{release}

%description -n efreet
Efreet is an implementation of the following specifications from
freedesktop.org:
 - Base Directory - Locations for system and user specific desktop
   configuration files,
 - Desktop Entries - The metadata associated with the applications
   installed on a system,
 - Application Menus - The arrangement of available applications into
   a hierarchical menu,
 - Icon Themes - A means of associating icons with various objects on
   the desktop in a themable fashion.

By following these specifications, Enlightenment 0.17 uses the same
format for describing application launchers, menus and icon themes as
the GNOME, KDE and XFCE Desktop Environments. A system must only
provide a single set of this data for use with any of these desktops.

%package -n efreet-libs
Summary:	Efreet shared libraries
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Efreet
Requires:	ecore-file = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}
Requires:	eet = %{version}-%{release}

%description -n efreet-libs
Efreet shared libraries.

%package -n efreet-devel
Summary:	Efreet header files
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Efreet
Requires:	ecore-file-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	efreet-libs = %{version}-%{release}
Requires:	eldbus-devel = %{version}-%{release}

%description -n efreet-devel
Header files for Efreet.

%package -n efreet-static
Summary:	Static Efreet library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Efreet
Requires:	efreet-devel = %{version}-%{release}

%description -n efreet-static
Static Efreet library.

%package -n eina
Summary:	Data types library (list, hash, etc.)
License:	LGPL v2.1+
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eina
%{?with_systemd:Requires:	systemd-libs}

%description -n eina
Data types library (list, hash, etc.)

%package -n eina-devel
Summary:	Eina header files
License:	LGPL v2.1+
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eina
Requires:	eina = %{version}-%{release}
%{?with_systemd:Requires:	systemd-devel}

%description -n eina-devel
Header files for Eina.

%package -n eina-static
Summary:	Static Eina library
License:	LGPL v2.1+
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eina
Requires:	eina-devel = %{version}-%{release}

%description -n eina-static
Static Eina library.

%package -n eina-cxx-devel
Summary:	C++ API for Eina library
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eina
Requires:	eina-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description -n eina-cxx-devel
C++ API for Eina library.

%package -n eio
Summary:	Enlightenment Input Output Library
License:	LGPL v2.1+
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eio
Requires:	ecore = %{version}-%{release}
Requires:	eet = %{version}-%{release}

%description -n eio
This library is intended to provide non blocking I/O by using thread
for all operation that may block. It depends only on eina and ecore
right now. It should integrate all the features/functions of
Ecore_File that could block.

%package -n eio-devel
Summary:	Header files for Eio library
Group:		Development/Libraries
Requires:	ecore-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	eio = %{version}-%{release}
Conflicts:	libeio-devel

%description -n eio-devel
Header files for Eio library.

%package -n eio-static
Summary:	Static Eio library
Group:		Development/Libraries
Requires:	eio-devel = %{version}-%{release}

%description -n eio-static
Static Eio library.

%package -n eldbus
Summary:	Easy access to D-Bus from EFL applications
License:	LGPL v2.1+
Group:		Libraries
Requires:	ecore = %{version}-%{release}
Requires:	eina = %{version}-%{release}

%description -n eldbus
Eldbus provides easy access to D-Bus from EFL applications.

Eldbus allows connecting to both system and session buses acting as
both client and service roles.

%package -n eldbus-devel
Summary:	Header files for eldbus library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	dbus-devel
Requires:	ecore-devel = %{version}-%{release}
Requires:	eina-devel = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}

%description -n eldbus-devel
Header files for eldbus library.

%package -n eldbus-static
Summary:	Static eldbus library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	eldbus-devel = %{version}-%{release}

%description -n eldbus-static
Static eldbus library.

%package -n embryo
Summary:	Enlightenment Fundation Libraries - Embryo
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Embryo
Requires:	eina = %{version}-%{release}

%description -n embryo
Embryo is a tiny library designed as a virtual machine to interpret a
limited set of small compiled programs.

%package -n embryo-devel
Summary:	Embryo header files
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Embryo
Requires:	eina-devel = %{version}-%{release}
Requires:	embryo = %{version}-%{release}

%description -n embryo-devel
Header files for Embryo.

%package -n embryo-static
Summary:	Static Embryo library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Embryo
Requires:	embryo-devel = %{version}-%{release}

%description -n embryo-static
Static Embryo library.

%package -n emotion
Summary:	Emotion - EFL media playback library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	ecore = %{version}-%{release}
Requires:	eet = %{version}-%{release}
Requires:	eeze = %{version}-%{release}
Requires:	eio = %{version}-%{release}
Requires:	evas = %{version}-%{release}
# for edje module
Requires:	edje-libs = %{version}-%{release}

%description -n emotion
Emotion is a library to easily integrate media playback into EFL
applications, it will take care of using Ecore's main loop and video
display is done using Evas.

%package -n emotion-devel
Summary:	Emotion header files
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	ecore-devel = %{version}-%{release}
Requires:	eio-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	eeze-devel = %{version}-%{release}
Requires:	emotion = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n emotion-devel
Header files for Emotion.

%package -n emotion-static
Summary:	Static Emotion library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	emotion-devel = %{version}-%{release}

%description -n emotion-static
Static Emotion library.

%package -n emotion-decoder-gstreamer
Summary:	Emotion decoder using gstreamer
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	emotion = %{version}-%{release}
Requires:	gstreamer >= 1.0
Requires:	gstreamer-plugins-base >= 1.0

%description -n emotion-decoder-gstreamer
Emotion decoder using gstreamer.

%package -n emotion-decoder-xine
Summary:	Emotion decoder using xine
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	emotion = %{version}-%{release}
Requires:	xine-lib >= 2:1.1.1

%description -n emotion-decoder-xine
Emotion decoder using xine.

%package -n eo
Summary:	Object type library
License:	BSD
Group:		Libraries
Requires:	eina = %{version}-%{release}

%description -n eo
Eo is an object type library.

%package -n eo-devel
Summary:	Header file for Eo library
License:	BSD
Group:		Development/Libraries
Requires:	eina-devel = %{version}-%{release}
Requires:	eo = %{version}-%{release}

%description -n eo-devel
Header file for Eo library.

%package -n eo-static
Summary:	Static Eo library
License:	BSD
Group:		Development/Libraries
Requires:	eo-devel = %{version}-%{release}

%description -n eo-static
Static Eo library.

%package -n eo-cxx-devel
Summary:	C++ API for Eo library
Group:		Development/Libraries
Requires:	eina-cxx-devel = %{version}-%{release}
Requires:	eo-devel = %{version}-%{release}

%description -n eo-cxx-devel
C++ API for Eo library.

%description -n eo-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Eo.

%package -n eo-gdb
Summary:	GDB Python support scripts for Eo types
Group:		Development/Debuggers
Requires:	eo = %{version}-%{release}
Requires:	gdb

%description -n eo-gdb
GDB Python support scripts for Eo types.

%package -n eolian
Summary:	EFL .eo parser and code generator library
License:	BSD
Group:		Libraries
Requires:	eina = %{version}-%{release}

%description -n eolian
Eolian is an EFL's .eo parser and code generator.

%package -n eolian-devel
Summary:	Header files for Eolian library
License:	BSD
Group:		Development/Libraries
Requires:	eina-devel = %{version}-%{release}
Requires:	eolian = %{version}-%{release}

%description -n eolian-devel
Header files for Eolian library.

%package -n eolian-static
Summary:	Static Eolian library
License:	BSD
Group:		Development/Libraries
Requires:	eolian-devel = %{version}-%{release}

%description -n eolian-static
Static Eolian library.

%package -n eolian-cxx-devel
Summary:	C++ API for Eolian library
Group:		Development/Libraries
Requires:	eo-devel = %{version}-%{release}
Requires:	eolian-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description -n eolian-cxx-devel
C++ API for Eolian library.

%package -n ephysics
Summary:	EPhysics - wrapper for physics engine
Group:		Libraries
Requires:	bullet
Requires:	ecore = %{version}-%{release}
Requires:	evas = %{version}-%{release}

%description -n ephysics
EPhysics is a wrapper for physics engine.

%package -n ephysics-devel
Summary:	Header file for EPhysics library
Group:		Development/Libraries
Requires:	bullet-devel
Requires:	ecore-devel = %{version}-%{release}
Requires:	ephysics = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n ephysics-devel
Header file for EPhysics library.

%package -n ephysics-static
Summary:	Static EPhysics library
Group:		Development/Libraries
Requires:	ephysics-devel = %{version}-%{release}

%description -n ephysics-static
Static EPhysics library.

%package -n ethumb
Summary:	Ethumb - thumbnail generation service and utilities
License:	LGPL v2.1
Group:		Applications/Graphics
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	dbus
Requires:	ethumb-libs = %{version}-%{release}
Obsoletes:	ethumb-plugin-epdf

%description -n ethumb
Ethumb is a thumbnail generation library. Features:
- create thumbnails with a predefined frame (possibly an edje frame);
- have an option to create fdo-like thumbnails;
- have a client/server utility.

%package -n ethumb-libs
Summary(pl.UTF-8):	Biblioteki współdzielone Ethumb
License:	LGPL v2.1
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-file = %{version}-%{release}
Requires:	edje-libs = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}

%description -n ethumb-libs
Ethumb shared libraries.

%package -n ethumb-devel
Summary:	Header files for Ethumb libraries
License:	LGPL v2.1
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	ethumb-libs = %{version}-%{release}
Requires:	ecore-evas-devel = %{version}-%{release}
Requires:	ecore-file-devel = %{version}-%{release}
Requires:	edje-devel = %{version}-%{release}
Requires:	eldbus-devel = %{version}-%{release}

%description -n ethumb-devel
Header files for Ethumb libraries.

%package -n ethumb-static
Summary:	Static Ethumb libraries
License:	LGPL v2.1
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	ethumb-devel = %{version}-%{release}

%description -n ethumb-static
Static Ethumb libraries.

%package -n ethumb-plugin-emotion
Summary:	Emotion plugin for Ethumb library
License:	LGPL v2.1
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	edje-libs = %{version}-%{release}
Requires:	emotion = %{version}-%{release}
Requires:	ethumb-libs = %{version}-%{release}

%description -n ethumb-plugin-emotion
Emotion plugin for Ethumb library. It creates thumbnails from movies
using Emotion library.

%package -n evas
Summary:	Multi-platform Canvas Library
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	eet = %{version}-%{release}
Requires:	eo = %{version}-%{release}
Requires:	fontconfig 
Requires:	freetype
Requires:	fribidi
Requires:	harfbuzz
# Provides for statically linked modules
Provides:	evas-engine-buffer = %{version}-%{release}
Provides:	evas-engine-software_generic = %{version}-%{release}
Provides:	evas-loader-eet = %{version}-%{release}
Provides:	evas-loader-pmaps = %{version}-%{release}
Provides:	evas-loader-xpm = %{version}-%{release}
Provides:	evas-saver-eet = %{version}-%{release}
# packages merged in
Obsoletes:	evas-engine-buffer < %{version}-%{release}
Obsoletes:	evas-engine-software_generic < %{version}-%{release}
Obsoletes:	evas-libs
Obsoletes:	evas-loader-eet < %{version}-%{release}
Obsoletes:	evas-loader-pmaps < %{version}-%{release}
Obsoletes:	evas-loader-xpm < %{version}-%{release}
Obsoletes:	evas-saver-eet < %{version}-%{release}
# obsolete packages
Obsoletes:	evas-engine-directfb
Obsoletes:	evas-engine-software_8
Obsoletes:	evas-engine-software_8_x11
Obsoletes:	evas-engine-software_16
Obsoletes:	evas-engine-software_16_sdl
Obsoletes:	evas-engine-software_16_x11
Obsoletes:	evas-engine-software_qtopia
Obsoletes:	evas-engine-xrender_x11
Obsoletes:	evas-engine-xrender_xcb
Obsoletes:	evas-loader-edb
Obsoletes:	evas-loader-svg
Obsoletes:	evas-saver-edb

%description -n evas
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%package -n evas-devel
Summary:	Evas header files
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	eo-devel = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	freetype-devel
Requires:	fribidi-devel
Requires:	harfbuzz-devel

%description -n evas-devel
Header files for Evas.

%package -n evas-static
Summary:	Static Evas library
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas-devel = %{version}-%{release}

%description -n evas-static
Static Evas library.

%package -n evas-cxx-devel
Summary:	C++ API for Evas library
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	eo-cxx-devel = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n evas-cxx-devel
C++ API for Evas library.

## EVAS MODULES
# engines:
%package -n evas-engine-drm
Summary:	DRM rendering engine module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-engine-drm
DRM rendering engine module for Evas.

%package -n evas-engine-fb
Summary:	Framebuffer rendering engine module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-engine-fb
Framebuffer rendering engine module for Evas.

%package -n evas-engine-gl_sdl
Summary:	SDL OpenGL rendering engine module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	sdl

%description -n evas-engine-gl_sdl
SDL OpenGL rendering engine module for Evas.

%package -n evas-engine-gl_x11
Summary:	OpenGL under X11 rendering engine module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-engine-gl_x11
OpenGL under X11 rendering engine module for Evas.

%package -n evas-engine-software_x11
Summary:	Software X11 rendering engine module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Obsoletes:	evas-engine-software_xcb

%description -n evas-engine-software_x11
Software X11 rendering engine module for Evas.

%package -n evas-engine-wayland_egl
Summary:	Wayland EGL rendering engine module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	mesa-libegl-devel
Requires:	mesa-libwayland-egl-devel
Requires:	evas = %{version}-%{release}

%description -n evas-engine-wayland_egl
Wayland EGL rendering engine module for Evas.

%package -n evas-engine-wayland_shm
Summary:	Wayland SHM rendering engine module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-engine-wayland_shm
Wayland SHM rendering engine module for Evas.

# loaders:
%package -n evas-loader-gif
Summary:	GIF Image loader module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-gif
GIF Image loader module for Evas.

%package -n evas-loader-jp2k
Summary:	JPEG2000 Image loader module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-jp2k
JPEG2000 Image loader module for Evas.

%package -n evas-loader-jpeg
Summary:	JPEG Image loader module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-jpeg
JPEG Image loader module for Evas.

%package -n evas-loader-png
Summary:	PNG Image loader module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	libpng

%description -n evas-loader-png
PNG Image loader module for Evas.

%package -n evas-loader-tiff
Summary:	TIFF Image loader module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-tiff
TIFF Image loader module for Evas.

%package -n evas-loader-webp
Summary:	WebP Image loader module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-webp
WebP Image loader module for Evas.

# savers:
%package -n evas-saver-jpeg
Summary:	JPEG Image saver module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-saver-jpeg
JPEG Image saver module for Evas.

%package -n evas-saver-png
Summary:	PNG Image saver module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	libpng 

%description -n evas-saver-png
PNG Image saver module for Evas.

%package -n evas-saver-tiff
Summary:	TIFF Image saver module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-saver-tiff
TIFF Image saver module for Evas.

%package -n evas-saver-webp
Summary:	WebP Image saver module for Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-saver-webp
WebP Image saver module for Evas.

%package -n vim-addon-efl
Summary:	EDC syntax support for Vim
Group:		Applications/Editors/Vim
Requires:	vim-rt
Obsoletes:	vim-syntax-edc

%description -n vim-addon-efl
EDC syntax support for Vim.

%prep
%setup -q

%build
%configure \
	%{?with_drm:--enable-drm} \
	%{?with_egl:--enable-egl} \
	%{?with_fb:--enable-fb} \
	%{?with_gesture:--enable-gesture} \
	%{!?with_gstreamer:--disable-gstreamer1} \
	%{?with_harfbuzz:--enable-harfbuzz} \
	%{!?with_ibus:--disable-ibus} \
	--enable-image-loader-gif \
	--enable-image-loader-jpeg \
	--enable-image-loader-jp2k \
	--enable-image-loader-png \
	--enable-image-loader-tiff \
	--enable-image-loader-webp \
	%{!?with_luajit:--enable-lua-old} \
	--enable-multisense \
	%{?with_pixman:--enable-pixman} \
	%{!?with_scim:--disable-scim} \
	%{?with_sdl:--enable-sdl} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	%{?with_systemd:--enable-systemd} \
	%{?with_wayland:--enable-wayland} \
	%{?with_xine:--enable-xine} \
	--enable-xinput22 \
	--with-crypto=%{?with_gnutls:gnutls}%{!?with_gnutls:openssl} \
	--with-x11=%{?with_xcb:xcb}%{!?with_xcb:xlib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles
cp -pr data/edje/vim/autoload $RPM_BUILD_ROOT%{_datadir}/vim
cp -pr data/edje/vim/ftdetect $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles
cp -pr data/edje/vim/ftplugin $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles
cp -pr data/edje/vim/indent $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles
cp -pr data/edje/vim/snippets $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles
cp -pr data/edje/vim/syntax $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ecore/system/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ecore_evas/engines/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ecore_imf/modules/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/edje/modules/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/eeze/modules/sensor/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/emotion/modules/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ethumb/modules/emotion/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evas/modules/*/*/*/module.la
# benchmarking script, requires expedite and python - should be in expedite?
%{__rm} $RPM_BUILD_ROOT%{_bindir}/eina-bench-cmp

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n ecore -p /sbin/ldconfig
%postun	-n ecore -p /sbin/ldconfig

%post	-n ecore-audio -p /sbin/ldconfig
%postun	-n ecore-audio -p /sbin/ldconfig

%post	-n ecore-avahi -p /sbin/ldconfig
%postun	-n ecore-avahi -p /sbin/ldconfig

%post	-n ecore-con -p /sbin/ldconfig
%postun	-n ecore-con -p /sbin/ldconfig

%post	-n ecore-drm -p /sbin/ldconfig
%postun	-n ecore-drm -p /sbin/ldconfig

%post	-n ecore-evas -p /sbin/ldconfig
%postun	-n ecore-evas -p /sbin/ldconfig

%post	-n ecore-fb -p /sbin/ldconfig
%postun	-n ecore-fb -p /sbin/ldconfig

%post	-n ecore-file -p /sbin/ldconfig
%postun	-n ecore-file -p /sbin/ldconfig

%post	-n ecore-imf -p /sbin/ldconfig
%postun	-n ecore-imf -p /sbin/ldconfig

%post	-n ecore-imf-evas -p /sbin/ldconfig
%postun	-n ecore-imf-evas -p /sbin/ldconfig

%post	-n ecore-input -p /sbin/ldconfig
%postun	-n ecore-input -p /sbin/ldconfig

%post	-n ecore-input-evas -p /sbin/ldconfig
%postun	-n ecore-input-evas -p /sbin/ldconfig

%post	-n ecore-ipc -p /sbin/ldconfig
%postun	-n ecore-ipc -p /sbin/ldconfig

%post	-n ecore-sdl -p /sbin/ldconfig
%postun	-n ecore-sdl -p /sbin/ldconfig

%post	-n ecore-wayland -p /sbin/ldconfig
%postun	-n ecore-wayland -p /sbin/ldconfig

%post	-n ecore-x -p /sbin/ldconfig
%postun	-n ecore-x -p /sbin/ldconfig

%post	-n edje-libs -p /sbin/ldconfig
%postun	-n edje-libs -p /sbin/ldconfig

%post	-n eet -p /sbin/ldconfig
%postun	-n eet -p /sbin/ldconfig

%post	-n eeze -p /sbin/ldconfig
%postun	-n eeze -p /sbin/ldconfig

%post	-n efreet-libs -p /sbin/ldconfig
%postun	-n efreet-libs -p /sbin/ldconfig

%post	-n eina -p /sbin/ldconfig
%postun	-n eina -p /sbin/ldconfig

%post	-n eio -p /sbin/ldconfig
%postun	-n eio -p /sbin/ldconfig

%post	-n eldbus -p /sbin/ldconfig
%postun	-n eldbus -p /sbin/ldconfig

%post	-n embryo -p /sbin/ldconfig
%postun	-n embryo -p /sbin/ldconfig

%post	-n emotion -p /sbin/ldconfig
%postun	-n emotion -p /sbin/ldconfig

%post	-n eo -p /sbin/ldconfig
%postun	-n eo -p /sbin/ldconfig

%post	-n eolian -p /sbin/ldconfig
%postun	-n eolian -p /sbin/ldconfig

%post	-n ephysics -p /sbin/ldconfig
%postun	-n ephysics -p /sbin/ldconfig

%post	-n ethumb-libs -p /sbin/ldconfig
%postun	-n ethumb-libs -p /sbin/ldconfig

%post	-n evas -p /sbin/ldconfig
%postun	-n evas -p /sbin/ldconfig

%files -n ecore -f efl.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore.so.1
%dir %{_libdir}/ecore
%dir %{_libdir}/ecore/system
%{_datadir}/ecore

%files -n ecore-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore.so
%{_includedir}/ecore-1
%{_pkgconfigdir}/ecore.pc
%{_libdir}/cmake/Ecore

%if %{with static_libs}
%files -n ecore-static
%defattr(644,root,root,755)
%{_libdir}/libecore.a
%endif

%files -n ecore-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/ecore-cxx-1
%{_pkgconfigdir}/ecore-cxx.pc
%{_libdir}/cmake/EcoreCxx

%if %{with systemd}
%files -n ecore-system-systemd
%defattr(644,root,root,755)
%dir %{_libdir}/ecore/system/systemd
%dir %{_libdir}/ecore/system/systemd/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore/system/systemd/%{arch_tag}/module.so
%endif

%files -n ecore-system-upower
%defattr(644,root,root,755)
%dir %{_libdir}/ecore/system/upower
%dir %{_libdir}/ecore/system/upower/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore/system/upower/%{arch_tag}/module.so

%files -n ecore-audio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_audio.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_audio.so.1

%files -n ecore-audio-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_audio.so
%{_includedir}/ecore-audio-1
%{_pkgconfigdir}/ecore-audio.pc

%if %{with static_libs}
%files -n ecore-audio-static
%defattr(644,root,root,755)
%{_libdir}/libecore_audio.a
%endif

%files -n ecore-audio-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/ecore-audio-cxx-1
%{_pkgconfigdir}/ecore-audio-cxx.pc

%files -n ecore-avahi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_avahi.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_avahi.so.1

%files -n ecore-avahi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_avahi.so
%{_includedir}/ecore-avahi-1
%{_pkgconfigdir}/ecore-avahi.pc

%if %{with static_libs}
%files -n ecore-avahi-static
%defattr(644,root,root,755)
%{_libdir}/libecore_avahi.a
%endif

%files -n ecore-con
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_con.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_con.so.1

%files -n ecore-con-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_con.so
%{_includedir}/ecore-con-1
%{_pkgconfigdir}/ecore-con.pc

%if %{with static_libs}
%files -n ecore-con-static
%defattr(644,root,root,755)
%{_libdir}/libecore_con.a
%endif

%files -n ecore-drm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_drm.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_drm.so.1
%dir %{_libdir}/ecore_drm
%dir %{_libdir}/ecore_drm/bin
%dir %{_libdir}/ecore_drm/bin/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_drm/bin/%{arch_tag}/ecore_drm_launch

%files -n ecore-drm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_drm.so
%{_includedir}/ecore-drm-1
%{_pkgconfigdir}/ecore-drm.pc

%if %{with static_libs}
%files -n ecore-drm-static
%defattr(644,root,root,755)
%{_libdir}/libecore_drm.a
%endif

%files -n ecore-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore_evas_convert
%attr(755,root,root) %{_libdir}/libecore_evas.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_evas.so.1
%dir %{_libdir}/ecore_evas
%dir %{_libdir}/ecore_evas/engines

%files -n ecore-evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_evas.so
%{_includedir}/ecore-evas-1
%{_pkgconfigdir}/ecore-evas.pc

%if %{with static_libs}
%files -n ecore-evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_evas.a
%endif

%files -n ecore-evas-engine-drm
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/drm
%dir %{_libdir}/ecore_evas/engines/drm/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/drm/%{arch_tag}/module.so

%files -n ecore-evas-engine-extn
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/extn
%dir %{_libdir}/ecore_evas/engines/extn/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/extn/%{arch_tag}/module.so

%if %{with fb}
%files -n ecore-evas-engine-fb
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/fb
%dir %{_libdir}/ecore_evas/engines/fb/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/fb/%{arch_tag}/module.so
%endif

%if %{with sdl}
%files -n ecore-evas-engine-sdl
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/sdl
%dir %{_libdir}/ecore_evas/engines/sdl/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/sdl/%{arch_tag}/module.so
%endif

%if %{with wayland}
%files -n ecore-evas-engine-wayland
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/wayland
%dir %{_libdir}/ecore_evas/engines/wayland/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/wayland/%{arch_tag}/module.so
%endif

%files -n ecore-evas-engine-x
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/x
%dir %{_libdir}/ecore_evas/engines/x/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/x/%{arch_tag}/module.so

%if %{with fb}
%files -n ecore-fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_fb.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_fb.so.1

%files -n ecore-fb-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_fb.so
%{_includedir}/ecore-fb-1
%{_pkgconfigdir}/ecore-fb.pc

%if %{with static_libs}
%files -n ecore-fb-static
%defattr(644,root,root,755)
%{_libdir}/libecore_fb.a
%endif
%endif

%files -n ecore-file
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_file.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_file.so.1

%files -n ecore-file-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_file.so
%{_includedir}/ecore-file-1
%{_pkgconfigdir}/ecore-file.pc

%if %{with static_libs}
%files -n ecore-file-static
%defattr(644,root,root,755)
%{_libdir}/libecore_file.a
%endif

%files -n ecore-imf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_imf.so.1
%dir %{_libdir}/ecore_imf
%dir %{_libdir}/ecore_imf/modules
%{_datadir}/ecore_imf

%files -n ecore-imf-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf.so
%{_includedir}/ecore-imf-1
%{_pkgconfigdir}/ecore-imf.pc

%if %{with static_libs}
%files -n ecore-imf-static
%defattr(644,root,root,755)
%{_libdir}/libecore_imf.a
%endif

%if %{with ibus}
%files -n ecore-imf-module-ibus
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_imf/modules/ibus
%dir %{_libdir}/ecore_imf/modules/ibus/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/ibus/%{arch_tag}/module.so
%endif

%if %{with scim}
%files -n ecore-imf-module-scim
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_imf/modules/scim
%dir %{_libdir}/ecore_imf/modules/scim/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/scim/%{arch_tag}/module.so
%endif

%if %{with wayland}
%files -n ecore-imf-module-wayland
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_imf/modules/wayland
%dir %{_libdir}/ecore_imf/modules/wayland/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/wayland/%{arch_tag}/module.so
%endif

%if %{without xcb_api}
%files -n ecore-imf-module-xim
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_imf/modules/xim
%dir %{_libdir}/ecore_imf/modules/xim/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/xim/%{arch_tag}/module.so
%endif

%files -n ecore-imf-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so.1

%files -n ecore-imf-evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so
%{_includedir}/ecore-imf-evas-1
%{_pkgconfigdir}/ecore-imf-evas.pc

%if %{with static_libs}
%files -n ecore-imf-evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_imf_evas.a
%endif

%files -n ecore-input
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_input.so.1

%files -n ecore-input-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input.so
%{_includedir}/ecore-input-1
%{_pkgconfigdir}/ecore-input.pc

%if %{with static_libs}
%files -n ecore-input-static
%defattr(644,root,root,755)
%{_libdir}/libecore_input.a
%endif

%files -n ecore-input-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input_evas.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_input_evas.so.1

%files -n ecore-input-evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input_evas.so
%{_includedir}/ecore-input-evas-1
%{_pkgconfigdir}/ecore-input-evas.pc

%if %{with static_libs}
%files -n ecore-input-evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_input_evas.a
%endif

%files -n ecore-ipc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_ipc.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_ipc.so.1

%files -n ecore-ipc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_ipc.so
%{_includedir}/ecore-ipc-1
%{_pkgconfigdir}/ecore-ipc.pc

%if %{with static_libs}
%files -n ecore-ipc-static
%defattr(644,root,root,755)
%{_libdir}/libecore_ipc.a
%endif

%if %{with sdl}
%files -n ecore-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_sdl.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_sdl.so.1

%files -n ecore-sdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_sdl.so
%{_includedir}/ecore-sdl-1
%{_pkgconfigdir}/ecore-sdl.pc

%if %{with static_libs}
%files -n ecore-sdl-static
%defattr(644,root,root,755)
%{_libdir}/libecore_sdl.a
%endif
%endif

%if %{with wayland}
%files -n ecore-wayland
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_wayland.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_wayland.so.1

%files -n ecore-wayland-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_wayland.so
%{_includedir}/ecore-wayland-1
%{_pkgconfigdir}/ecore-wayland.pc

%if %{with static_libs}
%files -n ecore-wayland-static
%defattr(644,root,root,755)
%{_libdir}/libecore_wayland.a
%endif
%endif

%files -n ecore-x
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_x.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_x.so.1

%files -n ecore-x-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_x.so
%{_includedir}/ecore-x-1
%{_pkgconfigdir}/ecore-x.pc

%if %{with static_libs}
%files -n ecore-x-static
%defattr(644,root,root,755)
%{_libdir}/libecore_x.a
%endif

%files -n edje
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/edje_cc
%attr(755,root,root) %{_bindir}/edje_codegen
%attr(755,root,root) %{_bindir}/edje_decc
%attr(755,root,root) %{_bindir}/edje_external_inspector
%attr(755,root,root) %{_bindir}/edje_inspector
%attr(755,root,root) %{_bindir}/edje_pick
%attr(755,root,root) %{_bindir}/edje_player
%attr(755,root,root) %{_bindir}/edje_recc
%attr(755,root,root) %{_bindir}/edje_watch
%dir %{_libdir}/edje/utils
%dir %{_libdir}/edje/utils/%{arch_tag}
%attr(755,root,root) %dir %{_libdir}/edje/utils/%{arch_tag}/epp
%{_datadir}/edje
%{_datadir}/mime/packages/edje.xml

%files -n edje-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so.*.*.*
%attr(755,root,root) %{_libdir}/libedje.so.1
%dir %{_libdir}/edje
%dir %{_libdir}/edje/modules

%files -n edje-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so
%{_includedir}/edje-1
%{_pkgconfigdir}/edje.pc
%{_libdir}/cmake/Edje

%if %{with static_libs}
%files -n edje-static
%defattr(644,root,root,755)
%{_libdir}/libedje.a
%endif

%files -n edje-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/edje-cxx-1
%{_pkgconfigdir}/edje-cxx.pc

%files -n edje-module-emotion
%defattr(644,root,root,755)
%dir %{_libdir}/edje/modules/emotion
%dir %{_libdir}/edje/modules/emotion/%{arch_tag}
%attr(755,root,root) %{_libdir}/edje/modules/emotion/%{arch_tag}/module.so

%files -n eet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eet
%attr(755,root,root) %{_bindir}/vieet
%attr(755,root,root) %{_libdir}/libeet.so.*.*.*
%attr(755,root,root) %{_libdir}/libeet.so.1

%files -n eet-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeet.so
%{_includedir}/eet-1
%{_pkgconfigdir}/eet.pc
%{_libdir}/cmake/Eet

%if %{with static_libs}
%files -n eet-static
%defattr(644,root,root,755)
%{_libdir}/libeet.a
%endif

%files -n eet-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/eet-cxx-1
%{_pkgconfigdir}/eet-cxx.pc
%{_libdir}/cmake/EetCxx

%files -n eeze
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eeze_disk_ls
%attr(755,root,root) %{_bindir}/eeze_mount
%attr(755,root,root) %{_bindir}/eeze_scanner
%attr(755,root,root) %{_bindir}/eeze_umount
%attr(755,root,root) %{_libdir}/libeeze.so.*.*.*
%attr(755,root,root) %{_libdir}/libeeze.so.1
%dir %{_libdir}/eeze
%dir %{_libdir}/eeze/modules
%dir %{_libdir}/eeze/modules/sensor
%dir %{_libdir}/eeze/modules/sensor/fake
%dir %{_libdir}/eeze/modules/sensor/fake/%{arch_tag}
%attr(755,root,root) %{_libdir}/eeze/modules/sensor/fake/%{arch_tag}/module.so
%dir %{_libdir}/eeze/modules/sensor/udev
%dir %{_libdir}/eeze/modules/sensor/udev/%{arch_tag}
%attr(755,root,root) %{_libdir}/eeze/modules/sensor/udev/%{arch_tag}/module.so
%{_datadir}/eeze

%files -n eeze-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeeze.so
%{_includedir}/eeze-1
%{_pkgconfigdir}/eeze.pc
%{_libdir}/cmake/Eeze

%if %{with static_libs}
%files -n eeze-static
%defattr(644,root,root,755)
%{_libdir}/libeeze.a
%endif

%files -n efreet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/efreetd
%dir %{_libdir}/efreet
%dir %{_libdir}/efreet/%{arch_tag}
%attr(755,root,root) %{_libdir}/efreet/%{arch_tag}/efreet_desktop_cache_create
%attr(755,root,root) %{_libdir}/efreet/%{arch_tag}/efreet_icon_cache_create
%if %{with systemd}
%{systemduserunitdir}/efreet.service
%endif
%{_datadir}/dbus-1/services/org.enlightenment.Efreet.service
%{_datadir}/efreet

%files -n efreet-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libefreet.so.*.*.*
%attr(755,root,root) %{_libdir}/libefreet.so.1
%attr(755,root,root) %{_libdir}/libefreet_mime.so.*.*.*
%attr(755,root,root) %{_libdir}/libefreet_mime.so.1
%attr(755,root,root) %{_libdir}/libefreet_trash.so.*.*.*
%attr(755,root,root) %{_libdir}/libefreet_trash.so.1

%files -n efreet-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libefreet.so
%attr(755,root,root) %{_libdir}/libefreet_mime.so
%attr(755,root,root) %{_libdir}/libefreet_trash.so
%{_includedir}/efreet-1
%{_pkgconfigdir}/efreet.pc
%{_pkgconfigdir}/efreet-mime.pc
%{_pkgconfigdir}/efreet-trash.pc
%{_libdir}/cmake/Efreet

%if %{with static_libs}
%files -n efreet-static
%defattr(644,root,root,755)
%{_libdir}/libefreet.a
%{_libdir}/libefreet_mime.a
%{_libdir}/libefreet_trash.a
%endif

%files -n eina
%defattr(644,root,root,755)
%doc AUTHORS COMPLIANCE COPYING ChangeLog NEWS README licenses/COPYING.{BSD,SMALL}
%attr(755,root,root) %{_libdir}/libeina.so.*.*.*
%attr(755,root,root) %{_libdir}/libeina.so.1

%files -n eina-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeina.so
# efl-1 is common for EFL - packaged here as eina is all-common EFL dependency
%{_includedir}/efl-1
%{_includedir}/eina-1
%{_pkgconfigdir}/eina.pc
%{_libdir}/cmake/Eina

%if %{with static_libs}
%files -n eina-static
%defattr(644,root,root,755)
%{_libdir}/libeina.a
%endif

%files -n eina-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/eina-cxx-1
%{_pkgconfigdir}/eina-cxx.pc
%{_libdir}/cmake/EinaCxx

%files -n eio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeio.so.*.*.*
%attr(755,root,root) %{_libdir}/libeio.so.1

%files -n eio-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeio.so
%{_includedir}/eio-1
%{_pkgconfigdir}/eio.pc

%if %{with static_libs}
%files -n eio-static
%defattr(644,root,root,755)
%{_libdir}/libeio.a
%endif

%files -n eldbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeldbus.so.*.*.*
%attr(755,root,root) %{_libdir}/libeldbus.so.1

%files -n eldbus-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eldbus-codegen
%attr(755,root,root) %{_libdir}/libeldbus.so
%{_includedir}/eldbus-1
%{_pkgconfigdir}/eldbus.pc
%{_libdir}/cmake/Eldbus

%if %{with static_libs}
%files -n eldbus-static
%defattr(644,root,root,755)
%{_libdir}/libeldbus.a
%endif

%files -n embryo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/embryo_cc
%attr(755,root,root) %{_libdir}/libembryo.so.*.*.*
%attr(755,root,root) %{_libdir}/libembryo.so.1
# for embryo_cc
%{_datadir}/embryo

%files -n embryo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libembryo.so
%{_includedir}/embryo-1
%{_pkgconfigdir}/embryo.pc

%if %{with static_libs}
%files -n embryo-static
%defattr(644,root,root,755)
%{_libdir}/libembryo.a
%endif

%files -n emotion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libemotion.so.*.*.*
%attr(755,root,root) %{_libdir}/libemotion.so.1
%dir %{_libdir}/emotion
%dir %{_libdir}/emotion/modules
%{_datadir}/emotion

%files -n emotion-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libemotion.so
%{_includedir}/emotion-1
%{_pkgconfigdir}/emotion.pc
%{_libdir}/cmake/Emotion

%if %{with static_libs}
%files -n emotion-static
%defattr(644,root,root,755)
%{_libdir}/libemotion.a
%endif

%if %{with gstreamer}
%files -n emotion-decoder-gstreamer
%defattr(644,root,root,755)
%dir %{_libdir}/emotion/modules/gstreamer1
%dir %{_libdir}/emotion/modules/gstreamer1/%{arch_tag}
%attr(755,root,root) %{_libdir}/emotion/modules/gstreamer1/%{arch_tag}/module.so
%endif

%if %{with xine}
%files -n emotion-decoder-xine
%defattr(644,root,root,755)
%dir %{_libdir}/emotion/modules/xine
%dir %{_libdir}/emotion/modules/xine/%{arch_tag}
%attr(755,root,root) %{_libdir}/emotion/modules/xine/%{arch_tag}/module.so
%endif

%files -n eo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeo.so.*.*.*
%attr(755,root,root) %{_libdir}/libeo.so.1

%files -n eo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeo.so
%{_includedir}/eo-1
%{_pkgconfigdir}/eo.pc
%{_libdir}/cmake/Eo

%if %{with static_libs}
%files -n eo-static
%defattr(644,root,root,755)
%{_libdir}/libeo.a
%endif

%files -n eo-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/eo-cxx-1
%{_pkgconfigdir}/eo-cxx.pc
%{_libdir}/cmake/EoCxx

%files -n eo-gdb
%defattr(644,root,root,755)
%dir %{_datadir}/eo
%{_datadir}/eo/gdb
%{_datadir}/gdb/auto-load/usr/%{_lib}/libeo.so.%{version}-gdb.py

%files -n eolian
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eolian_cxx
%attr(755,root,root) %{_bindir}/eolian_gen
%attr(755,root,root) %{_libdir}/libeolian.so.*.*.*
%attr(755,root,root) %{_libdir}/libeolian.so.1
%dir %{_datadir}/eolian
%dir %{_datadir}/eolian/include
# package everything here or per-library split?
%{_datadir}/eolian/include/ecore-1
%{_datadir}/eolian/include/edje-1
%{_datadir}/eolian/include/eo-1
%{_datadir}/eolian/include/evas-1

%files -n eolian-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeolian.so
%{_includedir}/eolian-1
%{_pkgconfigdir}/eolian.pc
%{_libdir}/cmake/Eolian

%files -n eolian-static
%defattr(644,root,root,755)
%{_libdir}/libeolian.a

%files -n eolian-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/eolian-cxx-1
%{_pkgconfigdir}/eolian-cxx.pc
%{_libdir}/cmake/EolianCxx

%files -n ephysics
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libephysics.so.*.*.*
%attr(755,root,root) %{_libdir}/libephysics.so.1

%files -n ephysics-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libephysics.so
%{_includedir}/ephysics-1
%{_pkgconfigdir}/ephysics.pc

%if %{with static_libs}
%files -n ephysics-static
%defattr(644,root,root,755)
%{_libdir}/libephysics.a
%endif

%files -n ethumb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ethumb
%attr(755,root,root) %{_bindir}/ethumbd
%attr(755,root,root) %{_bindir}/ethumbd_client
%dir %{_libdir}/ethumb_client
%dir %{_libdir}/ethumb_client/utils
%dir %{_libdir}/ethumb_client/utils/%{arch_tag}
%attr(755,root,root) %{_libdir}/ethumb_client/utils/%{arch_tag}/ethumbd_slave
%if %{with systemd}
%{systemduserunitdir}/ethumb.service
%endif
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ethumb
%{_datadir}/ethumb_client

%files -n ethumb-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libethumb.so.*.*.*
%attr(755,root,root) %{_libdir}/libethumb.so.1
%attr(755,root,root) %{_libdir}/libethumb_client.so.*.*.*
%attr(755,root,root) %{_libdir}/libethumb_client.so.1
%dir %{_libdir}/ethumb
%dir %{_libdir}/ethumb/modules

%files -n ethumb-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libethumb.so
%attr(755,root,root) %{_libdir}/libethumb_client.so
%{_includedir}/ethumb-1
%{_includedir}/ethumb-client-1
%{_pkgconfigdir}/ethumb.pc
%{_pkgconfigdir}/ethumb_client.pc
%{_libdir}/cmake/Ethumb
%{_libdir}/cmake/EthumbClient

%if %{with static_libs}
%files -n ethumb-static
%defattr(644,root,root,755)
%{_libdir}/libethumb.a
%{_libdir}/libethumb_client.a
%endif

%files -n ethumb-plugin-emotion
%defattr(644,root,root,755)
%dir %{_libdir}/ethumb/modules/emotion
%dir %{_libdir}/ethumb/modules/emotion/%{arch_tag}
%attr(755,root,root) %{_libdir}/ethumb/modules/emotion/%{arch_tag}/module.so
%{_libdir}/ethumb/modules/emotion/%{arch_tag}/template.edj

%files -n evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/evas_cserve2_client
%attr(755,root,root) %{_bindir}/evas_cserve2_debug
%attr(755,root,root) %{_bindir}/evas_cserve2_shm_debug
%attr(755,root,root) %{_bindir}/evas_cserve2_usage
%attr(755,root,root) %{_libdir}/libevas.so.*.*.*
%attr(755,root,root) %{_libdir}/libevas.so.1
%dir %{_libdir}/evas
%dir %{_libdir}/evas/cserve2
%dir %{_libdir}/evas/cserve2/bin
%dir %{_libdir}/evas/cserve2/bin/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/cserve2/bin/%{arch_tag}/evas_cserve2
%attr(755,root,root) %{_libdir}/evas/cserve2/bin/%{arch_tag}/evas_cserve2_slave
%dir %{_libdir}/evas/modules
%dir %{_libdir}/evas/modules/engines
%dir %{_libdir}/evas/modules/loaders
%dir %{_libdir}/evas/modules/savers
%{_datadir}/evas

%files -n evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevas.so
%{_includedir}/evas-1
%{_pkgconfigdir}/evas.pc
# engine private structures
%{?with_drm:%{_pkgconfigdir}/evas-drm.pc}
%{?with_fb:%{_pkgconfigdir}/evas-fb.pc}
%{?with_sdl:%{_pkgconfigdir}/evas-opengl-sdl.pc}
%{_pkgconfigdir}/evas-opengl-x11.pc
%{_pkgconfigdir}/evas-software-buffer.pc
%{_pkgconfigdir}/evas-software-x11.pc
%if %{with wayland}
%{?with_wayland_egl:%{_pkgconfigdir}/evas-wayland-egl.pc}
%{_pkgconfigdir}/evas-wayland-shm.pc
%endif
%{_libdir}/cmake/Evas

%if %{with static_libs}
%files -n evas-static
%defattr(644,root,root,755)
%{_libdir}/libevas.a
%endif

%files -n evas-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/evas-cxx-1
%{_pkgconfigdir}/evas-cxx.pc
%{_libdir}/cmake/EvasCxx

%if %{with drm}
%files -n evas-engine-drm
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/drm
%dir %{_libdir}/evas/modules/engines/drm/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/drm/%{arch_tag}/module.so
%endif

%if %{with fb}
%files -n evas-engine-fb
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/fb
%dir %{_libdir}/evas/modules/engines/fb/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/fb/%{arch_tag}/module.so
%endif

%if %{with sdl}
%files -n evas-engine-gl_sdl
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/gl_sdl
%dir %{_libdir}/evas/modules/engines/gl_sdl/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/gl_sdl/%{arch_tag}/module.so
%endif

%files -n evas-engine-gl_x11
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/gl_x11
%dir %{_libdir}/evas/modules/engines/gl_x11/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/gl_x11/%{arch_tag}/module.so

%files -n evas-engine-software_x11
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/software_x11
%dir %{_libdir}/evas/modules/engines/software_x11/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/software_x11/%{arch_tag}/module.so

%if %{with wayland}
%if %{with wayland_egl}
%files -n evas-engine-wayland_egl
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/wayland_egl
%dir %{_libdir}/evas/modules/engines/wayland_egl/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/wayland_egl/%{arch_tag}/module.so
%endif

%files -n evas-engine-wayland_shm
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/wayland_shm
%dir %{_libdir}/evas/modules/engines/wayland_shm/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/wayland_shm/%{arch_tag}/module.so
%endif

%files -n evas-loader-gif
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/gif
%dir %{_libdir}/evas/modules/loaders/gif/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/gif/%{arch_tag}/module.so

%files -n evas-loader-jp2k
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/jp2k
%dir %{_libdir}/evas/modules/loaders/jp2k/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/jp2k/%{arch_tag}/module.so

%files -n evas-loader-jpeg
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/jpeg
%dir %{_libdir}/evas/modules/loaders/jpeg/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/jpeg/%{arch_tag}/module.so

%files -n evas-loader-png
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/png
%dir %{_libdir}/evas/modules/loaders/png/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/png/%{arch_tag}/module.so

%files -n evas-loader-tiff
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/tiff
%dir %{_libdir}/evas/modules/loaders/tiff/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/tiff/%{arch_tag}/module.so

%files -n evas-loader-webp
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/webp
%dir %{_libdir}/evas/modules/loaders/webp/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/webp/%{arch_tag}/module.so

%files -n evas-saver-jpeg
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/savers/jpeg
%dir %{_libdir}/evas/modules/savers/jpeg/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/savers/jpeg/%{arch_tag}/module.so

%files -n evas-saver-png
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/savers/png
%dir %{_libdir}/evas/modules/savers/png/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/savers/png/%{arch_tag}/module.so

%files -n evas-saver-tiff
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/savers/tiff
%dir %{_libdir}/evas/modules/savers/tiff/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/savers/tiff/%{arch_tag}/module.so

%files -n evas-saver-webp
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/savers/webp
%dir %{_libdir}/evas/modules/savers/webp/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/savers/webp/%{arch_tag}/module.so

%files -n vim-addon-efl
%defattr(644,root,root,755)
%doc data/edje/vim/plugin-info.txt
%{_datadir}/vim/autoload/edccomplete.vim
%{_datadir}/vim/vimfiles/ftdetect/edc.vim
%{_datadir}/vim/vimfiles/ftplugin/edc.vim
%{_datadir}/vim/vimfiles/indent/edc.vim
# owner?
%dir %{_datadir}/vim/vimfiles/snippets
%{_datadir}/vim/vimfiles/snippets/edc.snippets
%{_datadir}/vim/vimfiles/syntax/edc.vim
%{_datadir}/vim/vimfiles/syntax/embryo.vim

%changelog
