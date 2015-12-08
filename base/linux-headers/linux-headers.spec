%global _default_patch_fuzz 3

Name:		linux-headers	
Version:	3.18.18
Release:	1%{?dist}
Summary:	Linux system headers	

Group:		Development/System
License:	GPLv2
URL:		http://kernel.org	
Source0:	http://www.linuxgrill.com/anonymous/kernel/v3.1x/linux-%{version}.tar.xz

Patch0: 1-4-glibc-specific-inclusion-of-sysinfo.h-in-kernel.h.patch
#Patch1: 3-4-libc-compat.h-fix-some-issues-arising-from-in6.h.patch
Patch1: 270-bridge_header_fix.patch
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
%setup -qn linux-%{version}
%patch0 -p1 
%patch1 -p1 
#%patch2 -p1 

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}
mkdir -p %{buildroot}/usr
make headers_install ARCH=%{_arch} INSTALL_HDR_PATH=%{buildroot}/usr
#find %{buildroot}/usr -name .install -exec rm -f {} ;
#find %{buildroot}/usr -name ..install.cmd -exec rm -f {} ;
# provided by libdrm
rm -rf $RPM_BUILD_ROOT/usr/include/drm


%files
/usr/include/*

%changelog
