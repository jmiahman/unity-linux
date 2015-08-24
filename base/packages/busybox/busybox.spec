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
Patch14:	linux-headers.patch

#BuildRequires:  
#Requires:       

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

%prep
%setup -q

%patch0  -p1 -b .%{name}-1.11.1-bb
%patch1  -p1 -b .busybox-uname-is-not-gnu
%patch2  -p1 -b .bb-app-location
%patch3  -p1 -b .loginutils-sha512
%patch4  -p1 -b .udhcpc-discover-retries
%patch5  -p1 -b .0001-ifupdown-pass-interface-device-name-for-ipv6-route-c
%patch6  -p1 -b .0001-ifupdown-use-x-hostname-NAME-with-udhcpc
%patch8  -p1 -b .0001-linedit-deluser-use-POSIX-getpwent-instead-of-getpwe
%patch9  -p1 -b .0001-diff-add-support-for-no-dereference
%patch10 -p1 -b .1000-fbsplash-use-virtual-y-size-in-mmap-size-calculation
%patch11 -p1 -b .1001-fbsplash-support-console-switching
%patch12 -p1 -b .1002-fbsplash-support-image-and-bar-alignment-and-positio
%patch13 -p1 -b .glibc
%patch14 -p1 -b .header

%__cp %{SOURCE2} loginutils/
%define _dyndir %{buildroot}/build-dynamic
mkdir -p %{_dyndir}

%build
	%__cc %{SOURCE1} -o bbsuid
	%__rm -f %{_dyndir}/.config
	%__cp %{SOURCE3} .config
	%__sed -i "s/CONFIG_EXTRA_COMPAT=y/CONFIG_EXTRA_COMPAT=n/" .config
	%__cp .config %{_dyndir}
	make O=%{_dyndir} silentoldconfig
	make

%install

mkdir -p %{buildroot}/usr/sbin %{buildroot}/usr/bin %{buildroot}/tmp \
	%{buildroot}/var/cache/misc %{buildroot}/bin %{buildroot}/sbin
chmod 1777 %{buildroot}/tmp
install -m755 busybox %{buildroot}/bin/busybox
install -m4111 bbsuid %{buildroot}/bin/bbsuid
# we need /bin/sh to be able to execute post-install
ln -sf /bin/busybox %{buildroot}/bin/sh

#ifupdown needs those dirs to be present
mkdir -p \
	%{buildroot}/etc/network/if-down.d \
	%{buildroot}/etc/network/if-post-down.d \
	%{buildroot}/etc/network/if-post-up.d \
	%{buildroot}/etc/network/if-pre-down.d \
	%{buildroot}/etc/network/if-pre-up.d \
	%{buildroot}/etc/network/if-up.d \

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/busybox --install -s


%files
%defattr(-,root,root,-)
%doc
/bin/busybox
/bin/bbsuid
/bin/sh
%dir /etc/network/if-down.d
%dir /etc/network/if-post-down.d
%dir /etc/network/if-post-up.d
%dir /etc/network/if-pre-down.d
%dir /etc/network/if-pre-up.d
%dir /etc/network/if-up.d

%changelog
