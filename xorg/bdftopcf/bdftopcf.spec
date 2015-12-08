Summary:	bdftopcf application - convert X font from BDF to PCF
Name:		bdftopcf
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/bdftopcf-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	pkgconfig
BuildRequires:	libxfont-devel
BuildRequires:	util-macros

%description
bdftopcf is a font compiler for the X server and font server. Fonts in
Portable Compiled Format can be read by any architecture, although the
file is structured to allow one particular architecture to read them
directly without reformatting. This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%prep
%setup -q -n bdftopcf-%{version}

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*

%changelog
