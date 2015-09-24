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
Source8:	consolefont.initd
Source9:	consolefont.confd
Source10:	openrc.logrotate

Patch0:		0001-Force-root-be-rw-before-localmount.patch
Patch1:		0001-sysctl.Linux.in-fix-for-busybox-sysctl.patch
Patch2:		swap-umount-tmpfs.patch
Patch3:		swap-ifexists.patch
Patch4:		hide-migrate-to-run-error.patch
Patch5:		rc-pull-in-sysinit-and-boot-as-stacked-levels-when-needed.patch
Patch6:		openrc-0.4.3-mkmntdirs.patch

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
%patch6 -p1

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
install -D -m755 %{SOURCE8} %{buildroot}/etc/init.d/consolefont
install -D -m644 %{SOURCE9} %{buildroot}/etc/conf.d/consolefont
install -d %{buildroot}/etc/local.d %{buildroot}/run

mkdir -p %{buildroot}/etc/runlevels
mkdir -p %{buildroot}/etc/runlevels/boot
mkdir -p %{buildroot}/etc/runlevels/default
mkdir -p %{buildroot}/etc/runlevels/shutdown
mkdir -p %{buildroot}/etc/runlevels/sysinit

cd %{buildroot}/etc/runlevels/boot
ln -sf /etc/init.d/bootmisc bootmisc
ln -sf /etc/init.d/hostname hostname
ln -sf /etc/init.d/hwclock hwclock
ln -sf /etc/init.d/modules modules
ln -sf /etc/init.d/sysctl sysctl
ln -sf /etc/init.d/syslog syslog

cd %{buildroot}/etc/runlevels/shutdown
ln -sf /etc/init.d/killprocs killprocs
ln -sf /etc/init.d/mount-ro mount-ro
ln -sf /etc/init.d/savecache savecache

cd %{buildroot}/etc/runlevels/sysinit
ln -sf /etc/init.d/devfs devfs
ln -sf /etc/init.d/dmesg dmesg
ln -sf /etc/init.d/hwdrivers hwdrivers
ln -sf /etc/init.d/mdev mdev
ln -sf /etc/init.d/modloop modloop

%files
%doc
/bin/rc-status
/etc/rc.conf
/etc/init.d/*
/etc/sysctl.d/README
/etc/conf.d/*
/etc/local.d/README
/lib/libeinfo.so.1
/lib/librc.so.1
/lib/rc/version
/lib/rc/sbin/*
/lib/rc/bin/*
/lib/rc/sh/*.sh
/sbin/*
/etc/runlevels/*
/etc/runlevels/boot/*
/etc/runlevels/shutdown/*
/etc/runlevels/sysinit/*

%dir /etc/runlevels
%dir /etc/runlevels/boot
%dir /etc/runlevels/shutdown
%dir /etc/runlevels/sysinit

%dir /etc/local.d
%dir /lib/rc/bin
%dir /lib/rc/sbin
%dir /lib/rc/sh
%dir /lib/rc

%changelog
