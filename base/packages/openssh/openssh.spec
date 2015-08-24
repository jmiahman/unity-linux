%define _target_platform %{_arch}-unity-linux-musl

# OpenSSH privilege separation requires a user & group ID
%define sshd_uid    22
%define sshd_gid    22

Name:		openssh
Version:	7.0p1	
Release:	1%{?dist}
Summary:	An open source implementation of SSH protocol versions 1 and 2

Group:		Applications/Internet
License:	BSD
URL:		http://www.openssh.com/portable.html
Source0:	ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
Source1:	sshd.confd
Source2:	sshd.initd

BuildRequires:	openssl-devel, zlib-devel
Requires:	openssh-client
Requires:	openssh-server

Patch0:		CVE-2015-5600.patch
Patch1:		openssh-fix-utmp.diff
Patch2:		openssh-sftp-interactive.diff
Patch3:		openssh6.5-peaktput.diff
Patch4:		openssh6.9-dynwindows.diff

%package client
Summary: An open source SSH client applications
Group: Applications/Internet

%package keysign
Summary: Keysign for SSH client applications                       
Group: Applications/Internet                                               
Requires: %{name}-client = %{version}

%package server
Summary: An open source SSH server daemon
Group: System Environment/Daemons
Requires: %{name}-client = %{version}

%description
SSH (Secure SHell) is a program for logging into and executing
commands on a remote machine. SSH is intended to replace rlogin and
rsh, and to provide secure encrypted communications between two
untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's version of the last free version of SSH, bringing
it up to date in terms of security and features.

This package includes the core files necessary for both the OpenSSH
client and server. To make this package useful, you should also
install openssh-clients, openssh-server, or both.

%description client
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package includes
the clients necessary to make encrypted connections to SSH servers.

%description keysign
OpenSSH helper program for host-based authentication

%description server
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package contains
the secure shell daemon (sshd). The sshd daemon allows SSH clients to
securely connect to your SSH server.


%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1

%build
sed -i -e '/_PATH_XAUTH/s:/usr/X11R6/bin/xauth:/usr/bin/xauth:' pathnames.h

./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc/ssh \
	--datadir=/usr/share/openssh \
	--libexecdir=/usr/lib/ssh \
	--mandir=/usr/share/man \
	--with-mantype=man \
	--with-ldflags=${LDFLAGS} \
	--disable-strip \
	--disable-lastlog \
	--disable-wtmp \
	--with-privsep-path=/var/empty \
	--with-privsep-user=sshd \
	--with-md5-passwords \
	--with-ssl-engine \
	--without-pam \

make

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/var/empty
install -D -m755 %{SOURCE1} \
	%{buildroot}/etc/init.d/sshd
install -D -m644 %{SOURCE2} \
	%{buildroot}/etc/conf.d/sshd
install -Dm644 %{_builddir}/%{name}-%{version}/contrib/ssh-copy-id.1 \
	%{buildroot}/usr/share/man/man1/ssh-copy-id.1
sed -i 's/#UseDNS yes/UseDNS no/' %{buildroot}/etc/ssh/sshd_config
install -Dm755 %{_builddir}/%{name}-%{version}/contrib/findssl.sh \
	%{buildroot}/usr/bin/findssl.sh
install -Dm755 %{_builddir}/%{name}-%{version}/contrib/ssh-copy-id \
	%{buildroot}/usr/bin/ssh-copy-id
install -d %{buildroot}/usr/lib/ssh

%pre server
getent group ssh_keys >/dev/null || groupadd -r ssh_keys || :
getent group sshd >/dev/null || groupadd -g %{sshd_uid} -r sshd || :
getent passwd sshd >/dev/null || \
  useradd -c "Privilege-separated SSH" -u %{sshd_uid} -g sshd \
  -s /sbin/nologin -r -d /var/empty/sshd sshd 2> /dev/null || :

%files client
%dir /etc/ssh
%dir /usr/lib/ssh
/etc/ssh/moduli
/etc/ssh/ssh_config
/usr/bin/ssh
/usr/bin/sftp
/usr/bin/scp
/usr/bin/ssh-keyscan
/usr/bin/ssh-copy-id
/usr/bin/ssh-add
/usr/bin/ssh-agent
/usr/bin/ssh-keygen
/usr/bin/slogin
/usr/bin/findssl.sh

%files keysign
/usr/lib/ssh/ssh-keysign

%files server

/etc/ssh/sshd_config
%dir /etc/init.d/
/etc/init.d/sshd
%dir /etc/conf.d/
/etc/conf.d/sshd
/usr/sbin/sshd
/usr/lib/ssh/ssh-pkcs11-helper
/usr/lib/ssh/sftp-server

%changelog

