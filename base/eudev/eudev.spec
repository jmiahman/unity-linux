%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64
%define _lib /lib64

%define _sysconfdir /etc

Summary:	Programs for dynamic creation of device nodes
Name:		eudev
Version:	3.1.2
Release:	1
License:	GPLv2
URL:		http://www.gentoo.org/proj/en/eudev
Group:		Base/System
Source0:	http://dev.gentoo.org/~blueness/eudev/eudev-3.1.2.tar.gz
Source1:	setup-udev
Source2:	udev-postmount.initd

BuildRequires:	gperf glib-devel linux-headers kmod-devel

%description
The eudev package contains programs for dynamic creation of device nodes.

%package devel                                                          
Summary: Development tools for %{name}
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel. 

%prep
%setup -q

sed -r -i 's|/usr(/bin/test)|\1|'      test/udev-test.pl

%build
aclocal
automake --add-missing
./configure \
	--bindir=/sbin \
	--sbindir=/sbin \
	--sysconfdir=/etc \
	--with-rootprefix= \
	--with-rootrundir=/run \
	--with-rootlibexecdir=/lib/udev \
	--libdir=%{_libdir} \
	--enable-split-usr \
	--enable-manpages \
	--disable-hwdb \
	--enable-kmod \
	--exec-prefix=/ \
	--enable-gudev \
	--enable-introspection \

make

make VERBOSE=1 %{?_smp_mflags}
install -vdm 755 %{buildroot}%{_sysconfdir}/udev/rules.d
%install
rm -rf %{buildroot}
install -vdm 755 %{buildroot}/%{_lib}/firmware
install -vdm 755 %{buildroot}/%{_lib}/udev/devices/pts
install -vdm 755 %{buildroot}/%{_lib}/udev/rules.d
install -vdm 755 %{buildroot}%{_sysconfdir}/udev/hwdb.d
install -vdm 755 %{buildroot}%{_sysconfdir}/udev/rules.d

make DESTDIR=%{buildroot} install
# symlink udevd to /lib/udev/udevd
ln -vs /sbin/udevd %{buildroot}/lib/udev/
mv %{buildroot}/usr/share/pkgconfig/udev.pc %{buildroot}%{_libdir}/pkgconfig
rmdir %{buildroot}/usr/share/pkgconfig
find %{buildroot} -name '*.la' -delete

install -m755 %{SOURCE1} %{buildroot}/sbin/setup-udev
install -dm755 %{buildroot}/etc/init.d/
install -m755 %{SOURCE2} %{buildroot}/etc/init.d/udev-postmount

%post
/sbin/ldconfig
/sbin/udevadm hwdb --update

%postun	-p /sbin/ldconfig

%files 
%defattr(-,root,root)
/lib/udev/accelerometer
/lib/udev/ata_id
/lib/udev/cdrom_id
/lib/udev/collect
/lib/udev/mtd_probe
/lib/udev/rules.d/42-usb-hid-pm.rules
/lib/udev/rules.d/50-udev-default.rules
/lib/udev/rules.d/60-cdrom_id.rules
/lib/udev/rules.d/60-drm.rules
/lib/udev/rules.d/60-persistent-alsa.rules
/lib/udev/rules.d/60-persistent-input.rules
/lib/udev/rules.d/60-persistent-storage-tape.rules
/lib/udev/rules.d/60-persistent-storage.rules
/lib/udev/rules.d/60-persistent-v4l.rules
/lib/udev/rules.d/61-accelerometer.rules
/lib/udev/rules.d/64-btrfs.rules
/lib/udev/rules.d/75-net-description.rules
/lib/udev/rules.d/75-probe_mtd.rules
/lib/udev/rules.d/78-sound-card.rules
/lib/udev/rules.d/80-net-name-slot.rules
/lib/udev/rules.d/60-block.rules                                                                  
/lib/udev/rules.d/60-evdev.rules                                            
/lib/udev/rules.d/60-serial.rules                                                            
/lib/udev/rules.d/70-mouse.rules                                       
/lib/udev/rules.d/70-touchpad.rules                                   
/lib/udev/rules.d/80-drivers.rules  

/lib/udev/scsi_id
/lib/udev/udevd
/lib/udev/v4l_id
%{_libdir}/libudev.so.1
%{_libdir}/libudev.so.1.*
%{_libdir}/libgudev-1.0.so.*.*.*
/sbin/udevadm
/sbin/udevd
/sbin/setup-udev
/etc/init.d/udev-postmount
%dir /%{_lib}/udev
%dir /etc/udev
/etc/udev/*
%dir /etc/udev/hwdb.d
%dir /%{_lib}/udev/rules.d
%{_mandir}/man*/*                                                                   

%files devel
%{_libdir}/libudev.a
%{_libdir}/libudev.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgudev-1.0.so
%{_libdir}/libgudev-1.0.so.0
%{_libdir}/libgudev-1.0.a
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/GUdev-1.0.gir
%{_libdir}/girepository-1.0/GUdev-1.0.typelib
%{_includedir}/*.h
%dir %{_includedir}/gudev-1.0/
%dir %{_includedir}/gudev-1.0/gudev/
%{_includedir}/gudev-1.0/gudev/*.h

%changelog
