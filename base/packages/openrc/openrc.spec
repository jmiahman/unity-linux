Name:		openrc
Version:	0.17
Release:	1%{?dist}
Summary:	OpenRC manages the services, startup and shutdown of a host

Group:		System Environment/Base
License:	FreeBSD License
URL:		https://wiki.gentoo.org/wiki/Project:OpenRC
Source0:	http://github.com/OpenRC/openrc/archive/%{version}.tar.gz

Source1:	hostname.initd
Source2:	hwdrivers.initd
Source3:	keymaps.initd
Source4:	modules.initd
Source5:	modloop.initd
Source6:	networking.initd
Source7:	modloop.confd

Patch0:		0001-Force-root-be-rw-before-localmount.patch
Patch1:		0001-sysctl.Linux.in-fix-for-busybox-sysctl.patch
Patch2:		swap-umount-tmpfs.patch
Patch3:		swap-ifexists.patch
Patch4:		hide-migrate-to-run-error.patch
Patch5:		rc-pull-in-sysinit-and-boot-as-stacked-levels-when-needed.patch

#BuildRequires:	
#Requires:	

%description
OpenRC is a dependency based init system that works with the system provided init program, normally located at /sbin/init. It is not a replacement for /sbin/init.

%prep
%setup -qn %{name}-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1 
%patch3 -p1 
%patch4 -p1 
%patch5 -p1 

sed -i -e '/^sed/d' pkgconfig/Makefile
%build
make LIBEXECDIR=/lib/rc

%install
rm -rf %{buildroot}

make LIBEXECDIR=/lib/rc DESTDIR=%{buildroot} install

rm -f %{buildroot}/etc/runlevels/*/*
rm -f %{buildroot}/etc/conf.d/network %{buildroot}/etc/init.d/network

install -D -m755 %{SOURCE1} %{buildroot}/etc/init.d/hostname
install -D -m755 %{SOURCE2} %{buildroot}/etc/init.d/hwdrivers
install -D -m755 %{SOURCE3} %{buildroot}/etc/init.d/keymaps
install -D -m755 %{SOURCE4} %{buildroot}/etc/init.d/modules
install -D -m755 %{SOURCE5} %{buildroot}/etc/init.d/modloop
install -D -m755 %{SOURCE6} %{buildroot}/etc/init.d/networking

install -D -m644 %{SOURCE7} %{buildroot}/etc/conf.d/modloop
install -d %{buildroot}/etc/local.d %{buildroot}/run

%files
%doc
/bin/rc-status
/etc/rc.conf
/etc/init.d/consolefont
/etc/init.d/modloop
/etc/init.d/tmpfiles.dev
/etc/init.d/localmount
/etc/init.d/swap
/etc/init.d/sysfs
/etc/init.d/devfs
/etc/init.d/networking
/etc/init.d/root
/etc/init.d/loopback
/etc/init.d/mtab
/etc/init.d/bootmisc
/etc/init.d/fsck
/etc/init.d/savecache
/etc/init.d/swclock
/etc/init.d/hwdrivers
/etc/init.d/netmount
/etc/init.d/swapfiles
/etc/init.d/staticroute
/etc/init.d/sysctl
/etc/init.d/osclock
/etc/init.d/local
/etc/init.d/hwclock
/etc/init.d/keymaps
/etc/init.d/hostname
/etc/init.d/numlock
/etc/init.d/tmpfiles.setup
/etc/init.d/modules
/etc/init.d/mount-ro
/etc/init.d/dmesg
/etc/init.d/procfs
/etc/init.d/binfmt
/etc/init.d/urandom
/etc/init.d/functions.sh
/etc/init.d/killprocs
/etc/init.d/termencoding
/etc/sysctl.d/README
/etc/conf.d/consolefont
/etc/conf.d/modloop
/etc/conf.d/localmount
/etc/conf.d/devfs
/etc/conf.d/bootmisc
/etc/conf.d/fsck
/etc/conf.d/tmpfiles
/etc/conf.d/netmount
/etc/conf.d/staticroute
/etc/conf.d/hwclock
/etc/conf.d/keymaps
/etc/conf.d/hostname
/etc/conf.d/modules
/etc/conf.d/dmesg
/etc/conf.d/urandom
/etc/conf.d/killprocs
/etc/local.d/README
/lib/libeinfo.so.1
/lib/librc.so.1
/lib/rc/version
/lib/rc/sbin/mark_service_failed
/lib/rc/sbin/mark_service_hotplugged
/lib/rc/sbin/mark_service_stopped
/lib/rc/sbin/mark_service_started
/lib/rc/sbin/swclock
/lib/rc/sbin/mark_service_inactive
/lib/rc/sbin/rc-abort
/lib/rc/sbin/mark_service_wasinactive
/lib/rc/sbin/mark_service_stopping
/lib/rc/sbin/mark_service_starting
/lib/rc/bin/service_started
/lib/rc/bin/service_started_daemon
/lib/rc/bin/eoutdent
/lib/rc/bin/einfo
/lib/rc/bin/service_crashed
/lib/rc/bin/eval_ecolors
/lib/rc/bin/veindent
/lib/rc/bin/on_ac_power
/lib/rc/bin/eend
/lib/rc/bin/vewarn
/lib/rc/bin/eerror
/lib/rc/bin/get_options
/lib/rc/bin/service_get_value
/lib/rc/bin/service_starting
/lib/rc/bin/ebegin
/lib/rc/bin/esyslog
/lib/rc/bin/service_wasinactive
/lib/rc/bin/ewarnn
/lib/rc/bin/veinfo
/lib/rc/bin/is_newer_than
/lib/rc/bin/service_stopping
/lib/rc/bin/vebegin
/lib/rc/bin/save_options
/lib/rc/bin/ewaitfile
/lib/rc/bin/checkpath
/lib/rc/bin/eindent
/lib/rc/bin/service_stopped
/lib/rc/bin/eerrorn
/lib/rc/bin/is_older_than
/lib/rc/bin/vewend
/lib/rc/bin/rc-depend
/lib/rc/bin/fstabinfo
/lib/rc/bin/einfon
/lib/rc/bin/veend
/lib/rc/bin/service_hotplugged
/lib/rc/bin/mountinfo
/lib/rc/bin/ewend
/lib/rc/bin/service_inactive
/lib/rc/bin/ewarn
/lib/rc/bin/service_set_value
/lib/rc/bin/veoutdent
/lib/rc/bin/shell_var
/lib/rc/sh/gendepends.sh
/lib/rc/sh/migrate-to-run.sh
/lib/rc/sh/openrc-run.sh
/lib/rc/sh/binfmt.sh
/lib/rc/sh/rc-cgroup.sh
/lib/rc/sh/init.sh
/lib/rc/sh/init-early.sh
/lib/rc/sh/tmpfiles.sh
/lib/rc/sh/functions.sh
/lib/rc/sh/rc-mount.sh
/lib/rc/sh/rc-functions.sh
/lib/rc/sh/cgroup-release-agent.sh
/sbin/runscript
/sbin/rc-update
/sbin/rc
/sbin/start-stop-daemon
/sbin/rc-service
/sbin/openrc-run
/sbin/service
/sbin/openrc

%dir /etc/local.d
%dir /lib/rc/bin
%dir /lib/rc/sbin
%dir /lib/rc/sh
%dir /lib/rc

%changelog
