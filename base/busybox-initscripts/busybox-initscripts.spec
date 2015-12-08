Name:		busybox-initscripts		
Version:	0.1
Release:	1%{?dist}
Summary:	Init scripts for busybox daemons

Group:		System Environment/Shells	
License:	GPLv2
URL:		unity-linux.org
Source0:	busybox-initscripts-0.1.tar.gz

#BuildRequires:	
#Requires:	busybox

%description
Init scripts for busybox daemons

%prep
%setup -q


%build
#nothing here

%install
local i
mkdir -p %{buildroot}/etc/conf.d %{buildroot}/etc/init.d %{buildroot}/lib/mdev\
	%{buildroot}/etc/acpi/PWRF

for i in *.initd; do
	install -m755 $i %{buildroot}/etc/init.d/${i%.*}
done

for i in *.confd; do
	install -m644 $i %{buildroot}/etc/conf.d/${i%.*}
done

install -m644 mdev.conf %{buildroot}/etc
install -m755 dvbdev ide_links usbdev usbdisk_link xvd_links %{buildroot}/lib/mdev/

# poweroff script for acpid
cat >%{buildroot}/etc/acpi/PWRF/00000080 <<EOF
#!/bin/sh
poweroff
EOF

chmod +x %{buildroot}/etc/acpi/PWRF/00000080

# script for udhcpc
install -Dm755 default.script \
	%{buildroot}/usr/share/udhcpc/default.script

%post
if [ -L /etc/runlevels/boot/mdev ]; then
        mkdir -p /etc/runlevels/sysinit
        mv /etc/runlevels/boot/mdev /etc/runlevels/sysinit/ 2>/dev/null
fi


%files
/etc/mdev.conf
/etc/init.d/rdate
/etc/init.d/httpd
/etc/init.d/watchdog
/etc/init.d/mdev
/etc/init.d/inetd
/etc/init.d/acpid
/etc/init.d/klogd
/etc/init.d/dnsd
/etc/init.d/ntpd
/etc/init.d/syslog
/etc/init.d/cron
/etc/acpi/PWRF/00000080
/etc/conf.d/rdate
/etc/conf.d/watchdog
/etc/conf.d/klogd
/etc/conf.d/ntpd
/etc/conf.d/syslog
/etc/conf.d/cron
/lib/mdev/usbdisk_link
/lib/mdev/ide_links
/lib/mdev/xvd_links
/lib/mdev/usbdev
/lib/mdev/dvbdev
/usr/share/udhcpc/default.script

%dir /etc/acpi
%dir /etc/acpi/PWRF
%dir /lib/mdev
%dir /usr/share/udhcpc

%changelog
