%define _target_platform %{_arch}-unity-linux-musl

Name:		linux-pam	
Version:	1.2.1
Release:	1%{?dist}
Summary:	An extensible library which provides authentication for applications

Group:		System Environment/Base
License:	BSD and GPLv2+
URL:		http://www.kernel.org/pub/linux/libs/pam
Source0:	http://linux-pam.org/library/Linux-PAM-%{version}.tar.bz2
Source1:        base-account.pamd
Source2:        base-auth.pamd
Source3:        base-password.pamd
Source4:        base-session-noninteractive.pamd
Source5:        base-session.pamd
Source6:        other.pamd

Patch0:		pam-fix-compat.patch
Patch1:		libpam-fix-build-with-eglibc-2.16.patch
Patch2:		linux-pam-innetgr.patch
Patch3:		musl-fix-pam_exec.patch


BuildRequires:	bison, flex-devel, autoconf, automake, libtool
#Requires:	

%description
Linux-PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

%package devel
Group: Development/Libraries
Summary: Files needed for developing PAM-aware applications and modules for PAM
Requires: linux-pam = %{version}-%{release}

%description devel
Linux-PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. This package
contains header files used for building both PAM-aware applications
and modules for use with the PAM system.

%prep
%setup -q -n Linux-PAM-1.2.1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build


sed -e 's/pam_rhosts//g' -i modules/Makefile.am
autoreconf -vif
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--libdir=/lib \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \
	--disable-nls \
	--disable-db \
	--disable-nis \
	--disable-cracklib \
	--disable-audit \
	--disable-selinux \
	ac_cv_search_crypt=no \
	BUILD_CFLAGS=-Os \
	BUILD_LDFLAGS=

make 

%install
make DESTDIR=%{buildroot} install

# do not install pam.d files bundled with the source, they could be broken
rm -rf %{buildroot}/etc/pam.d

# install our pam.d files
mkdir %{buildroot}/etc/pam.d

%__cp %{SOURCE1} %{buildroot}/etc/pam.d/base-account
%__cp %{SOURCE2} %{buildroot}/etc/pam.d/base-auth
%__cp %{SOURCE3} %{buildroot}/etc/pam.d/base-password
%__cp %{SOURCE4} %{buildroot}/etc/pam.d/base-session-noninteractive
%__cp %{SOURCE5} %{buildroot}/etc/pam.d/base-session
%__cp %{SOURCE6} %{buildroot}/etc/pam.d/other

# delete pointless libtool archives.
find %{buildroot} -name *.la -print | xargs rm

chgrp shadow %{buildroot}/sbin/unix_chkpwd \
	&& chmod g+s %{buildroot}/sbin/unix_chkpwd


%files
/etc/environment
%dir /etc/security/
/etc/security/pam_env.conf
/etc/security/group.conf
/etc/security/time.conf
/etc/security/access.conf
/etc/security/limits.conf
/etc/security/namespace.conf
/etc/security/namespace.init
%dir /etc/pam.d
/etc/pam.d/base-session-noninteractive
/etc/pam.d/base-account
/etc/pam.d/other
/etc/pam.d/base-auth
/etc/pam.d/base-password
/etc/pam.d/base-session
/lib/libpam.so.0
/lib/libpamc.so.0
/lib/libpamc.so.0.82.1
/lib/libpam_misc.so.0
/lib/libpam_misc.so.0.82.1
/lib/libpam.so.0.84.1
%dir /lib/security/
/lib/security/pam_tally.so
/lib/security/pam_mail.so
/lib/security/pam_ftp.so
/lib/security/pam_unix.so
/lib/security/pam_motd.so
/lib/security/pam_limits.so
/lib/security/pam_namespace.so
/lib/security/pam_echo.so
/lib/security/pam_time.so
%dir /lib/security/pam_filter
/lib/security/pam_filter/upperLOWER
/lib/security/pam_keyinit.so
/lib/security/pam_debug.so
/lib/security/pam_tally2.so
/lib/security/pam_issue.so
/lib/security/pam_loginuid.so
/lib/security/pam_securetty.so
/lib/security/pam_stress.so
/lib/security/pam_wheel.so
/lib/security/pam_rootok.so
/lib/security/pam_warn.so
/lib/security/pam_localuser.so
/lib/security/pam_group.so
/lib/security/pam_exec.so
/lib/security/pam_timestamp.so
/lib/security/pam_deny.so
/lib/security/pam_umask.so
/lib/security/pam_faildelay.so
/lib/security/pam_env.so
/lib/security/pam_xauth.so
/lib/security/pam_filter.so
/lib/security/pam_mkhomedir.so
/lib/security/pam_lastlog.so
/lib/security/pam_succeed_if.so
/lib/security/pam_nologin.so
/lib/security/pam_pwhistory.so
/lib/security/pam_listfile.so
/lib/security/pam_access.so
/lib/security/pam_permit.so
/lib/security/pam_shells.so
/sbin/mkhomedir_helper
/sbin/pam_tally2
/sbin/pam_timestamp_check
/sbin/unix_update
/sbin/unix_chkpwd
/sbin/pam_tally

%files devel
/lib/libpam_misc.so
/lib/libpam.so
/lib/libpamc.so
%dir /usr/include/security
/usr/include/security/_pam_compat.h
/usr/include/security/_pam_macros.h
/usr/include/security/pam_filter.h
/usr/include/security/pam_ext.h
/usr/include/security/pam_client.h
/usr/include/security/pam_modutil.h
/usr/include/security/pam_misc.h
/usr/include/security/pam_modules.h
/usr/include/security/_pam_types.h
/usr/include/security/pam_appl.h

%changelog

