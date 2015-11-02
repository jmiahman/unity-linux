Summary:	X Evie extension library
Name:		libxevie
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXevie-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig 
BuildRequires:	libxext-devel
BuildRequires:	evieext
BuildRequires:	util-macros

%description
X Evie extension library.

%package devel
Summary:	Header files for libXevie library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxext-devel
Requires:	evieext

%description devel
X Evie extension library

This package contains the header files needed to develop programs that
use libXevie.

%package static
Summary:	Static libXevie library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
X Evie extension library

This package contains the static libXevie library.

%prep
%setup -q -n libXevie-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXevie.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXevie.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXevie.so
%{_libdir}/libXevie.la
%{_includedir}/X11/extensions/Xevie.h
%{_libdir}/pkgconfig/xevie.pc
%{_mandir}/man3/Xevie*.3*
