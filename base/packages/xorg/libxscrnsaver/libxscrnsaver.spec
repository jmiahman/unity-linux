Summary:	XScrnSaver (X11 Screen Saver) extension client library
Name:		libxScrnSaver
Version:	1.2.2
Release:	1%{?dist}
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.bz2
# Source0-md5:	7a773b16165e39e938650bcc9027c1d5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	libxext-devel
BuildRequires:	scrnsaverproto >= 1.2
BuildRequires:	xextproto
BuildRequires:	util-macros >= 1.8

%description
XScrnSaver (X11 Screen Saver) extension client library.

%package devel
Summary:	Header files for libXScrnSaver library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxext-devel
Requires:	scrnsaverproto >= 1.2

%description devel
XScrnSaver (X11 Screen Saver) extension client library.

This package contains the header files needed to develop programs that
use libXScrnSaver.

%package static
Summary:	Static libXScrnSaver library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XScrnSaver (X11 Screen Saver) extension client library.

This package contains the static libXScrnSaver library.

%prep
%setup -q -n libXScrnSaver-%{version}

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
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXss.so.*.*.*
%attr(755,root,root) %{_libdir}/libXss.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXss.so
%{_libdir}/libXss.la
%{_includedir}/X11/extensions/scrnsaver.h
%{_libdir}/pkgconfig/xscrnsaver.pc
%{_mandir}/man3/XScreenSaver*.3*
%{_mandir}/man3/Xss.3*

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libXss.a

%changelog
