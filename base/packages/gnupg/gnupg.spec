%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \


Name:		gnupg	
Version:	2.1.7
Release:	1%{?dist}
Summary:	A GNU utility for secure communication and data storage

Group:		Applications/System
License:	GPLv3+ with exceptions	
URL:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2

Patch0: 	0001-Include-sys-select.h-for-FD_SETSIZE.patch

BuildRequires:	libcurl-devel libassuan libksba-devel 
BuildRequires:  libgcrypt-devel libgpg-error-devel
BuildRequires:  npth-devel zlib-devel libassuan-devel

#Disable OpenLDAP for now, remove --disable in configure as well
#BuildRequires:  openldap-devel

%description
GnuPG is GNU's tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440 and the S/MIME
standard as described by several RFCs.

GnuPG 2.0 is a newer version of GnuPG with additional support for
S/MIME.  It has a different design philosophy that splits
functionality up into several modules. The S/MIME and smartcard functionality
is provided by the gnupg2-smime package.


%prep
%setup -q
%patch0 -p1

%build

./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--disable-nls \
	--disable-ldap \

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
# compat symlink
cd %{buildroot}/usr/bin/
ln -s gpg2 gpg


%files
/usr/sbin/*
/usr/libexec/*
/usr/bin/*
%dir /usr/share/gnupg
/usr/share/gnupg/*.txt
/usr/share/gnupg/gpg-conf.skel
/usr/share/gnupg/com-certs.pem
/usr/share/gnupg/distsigkey.gpg

%changelog

