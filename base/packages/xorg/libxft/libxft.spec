%define _pkgconfigdir %{_libdir}/pkgconfig

Summary:	X Font Rendering library
Name:		libxft
Version:	2.3.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/lib/libXft-%{version}.tar.bz2
# Source0-md5:	331b3a2a3a1a78b5b44cfbd43f86fcfe
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	libxrender-devel
BuildRequires:	util-macros
Requires:	fontconfig
Requires:	freetype
Requires:	libxrender 

%description
Xft is a library that connects X applications with the FreeType font
rasterization library. Xft uses fontconfig to locate fonts so it has
no configuration files.

%package devel
Summary:	Header files for libXft library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	freetype-devel
Requires:	libxrender-devel

%description devel
Header files for libXft library.

%prep
%setup -q -n libXft-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libXft.so.*.*.*
%{_libdir}/libXft.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXft.so
%{_libdir}/libXft.la
%dir %{_includedir}/X11/Xft
%{_includedir}/X11/Xft/*.h
%{_libdir}/pkgconfig/xft.pc
%{_mandir}/man3/Xft.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXft.a
