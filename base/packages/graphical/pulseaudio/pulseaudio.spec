%define		_sysconfdir	/etc

Name:           pulseaudio
Summary:        Improved Linux Sound Server
Version:        7.1
Release:        1%{?dist}
Group:		Libraries
License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/PulseAudio
Source0:        http://freedesktop.org/software/pulseaudio/releases/pulseaudio-%{version}.tar.xz

Source1:	%{name}.initd
Source2:	%{name}.confd

Patch0:		xlocale.patch	
Patch1:		0001-padsp-Make-it-compile-on-musl.patch

BuildRequires:  glib-devel
BuildRequires:  xproto
BuildRequires:  libxtst-devel
BuildRequires:  libxi-devel
BuildRequires:  libsm-devel
BuildRequires:  libx11-devel
BuildRequires:  libice-devel
BuildRequires:  dbus-devel

Requires(pre): shadow
Requires: libattr
Requires: libuuid
Requires: util-linux
Requires: dbus-libs
Requires: flac
Requires: json-c
Requires: libasyncns
Requires: libcap
Requires: libice
Requires: libltdl
Requires: libogg
Requires: libsm
Requires: libsndfile
Requires: libvorbis
Requires: libx11
Requires: libxau
Requires: libxcb
Requires: libxext
Requires: libxi
Requires: libxtst
Requires: speexdsp
Requires: tdb
Requires: %{name}-libs = %{version}-%{release}

%description
PulseAudio is a sound server for Linux and other Unix like operating
systems. It is intended to be an improved drop-in replacement for the
Enlightened Sound Daemon (ESOUND).

%package libs
Summary:        Libraries for PulseAudio clients
License:        LGPLv2+

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PulseAudio sound server.

%package libs-glib
Summary:        GLIB 2.x bindings for PulseAudio clients
License:        LGPLv2+
Requires:       %{name}-libs = %{version}-%{release}

%description libs-glib
This package contains bindings to integrate the PulseAudio client library with
a GLIB 2.x based application.

%package devel
Summary:        Headers and libraries for PulseAudio client development
License:        LGPLv2+
Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-libs-glib = %{version}-%{release}
%description devel
Headers and libraries for developing applications that can communicate with
a PulseAudio sound server.

%package esound-compat
Summary:        PulseAudio EsounD daemon compatibility script
Requires:       %{name} = %{version}-%{release}
%description esound-compat
A compatibility script that allows applications to call /usr/bin/esd
and start PulseAudio with EsounD protocol modules.

%package module-x11
Summary:        X11 support for the PulseAudio sound server
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-utils

%description module-x11
X11 bell and security modules for the PulseAudio sound server.

%package utils
Summary:        PulseAudio sound server utilities
License:        LGPLv2+
Requires:       %{name}-libs = %{version}-%{release}

%description utils
This package contains command line utilities for the PulseAudio sound server.


%prep
%setup -q -n %{name}-%{version}

%patch0 -p0
%patch1 -p1

%build
LDFLAGS="$LDFLAGS -lintl" \
./configure \
  --prefix=/usr \
  --sysconfdir=%{_sysconfdir} \
  --disable-static \
  --disable-rpath \
  --localstatedir=/var \
  --with-system-user=pulse \
  --with-system-group=pulse \
  --with-access-group=pulse-access \
  --disable-oss-output \
  --disable-jack \
  --disable-lirc \
  --disable-bluez4 \
  --disable-bluez5 \
  --enable-udev \
  --with-udev-rules-dir=/lib/udev/rules.d/ \
  --disable-systemd 

make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

## unpackaged files
rm -fv $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/*.la

#gzip man pages and resymlink them
for file in %{buildroot}%{_mandir}/man1/* ; do
    if ! [[ -L "$file" ]]; then 
    	gzip $file; 
    else 
    	sympath=`readlink $file`
	ln -sf $sympath.gz $file.gz
	rm $file
    fi
done

#copy openrc service files
install -d %{buildroot}/etc/init.d/
install -d %{buildroot}/etc/conf.d/
install -D -m755 %{SOURCE1} \
	%{buildroot}/etc/init.d/%{name}
install -D -m644 %{SOURCE2} \
	%{buildroot}/etc/conf.d/%{name}

%pre
getent group pulse >/dev/null || groupadd -r pulse
getent passwd pulse >/dev/null || useradd -r -g pulse -d /dev/null -s /sbin/nologin \
	-c "account for pulseaudio" pulse
exit 0

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post libs-glib -p /sbin/ldconfig
%postun libs-glib -p /sbin/ldconfig

%files
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %{_sysconfdir}/pulse/system.pa
%{_sysconfdir}/init.d/%{name}
%{_sysconfdir}/conf.d/%{name}
%{_sysconfdir}/dbus-1/system.d/pulseaudio-system.conf
#%dir %{_sysconfdir}/bash_completion.d/
#%{_sysconfdir}/bash_completion.d/pa*
#%{_sysconfdir}/bash_completion.d/pulseaudio
#%{_datadir}/zsh/site-functions/_pulseaudio
%{_bindir}/pulseaudio
%{_libdir}/libpulsecore-%{version}.so
%dir %{_libdir}/pulse-%{version}/
%dir %{_libdir}/pulse-%{version}/modules/
%{_libdir}/pulse-%{version}/modules/libcli.so
%{_libdir}/pulse-%{version}/modules/libprotocol-cli.so
%{_libdir}/pulse-%{version}/modules/libprotocol-esound.so
%{_libdir}/pulse-%{version}/modules/libprotocol-http.so
%{_libdir}/pulse-%{version}/modules/libprotocol-native.so
%{_libdir}/pulse-%{version}/modules/libprotocol-simple.so
%{_libdir}/pulse-%{version}/modules/librtp.so
%if 0%{?with_webrtc}
%{_libdir}/pulse-%{version}/modules/libwebrtc-util.so
%endif
%{_libdir}/pulse-%{version}/modules/module-cli-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-cli-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-cli.so
%{_libdir}/pulse-%{version}/modules/module-combine.so
%{_libdir}/pulse-%{version}/modules/module-combine-sink.so
%{_libdir}/pulse-%{version}/modules/module-dbus-protocol.so
%{_libdir}/pulse-%{version}/modules/module-filter-apply.so
%{_libdir}/pulse-%{version}/modules/module-filter-heuristics.so
%{_libdir}/pulse-%{version}/modules/module-device-manager.so
%{_libdir}/pulse-%{version}/modules/module-loopback.so
%{_libdir}/pulse-%{version}/modules/module-esound-compat-spawnfd.so
%{_libdir}/pulse-%{version}/modules/module-esound-compat-spawnpid.so
%{_libdir}/pulse-%{version}/modules/module-esound-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-esound-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-esound-sink.so
%{_libdir}/pulse-%{version}/modules/module-http-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-http-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-match.so
%{_libdir}/pulse-%{version}/modules/module-mmkbd-evdev.so
%{_libdir}/pulse-%{version}/modules/module-native-protocol-fd.so
%{_libdir}/pulse-%{version}/modules/module-native-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-native-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-null-sink.so
%{_libdir}/pulse-%{version}/modules/module-null-source.so
%{_libdir}/pulse-%{version}/modules/module-pipe-sink.so
%{_libdir}/pulse-%{version}/modules/module-pipe-source.so
%{_libdir}/pulse-%{version}/modules/module-remap-source.so
%{_libdir}/pulse-%{version}/modules/module-rescue-streams.so
%{_libdir}/pulse-%{version}/modules/module-role-ducking.so
%{_libdir}/pulse-%{version}/modules/module-rtp-recv.so
%{_libdir}/pulse-%{version}/modules/module-rtp-send.so
%{_libdir}/pulse-%{version}/modules/module-simple-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-simple-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-sine.so
%{_libdir}/pulse-%{version}/modules/module-switch-on-port-available.so
%{_libdir}/pulse-%{version}/modules/module-udev-detect.so
%{_libdir}/pulse-%{version}/modules/module-tunnel-sink-new.so
%{_libdir}/pulse-%{version}/modules/module-tunnel-sink.so
%{_libdir}/pulse-%{version}/modules/module-tunnel-source-new.so
%{_libdir}/pulse-%{version}/modules/module-tunnel-source.so
%{_libdir}/pulse-%{version}/modules/module-volume-restore.so
%{_libdir}/pulse-%{version}/modules/module-suspend-on-idle.so
%{_libdir}/pulse-%{version}/modules/module-default-device-restore.so
%{_libdir}/pulse-%{version}/modules/module-device-restore.so
%{_libdir}/pulse-%{version}/modules/module-stream-restore.so
%{_libdir}/pulse-%{version}/modules/module-card-restore.so
%{_libdir}/pulse-%{version}/modules/module-ladspa-sink.so
%{_libdir}/pulse-%{version}/modules/module-remap-sink.so
%{_libdir}/pulse-%{version}/modules/module-always-sink.so
%{_libdir}/pulse-%{version}/modules/module-console-kit.so
%{_libdir}/pulse-%{version}/modules/module-position-event-sounds.so
%{_libdir}/pulse-%{version}/modules/module-augment-properties.so
%{_libdir}/pulse-%{version}/modules/module-role-cork.so
%{_libdir}/pulse-%{version}/modules/module-sine-source.so
%{_libdir}/pulse-%{version}/modules/module-intended-roles.so
%{_libdir}/pulse-%{version}/modules/module-rygel-media-server.so
%{_libdir}/pulse-%{version}/modules/module-echo-cancel.so
%{_libdir}/pulse-%{version}/modules/module-switch-on-connect.so
%{_libdir}/pulse-%{version}/modules/module-virtual-sink.so
%{_libdir}/pulse-%{version}/modules/module-virtual-source.so
%{_libdir}/pulse-%{version}/modules/module-virtual-surround-sink.so
%{_libdir}/pulse-%{version}/modules/libraop.so
%{_libdir}/pulse-%{version}/modules/module-detect.so
%{_libdir}/pulse-%{version}/modules/module-raop-sink.so

%{_mandir}/man1/pulseaudio.1*
%{_mandir}/man5/default.pa.5*
%{_mandir}/man5/pulse-cli-syntax.5*
%{_mandir}/man5/pulse-client.conf.5*
%{_mandir}/man5/pulse-daemon.conf.5*

%files libs
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%{_libdir}/libpulse.so.0*
%{_libdir}/libpulse-simple.so.0*
%dir %{_libdir}/pulseaudio/
%{_libdir}/pulseaudio/libpulsecommon-%{version}.*
%{_libdir}/pulseaudio/libpulsedsp.*

%files libs-glib
%{_libdir}/libpulse-mainloop-glib.so.0*

%files devel
%{_includedir}/pulse/
%{_libdir}/libpulse.so
%{_libdir}/libpulse-mainloop-glib.so
%{_libdir}/libpulse-simple.so
%{_libdir}/pkgconfig/libpulse*.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libpulse.vapi
%{_datadir}/vala/vapi/libpulse.deps
%{_datadir}/vala/vapi/libpulse-simple.vapi
%{_datadir}/vala/vapi/libpulse-simple.deps
%{_datadir}/vala/vapi/libpulse-mainloop-glib.vapi
%{_datadir}/vala/vapi/libpulse-mainloop-glib.deps
%dir %{_libdir}/cmake
%{_libdir}/cmake/PulseAudio/

%files esound-compat
%{_bindir}/esdcompat
%{_mandir}/man1/esdcompat.1.gz

%files module-x11
%{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%{_bindir}/start-pulseaudio-x11
%{_libdir}/pulse-%{version}/modules/module-x11-bell.so
%{_libdir}/pulse-%{version}/modules/module-x11-publish.so
%{_libdir}/pulse-%{version}/modules/module-x11-xsmp.so
%{_libdir}/pulse-%{version}/modules/module-x11-cork-request.so
%{_mandir}/man1/start-pulseaudio-x11.1.gz

%files utils
%{_bindir}/pacat
%{_bindir}/pacmd
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pamon
%{_bindir}/parecord
%{_bindir}/pax11publish
%{_bindir}/padsp
%ifarch %{multilib_archs}
%{_bindir}/padsp-32
%endif
%{_bindir}/pasuspender
%{_mandir}/man1/pacat.1.gz
%{_mandir}/man1/pacmd.1.gz
%{_mandir}/man1/pactl.1.gz
%{_mandir}/man1/paplay.1.gz
%{_mandir}/man1/pasuspender.1.gz
%{_mandir}/man1/padsp.1.gz
%{_mandir}/man1/pax11publish.1.gz

%changelog
