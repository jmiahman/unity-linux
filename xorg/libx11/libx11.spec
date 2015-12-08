Summary: Core X11 protocol client library
Name: libx11
Version: 1.6.3
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: http://xorg.freedesktop.org/archive/individual/lib/libX11-%{version}.tar.bz2

BuildRequires: xproto
BuildRequires: xtrans
BuildRequires: libxcb-devel
BuildRequires: libxau-devel libxdmcp
BuildRequires: inputproto
BuildRequires: util-macros
BuildRequires: kbproto

%description
Core X11 protocol client library.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libX11 development package

%prep
%setup -q -n libX11-%{version}

%build
# sodding libtool
%configure --disable-static --with-xcb
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
find $RPM_BUILD_ROOT -type f -name '*.la' -delete

# FIXME: Don't install Xcms.txt - find out why upstream still ships this.
find $RPM_BUILD_ROOT -name 'Xcms.txt' -delete

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libX11.so.6
%{_libdir}/libX11.so.6.3.0
%{_libdir}/libX11-xcb.so.1
%{_libdir}/libX11-xcb.so.1.0.0
#%doc AUTHORS COPYING README NEWS
%dir %{_datadir}/X11
%{_datadir}/X11/locale/
%{_datadir}/X11/XErrorDB

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/ImUtil.h
%{_includedir}/X11/XKBlib.h
%{_includedir}/X11/Xcms.h
%{_includedir}/X11/Xlib.h
%{_includedir}/X11/XlibConf.h
%{_includedir}/X11/Xlibint.h
%{_includedir}/X11/Xlib-xcb.h
%{_includedir}/X11/Xlocale.h
%{_includedir}/X11/Xregion.h
%{_includedir}/X11/Xresource.h
%{_includedir}/X11/Xutil.h
%{_includedir}/X11/cursorfont.h
%{_libdir}/libX11.so
%{_libdir}/libX11-xcb.so
%{_libdir}/pkgconfig/x11.pc
%{_libdir}/pkgconfig/x11-xcb.pc
#%{_mandir}/man3/*.3*
#%{_mandir}/man5/*.5*

%changelog
