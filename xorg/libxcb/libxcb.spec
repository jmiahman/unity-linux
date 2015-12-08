Name:       libxcb
Version:    1.11
Release:    1%{?dist}
Summary:    A C binding to the X11 protocol
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2

## upstream patches (post 1.11 tag commits)
#Patch53: 0053-Call-_xcb_wake_up_next_reader-from-xcb_wait_for_spec.patch
#Patch54: 0054-Fix-a-thread-hang-with-xcb_wait_for_special_event.patch

BuildRequires:  libxslt
BuildRequires:  python
BuildRequires:  libxau-devel
BuildRequires:  xcb-proto
BuildRequires:	libpthread-stubs
BuildRequires:	libxdmcp

%description
The X protocol C-language Binding (XCB) is a replacement for Xlib featuring a
small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

#%package doc
#Summary:    Documentation for %{name}
#BuildArch:  noarch

#%description doc
#The %{name}-doc package contains documentation for the %{name} library.

%prep
%setup -q

%build
# autoreconf -f needed to expunge rpaths
#autoreconf -v -f --install
%configure \
    --enable-xkb \
    --enable-xinput \
    --disable-xprint \

# Remove rpath from libtool (extra insurance if autoreconf is ever dropped)
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
#install -pm 644 COPYING NEWS README $RPM_BUILD_ROOT%{_pkgdocdir}

find $RPM_BUILD_ROOT -name '*.la' -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libxcb-composite.so.0*
%{_libdir}/libxcb-damage.so.0*
%{_libdir}/libxcb-dpms.so.0*
%{_libdir}/libxcb-dri2.so.0*
%{_libdir}/libxcb-dri3.so.0*
%{_libdir}/libxcb-glx.so.0*
%{_libdir}/libxcb-present.so.0*
%{_libdir}/libxcb-randr.so.0*
%{_libdir}/libxcb-record.so.0*
%{_libdir}/libxcb-render.so.0*
%{_libdir}/libxcb-res.so.0*
%{_libdir}/libxcb-screensaver.so.0*
%{_libdir}/libxcb-shape.so.0*
%{_libdir}/libxcb-shm.so.0*
%{_libdir}/libxcb-sync.so.1*
%{_libdir}/libxcb-xevie.so.0*
%{_libdir}/libxcb-xf86dri.so.0*
%{_libdir}/libxcb-xfixes.so.0*
%{_libdir}/libxcb-xinerama.so.0*
%{_libdir}/libxcb-xinput.so.0*
%{_libdir}/libxcb-xkb.so.1*
%{_libdir}/libxcb-xtest.so.0*
%{_libdir}/libxcb-xv.so.0*
%{_libdir}/libxcb-xvmc.so.0*
%{_libdir}/libxcb.so.1*

%files devel
%{_includedir}/xcb
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#%{_mandir}/man3/*.3*

#%files doc
#%{_pkgdocdir}

%changelog
