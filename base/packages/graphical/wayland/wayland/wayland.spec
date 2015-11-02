Name:           wayland
Version:        1.9.0
Release:        1%{?dist}
Summary:        Wayland Compositor Infrastructure

Group:          User Interface/X
License:        MIT
URL:            http://%{name}.freedesktop.org/
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  libffi
BuildRequires:  expat-devel
BuildRequires:  chrpath

#BuildRequires:  doxygen
#BuildRequires:  libxslt
#BuildRequires:  docbook-style-xsl
#BuildRequires:  xmlto
#BuildRequires:  graphviz

%description
Wayland is a protocol for a compositor to talk to its clients as well as a C
library implementation of that protocol. The compositor can be a standalone
display server running on Linux kernel modesetting and evdev input devices,
an X application, or a wayland client itself. The clients can be traditional
applications, X servers (rootless or fullscreen) or other display servers.

%package devel
Summary: Common headers for wayland
License: MIT
%description devel
Common headers for wayland

#%package docs
#Summary: Wayland development documentation
#License: MIT
#BuildArch: noarch
#%description docs
#Wayland development documentation

%package -n libwayland-client
Summary: Wayland client library
License: MIT
%description -n libwayland-client
Wayland client library

%package -n libwayland-cursor
Summary: Wayland cursor library
License: MIT
%description -n libwayland-cursor
Wayland cursor library

%package -n libwayland-server
Summary: Wayland server library
License: MIT
%description -n libwayland-server
Wayland server library

%package -n libwayland-client-devel
Summary: Headers and symlinks for developing wayland client applications
License: MIT
Requires: libwayland-client%{?_isa} = %{version}-%{release}
Requires: wayland-devel%{?_isa} = %{version}-%{release}
%description -n libwayland-client-devel
Headers and symlinks for developing wayland client applications.

%package -n libwayland-cursor-devel
Summary: Headers and symlinks for developing wayland cursor applications
License: MIT
Requires: libwayland-cursor%{?_isa} = %{version}-%{release}
Requires: wayland-devel%{?_isa} = %{version}-%{release}
%description -n libwayland-cursor-devel
Headers and symlinks for developing wayland cursor applications.

%package -n libwayland-server-devel
Summary: Headers and symlinks for developing wayland server applications
License: MIT
Requires: libwayland-server%{?_isa} = %{version}-%{release}
Requires: wayland-devel%{?_isa} = %{version}-%{release}
%description -n libwayland-server-devel
Headers and symlinks for developing wayland server applications.

%prep
%setup -q

%build
%configure --disable-static --disable-documentation
make %{?_smp_mflags}


%install
%make_install

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

# Remove lib64 rpaths
chrpath -d $RPM_BUILD_ROOT%{_libdir}/libwayland-cursor.so

%check
mkdir -m 700 tests/run
# known failure in i686 koji (not always, but sometimes?):
#     resources-test, test "destroy_res_tst":	signal 11, fail
XDG_RUNTIME_DIR=$PWD/tests/run make check || \
{ rc=$?; cat tests/test-suite.log; } # exit $rc; }


%post -n libwayland-client -p /sbin/ldconfig
%postun -n libwayland-client -p /sbin/ldconfig

%post -n libwayland-cursor -p /sbin/ldconfig
%postun -n libwayland-cursor -p /sbin/ldconfig

%post -n libwayland-server -p /sbin/ldconfig
%postun -n libwayland-server -p /sbin/ldconfig


%files devel
%{_bindir}/wayland-scanner
%{_includedir}/wayland-util.h
%{_includedir}/wayland-egl.h
%{_includedir}/wayland-egl-core.h
%{_includedir}/wayland-version.h
%{_datadir}/aclocal/wayland-scanner.m4
%{_libdir}/pkgconfig/wayland-scanner.pc
%dir %{_datadir}/wayland
%{_datadir}/wayland/wayland-scanner.mk
%{_datadir}/wayland/wayland.xml
%{_datadir}/wayland/wayland.dtd
#%{_mandir}/man3/*.3*

#%files docs
#%doc README TODO
#%{_datadir}/doc/wayland/

%files -n libwayland-client
%{_libdir}/libwayland-client.so.0*

%files -n libwayland-cursor
%{_libdir}/libwayland-cursor.so.0*

%files -n libwayland-server
%{_libdir}/libwayland-server.so.0*

%files -n libwayland-client-devel
%{_includedir}/wayland-client*.h
%{_libdir}/libwayland-client.so
%{_libdir}/pkgconfig/wayland-client.pc

%files -n libwayland-cursor-devel
%{_includedir}/wayland-cursor*.h
%{_libdir}/libwayland-cursor.so
%{_libdir}/pkgconfig/wayland-cursor.pc

%files -n libwayland-server-devel
%{_includedir}/wayland-server*.h
%{_libdir}/libwayland-server.so
%{_libdir}/pkgconfig/wayland-server.pc

%changelog
