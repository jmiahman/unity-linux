Summary: Cursor management library
Name: libxcursor
Version: 1.1.14
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: http://xorg.freedesktop.org/archive/individual/lib/libXcursor-%{version}.tar.bz2

BuildRequires: xproto libx11-devel libxrender-devel libxfixes-devel

%description
This is  a simple library designed to help locate and load cursors.
Cursors can be loaded from files or memory. A library of common cursors
exists which map to the standard X cursor names.Cursors can exist in
several sizes and the library automatically picks the best size.

%package devel
Summary: Development files for libXcursor
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
libXcursor development package.

%package docs
Summary: Document files for libXcursor
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description docs
libXcursor document package.

%prep
%setup -q -n libXcursor-%{version}

%build

%configure \
 --disable-static

make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/libXcursor.so.1
%{_libdir}/libXcursor.so.1.0.2

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/Xcursor.h
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc

%files docs
%{_mandir}/man3/Xcursor*.3*



%changelog
