%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \


Summary: CMS and X.509 library
Name:    libksba
Version: 1.3.3
Release: 1%{?dist}

# The library is licensed under LGPLv3+ or GPLv2+,
# the rest of the package under GPLv3+
License: (LGPLv3+ or GPLv2+) and GPLv3+
Group:   System Environment/Libraries
URL:     http://www.gnupg.org/
Source0: ftp://ftp.gnupg.org/gcrypt/libksba/libksba-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libksba/libksba-%{version}.tar.bz2.sig

BuildRequires: gawk
BuildRequires: libgpg-error-devel
BuildRequires: libgcrypt-devel

%description
KSBA (pronounced Kasbah) is a library to make X.509 certificates as
well as the CMS easily accessible by other applications.  Both
specifications are building blocks of S/MIME and TLS.

%package devel
Summary: Development headers and libraries for %{name}
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}
#Requires(post): /sbin/install-info
#Requires(preun): /sbin/install-info
%description devel
%{summary}.


%prep
%setup -q

%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%check
make check


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

#%post devel
#install-info %{_infodir}/ksba.info %{_infodir}/dir ||:

#%preun devel
#if [ $1 -eq 0 ]; then
#  install-info --delete %{_infodir}/ksba.info %{_infodir}/dir ||:
#fi


%files
%defattr(-,root,root,-)
#%doc AUTHORS ChangeLog COPYING* NEWS README* THANKS TODO
%{_libdir}/libksba.so.8*

%files devel
%defattr(-,root,root,-)
%{_bindir}/ksba-config
%{_libdir}/libksba.so
%{_includedir}/ksba.h
%{_datadir}/aclocal/ksba.m4
#%{_infodir}/ksba.info*


%changelog
