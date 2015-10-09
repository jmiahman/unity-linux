%define _target_platform %{_arch}-unity-linux-musl

Name:		lvm2	
Version:	2.02.132
Release:	1%{?dist}
Summary:	Userland logical volume management tools

Group:		System Environment/Base
License:	GPLv2
URL:		http://sources.redhat.com/lvm2

Source0:	ftp://sources.redhat.com/pub/lvm2/LVM2.2.02.132.tgz
Source1:	lvm.initd
Source2:	lvm.confd
Source3:	dmeventd.initd

BuildRequires: libblkid-devel
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: %{name}-libs = %{version}-%{release}

Patch0:	fix-stdio-usage.patch
Patch1:	mallinfo.patch
Patch2:	library_dir-default-config.patch
Patch3:	mlockall-default-config.patch

%description
LVM2 includes all of the support for handling read/write operations on
physical volumes (hard disks, RAID-Systems, magneto optical, etc.,
multiple devices (MD), see mdadd(8) or even loop devices, see
losetup(8)), creating volume groups (kind of virtual disks) from one
or more physical volumes and creating one or more logical volumes
(kind of logical partitions) in volume groups.

%package dmeventd
Summary: Device-mapper event daemon
Group: System Environment/Base

%description dmeventd
dmeventd is the event monitoring daemon for device-mapper devices.

%package docs
Summary: Docs for LVM2
Group: System Environment/Base

%description docs
Documentation for Logical Volume Manager 2 utilities

%package libs
Summary: LVM2 shared libraries
Group: System Environment/Base

%description libs
This package contains shared lvm2 libraries for applications.

%package -n device-mapper
Summary: Device mapper userspace library and tools from LVM2
Group: System Environment/Base

%description -n device-mapper
The device mapper is a framework provided by the Linux kernel for 
mapping physical block devices onto higher-level virtual block devices. 
It forms the foundation of LVM2, software RAIDs and dm-crypt 
disk encryption, and offers additional features such as file 
system snapshots

%package devel
Summary: Devel files for LVM2
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: device-mapper = %{version}-%{release}

%description devel
Development files for Logical Volume Manager 2 utilities

%prep
%setup -q -n LVM2.%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -rf %{buildroot}
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc \
	--libdir=/lib \
	--sbindir=/sbin \
	--localstatedir=/var \
	--disable-nls \
	--disable-readline \
	--enable-pkgconfig \
	--enable-applib \
	--with-thin=internal \
	--enable-dmeventd \
	--enable-cmdlib \
	--with-thin-check=/sbin/thin_check \
	--with-thin-dump=/sbin/thin_dump \
	--with-thin-repair=/sbin/thin_repair \
	--with-dmeventd-path=/sbin/dmeventd \
	CLDFLAGS="$LDFLAGS" \

make



%install
make -j1 DESTDIR=%{buildroot} install

install -d %{buildroot}/etc/lvm/archive %{buildroot}/etc/lvm/backup
install -Dm755 %{SOURCE1} %{buildroot}/etc/init.d/lvm
install -Dm644 %{SOURCE2} %{buildroot}/etc/conf.d/lvm
cd %{buildroot}/lib
ln -s libdevmapper.so.1.02 libdevmapper.so
install -Dm755 %{SOURCE3} %{buildroot}/etc/init.d/dmeventd
gzip %{buildroot}/usr/share/man/man*/*


%files
/etc/init.d/lvm
/etc/conf.d/lvm
%dir /etc/lvm
/etc/lvm/lvmlocal.conf
%dir /etc/lvm/profile
/etc/lvm/profile/thin-generic.profile
/etc/lvm/profile/cache-mq.profile
/etc/lvm/profile/cache-smq.profile
/etc/lvm/profile/command_profile_template.profile
/etc/lvm/profile/metadata_profile_template.profile
/etc/lvm/profile/thin-performance.profile
/etc/lvm/lvm.conf
/lib/libdevmapper-event.so.1.02
/lib/libdevmapper-event-lvm2.so.2.02
%dir /lib/device-mapper/
/lib/device-mapper/libdevmapper-event-lvm2snapshot.so
/lib/device-mapper/libdevmapper-event-lvm2raid.so
/lib/device-mapper/libdevmapper-event-lvm2mirror.so
/lib/device-mapper/libdevmapper-event-lvm2thin.so
/sbin/vgsplit
/sbin/lvconvert
/sbin/lvdisplay
/sbin/lvremove
/sbin/pvck
/sbin/pvmove
/sbin/lvresize
/sbin/pvs
/sbin/blkdeactivate
/sbin/vgexport
/sbin/vgck
/sbin/vgmerge
/sbin/pvchange
/sbin/vgs
/sbin/vgchange
/sbin/vgdisplay
/sbin/lvmsadc
/sbin/lvcreate
/sbin/lvmchange
/sbin/vgcfgbackup
/sbin/lvmconf
/sbin/vgconvert
/sbin/pvremove
/sbin/lvmconfig
/sbin/vgmknodes
/sbin/lvs
/sbin/pvscan
/sbin/lvm
/sbin/pvdisplay
/sbin/vgextend
/sbin/vgimport
/sbin/lvrename
/sbin/lvmdump
/sbin/lvreduce

%files dmeventd
/etc/init.d/dmeventd
/sbin/dmeventd

%files docs
/usr/share/man/man5/lvm.conf.5.gz
/usr/share/man/man8/pvremove.8.gz
/usr/share/man/man8/lvmsadc.8.gz
/usr/share/man/man8/vgconvert.8.gz
/usr/share/man/man8/vgremove.8.gz
/usr/share/man/man8/vgs.8.gz
/usr/share/man/man8/pvchange.8.gz
/usr/share/man/man8/blkdeactivate.8.gz
/usr/share/man/man8/pvmove.8.gz
/usr/share/man/man8/lvresize.8.gz
/usr/share/man/man8/lvremove.8.gz
/usr/share/man/man8/vgscan.8.gz
/usr/share/man/man8/vgextend.8.gz
/usr/share/man/man8/vgmknodes.8.gz
/usr/share/man/man8/vgchange.8.gz
/usr/share/man/man8/vgmerge.8.gz
/usr/share/man/man8/lvcreate.8.gz
/usr/share/man/man8/lvextend.8.gz
/usr/share/man/man8/vgcfgbackup.8.gz
/usr/share/man/man8/vgcreate.8.gz
/usr/share/man/man8/vgrename.8.gz
/usr/share/man/man8/lvs.8.gz
/usr/share/man/man8/vgck.8.gz
/usr/share/man/man8/vgreduce.8.gz
/usr/share/man/man8/pvck.8.gz
/usr/share/man/man8/lvdisplay.8.gz
/usr/share/man/man8/lvmdiskscan.8.gz
/usr/share/man/man8/lvscan.8.gz
/usr/share/man/man8/pvs.8.gz
/usr/share/man/man8/lvchange.8.gz
/usr/share/man/man8/vgexport.8.gz
/usr/share/man/man8/lvm.8.gz
/usr/share/man/man8/lvm-config.8.gz
/usr/share/man/man8/lvm-lvpoll.8.gz
/usr/share/man/man8/lvmsar.8.gz
/usr/share/man/man8/vgsplit.8.gz
/usr/share/man/man8/lvmconfig.8.gz
/usr/share/man/man8/lvreduce.8.gz
/usr/share/man/man8/vgdisplay.8.gz
/usr/share/man/man8/vgcfgrestore.8.gz
/usr/share/man/man8/dmsetup.8.gz
/usr/share/man/man8/fsadm.8.gz
/usr/share/man/man8/lvrename.8.gz
/usr/share/man/man8/lvmconf.8.gz
/usr/share/man/man8/dmstats.8.gz
/usr/share/man/man8/dmeventd.8.gz
/usr/share/man/man8/vgimportclone.8.gz
/usr/share/man/man8/lvmchange.8.gz
/usr/share/man/man8/pvcreate.8.gz
/usr/share/man/man8/pvdisplay.8.gz

%files libs
/lib/liblvm2app.so.*.*
/lib/liblvm2cmd.so.*.*

%files -n device-mapper
/lib/libdevmapper.so.*.*
/sbin/dmstats
/sbin/dmsetup

%files devel
/lib/libdevmapper-event-lvm2snapshot.so
/lib/libdevmapper.so
/lib/libdevmapper-event-lvm2raid.so
/lib/libdevmapper-event-lvm2mirror.so
/lib/libdevmapper-event-lvm2thin.so
/usr/lib/libdevmapper.so
/usr/lib/liblvm2app.so
/usr/lib/libdevmapper-event-lvm2.so
/usr/lib/pkgconfig/devmapper.pc
/usr/lib/pkgconfig/lvm2app.pc
/usr/lib/pkgconfig/devmapper-event.pc
/usr/lib/liblvm2cmd.so
/usr/lib/libdevmapper-event.so
/usr/include/libdevmapper.h
/usr/include/lvm2cmd.h
/usr/include/libdevmapper-event.h
/usr/include/lvm2app.h

%changelog

