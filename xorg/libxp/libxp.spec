Summary:	X Print Client library
Name:		libxp
Version:	1.0.3
Release:	1%{?dist}
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXp-%{version}.tar.bz2
# Source0-md5:	df9e6bf0d988de6694f08693b8002079
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	libx11-devel >= 1.6
BuildRequires:	libxau-devel
BuildRequires:	libxext-devel
BuildRequires:	printproto
BuildRequires:	xextproto
BuildRequires:	util-macros >= 1.8
Requires:	libx11 >= 1.6

%description
X Print Client library.

%package devel
Summary:	Header files for libXp library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libx11-devel >= 1.6
Requires:	libxau-devel
Requires:	libxext-devel
Requires:	printproto

%description devel
DtPrint extension library.

This package contains the header files needed to develop programs that
use libXp.

%package static
Summary:	Static libXp library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
DtPrint extension library.

This package contains the static libXp library.

%prep
%setup -q -n libXp-%{version}

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXp.so.*.*.*
%attr(755,root,root) %{_libdir}/libXp.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXp.so
%{_libdir}/libXp.la
%{_libdir}/pkgconfig/xp.pc
%{_mandir}/man3/Xp*.3*
%{_mandir}/man3/libXp.3*

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libXp.a
