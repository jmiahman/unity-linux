Summary:	Font post (un)installation script
Name:		fontpostinst
Version:	0.1
Release:	1
License:	Free
Group:		Applications/System
Source0:	%{name}
Requires:	coreutils
BuildArch:	noarch

%description
Script to be called after each fonts installation or uninstallation.
It supports regeneration of XFree86 fonts.alias, fonts.scale,
fonts.dir files, gnome-font catalogs, ghostscript Fontmaps,
fontconfig/xft cache and t1lib FontDatabase.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%changelog
