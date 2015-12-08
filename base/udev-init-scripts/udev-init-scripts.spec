Name:		udev-init-scripts	
Version:	30
Release:	1%{?dist}
Summary:	eudev startup scripts for openrc

Group:		Base/System	
License:	GPLv2
URL:		https://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/sys-fs/udev-init-scripts/
Source0:	http://dev.gentoo.org/~williamh/dist/udev-init-scripts-%{version}.tar.gz

Patch0:		provide-dev.patch

BuildRequires: make
Requires: eudev

%description
eudev startup scripts for OpenRC


%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags}


%install
%make_install

%post
if ! [ -e /etc/runlevels/sysinit/udev ]; then
	exit 0
fi

if ! [ /etc/runlevels/sysinit/udev-trigger ]; then
	ln -s /etc/init.d/udev-trigger /etc/runlevels/sysinit/udev-trigger
	# eudev does not work without libkmod, so we fall back to mdev style
	# modalias loading for now
	ln -s /etc/init.d/hwdrivers /etc/runlevels/sysinit/hwdrivers
fi

%files
/etc/init.d/udev-settle
/etc/init.d/udev-trigger
/etc/init.d/udev
/etc/conf.d/udev-settle
/etc/conf.d/udev-trigger
/etc/conf.d/udev

%changelog

