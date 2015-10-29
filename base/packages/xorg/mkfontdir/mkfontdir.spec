Summary:	mkfontdir application - create an index of X font files in a directory
Name:		mkfontdir
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/mkfontdir-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	util-macros
Requires:	mkfontscale
BuildArch:	noarch

%description
mkfontdir creates the fonts.dir files needed by the legacy X server
core font system. The current implementation is a simple wrapper
script around the mkfontscale program, which must be installed first.

%prep
%setup -q -n mkfontdir-%{version}

%build
%configure \
	--build=%{_host} \
	--host=%{_host}

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
%attr(755,root,root) %{_bindir}/mkfontdir
%{_datadir}/man/man1/mkfontdir.1*

%changelog
