%define _pixmapsdir %{_datadir}/pixmaps

Summary:	Terminal emulator for X
Name:		xterm
Version:	320
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	ftp://invisible-island.net/xterm/%{name}-%{version}.tgz
# Source0-md5:	0d7f0e6390d132ae59876b3870e5783d
Source1:	XTerm.ad-pl
Source2:	%{name}.desktop
Source3:	%{name}.png
Source4:	%{name}.1x.ko
Patch0:		%{name}-tinfo.patch
URL:		http://invisible-island.net/xterm/
BuildRequires:	fontconfig-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	libice-devel
BuildRequires:	libxaw-devel
BuildRequires:	libxft-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxpm-devel
BuildRequires:	libxt-devel 
Requires:	libxt

%description
The xterm program is a terminal emulator for the X Window System. It
provides DEC VT102/VT220 (VTxxx) and Tektronix 4014 compatible
terminals for programs that cannot use the window system directly.

This version implements ISO/ANSI colors using the "new" color model
(i.e., background color erase). It also implements most of the control
sequences for VT220.

%prep
%setup -q
%patch0 -p1

%build
# don't run autoconf, modified version of autoconf is required
CPPFLAGS="-I/usr/include/ncurses %{rpmcppflags}"
%configure \
	--enable-256-color \
	--enable-wide-chars \
	--with-app-defaults=%{_datadir}/X11/app-defaults \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so xterm.1' > $RPM_BUILD_ROOT%{_mandir}/man1/uxterm.1

install -D xterm.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/xterm.appdata.xml

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults/XTerm
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/xterm.desktop
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/xterm.png
install -D %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/ko/man1/xterm.1
echo '.so xterm.1' > $RPM_BUILD_ROOT%{_mandir}/ko/man1/uxterm.1

# cleanup unpackaged icons
%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/filled-xterm_*x*.xpm
%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/mini.xterm_*x*.xpm
%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/xterm-color_*x*.xpm
%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/xterm_*x*.xpm


%clean
rm -rf $RPM_BUILD_ROOT

%files
#### For Now take out later

%dir /usr/share/X11/app-defaults
%dir /usr/share/appdata


%defattr(644,root,root,755)
%doc README README.i18n xterm.log.html
%attr(755,root,root) %{_bindir}/resize
%attr(755,root,root) %{_bindir}/xterm
%attr(755,root,root) %{_bindir}/uxterm
%attr(755,root,root) %{_bindir}/koi8rxterm
%{_datadir}/X11/app-defaults/UXTerm
%{_datadir}/X11/app-defaults/UXTerm-color
%{_datadir}/X11/app-defaults/XTerm
%{_datadir}/X11/app-defaults/XTerm-color
%{_datadir}/X11/app-defaults/KOI8RXTerm
%{_datadir}/X11/app-defaults/KOI8RXTerm-color
%{_datadir}/appdata/xterm.appdata.xml
%{_desktopdir}/xterm.desktop
%{_pixmapsdir}/xterm.png
%{_mandir}/man1/resize.1*
%{_mandir}/man1/xterm.1*
%{_mandir}/man1/uxterm.1*
%{_mandir}/man1/koi8rxterm.1*

%changelog
