%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \


Name: libgcrypt
Version: 1.6.3
Release: 1%{?dist}
URL: http://www.gnupg.org/
Source0: ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2.sig

%define gcrylibdir %{_libdir}

License: LGPLv2+
Summary: A general-purpose cryptography library
BuildRequires: gawk, libgpg-error-devel, pkgconfig
Group: System Environment/Libraries

%package devel
Summary: Development files for the %{name} package
License: LGPLv2+ and GPLv2+
Group: Development/Libraries
#Requires(pre): /sbin/install-info
#Requires(post): /sbin/install-info
Requires: libgpg-error-devel
Requires: %{name} = %{version}-%{release}

%description
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This is a development version.

%description devel
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This package contains files needed to develop
applications using libgcrypt.

%prep
%setup -q

%build
#for future reference.. use below for arch builds, need if flag
# disable arm assembly for now as it produces TEXTRELs
#export gcry_cv_gcc_arm_platform_as_ok=no



./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--disable-static \
	--enable-padlock-support \

make

%install
make -j1 install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

#%post devel
#[ -f %{_infodir}/gcrypt.info.gz ] && \
#    /sbin/install-info %{_infodir}/gcrypt.info.gz %{_infodir}/dir
#exit 0

#%preun devel
#if [ $1 = 0 -a -f %{_infodir}/gcrypt.info.gz ]; then
#    /sbin/install-info --delete %{_infodir}/gcrypt.info.gz %{_infodir}/dir
#fi
#exit 0

%files
%defattr(-,root,root,-)
%{_libdir}/libgcrypt.so.*
#%{!?_licensedir:%global license %%doc}
#%license COPYING.LIB
#%doc AUTHORS NEWS THANKS

%files devel
%defattr(-,root,root,-)
%{_bindir}/%{name}-config
%{_bindir}/dumpsexp
%{_bindir}/hmac256
%{_bindir}/mpicalc
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*
#%{_mandir}/man1/*

#%{_infodir}/gcrypt.info*
#%{!?_licensedir:%global license %%doc}
#%license COPYING

%changelog
