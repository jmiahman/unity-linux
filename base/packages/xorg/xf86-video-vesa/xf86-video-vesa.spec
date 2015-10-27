Summary:	X.org video driver for generic VESA video cards
Name:		xf86-video-vesa
Version:	2.3.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build
BuildRequires:	libpciaccess
BuildRequires:	fontsproto
BuildRequires:	randrproto
BuildRequires:	renderproto
BuildRequires:	xextproto
BuildRequires:	util-macros
BuildRequires:	xorg-server-devel
%{?requires_xorg_xserver_videodrv}
Requires:	libpciaccess 
Requires:	xorg-server 
Provides:	xorg-driver-video

%description
X.org video driver for generic VESA video cards.

%prep
%setup -q -n xf86-video-vesa-%{version}

%build

export LDFLAGS="$LDFLAGS -Wl,-z,lazy"
%configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/vesa_drv.so
%{_mandir}/man4/vesa.4*
