Summary: Simple kernel loader which boots from a FAT filesystem
Name: syslinux
Version: 6.03
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://syslinux.zytor.com/wiki/index.php/The_Syslinux_Project
Source0: https://www.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.xz

Source1: update-extlinux.conf 
Source2: update-extlinux

%define _binaries_in_noarch_packages_terminate_build 0

ExclusiveArch: %{ix86} x86_64
BuildRequires: nasm, perl 
BuildRequires: libuuid-devel, linux-headers, gnu-efi-devel
Requires: syslinux-nonlinux = %{version}-%{release}
%ifarch %{ix86}
Requires: mtools, libc.so.6
%endif
%ifarch x86_64
Requires: mtools, libc.so.6()(64bit)
%endif

# NOTE: extlinux belongs in /sbin, not in /usr/sbin, since it is typically
# a system bootloader, and may be necessary for system recovery.
%define _sbindir /sbin

%description
SYSLINUX is a suite of bootloaders, currently supporting DOS FAT
filesystems, Linux ext2/ext3 filesystems (EXTLINUX), PXE network boots
(PXELINUX), or ISO 9660 CD-ROMs (ISOLINUX).  It also includes a tool,
MEMDISK, which loads legacy operating systems from these media.

%package perl
Summary: Syslinux tools written in perl
Group: Applications/System

%description perl
Syslinux tools written in perl

%package devel
Summary: Headers and libraries for syslinux development.
Group: Development/Libraries
Provides: %{name}-static = %{version}-%{release}

%description devel
Headers and libraries for syslinux development.

%package extlinux
Summary: The EXTLINUX bootloader, for booting the local system.
Group: System/Boot
Requires: syslinux
Requires: syslinux-extlinux-nonlinux = %{version}-%{release}

%description extlinux
The EXTLINUX bootloader, for booting the local system, as well as all
the SYSLINUX/PXELINUX modules in /boot.

%ifarch %{ix86}
%package tftpboot
Summary: SYSLINUX modules in /tftpboot, available for network booting
Group: Applications/Internet
BuildArch: noarch
ExclusiveArch: %{ix86} x86_64
Requires: syslinux

%description tftpboot
All the SYSLINUX/PXELINUX modules directly available for network
booting in the /tftpboot directory.

%package extlinux-nonlinux
Summary: The parts of the EXTLINUX bootloader which aren't run from linux.
Group: System/Boot
Requires: syslinux
BuildArch: noarch
ExclusiveArch: %{ix86} x86_64

%description extlinux-nonlinux
All the EXTLINUX binaries that run from the firmware rather than
from a linux host.

%package nonlinux
Summary: SYSLINUX modules which aren't run from linux.
Group: System/Boot
Requires: syslinux
BuildArch: noarch
ExclusiveArch: %{ix86} x86_64

%description nonlinux
All the SYSLINUX binaries that run from the firmware rather than from a
linux host. It also includes a tool, MEMDISK, which loads legacy operating
systems from media.
%endif

%ifarch %{x86_64}
%package efi64
Summary: SYSLINUX binaries and modules for 64-bit UEFI systems
Group: System/Boot

%description efi64
SYSLINUX binaries and modules for 64-bit UEFI systems
%endif

%prep
%setup -q -n syslinux-%{version}

%build
#make bios clean all
make installer
%ifarch %{x86_64}
#make efi64 clean all
make efi64 installer
%endif

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_prefix}/lib/syslinux
mkdir -p %{buildroot}%{_includedir}
make bios install \
	INSTALLROOT=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_sbindir} \
	LIBDIR=%{_prefix}/lib DATADIR=%{_datadir} \
	MANDIR=%{_mandir} INCDIR=%{_includedir} \
	LDLINUX=ldlinux.c32
%ifarch %{x86_64}
make efi64 install netinstall \
	INSTALLROOT=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_sbindir} \
	LIBDIR=%{_prefix}/lib DATADIR=%{_datadir} \
	MANDIR=%{_mandir} INCDIR=%{_includedir} \
	LDLINUX=ldlinux.c32
%endif

mkdir -p %{buildroot}/%{_docdir}/%{name}/sample
install -m 644 sample/sample.* %{buildroot}/%{_docdir}/%{name}/sample/
mkdir -p %{buildroot}/etc
( cd %{buildroot}/etc && ln -s ../boot/extlinux/extlinux.conf . )

mkdir -p %{buildroot}/etc/update-extlinux.d
cp %{SOURCE1} %{buildroot}/etc/
sed "/^version=/s/=.*/=%{version}-r%{release}/" %{SOURCE2} \
	> %{buildroot}/sbin/update-extlinux
chmod 755 %{buildroot}/sbin/update-extlinux

# don't ship libsyslinux, at least, not for now
rm -f %{buildroot}%{_prefix}/lib/libsyslinux*
rm -f %{buildroot}%{_includedir}/syslinux.h

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%doc NEWS README*
#%doc doc/* 
#%doc sample
#%{_mandir}/man1/gethostip*
#%{_mandir}/man1/syslinux*
#%{_mandir}/man1/extlinux*
#%{_mandir}/man1/isohybrid*
#%{_mandir}/man1/memdiskfind*
%{_bindir}/gethostip
%{_bindir}/isohybrid
%{_bindir}/memdiskfind
%{_bindir}/syslinux
%dir %{_datadir}/syslinux
%dir %{_datadir}/syslinux/dosutil
%{_datadir}/syslinux/dosutil/*
%dir %{_datadir}/syslinux/diag/
%{_datadir}/syslinux/diag/*
%ifarch %{ix86}
%{_datadir}/syslinux/syslinux.exe
%else
%{_datadir}/syslinux/syslinux64.exe
%endif

%files perl
%defattr(-,root,root)
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%{_mandir}/man1/lss16toppm*
#%{_mandir}/man1/ppmtolss16*
#%{_mandir}/man1/syslinux2ansi*
%{_bindir}/keytab-lilo
%{_bindir}/lss16toppm
%{_bindir}/md5pass
%{_bindir}/mkdiskimage
%{_bindir}/ppmtolss16
%{_bindir}/pxelinux-options
%{_bindir}/sha1pass
%{_bindir}/syslinux2ansi
%{_bindir}/isohybrid.pl

%files devel
%defattr(-,root,root)
#%{!?_licensedir:%global license %%doc}
#%license COPYING
%dir %{_datadir}/syslinux/com32
%{_datadir}/syslinux/com32

%files extlinux
%{_sbindir}/extlinux
%{_sbindir}/update-extlinux
%config /etc/update-extlinux.conf
%config /etc/extlinux.conf

%ifarch %{ix86}
%files tftpboot
/tftpboot

%files nonlinux
%{_datadir}/syslinux/*.com
%{_datadir}/syslinux/*.exe
%{_datadir}/syslinux/*.c32
%{_datadir}/syslinux/*.bin
%{_datadir}/syslinux/*.0
%{_datadir}/syslinux/memdisk

%files extlinux-nonlinux
/boot/extlinux

%else
%exclude %{_datadir}/syslinux/memdisk
%exclude %{_datadir}/syslinux/*.com
%exclude %{_datadir}/syslinux/*.exe
%exclude %{_datadir}/syslinux/*.c32
%exclude %{_datadir}/syslinux/*.bin
%exclude %{_datadir}/syslinux/*.0
#%exclude /boot/extlinux
#%exclude /tftpboot
%endif

%ifarch %{x86_64}
%files efi64
#%{!?_licensedir:%global license %%doc}
#%license COPYING
%dir %{_datadir}/syslinux/efi64
%{_datadir}/syslinux/efi64
%endif

%post extlinux
# If we have a /boot/extlinux.conf file, assume extlinux is our bootloader
# and update it.
if [ -f /boot/extlinux/extlinux.conf ]; then \
	extlinux --update /boot/extlinux ; \
elif [ -f /boot/extlinux.conf ]; then \
	mkdir -p /boot/extlinux && \
	mv /boot/extlinux.conf /boot/extlinux/extlinux.conf && \
	extlinux --update /boot/extlinux ; \
fi

%changelog
