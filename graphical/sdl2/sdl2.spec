#
# Conditional build:
%bcond_with	directfb	# DirectFB graphics support
%bcond_with	nas		# NAS audio support
%bcond_without	alsa		# ALSA audio support
%bcond_with	arts		# aRts audio support
%bcond_with	esd		# EsounD audio support
%bcond_without	gl		# OpenGL (GLX) support
%bcond_without	gles		# OpenGL ES (EGL) support
%bcond_with	mir		# Mir graphics support
%bcond_with	wayland		# Wayland graphics support
%bcond_without	static_libs	# don't build static libraries
%bcond_with	mmx		# MMX instructions
%bcond_with	sse		# SSE instructions
%bcond_with	sse2		# SSE2 instructions
%bcond_with	3dnow		# 3Dnow! instructions
%bcond_with	altivec		# Altivec instructions

%ifarch k6 athlon
%define	with_3dnow	1
%endif
%ifarch %{x8664} pentium2 pentium3 pentium4 athlon
%define	with_mmx	1
%endif
%ifarch %{x8664} pentium3 pentium4
%define	with_sse	1
%endif
%ifarch %{x8664} pentium4
%define	with_sse2	1
%endif

Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Name:		sdl2
Version:	2.0.3
Release:	1
License:	Zlib (BSD-like)
Group:		Libraries
Source0:	http://www.libsdl.org/release/SDL2-%{version}.tar.gz
# Source0-md5:	fe6c61d2e9df9ef570e7e80c6e822537
Patch0:		%{name}-config.patch
Patch1:		%{name}-cflags.patch
URL:		http://www.libsdl.org/
%{?with_wayland:BuildRequires:	Mesa-libwayland-egl-devel}
%{?with_directfb:BuildRequires:	DirectFB-devel >= 1.0.0}
%{?with_directfb:BuildRequires:	FusionSound-devel >= 1.1.1}
%{?with_gl:BuildRequires:	mesa-libgl-devel}
%{?with_gles:BuildRequires:	mesa-libgles-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%{?with_arts:BuildRequires:	artsc-devel >= 1.1}
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	dbus-devel
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
BuildRequires:	gcc >= 4.0
BuildRequires:	libtool >= 2.0
%{?with_mir:BuildRequires:	mir-devel}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	perl
BuildRequires:	pkgconfig >= 0.7
BuildRequires:	pulseaudio-devel >= 0.9
BuildRequires:	tslib-devel
BuildRequires:	eudev-devel
# wayland-client, wayland-cursor
%{?with_wayland:BuildRequires:	wayland-devel}
BuildRequires:	libx11-devel
BuildRequires:	libxscrnsaver-devel
BuildRequires:	libxcursor-devel
BuildRequires:	libxext-devel
BuildRequires:	libxi-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxrender-devel
BuildRequires:	libxxf86vm-devel
%if %{with mir} || %{with wayland}
BuildRequires:	libxkbcommon-devel
%endif
BuildRequires:	xextproto

%define		specflags_ppc	-maltivec

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%package devel
Summary:	SDL - Header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_directfb:Requires:	directfb-devel >= 1.0.0}
Requires:	tslib-devel
Requires:	libx11-devel
Suggests:	glu-devel

%description devel
SDL - Header files.

%package static
Summary:	SDL - static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SDL - static libraries.

%package examples
Summary:	SDL - example programs
License:	Public Domain
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
SDL - example programs.

%prep
%setup -q -n SDL2-%version 
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I acinclude
%{__autoconf}
%configure \
	%{!?with_3dnow:--disable-3dnow} \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_altiveca:--disable-altivec} \
	%{!?with_arts:--disable-arts} \
	%{!?with_esd:--disable-esd} \
	%{!?with_mmx:--disable-mmx} \
	%{!?with_nas:--disable-nas} \
	--disable-rpath \
	%{!?with_sse:--disable-sse --disable-ssemath} \
	%{!?with_sse2:--disable-sse2} \
	%{?with_sse:--enable-ssemath} \
	%{!?with_static_libs:--disable-static} \
	%{!?with_directfb:--disable-video-directfb} \
	%{?with_mir:--enable-video-mir} \
	--enable-video-opengl%{!?with_opengl:=no} \
	--enable-video-opengles%{!?with_gles:=no} \
	%{?with_wayland:--enable-video-wayland} \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_datadir}/aclocal

cp -pr test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# non-Linux READMEs packaged for portability information
%doc BUGS.txt COPYING.txt CREDITS.txt README*.txt TODO.txt WhatsNew.txt
%attr(755,root,root) %{_libdir}/libSDL2-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libSDL2-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sdl2-config
%attr(755,root,root) %{_libdir}/libSDL2.so
%{_libdir}/libSDL2.la
%{_libdir}/libSDL2_test.a
%{_libdir}/libSDL2main.a
%{_includedir}/SDL2
%{_datadir}/aclocal/sdl2.m4
%{_libdir}/pkgconfig/sdl2.pc

#%if %{with static_libs}
#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libSDL2.a
#%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
