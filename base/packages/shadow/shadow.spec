Name:		shadow	
Version:	4.2.1
Release:	1%{?dist}
Summary:	Utilities for managing accounts and shadow password files

Group:		Environment/Base
License:	BSD and GPLv2+
URL:		http://pkg-shadow.alioth.debian.org/
Source0:	http://pkg-shadow.alioth.debian.org/releases/%{name}-%{version}.tar.xz
Source1:	login.pamd

BuildRequires:	linux-pam-devel
#Requires:	

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
	--without-nscd \
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

%files
/bin/groups
/bin/su
/bin/login
/etc/login.defs
%dir /etc/default
/etc/default/useradd
/etc/pam.d/login
/usr/sbin/newusers
/usr/sbin/useradd
/usr/sbin/usermod
/usr/sbin/groupadd
/usr/sbin/vipw
/usr/sbin/userdel
/usr/sbin/pwck
/usr/sbin/groupmems
/usr/sbin/chgpasswd
/usr/sbin/groupmod
/usr/sbin/grpck
/usr/sbin/grpunconv
/usr/sbin/grpconv
/usr/sbin/chpasswd
/usr/sbin/pwconv
/usr/sbin/vigr
/usr/sbin/pwunconv
/usr/sbin/logoutd
/usr/sbin/groupdel
/usr/bin/sg
/usr/bin/lastlog
/usr/bin/newuidmap
/usr/bin/expiry
/usr/bin/chage
/usr/bin/faillog
/usr/bin/newgidmap
/usr/bin/chfn
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/newgrp

%changelog

