Summary:	X.org mouse input driver
Name:		xf86-input-mouse
Version:	1.9.1
Release:	1%{?dist}
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build
BuildRequires:	inputproto
BuildRequires:	xproto
BuildRequires:	util-macros
BuildRequires:	xorg-server-devel
%{?requires_xorg_xserver_xinput}
Requires:	xorg-server
Requires:	mdocml-docs

%description
X.org mouse input driver. It supports most available mouse types and
interfaces, including USB and PS/2.

%package devel
Summary:	Header file for mouse driver
Summary(pl.UTF-8):	Plik nagłówkowy sterownika myszy
Group:		Development/Libraries

%description devel
Header file for mouse driver.

%prep
%setup -q -n xf86-input-mouse-%{version}

%build
export LDFLAGS="$LDFLAGS -Wl,-z,lazy"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/mouse_drv.so
%{_mandir}/man4/mousedrv.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/xf86-mouse-properties.h
%{_pkgconfigdir}/xorg-mouse.pc

%changelog
