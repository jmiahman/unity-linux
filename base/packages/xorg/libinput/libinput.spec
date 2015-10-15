Name:           libinput
Version:        1.0.1
Release:        1%{?dist}
Summary:        Input device library
Group:          User Interface/X

License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/libinput/
Source0:        http://www.freedesktop.org/software/libinput/libinput-%{version}.tar.xz

# Not upstream, keep until kernel 4.2 or 4.1.x with dbf3c37086 
Patch01:        0001-touchpad-serial-synaptics-need-to-fake-new-touches-o.patch

# Bug 1256045 - Libinput regularly interprets two-finger scrolling as right-mouse click
Patch02:        0001-touchpad-don-t-tap-for-2fg-down-followed-by-a-single.patch

# fdo Bug 92016 - Multi-tap-and-drag sends one too many clicks
Patch03:        0001-touchpad-fix-the-number-of-button-clicks-in-multitap.patch

BuildRequires:  autoconf automake libtool pkgconfig
BuildRequires:  libevdev-devel
BuildRequires:  eudev-devel
BuildRequires:  mtdev-devel
BuildRequires:  eudev

%description
libinput is a library that handles input devices for display servers and other
applications that need to directly deal with input devices.

It provides device detection, device handling, input device event processing
and abstraction so minimize the amount of custom input code the user of
libinput need to provide the common set of functionality that users expect.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q 

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -v --install --force || exit 1
%configure --disable-static --disable-silent-rules --with-udev-dir=%{udevdir}
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete


%post
/sbin/ldconfig
/usr/bin/udevadm hwdb --update  >/dev/null 2>&1 || :

%postun -p /sbin/ldconfig


%files
%doc COPYING
%{_libdir}/libinput.so.*
%{udevdir}/libinput-device-group
%{udevdir}/libinput-model-quirks
%{udevdir}/rules.d/80-libinput-device-groups.rules
%{udevdir}/rules.d/90-libinput-model-quirks.rules
%{udevdir}/hwdb.d/90-libinput-model-quirks.hwdb
%{_bindir}/libinput-list-devices
%{_bindir}/libinput-debug-events
%{_mandir}/man1/libinput-list-devices.1*
%{_mandir}/man1/libinput-debug-events.1*

%files devel
%{_includedir}/libinput.h
%{_libdir}/libinput.so
%{_libdir}/pkgconfig/libinput.pc


%changelog
