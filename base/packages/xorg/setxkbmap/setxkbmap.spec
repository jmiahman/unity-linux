Summary:	setxkbmap application - set the keyboard using the X Keyboard Extension
Name:		setxkbmap
Version:	1.3.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/setxkbmap-%{version}.tar.bz2
# Source0-md5:	2c47a1b8e268df73963c4eb2316b1a89
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	libx11-devel
BuildRequires:	libxkbfile-devel
BuildRequires:	util-macros >= 1.8

%description
The setxkbmap command maps the keyboard to use the layout determined
by the options specified on the command line.

An XKB keymap is constructed from a number of components which are
compiled only as needed.

%prep
%setup -q -n setxkbmap-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1*

%changelog
