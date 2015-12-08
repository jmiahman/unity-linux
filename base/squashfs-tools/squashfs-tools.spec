#So very Naughty.. I need to fix this..
%global _default_patch_fuzz 1

Summary: Utility for the creation of squashfs filesystems
Name: squashfs-tools
Version: 4.3
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://squashfs.sourceforge.net/
Source0: http://downloads.sourceforge.net/squashfs/squashfs%{version}.tar.gz
# manpages from http://ftp.debian.org/debian/pool/main/s/squashfs-tools/squashfs-tools_4.2+20121212-1.debian.tar.xz
# The man pages have been modified for 4.3 for Unity.
Source1: mksquashfs.1
Source2: unsquashfs.1
# From master branch (55f7ba830d40d438f0b0663a505e0c227fc68b6b).
# 32 bit process can use too much memory when using PAE or 64 bit kernels
Patch0:  PAE.patch
# From master branch (604b607d8ac91eb8afc0b6e3d917d5c073096103).
# Prevent overflows when using the -mem option.
Patch1:  mem-overflow.patch
# From squashfs-devel@lists.sourceforge.net by Guan Xin <guanx.bac@gmail.com>
# For https://bugzilla.redhat.com/show_bug.cgi?id=1141206
Patch2:  2gb.patch
# From https://github.com/gcanalesb/sasquatch/commit/6777e08cc38bc780d27c69c1d8c272867b74524f
# Which is forked from Phillip's squashfs-tools, though it looks like 
# the issue applies to us.
Patch3:  cve-2015-4645.patch
# Update formats to match changes in cve-2015-4645.patch
Patch4:  local-cve-fix.patch
# Disable FNM_EXTMATCH (Glob support) not offered with MUSL
Patch5:  fix-compat.patch

BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: lzo-devel
BuildRequires: libattr-devel
BuildRequires: lz4-devel

%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains the utilities for manipulating squashfs filesystems.

%prep
%setup -q -n squashfs%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p0
%patch5 -p1

%build
cd squashfs-tools
sed -i 's/\|FNM_EXTMATCH//' $(grep -l FNM_EXTMATCH *)
#CFLAGS="%{optflags}" XZ_SUPPORT=1 LZO_SUPPORT=1 LZMA_XZ_SUPPORT=1 LZ4_SUPPORT=1 make %{?_smp_mflags}
XZ_SUPPORT=1 LZO_SUPPORT=1 make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man1
install -m 755 squashfs-tools/mksquashfs %{buildroot}%{_sbindir}/mksquashfs
install -m 755 squashfs-tools/unsquashfs %{buildroot}%{_sbindir}/unsquashfs
#install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/mksquashfs.1
#install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/unsquashfs.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%doc README ACKNOWLEDGEMENTS DONATIONS PERFORMANCE.README README-4.3 CHANGES pseudo-file.example COPYING

#%doc README
#%{_mandir}/man1/*

%{_sbindir}/mksquashfs
%{_sbindir}/unsquashfs

%changelog
