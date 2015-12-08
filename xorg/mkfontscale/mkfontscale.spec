Summary:    mkfontscale application - create an index of scalable font files for X
Name:       mkfontscale
Version:    1.1.2
Release:    1%{?dist}
License:    MIT
Group:      User Interface/X
URL:        http://www.x.org

Source0:    http://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires: libfontenc-devel freetype-devel xproto zlib-devel

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by
the legacy X11 font system.

%package docs
Summary:  Doc files for xkbcomp
Requires: %{name} = %{version}

%description docs
Documentation files for mkfontscale

%prep
%setup -q 

%build

%configure \
	--with-bzip2 \

make %{?_smp_mflags}

%install
%make_install

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/mkfontscale

%files docs
%{_mandir}/man1/*.1*
