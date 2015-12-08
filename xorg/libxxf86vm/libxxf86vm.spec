Summary: X.Org X11 libXxf86vm runtime library
Name: libxxf86vm
Version: 1.1.4
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: http://xorg.freedesktop.org/archive/individual/lib/libXxf86vm-%{version}.tar.bz2

Requires: libx11

BuildRequires: util-macros
BuildRequires: libxext-devel xf86vidmodeproto
BuildRequires: libx11-devel 

%description
X.Org X11 libXxf86vm runtime library

%package devel
Summary: X.Org X11 libXxf86vm development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXxf86vm development package

%package docs
Summary: X.Org X11 libXxf86vm documentation package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description docs
X.Org X11 libXxf86vm documentation package

%prep
%setup -q -n libXxf86vm-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libXxf86vm.so.1
%{_libdir}/libXxf86vm.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
%{_includedir}/X11/extensions/xf86vmode.h

%files docs
%{_mandir}/man3/*.3*
%doc README COPYING

%changelog
