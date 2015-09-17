#%define _default_patch_flags -p1

Name:		coreutils	
Version:	8.23
Release:	1%{?dist}
Summary:	A set of basic GNU tools commonly used in shell scripts

Group:		System Environment/Base
License:	GPLv3+
URL:		http://www.gnu.org/software/coreutils/
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz	

BuildRequires:	bash libacl-devel perl openssl-devel

%description
These are the GNU core utilities.  This package is the combination of
the old GNU fileutils, sh-utils, and textutils packages.

%prep
%setup -q

%build
LIBS=-lrt \
FORCE_UNSAFE_CONFIGURE=1 \
CC=gcc \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-nls \
	--without-gmp \
	--with-openssl \
	--enable-install-program=arch \
	--enable-no-install-program=hostname,su,kill,uptime \

make


%install
make DESTDIR=%{buildroot} install


rm -rf %{buildroot}/usr/lib/charset.alias

install -d %{buildroot}/bin %{buildroot}/usr/sbin
cd %{buildroot}/usr/bin/

# binaries that busybox puts in /bin
mv base64 cat chgrp chmod chown cp date dd df 'echo' false ln ls \
	mkdir mknod mktemp mv nice printenv pwd rm rmdir sleep stat \
	stty sync touch true uname \
	%{buildroot}/bin

mv chroot %{buildroot}/usr/sbin/

%files
/bin/*
/usr/sbin/*
/usr/libexec/coreutils/libstdbuf.so
%dir /usr/libexec/coreutils
/usr/bin/*

%changelog
