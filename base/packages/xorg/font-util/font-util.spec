%define _fontsdir %{_datadir}/fonts

Summary:	BDF font utilities (bdftruncate, ucs2any)
Name:		font-util
Version:	1.3.1
Release:	1
License:	BSD
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf 
BuildRequires:	automake
BuildRequires:	util-macros
Requires:	pkgconf

%description
X.org font package creation/installation utilities:
- bdftruncate generates truncated BDF font from ISO 10646-1-encoded
  BDF font
- ucs2any generates BDF fonts containing subsets of ISO 10646-1
  codepoints

%prep
%setup -q -n font-util-%{version}

%build
%configure \
	--with-mapdir=%{_fontsdir}/util \
	--with-fontrootdir=%{_fontsdir}

make

%install
rm -rf $RPM_BUILD_ROOT

make -j1 DESTDIR=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(0755, root, root) %{_bindir}/bdftruncate
%attr(0755, root, root) %{_bindir}/ucs2any
%dir %{_fontsdir}
%{_fontsdir}/util
%{_datadir}/man/man1/bdftruncate.1*
%{_datadir}/man/man1/ucs2any.1*
%{_datadir}/aclocal/fontutil.m4
%{_libdir}/pkgconfig/fontutil.pc

%changelog
