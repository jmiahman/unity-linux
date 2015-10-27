Summary:	XCB util-image module
Name:		xcb-util-image
Version:	0.4.0
Release:	1%{?dist}
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto
BuildRequires:	xcb-util-devel >= 0.4.0
BuildRequires:	xproto
Requires:	libxcb
Requires:	xcb-util

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-image module provides the following library:
- image: Port of Xlib's XImage and XShmImage functions.

%package devel
Summary:	Header files for XCB util-image library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB util-image
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel
Requires:	xcb-util-devel

%description devel
Header files for XCB util-image library.

%prep
%setup -q

%build
%configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \
	--disable-silent-rules
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxcb-image.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-image.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-image.so
%{_libdir}/libxcb-image.la
%{_includedir}/xcb/xcb_bitops.h
%{_includedir}/xcb/xcb_image.h
%{_includedir}/xcb/xcb_pixel.h
%{_pkgconfigdir}/xcb-image.pc

%changelog
