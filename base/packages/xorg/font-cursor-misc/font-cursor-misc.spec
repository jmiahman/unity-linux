%define _fontsdir %{_datadir}/fonts

Summary:	cursor font
Name:		font-cursor-misc
Version:	1.0.3
Release:	1%{?dist}
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-cursor-misc-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	bdftopcf
BuildRequires:	mkfontdir
BuildRequires:	mkfontscale
BuildRequires:	font-util
BuildRequires:	util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch

%description
cursor font needed by X server.

%prep
%setup -q -n font-cursor-misc-%{version}

%build
%configure \
	--build=%{_host} \
	--host=%{_host} \
	--with-fontdir=%{_fontsdir}/misc \
	--with-mapfiles=/usr/share/fonts/util

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_fontsdir}/misc/cursor.pcf.gz

%changelog
