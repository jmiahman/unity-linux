Summary:	X.org input driver for Linux generic event devices
Name:		xf86-input-evdev	
Version:	2.9.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-%{version}.tar.bz2
Source1:	evdev.conf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libevdev-devel
BuildRequires:	libtool
BuildRequires:	mtdev-devel
BuildRequires:	pkgconfig 
BuildRequires:	rpm-build
BuildRequires:	eudev-devel
BuildRequires:	inputproto
BuildRequires:	kbproto
BuildRequires:	util-macros
BuildRequires:	xorg-server-devel
%{?requires_xorg_xserver_xinput}
Requires:	libevdev
Requires:	mdocml-docs
Requires:	xorg-server >= 1.12

%description
X.org input driver for Linux generic event devices. It supports all
input devices that the kernel knows about, including most mice and
keyboards.

%package devel
Summary:	Header file for evdev driver
Summary(pl.UTF-8):	Plik nagłówkowy sterownika evdev
Group:		Development/Libraries

%description devel
Header file for evdev driver.

%prep
%setup -q -n xf86-input-evdev-%{version}

%build
export LDFLAGS="$LDFLAGS -Wl,-z,lazy"
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/xorg.conf.d
cp -p %{SOURCE1}  $RPM_BUILD_ROOT/etc/X11/xorg.conf.d/10-evdev.conf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%config(noreplace) %verify(not md5 mtime size) /etc/X11/xorg.conf.d/10-evdev.conf
%attr(755,root,root) %{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/evdev-properties.h
%{_pkgconfigdir}/xorg-evdev.pc

%changelog
