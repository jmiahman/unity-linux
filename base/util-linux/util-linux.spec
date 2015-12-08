%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64
%define _lib /lib64

Name:		util-linux	
Version:	2.26.2
Release:	3%{?dist}
Summary:	A collection of basic system utilities

Group:		System Environment/Base	
License:	GPLv2 and GPLv2+ and LGPLv2+ and BSD with advertising and Public Domain	
URL:		http://en.wikipedia.org/wiki/Util-linux
Source0:	ftp://ftp.kernel.org/pub/linux/utils/util-linux/v2.26/util-linux-%{version}.tar.xz
Source1: 	ttydefaults.h

BuildRequires: zlib-devel, sed, ncurses-devel, tar 
BuildRequires: autoconf, automake, libtool 
BuildRequires: python-devel, linux-headers

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, Util-linux contains the fdisk configuration tool and the login
program.

%package libs 
Summary: Shared libs for %{name} 
Group: System Environment/Base                                                 
License: LGPLv2+

%description libs
These are shared libs used for mutliple %{name} programs

%package libs-devel
Summary: Headers for shared libs in %{name}
Group: Development/Libraries
License: LGPLv2+

%description libs-devel
These are development headers used for mutliple %{name}-libs.

%package -n blkid
Summary: Block device identification tool.
Group: System Environment/Base
License: LGPLv2+
Requires: libblkid = %{version}-%{release}

%description -n blkid
This is block device identification library, part of util-linux.

%package -n libblkid
Summary: Block device identification tool.
Group: Development/Libraries
License: LGPLv2+
Requires: libuuid = %{version}-%{release}

%description -n libblkid
This is block device identification library, part of util-linux.

%package -n libblkid-devel
Summary:  Block device identification library from util-linux.
Group: Development/Libraries
License: LGPLv2+
Requires: libblkid = %{version}-%{release}
Requires: pkgconfig

%description -n libblkid-devel
This is the block device identification development library and headers,
part of util-linux.

%package -n libuuid
Summary: DCE compatible Universally Unique Identifier library.
Group: Development/Libraries
License: LGPLv2+

%description -n libuuid
DCE compatible Universally Unique Identifier library.

%package -n libuuid-devel
Summary: Universally unique ID library
Group: Development/Libraries
License: LGPLv2+
Requires: libuuid = %{version}-%{release}
Requires: pkgconfig

%description -n libuuid-devel
This is the universally unique ID development library and headers,
part of util-linux.

%package -n libmount
Summary: Device mounting library
Group: Development/Libraries
License: LGPLv2+
Requires: libblkid = %{version}-%{release}
Requires: libuuid = %{version}-%{release}

%description -n libmount
This is the device mounting library, part of util-linux.


%package -n libmount-devel
Summary: Device mounting library
Group: Development/Libraries
License: LGPLv2+
Requires: libmount = %{version}-%{release}
Requires: pkgconfig

%description -n libmount-devel
This is the device mounting development library and headers,
part of util-linux.

%package -n cfdisk
Summary: Curses based partition table manipulator from util-linux.
Group: System Environment/Base
License: LGPLv2+
Requires: pkgconfig
Requires: %{name}-libs

%description -n cfdisk
cfdisk is a curses based program for partitioning any hard disk drive.


%package -n sfdisk
Summary: Partition table manipulator from util-linux
Group: System Environment/Base
License: LGPLv2+
Requires: pkgconfig
Requires: %{name}-libs

%description -n sfdisk
sfdisk has four (main) uses: list the size of a partition, list the partitions on a device, check the partitions on a device, and - very dangerous - repartition a device.

%package -n mcookie
Summary: Generate magic cookies for xauth
Group: System Environment/Base
License: LGPLv2+

%description -n mcookie
Mcookie generates a 128-bit random hexadecimal number for use with the X authority system.

%package -n python-libmount
Summary: A wrapper around libmount
Group: Development/Libraries
License: BSD
Requires: libmount = %{version}-%{release}
Requires: pkgconfig

%description -n  python-libmount
A wrapper around libmount, for reading and manipulating filesystem tables

%package -n bash-completion-%{name}
Summary:        bash-completion for linux utilities
Group:          Applications/Shells
Requires:       bash-completion >= 2.0
BuildArch:      noarch

%description -n bash-completion-%{name}
bash-completion for kmod utilities.

%prep
%setup -q


%build
cp -rf %{SOURCE1} include/
libtoolize --force
aclocal -I m4
autoconf
automake --add-missing

./configure \
	--prefix=/usr \
	--libdir=%{_libdir} \
	--enable-raw \
	--disable-uuidd \
	--disable-nls \
	--disable-tls \
	--disable-kill \
	--with-ncurses \
	--disable-login \
	--disable-last \
	--disable-sulogin \
	--disable-su \
	--enable-usrdir-path \
	--enable-chsh-only-listed \
	--with-python='2.7'

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make -j1 install DESTDIR=%{buildroot}
# use pkg-config
rm -f %{buildroot}/%{_libdir}/*.la \
	%{buildroot}/%{_libdir}/python*/site-packages/libmount/*.la


%files
%{_mandir}/man*/*.*
%{_libdir}
/usr/bin/*
/usr/sbin/*
/bin/*
/sbin/agetty
/sbin/blkdiscard
/sbin/blockdev
/sbin/chcpu
/sbin/ctrlaltdel
/sbin/fdisk
/sbin/findfs
/sbin/fsck
/sbin/fsck.cramfs
/sbin/fsck.minix
/sbin/fsfreeze
/sbin/fstrim
/sbin/hwclock
/sbin/losetup
/sbin/mkfs
/sbin/mkfs.bfs
/sbin/mkfs.cramfs
/sbin/mkfs.minix
/sbin/mkswap
/sbin/nologin
/sbin/pivot_root
/sbin/raw
/sbin/runuser
/sbin/swaplabel
/sbin/swapoff
/sbin/swapon
/sbin/switch_root
/sbin/wipefs
/sbin/zramctl

%exclude /sbin/blkid
%exclude %{_libdir}/libblkid.so
%exclude %{_includedir}/blkid
%exclude %{_libdir}/pkgconfig/blkid.pc
%exclude %{_libdir}/libuuid.so
%exclude %{_includedir}/uuid
%exclude %{_libdir}/pkgconfig/uuid.pc
%exclude %{_libdir}/libmount.so 
%exclude %{_includedir}/libmount
%exclude %{_libdir}/pkgconfig/mount.pc
%exclude /sbin/cfdisk
%exclude /sbin/sfdisk
%exclude %{_bindir}/mcookie
#%exclude %{_libdir}/python*/site-packages/libmount/*
%exclude %{_libdir}/libfdisk.so.*
%exclude %{_libdir}/libsmartcols.so.*
%exclude %{_libdir}/libblkid.so.*
%exclude %{_libdir}/libuuid.so.*
%exclude %{_libdir}/libmount.so.*
%exclude %{_mandir}/man*/blkid.*

%files libs
%{_libdir}/libfdisk.so.*
%{_libdir}/libsmartcols.so.*

%files -n blkid
/sbin/blkid
%{_mandir}/man*/blkid.*

%files -n libblkid
%{_libdir}/libblkid.so.*

%files -n libblkid-devel
%{_libdir}/libblkid.so
%{_includedir}/blkid
%{_libdir}/pkgconfig/blkid.pc

%files -n libuuid
%{_libdir}/libuuid.so.*

%files -n libuuid-devel
%{_libdir}/libuuid.so
%{_includedir}/uuid
%{_libdir}/pkgconfig/uuid.pc

%files libs-devel
%{_includedir}/libfdisk
%{_includedir}/libsmartcols
%{_docdir}/util-linux/

%files -n libmount
%{_libdir}/libmount.so.* 

%files -n libmount-devel
%{_libdir}/libmount.so
%{_includedir}/libmount
%{_libdir}/pkgconfig/mount.pc

%files -n cfdisk
/sbin/cfdisk

%files -n sfdisk
/sbin/sfdisk

%files -n mcookie
%{_bindir}/mcookie

%files -n python-libmount
%{_libdir}/python*/site-packages/libmount/*
%dir %{_libdir}/python*/site-packages/libmount/

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{_datadir}/bash-completion/completions/

%changelog
* Tue Dec 08 2015 JMiahMan <JMiahMan@unity-linux.org> - 2.26.2-3
- Place doc in libs-devel and not libs

* Tue Dec 08 2015 JMiahMan <JMiahMan@unity-linux.org> - 2.26.2-2
- Rebuild for rpm4 and MUSL qsort_r patch drop

* Mon Nov 30 2015 <JMiahMan@unity-linux.org> - 2.26.2-1
- Initial build for Unity-Linux
