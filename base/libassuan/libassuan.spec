%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \


Name:    libassuan
Summary: GnuPG IPC library
Version: 2.2.1
Release: 1%{?dist}

# The library is LGPLv2+, the documentation GPLv3+
License: LGPLv2+ and GPLv3+
Source0: ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-%{version}.tar.bz2.sig
URL:     http://www.gnupg.org/
Group:   System Environment/Libraries

BuildRequires: gawk
BuildRequires: libgpg-error-devel
BuildRequires: npth-devel

%description
This is the IPC library used by GnuPG 2, GPGME and a few other
packages.

%package devel 
Summary: GnuPG IPC library 
Group: Development/Libraries
Provides: libassuan2-devel = %{version}-%{release}
Provides: libassuan2-devel = %{version}-%{release}
Requires: npth-devel
Requires: libassuan = %{version}-%{release}
#Requires(post): /sbin/install-info
#Requires(preun): /sbin/install-info
%description devel 
This is the IPC static library used by GnuPG 2, GPGME and a few other
packages.

This package contains files needed to develop applications using %{name}.


%prep
%setup -q

%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

## Unpackaged files
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/lib*.la


%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

#%post devel 
#/sbin/install-info %{_infodir}/assuan.info %{_infodir}/dir &>/dev/null || :

#%preun devel 
#if [ $1 -eq 0 ]; then
#  /sbin/install-info --delete %{_infodir}/assuan.info %{_infodir}/dir &>/dev/null || :
#fi


%files
%defattr(-,root,root,-)
#%{!?_licensedir:%global license %%doc}
#%license COPYING COPYING.LIB
#%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_libdir}/libassuan.so.0*

%files devel 
%defattr(-,root,root,-)
%{_bindir}/libassuan-config
%{_includedir}/*.h
%{_libdir}/libassuan.so
%{_datadir}/aclocal/libassuan.m4
#%{_infodir}/assuan.info*


%changelog
