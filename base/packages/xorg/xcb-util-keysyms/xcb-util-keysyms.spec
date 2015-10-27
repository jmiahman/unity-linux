Summary:	XCB util-keysyms module
Name:		xcb-util-keysyms
Version:	0.4.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	xproto
Requires:	libxcb

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-keysyms module provides the following library:
- keysyms: Standard X key constants and conversion to/from keycodes.

%package devel
Summary:	Header files for XCB util-keysyms library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4

%description devel
Header files for XCB util-keysyms library.

%prep
%setup -q

%build
%configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \
	--disable-silent-rules \

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
%attr(755,root,root) %{_libdir}/libxcb-keysyms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-keysyms.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-keysyms.so
%{_libdir}/libxcb-keysyms.la
%{_includedir}/xcb/xcb_keysyms.h
%{_pkgconfigdir}/xcb-keysyms.pc

%changelog
