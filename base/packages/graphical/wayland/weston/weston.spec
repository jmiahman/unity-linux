Name:           weston
Version:        1.9.0
Release:        1%{?dist}
Summary:        Reference compositor for Wayland
Group:          User Interface/X
License:        BSD and CC-BY-SA
URL:            http://wayland.freedesktop.org/
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  cairo-devel
BuildRequires:  glib-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libinput-devel
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel
BuildRequires:  libwayland-cursor-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  mtdev-devel
BuildRequires:  pixman-devel

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
%configure \
	--disable-egl \
	--disable-x11-compositor \
	--enable-demo-clients-install \
	--disable-weston-launch \
	WESTON_NATIVE_BACKEND="fbdev-backend.so" \

#--disable-drm-compositor \

make %{?_smp_mflags}

%install
%make_install

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%files
%doc README
#%license COPYING
%{_bindir}/weston
%{_bindir}/weston-info
#%attr(4755,root,root) %{_bindir}/weston-launch
%{_bindir}/weston-terminal
%{_bindir}/wcap-decode
%dir %{_libdir}/weston
#%{_libdir}/weston/cms-colord.so
%{_libdir}/weston/cms-static.so
%{_libdir}/weston/desktop-shell.so
#%{_libdir}/weston/drm-backend.so
%{_libdir}/weston/fbdev-backend.so
%{_libdir}/weston/headless-backend.so
#%{_libdir}/weston/rdp-backend.so
#%{_libdir}/weston/gl-renderer.so
#%{_libdir}/weston/wayland-backend.so
#%{_libdir}/weston/x11-backend.so
#%{_libdir}/weston/xwayland.so
%{_libdir}/weston/fullscreen-shell.so
%{_libdir}/weston/hmi-controller.so
%{_libdir}/weston/ivi-shell.so
%{_libexecdir}/weston-*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
#%{_mandir}/man7/*.7*
%dir %{_datadir}/weston
%{_datadir}/weston/*.png
%{_datadir}/weston/wayland.svg
%dir %{_datadir}/wayland-sessions/
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

%changelog
