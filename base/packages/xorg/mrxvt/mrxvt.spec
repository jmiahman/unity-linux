%define _desktopdir /usr/share/applications
%define _pixmapsdir /usr/share/pixmaps
%define _sysconfdir /etc

Summary:	mrxvt - tabbed terminal emulator in an X Window System
Name:		mrxvt
Version:	0.5.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/materm/%{name}-%{version}.tar.gz
# Source0-md5:	0232c8868484751dcb931a28f0756f69
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-xkill.patch
Patch1:		%{name}-0.5.4-002-fix-segfault-when-wd-empty.patch
Patch2:		musl-fix-includes.patch

URL:		http://materm.sourceforge.net/
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libx11-devel
Requires:	ncurses-terminfo

%description
Mrxvt is a multi-tabbed color vt102 terminal emulator for X Window
System. It features multi-tab support, fast pseudo-transparent
background, user supplied XPM/JPEG/PNG images for background, tinting,
off-focus fading, text shadow, NeXT/Rxvt/Xterm/SGI/Plain style
scrollbars, XIM and multi-languages (Chinese/Korea/Japanese), and
logging.

Mrxvt does NOT require KDE or GNOME desktop environment.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

%configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--enable-xft \
	--enable-text-shadow \
	--enable-transparency \
	--enable-smart-resize \
	--enable-menubar \
	--disable-ourstrings \
	--enable-linespace \
	--enable-256colors \
	--enable-xim \
	--enable-thai \
	--enable-greek \
	--enable-cjk \
	--enable-backspace-key \
	--with-save-lines=2048 \

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS NEWS TODO
%doc doc/README.*
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/mrxvt
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}-csh.png
%{_pixmapsdir}/%{name}-root.png
