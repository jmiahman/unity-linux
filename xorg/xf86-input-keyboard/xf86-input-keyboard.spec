Summary:	X.org keyboard input drivers
Name:		xf86-input-keyboard
Version:	1.8.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-keyboard-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	inputproto
BuildRequires:	kbproto
BuildRequires:	util-macros
BuildRequires:	xorg-server-devel
BuildRequires:	rpm-build
%{?requires_xorg_xserver_xinput}
Requires:	xorg-server
Requires:	mdocml-docs

%description
X.org keyboard input drivers. They support the standard OS-provided
keyboard interface.

%prep
%setup -q -n xf86-input-keyboard-%{version}

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
%attr(755,root,root) %{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.4*

%changelog
