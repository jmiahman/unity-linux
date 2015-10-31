%define		_xsessdir	/usr/share/xsessions
# for system.twmrc
%define		_sysconfdir	/etc

Summary:	Tab Window Manager for the X Window System
Name:		twm
Version:	1.0.9
Release:	1
License:	MIT
Group:		X11/Window Managers
Source0:	http://xorg.freedesktop.org/releases/individual/app/twm-%{version}.tar.bz2
Source1:	twm-xsession.desktop
URL:		http://xorg.freedesktop.org/

Patch0: 	twm-1.0.9-unity.patch	

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig
BuildRequires:	libice-devel
BuildRequires:	libsm-devel
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxt-devel
BuildRequires:	xproto
BuildRequires:	util-macros
Suggests:	mrxvt

%description
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%prep
%setup -q -n twm-%{version}
%patch0 -p1

%build
%configure \
	--datarootdir=/etc \
	--sysconfdir=/etc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_xsessdir}/twm.desktop

# install the default config file currently.  We'll work around it here for now.
{
   echo "FIXME: Upstream doesn't install systemwide config by default"
   mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/twm
   install -p -m 0644 src/system.twmrc $RPM_BUILD_ROOT%{_sysconfdir}/X11/twm/
   rm -fr $RPM_BUILD_ROOT%{_datadir}/X11
}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/twm
%dir %{_sysconfdir}/X11/twm
%{_sysconfdir}/X11/twm/system.twmrc
%{_xsessdir}/twm.desktop
%{_datadir}/man/man1/twm.1*
