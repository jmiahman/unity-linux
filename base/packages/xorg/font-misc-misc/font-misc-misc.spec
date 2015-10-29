%define _fontsdir %{_datadir}/fonts

Summary:	Fixed bitmap fonts
Name:		font-misc-misc
Version:	1.1.2
Release:	1%{?dist}
License:	Public Domain
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-misc-misc-%{version}.tar.bz2
# Source0-md5:	c88eb44b3b903d79fb44b860a213e623
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	bdftopcf
BuildRequires:	mkfontdir
BuildRequires:	mkfontscale
BuildRequires:	font-util
BuildRequires:	util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
# contains useful aliases for these fonts
Requires:	font-alias
BuildArch:	noarch

%description
Fixed bitmap fonts. Main package contains Unicode fonts, Japanese k14
font and nil2 font.


%prep
%setup -q -n font-misc-misc-%{version}

%build
%configure \
	--build=%{_host} \
	--host=%{_host} \
	--prefix=/usr \
	--with-fontdir=%{_fontsdir}/misc \
	--with-mapfiles=/usr/share/fonts/util

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

make -j1 \
	DESTDIR=%{buildroot} \
	MKFONTDIR=: \
	MKFONTSCALE=: \
	FCCACHE=: \
install

mkfontdir %{buildroot}%{_fontsdir}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%{_fontsdir}/misc/4x6.pcf.gz
%{_fontsdir}/misc/5x7.pcf.gz
%{_fontsdir}/misc/5x8.pcf.gz
%{_fontsdir}/misc/6x9.pcf.gz
%{_fontsdir}/misc/6x10.pcf.gz
%{_fontsdir}/misc/6x12.pcf.gz
%{_fontsdir}/misc/6x13.pcf.gz
%{_fontsdir}/misc/6x13[BO].pcf.gz
%{_fontsdir}/misc/7x13.pcf.gz
%{_fontsdir}/misc/7x13[BO].pcf.gz
%{_fontsdir}/misc/7x14.pcf.gz
%{_fontsdir}/misc/7x14-JISX0201.1976-0.pcf.gz
%{_fontsdir}/misc/7x14B.pcf.gz
%{_fontsdir}/misc/8x13.pcf.gz
%{_fontsdir}/misc/8x13[BO].pcf.gz
%{_fontsdir}/misc/9x15.pcf.gz
%{_fontsdir}/misc/9x15B.pcf.gz
%{_fontsdir}/misc/9x18.pcf.gz
%{_fontsdir}/misc/9x18B.pcf.gz
%{_fontsdir}/misc/10x20.pcf.gz
%{_fontsdir}/misc/12x13ja.pcf.gz
%{_fontsdir}/misc/18x18ja.pcf.gz
%{_fontsdir}/misc/18x18ko.pcf.gz
%{_fontsdir}/misc/k14.pcf.gz
%{_fontsdir}/misc/nil2.pcf.gz
%{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz
%{_fontsdir}/misc/fonts.dir
%{_fontsdir}/misc/[45]x*-ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x9-ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x10-ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x12-ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x13[BO]-ISO8859-1.pcf.gz
%{_fontsdir}/misc/[789]x*-ISO8859-1.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-1.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-2.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-2.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-3.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-3.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-4.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-4.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-5.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-5.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-7.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-7.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-8.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-8.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-9.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-9.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-10.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-10.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-11.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-11.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-13.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-13.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-14.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-14.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-15.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-15.pcf.gz
%{_fontsdir}/misc/[456789]x*-ISO8859-16.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-16.pcf.gz
%{_fontsdir}/misc/[456789]x*-KOI8-R.pcf.gz
%{_fontsdir}/misc/10x20-KOI8-R.pcf.gz

%changelog
