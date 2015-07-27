Name:		linux-headers	
Version:	3.18.5
Release:	1%{?dist}
Summary:	Linux system headers	

Group:		Development/System
License:	GPLv2
URL:		http://kernel.org	
Source0:	http://www.linuxgrill.com/anonymous/kernel/v3.1x/linux-%{version}.tar.xz
Patch0: 1-4-glibc-specific-inclusion-of-sysinfo.h-in-kernel.h.patch
Patch1: 3-4-libc-compat.h-fix-some-issues-arising-from-in6.h.patch
Patch2: 4-4-libc-compat.h-prevent-redefinition-of-struct-ethhdr.patch

#BuildRequires:	
#Requires:	

%description
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%prep
%setup -q
%patch0 -p1 -b .inclusion-of-sysinfo
%patch1 -p1 -b .in6
%patch2 -p1 -b .prevent-redefinition-of-struct-ethhdr

%build
#

%install
cd $RPM_BUILD_ROOT/linux-%{version}
mkdir -p $RPM_BUILD_ROOT/usr
make headers_install ARCH=${_arch} INSTALL_HDR_PATH=$RPM_BUILD_ROOT/usr
find $RPM_BUILD_ROOT/usr ( -name .install -o -name ..install.cmd ) -exec rm -f {} ;
# provided by libdrm
rm -rf $RPM_BUILD_ROOT/usr/include/drm


%files
%doc



%changelog
