Name:		linux-vanilla
Version:	3.18.18	
Release:	1%{?dist}
Summary:	The Linux kernel

Group:		System Environment/Kernel		
License:	GPLv2 and Redistributable, no modification permitted
URL:		http://ftp.kernel.org
Source0:	http://ftp.kernel.org/pub/linux/kernel/v3.x/linux-%{version}.tar.xz	

Source1:	kernelconfig.armhf
Source2:	kernelconfig.x86
Source3:	kernelconfig.x86_64

#BuildRequires:	
#Requires:	

%description
The Linux kernel %{version}

%package devel
Summary:        This package provides kernel headers and makefiles sufficient to build modules
Group:          System Environment/Kernel
Requires:       %{name} = %{version}

%description devel
This package provides kernel headers and makefiles sufficient to build modules

%prep
rm -rf %{buildroot}
%setup -qn linux-%{version}

mkdir -p %{buildroot}/build
%ifarch armv7l armv5el
%__cp %{SOURCE1} .config
%endif

%ifarch i386 i486 i586 i686
%__cp %{SOURCE2} .config
%endif

%ifarch x86_64
rm -f %{buildroot}/build/.config
rm -f %{buildroot}/.config

%__cp -f %{SOURCE3} %{buildroot}/build/.config
%__cp -f %{SOURCE3} %{buildroot}/.config
%endif

%build
make O=%{buildroot}/build silentoldconfig
cd %{buildroot}/build
export CC="musl-gcc"
make KBUILD_BUILD_VERSION=%{version}-%{release}-Unity

mkdir -p %{buildroot}/usr/src/linux-headers-%{version}
make -j1 O=%{buildroot}/usr/src/linux-headers-%{version} silentoldconfig prepare modules_prepare scripts

%install
cd %{buildroot}/build
mkdir -p %{buildroot}/boot 
mkdir -p %{buildroot}/lib/modules
make -j1 modules_install firmware_install install \
INSTALL_MOD_STRIP=1 \
INSTALL_MOD_PATH=%{buildroot} \
INSTALL_PATH=%{buildroot}/boot \

rm -rf %{buildroot}/lib/modules/%{version}/build 
rm -rf %{buildroot}/lib/modules/%{version}/source
rm -rf %{buildroot}/lib/firmware

mkdir -p %{buildroot}/usr/share/kernel/unity/
install -D include/config/kernel.release \
%{buildroot}/usr/share/kernel/unity/kernel.release

ln -sf /usr/src/linux-headers-%{version} %{buildroot}/lib/modules/%{version}/build

find %{buildroot}/build -path './include/*' -prune -o -path './scripts/*' -prune \
	-o -type f \( -name 'Makefile*' -o -name 'Kconfig*' \
	-o -name 'Kbuild*' -o -name '*.sh' -o -name '*.pl' \
	-o -name '*.lds' \) | cpio -pdm /usr/src/linux-headers-%{version}


# /boot
install -d $RPM_BUILD_ROOT/boot
cp -a $RPM_BUILD_ROOT/boot/System.map $RPM_BUILD_ROOT/boot/System.map-%{version}
cp -aL $RPM_BUILD_ROOT/.config $RPM_BUILD_ROOT/boot/config-%{version}
%__cp -aL $RPM_BUILD_ROOT/build/arch/x86/boot/bzImage $RPM_BUILD_ROOT/boot/vmlinuz-%{version}
install -p $RPM_BUILD_ROOT/build/vmlinux $RPM_BUILD_ROOT/boot/vmlinux-%{version}

%files
%doc
/boot/
/lib/modules/%{version}/
/usr/share/kernel/

%files devel
/usr/src/

%changelog
