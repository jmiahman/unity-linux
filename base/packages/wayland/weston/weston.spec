Name:           weston
Version:        1.9.0
Release:        1%{?dist}
Summary:        Reference compositor for Wayland
Group:          User Interface/X
License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  cairo-devel >= 1.10.0
BuildRequires:  glib2-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2
BuildRequires:  libinput-devel >= 0.8
# libunwind available only on selected arches
%ifarch %{arm} aarch64 hppa ia64 mips ppc %{power64} %{ix86} x86_64
BuildRequires:	libunwind-devel
%endif
BuildRequires:  libva-devel
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel >= 1.3.0
BuildRequires:  libwayland-cursor-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxkbcommon-devel >= 0.1.0-8
BuildRequires:  mesa-libEGL-devel >= 8.1
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libwayland-egl-devel
BuildRequires:  mtdev-devel
BuildRequires:  pam-devel
BuildRequires:  pixman-devel
BuildRequires:  poppler-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  systemd-devel
BuildRequires:  dbus-devel
BuildRequires:  lcms2-devel
BuildRequires:  colord-devel
BuildRequires:  freerdp-devel >= 1.1.0

%description
Weston is the reference wayland compositor that can run on KMS, under X11
or under another compositor.

%package devel
Summary: Common headers for weston
License: MIT
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Common headers for weston

%prep
%setup -q

%build
%configure --disable-static --disable-setuid-install --enable-xwayland \
           --enable-rdp-compositor
make %{?_smp_mflags}

%install
%make_install

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%files
%doc README
%license COPYING
%{_bindir}/weston
%{_bindir}/weston-info
%attr(4755,root,root) %{_bindir}/weston-launch
%{_bindir}/weston-terminal
%{_bindir}/wcap-decode
%dir %{_libdir}/weston
%{_libdir}/weston/cms-colord.so
%{_libdir}/weston/cms-static.so
%{_libdir}/weston/desktop-shell.so
%{_libdir}/weston/drm-backend.so
%{_libdir}/weston/fbdev-backend.so
%{_libdir}/weston/headless-backend.so
%{_libdir}/weston/rdp-backend.so
%{_libdir}/weston/gl-renderer.so
%{_libdir}/weston/wayland-backend.so
%{_libdir}/weston/x11-backend.so
%{_libdir}/weston/xwayland.so
%{_libdir}/weston/fullscreen-shell.so
%{_libdir}/weston/hmi-controller.so
%{_libdir}/weston/ivi-shell.so
%{_libexecdir}/weston-*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%dir %{_datadir}/weston
%{_datadir}/weston/*.png
%{_datadir}/weston/wayland.svg
%{_datadir}/wayland-sessions/weston.desktop

%files devel
%dir %{_includedir}/weston
%{_includedir}/weston/compositor.h
%{_includedir}/weston/config-parser.h
%{_includedir}/weston/timeline-object.h
%{_includedir}/weston/matrix.h
%{_includedir}/weston/platform.h
%{_includedir}/weston/version.h
%{_includedir}/weston/zalloc.h
%{_libdir}/pkgconfig/weston.pc

%changelo
