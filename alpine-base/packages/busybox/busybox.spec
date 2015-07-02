Name:           busybox
Version:        1.23.2
Release:        1%{?dist}
Summary:        Size optimized toolbox of many common UNIX utilities

Group:          System Environment/Shells
License:        GPLv2
URL:            http://busybox.net
Source0:	http://busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1:	bbsuid.c
Source2:	nologin.c
Source3:	busyboxconfig

Patch0:		%{name}-1.11.1-bb.patch
Patch1:		busybox-uname-is-not-gnu.patch
Patch2:		bb-app-location.patch
Patch3:		loginutils-sha512.patch
Patch4:		udhcpc-discover-retries.patch
Patch5:		0001-ifupdown-pass-interface-device-name-for-ipv6-route-c.patch
Patch6:		0001-ifupdown-use-x-hostname-NAME-with-udhcpc.patch
Patch8:		0001-linedit-deluser-use-POSIX-getpwent-instead-of-getpwe.patch
Patch9:		0001-diff-add-support-for-no-dereference.patch
Patch10:	1000-fbsplash-use-virtual-y-size-in-mmap-size-calculation.patch
Patch11:	1001-fbsplash-support-console-switching.patch
Patch12:	1002-fbsplash-support-image-and-bar-alignment-and-positio.patch
Patch13:	glibc.patch

#BuildRequires:  
#Requires:       

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

%prep
%setup -q


%build

	%__gcc %{SOURCE1} -o %{BUILDROOT}/bbsuid
	%__cp %{SOURCE3} .config
	[ "$CLIBC" = musl ] && sed -i \
		-e "s/CONFIG_EXTRA_COMPAT=y/CONFIG_EXTRA_COMPAT=n/" \
		.config
	make -C %{BUILDROOT} O="$PWD" silentoldconfig
	make

#%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/sbin/busybox
%{_mandir}/man1/busybox.1.gz


%changelog
