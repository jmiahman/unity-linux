%define _fontsdir %{_datadir}/fonts

Summary:	X font encodings database
Name:		encodings
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/releases/individual/font/encodings-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	mkfontscale
BuildRequires:	font-util
BuildRequires:	util-macros
Requires:	font-util
BuildArch:	noarch

%description
X font encodings database.

%prep
%setup -q -n encodings-%{version}

%build
%configure \
	--build=%{_host} \
	--host=%{_host} \
	--with-encodingsdir=%{_fontsdir}/encodings

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
%{_fontsdir}/encodings

%changelog
