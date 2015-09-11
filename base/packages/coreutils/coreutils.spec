#%define _default_patch_flags -p1

Name:		coreutils	
Version:	8.23
Release:	1%{?dist}
Summary:	A set of basic GNU tools commonly used in shell scripts

Group:		System Environment/Base
License:	GPLv3+
URL:		http://www.gnu.org/software/coreutils/
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz	

Patch0:		coreutils-8.22-shuf-segfault.patch

#BuildRequires:	bash, acl-devel, perl
#Requires:	

%description
These are the GNU core utilities.  This package is the combination of
the old GNU fileutils, sh-utils, and textutils packages.

%prep
%setup -q
#%patch0

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
/bin/nice
/bin/stat
/bin/stty
/bin/mknod
/bin/chgrp
/bin/ls
/bin/touch
/bin/rm
/bin/date
/bin/base64
/bin/mv
/bin/sync
/bin/cat
/bin/mkdir
/bin/echo
/bin/false
/bin/sleep
/bin/df
/bin/uname
/bin/chown
/bin/chmod
/bin/true
/bin/mktemp
/bin/cp
/bin/pwd
/bin/ln
/bin/printenv
/bin/dd
/bin/rmdir
/usr/sbin/chroot
/usr/libexec/coreutils/libstdbuf.so
%dir /usr/libexec/coreutils
/usr/bin/tail
/usr/bin/expand
/usr/bin/sha256sum
/usr/bin/users
/usr/bin/unlink
/usr/bin/tac
/usr/bin/shuf
/usr/bin/md5sum
/usr/bin/tty
/usr/bin/pathchk
/usr/bin/cut
/usr/bin/paste
/usr/bin/split
/usr/bin/basename
/usr/bin/env
/usr/bin/pr
/usr/bin/groups
/usr/bin/tr
/usr/bin/join
/usr/bin/expr
/usr/bin/pinky
/usr/bin/seq
/usr/bin/sha1sum
/usr/bin/uniq
/usr/bin/dir
/usr/bin/dircolors
/usr/bin/logname
/usr/bin/runcon
/usr/bin/link
/usr/bin/vdir
/usr/bin/whoami
/usr/bin/sha512sum
/usr/bin/stdbuf
/usr/bin/head
/usr/bin/comm
/usr/bin/od
/usr/bin/numfmt
/usr/bin/ptx
/usr/bin/nl
/usr/bin/wc
/usr/bin/fold
/usr/bin/fmt
/usr/bin/who
/usr/bin/tee
/usr/bin/test
/usr/bin/printf
/usr/bin/id
/usr/bin/unexpand
/usr/bin/shred
/usr/bin/hostid
/usr/bin/realpath
/usr/bin/mkfifo
/usr/bin/[
/usr/bin/sum
/usr/bin/du
/usr/bin/tsort
/usr/bin/readlink
/usr/bin/factor
/usr/bin/install
/usr/bin/dirname
/usr/bin/timeout
/usr/bin/yes
/usr/bin/chcon
/usr/bin/sha384sum
/usr/bin/nohup
/usr/bin/nproc
/usr/bin/csplit
/usr/bin/sort
/usr/bin/truncate
/usr/bin/sha224sum
/usr/bin/cksum

%changelog
