Summary: Utilities for managing ext2, ext3, and ext4 filesystems
Name: e2fsprogs
Version: 1.42.13
Release: 1%{?dist}

License: GPLv2
Group: System Environment/Base
Source0: https://www.kernel.org/pub/linux/kernel/people/tytso/%{name}/v%{version}/%{name}-%{version}.tar.xz

Url: http://e2fsprogs.sourceforge.net/
Requires: libcom_err%{?_isa} = %{version}-%{release}


BuildRequires: pkgconfig, texinfo, linux-headers
BuildRequires: gettext, util-linux

%description
The e2fsprogs package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in second,
third and fourth extended (ext2/ext3/ext4) filesystems. E2fsprogs
contains e2fsck (used to repair filesystem inconsistencies after an
unclean shutdown), mke2fs (used to initialize a partition to contain
an empty ext2 filesystem), debugfs (used to examine the internal
structure of a filesystem, to manually repair a corrupted
filesystem, or to create test cases for e2fsck), tune2fs (used to
modify filesystem parameters), and most of the other core ext2fs
filesystem utilities.

You should install the e2fsprogs package if you need to manage the
performance of an ext2, ext3, or ext4 filesystem.

%package devel
Summary: Ext2/3/4 filesystem-specific libraries and headers
Group: Development/Libraries
License: GPLv2 and LGPLv2
Requires: e2fsprogs = %{version}-%{release}
Requires: libcom_err = %{version}-%{release}
Requires: gawk
Requires: pkgconfig
#Requires(post): info
#Requires(preun): info

%description devel
E2fsprogs-devel contains the libraries and header files needed to
develop second, third and fourth extended (ext2/ext3/ext4)
filesystem-specific programs.

You should install e2fsprogs-devel if you want to develop ext2/3/4
filesystem-specific programs. If you install e2fsprogs-devel, you'll
also want to install e2fsprogs.

%package -n libcom_err
Summary: Common error description library
Group: Development/Libraries
License: MIT

%description -n libcom_err
This is the common error description library, part of e2fsprogs.

libcom_err is an attempt to present a common error-handling mechanism.

%prep
%setup -q

%build
%configure \
	--mandir=/usr/share/man \
	--enable-elf-shlibs \
	--disable-fsck \
	--disable-uuidd \
	--disable-libuuid \
	--disable-libblkid \
	--disable-tls \
	--disable-nls \

make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
make -j1 LDCONFIG=: DESTDIR=%{buildroot} install install-libs

# ugly hack to allow parallel install of 32-bit and 64-bit -devel packages:
#%define multilib_arches %{ix86} x86_64 ppc ppc64 s390 s390x sparcv9 sparc64

#%ifarch %{multilib_arches}
#mv -f %{buildroot}%{_includedir}/ext2fs/ext2_types.h \
#      %{buildroot}%{_includedir}/ext2fs/ext2_types-%{_arch}.h
#install -p -m 644 %{SOURCE1} %{buildroot}%{_includedir}/ext2fs/ext2_types.h
#%endif

# Hack for now, otherwise strip fails.
chmod +w %{buildroot}%{_libdir}/*.a

# Let boot continue even if *gasp* clock is wrong
#install -p -m 644 %{SOURCE2} %{buildroot}/etc/e2fsck.conf

%clean
rm -rf %{buildroot}

#%post devel
# Test for file; if installed with --excludedocs it may not be there
#if [ -f %{_infodir}/libext2fs.info.gz ]; then
#   /sbin/install-info %{_infodir}/libext2fs.info.gz %{_infodir}/dir || :
#fi

#%preun devel
#if [ $1 = 0 -a -f %{_infodir}/libext2fs.info.gz ]; then
#   /sbin/install-info --delete %{_infodir}/libext2fs.info.gz %{_infodir}/dir || :
#fi
#exit 0

%post -n libcom_err -p /sbin/ldconfig
%postun -n libcom_err -p /sbin/ldconfig

%files 
%defattr(-,root,root)
#%doc README RELEASE-NOTES
#%license COPYING

#%config(noreplace) /etc/mke2fs.conf
#%config(noreplace) /etc/e2fsck.conf
%{_sbindir}/badblocks
%{_sbindir}/debugfs
%{_sbindir}/dumpe2fs
%{_sbindir}/e2fsck
%{_sbindir}/e2image
%{_sbindir}/e2label
%{_sbindir}/e2undo
%{_sbindir}/fsck.ext2
%{_sbindir}/fsck.ext3
%{_sbindir}/fsck.ext4
%{_sbindir}/fsck.ext4dev
%{_sbindir}/logsave
%{_sbindir}/mke2fs
%{_sbindir}/mkfs.ext2
%{_sbindir}/mkfs.ext3
%{_sbindir}/mkfs.ext4
%{_sbindir}/mkfs.ext4dev
%{_sbindir}/resize2fs
%{_sbindir}/tune2fs
%{_sbindir}/filefrag
%{_sbindir}/e2freefrag
%{_sbindir}/e4defrag
%{_sbindir}/mklost+found

%{_bindir}/chattr
%{_bindir}/lsattr
#%{_mandir}/man1/chattr.1*
#%{_mandir}/man1/lsattr.1*

#%{_mandir}/man5/ext2.5*
#%{_mandir}/man5/ext3.5*
#%{_mandir}/man5/ext4.5*
#%{_mandir}/man5/e2fsck.conf.5*
#%{_mandir}/man5/mke2fs.conf.5*

#%{_mandir}/man8/badblocks.8*
#%{_mandir}/man8/debugfs.8*
#%{_mandir}/man8/dumpe2fs.8*
#%{_mandir}/man8/e2fsck.8*
#%{_mandir}/man8/filefrag.8*
#%{_mandir}/man8/e2freefrag.8*
#%{_mandir}/man8/e4defrag.8*
#%{_mandir}/man8/fsck.ext2.8*
#%{_mandir}/man8/fsck.ext3.8*
#%{_mandir}/man8/fsck.ext4.8*
#%{_mandir}/man8/fsck.ext4dev.8*
#%{_mandir}/man8/e2image.8*
#%{_mandir}/man8/e2label.8*
#%{_mandir}/man8/e2undo.8*
#%{_mandir}/man8/logsave.8*
#%{_mandir}/man8/mke2fs.8*
#%{_mandir}/man8/mkfs.ext2.8*
#%{_mandir}/man8/mkfs.ext3.8*
#%{_mandir}/man8/mkfs.ext4.8*
#%{_mandir}/man8/mkfs.ext4dev.8*
#%{_mandir}/man8/mklost+found.8*
#%{_mandir}/man8/resize2fs.8*
#%{_mandir}/man8/tune2fs.8*
%{_libdir}/libe2p.so.*
%{_libdir}/libext2fs.so.*

%{_libdir}/libss.so.*

%files devel
%defattr(-,root,root)
#%{_infodir}/libext2fs.info*
%{_libdir}/libe2p.so
%{_libdir}/libext2fs.so
%{_libdir}/pkgconfig/e2p.pc
%{_libdir}/pkgconfig/ext2fs.pc

%{_includedir}/e2p
%{_includedir}/ext2fs
%{_libdir}/*.a

%{_bindir}/mk_cmds                                                               
%{_libdir}/libss.so                                                              
%{_datadir}/ss                                                                   
%{_includedir}/ss                                                                
#%{_mandir}/man1/mk_cmds.1*                                                       
%{_libdir}/pkgconfig/ss.pc

%files -n libcom_err
%defattr(-,root,root)
#%license COPYING
%{_libdir}/libcom_err.so.*
%{_bindir}/compile_et
%{_libdir}/libcom_err.so
%{_datadir}/et
%{_includedir}/et
%{_includedir}/com_err.h
#%{_mandir}/man1/compile_et.1*
#%{_mandir}/man3/com_err.3*
%{_libdir}/pkgconfig/com_err.pc

%changelog
