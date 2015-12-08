%define _target_platform %{_arch}-unity-linux-musl

Name:    gpgme
Summary: GnuPG Made Easy - high level crypto API
Version: 1.5.4
Release: 1%{?dist}
Group:   Applications/System

License: LGPLv2+
URL:     http://www.gnupg.org/related_software/gpgme/
Source0: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig


BuildRequires: gawk
BuildRequires: libgpg-error-devel >= 1.8
BuildRequires: libassuan-devel >= 2.0.2
Requires: gnupg

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:  Development headers and libraries for %{name}
Requires: %{name} = %{version}-%{release}
Requires: libgpg-error-devel
#Requires(post): /sbin/install-info
#Requires(postun): /sbin/install-info
%description devel
%{summary}


%prep
%setup -q

%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -fv $RPM_BUILD_ROOT%{_libdir}/lib*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
#%license COPYING*
#%doc AUTHORS ChangeLog NEWS README* THANKS TODO VERSION
%{_libdir}/libgpgme.so.11*
%{_libdir}/libgpgme-pthread.so.11*

#%post devel
#/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

#%preun devel
#if [ $1 -eq 0 ] ; then
#  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
#fi

%files devel
%{_bindir}/gpgme-config
%{_includedir}/gpgme.h
%{_libdir}/libgpgme*.so
%{_datadir}/aclocal/gpgme.m4
#%{_infodir}/gpgme.info*


%changelog
