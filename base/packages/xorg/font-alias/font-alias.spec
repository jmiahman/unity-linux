%define _fontsdir %{_datadir}/fonts

Summary:	X font alias databases
Name:		font-alias
Version:	1.0.3
Release:	1%{?dist}
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-alias-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	font-util
BuildRequires:	util-macros
Requires(post,postun):	fontpostinst
Requires:	font-util
BuildArch:	noarch

%description
X font alias databases.

%prep
%setup -q -n font-alias-%{version}

%build
%configure \
	--build=%{_host} \
	--host=%{_host} \
	--with-fontrootdir=%{_fontsdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for d in 100dpi 75dpi cyrillic misc ; do
	mv $RPM_BUILD_ROOT%{_fontsdir}/$d/fonts.alias $RPM_BUILD_ROOT%{_fontsdir}/$d/fonts.alias.xorg
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst 100dpi
fontpostinst 75dpi
fontpostinst cyrillic
fontpostinst misc

%postun
fontpostinst 100dpi
fontpostinst 75dpi
fontpostinst cyrillic
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%dir %{_fontsdir}/100dpi/                                                             
%dir %{_fontsdir}/75dpi/                                                              
%dir %{_fontsdir}/cyrillic/                                                           
%dir %{_fontsdir}/misc/
%{_fontsdir}/100dpi/fonts.alias.xorg
%{_fontsdir}/75dpi/fonts.alias.xorg
%{_fontsdir}/cyrillic/fonts.alias.xorg
%{_fontsdir}/misc/fonts.alias.xorg

%changelog
