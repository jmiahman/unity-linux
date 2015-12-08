%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64
%define _lib /lib64

Name:		shadow	
Version:	4.2.1
Release:	1%{?dist}
Summary:	Utilities for managing accounts and shadow password files

Group:		Environment/Base
License:	BSD and GPLv2+
URL:		http://pkg-shadow.alioth.debian.org/
Source0:	http://pkg-shadow.alioth.debian.org/releases/%{name}-%{version}.tar.xz
Source1:	login.pamd

BuildRequires: linux-pam-devel
BuildRequires: libacl-devel libattr-devel
BuildRequires: bison flex 
Requires(pre): coreutils
Requires(post): coreutils

%description
The shadow-utils package includes the necessary programs for
converting UNIX password files to the shadow password format, plus
programs for managing user and group accounts. The pwconv command
converts passwords to the shadow password format. The pwunconv command
unconverts shadow passwords and generates a passwd file (a standard
UNIX password file). The pwck command checks the integrity of password
and shadow files. The lastlog command prints out the last login times
for all users. The useradd, userdel, and usermod commands are used for
managing user accounts. The groupadd, groupdel, and groupmod commands
are used for managing group accounts.

%prep
%setup -q


%build

./configure --prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \
	--libdir=%{_libdir} \
	--without-nscd \
	--without-chsh \
	--without-chfn \
	--without-nologin \
	--disable-nls \

make

%install

make DESTDIR=%{buildroot} install

# do not install these pam.d files they are broken and outdated
# nologin is provided by util-linux
rm %{buildroot}/etc/pam.d/* \
	%{buildroot}/sbin/nologin

# however, install our own for login
cp %{SOURCE1} %{buildroot}/etc/pam.d/login

# /etc/login.defs is not very useful - replace it with a blank file
rm %{buildroot}/etc/login.defs
touch %{buildroot}/etc/login.defs

# avoid conflict with man-pages
rm %{buildroot}/usr/share/man/man3/getspnam.3* \
	%{buildroot}/usr/share/man/man5/passwd.5*

#Provided by util-linux
rm %{buildroot}%{_bindir}/chsh
rm %{buildroot}%{_bindir}/chfn

%files
%{_mandir}/man*/*.*
/bin/groups
/bin/su
/bin/login
/etc/login.defs
%dir /etc/default
/etc/default/useradd
/etc/pam.d/login
%{_sbindir}/newusers
%{_sbindir}/useradd
%{_sbindir}/usermod
%{_sbindir}/groupadd
%{_sbindir}/vipw
%{_sbindir}/userdel
%{_sbindir}/pwck
%{_sbindir}/groupmems
%{_sbindir}/chgpasswd
%{_sbindir}/groupmod
%{_sbindir}/grpck
%{_sbindir}/grpunconv
%{_sbindir}/grpconv
%{_sbindir}/chpasswd
%{_sbindir}/pwconv
%{_sbindir}/vigr
%{_sbindir}/pwunconv
%{_sbindir}/logoutd
%{_sbindir}/groupdel
%{_bindir}/sg
%{_bindir}/lastlog
%{_bindir}/newuidmap
%{_bindir}/expiry
%{_bindir}/chage
%{_bindir}/faillog
%{_bindir}/newgidmap
%{_bindir}/passwd
%{_bindir}/gpasswd
%{_bindir}/newgrp

%changelog

