#
# Conditional build:
%bcond_with	aalib		# aalib graphics support
%bcond_with	caca		# caca graphics support
%bcond_with	directfb	# DirectFB graphics support
%bcond_with	ggi		# GGI graphics support
%bcond_with	nas		# NAS audio support
%bcond_with	svga		# svgalib graphics support
%bcond_without	alsa		# ALSA audio support
%bcond_with	arts		# aRts audio support
%bcond_with	esd		# EsounD audio support
%bcond_with	new_gamma_ramp  # causes crashes on nvidia drivers
%bcond_with	static_libs	# don't build static libraries
#
# NOTE: the following libraries are dlopened by soname detected at build time:
# libartsc.so.?		[if with arts]
# libasound.so.2	[if with alsa]
# libaudio.so.2		[if with nas]
# libesd.so.0		[if with esd]
# libpulse-simple.so.0
# libX11.so.6
# libXext.so.6
# libXrender.so.1
# libXrandr.so.2

%define         specflags_ppc   -maltivec
%define		_aclocaldir	%{_datadir}/aclocal
%define		_pkgconfigdir	%{_libdir}/pkgconfig

Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Name:		sdl
Version:	1.2.15
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.libsdl.org/release/SDL-%{version}.tar.gz
# Source0-md5:	9d96df8417572a2afb781a7c4c811a85
Patch0:		SDL-acfix.patch
Patch1:		SDL-new_gamma_ramp_support.patch
Patch2:		fix-mouse-click.patch
Patch3:		SDL-config.patch
Patch4:		SDL-const_XData32.patch
Patch5:		SDL-1.2.10-GrabNotViewable.patch


URL:		http://www.libsdl.org/
%{?with_directfb:BuildRequires:	directfb-devel}
BuildRequires:	glu-devel
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel >= 1.1}
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
BuildRequires:	gcc
%{?with_caca:BuildRequires:	libcaca-devel}
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libtool >= 2.0
%{?with_nas:BuildRequires:	nas-devel}
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	tslib-devel
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxrender-devel
BuildRequires:	xextproto

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%package devel
Summary:	SDL - Header files
Group:		Development/Libraries
Requires:	sdl = %{version}-%{release}
%{?with_directfb:Requires:	DirectFB-devel >= 0.9.15}
%{?with_aa:Requires:	aalib-devel}
%{?with_caca:Requires:	libcaca-devel}
%{?with_ggi:Requires:	libggi-devel}
%{?with_svga:Requires:	svgalib-devel >= 1.4.0}
Requires:	tslib-devel
Requires:	libx11-devel
Suggests:	glu-devel

%description devel
SDL - Header files.

%package static
Summary:	SDL - static libraries
Group:		Development/Libraries
Requires:	sdl-devel = %{version}-%{release}

%description static
SDL - static libraries.

%package examples
Summary:	SDL - example programs
License:	Public Domain
Group:		Development/Libraries
Requires:	sdl-devel = %{version}-%{release}

%description examples
SDL - example programs.

%prep
%setup -q -n SDL-%{version}
%patch0 -p1
%{?with_new_gamma_ramp:%patch1 -p1}
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

: > acinclude.m4
%{!?with_alsa:echo 'AC_DEFUN([AM_PATH_ALSA],[$3])' >> acinclude.m4}
%{!?with_esd:echo 'AC_DEFUN([AM_PATH_ESD],[$3])' >> acinclude.m4}

%build
%configure \
	--disable-nasm \
	--disable-nls \
	--disable-rpath \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_arts:--disable-arts} \
	--enable-dga \
	%{!?with_esd:--disable-esd} \
	%{!?with_nas:--disable-nas} \
	%{?with_aalib:--enable-video-aalib} \
	%{?with_caca:--enable-video-caca} \
	%{!?with_directfb:--disable-video-directfb} \
	--enable-video-dga \
	--enable-video-fbcon \
	%{?with_ggi:--enable-video-ggi} \
	--enable-video-opengl \
	%{!?with_svga:--disable-video-svga} \
	--enable-video-x11-dgamouse \
	--enable-video-x11-vm \
	--enable-video-x11-xinerama \
	--enable-video-x11-xme \
	--enable-video-x11-xrandr \
	--enable-video-x11-xv \
	--with-x \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/SDL-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -rf test/autom4te.cache
install test/* $RPM_BUILD_ROOT%{_examplesdir}/SDL-%{version}

rm -rf docs/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS README README-SDL.txt TODO WhatsNew
%attr(755,root,root) %{_libdir}/libSDL-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL-1.2.so.0

%files devel
%defattr(644,root,root,755)
%doc docs.html docs
%attr(755,root,root) %{_bindir}/sdl-config
%attr(755,root,root) %{_libdir}/libSDL.so
%{_libdir}/libSDL.la
%{_libdir}/libSDLmain.a
%{_includedir}/SDL
%{_aclocaldir}/sdl.m4
%{_pkgconfigdir}/sdl.pc
%{_mandir}/man3/SDL*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL.a
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/SDL-%{version}
