Summary:	XCB util-wm module
Name:		xcb-util-wm
Version:	0.4.1
Release:	1%{?dist}
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	87b19a1cd7bfcb65a24e36c300e03129
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	gperf
BuildRequires:	libxcb-devel
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto
BuildRequires:	util-macros
Requires:	libxcb

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-wm module provides the following libraries:
- ewmh: Both client and window-manager helpers for EWMH.
- icccm: Both client and window-manager helpers for ICCCM.

%package devel
Summary:	Header files for XCB util-wm libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel

%description devel
Header files for XCB util-wm libraries.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \

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
%attr(755,root,root) %{_libdir}/libxcb-icccm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-icccm.so.4
%attr(755,root,root) %{_libdir}/libxcb-ewmh.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-ewmh.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-ewmh.so
%attr(755,root,root) %{_libdir}/libxcb-icccm.so
%{_libdir}/libxcb-ewmh.la
%{_libdir}/libxcb-icccm.la
%{_includedir}/xcb/xcb_ewmh.h
%{_includedir}/xcb/xcb_icccm.h
%{_libdir}/pkgconfig/xcb-ewmh.pc
%{_libdir}/pkgconfig/xcb-icccm.pc

%changelog
