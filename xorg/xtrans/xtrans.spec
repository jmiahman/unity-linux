Name:       xtrans
Version:    1.3.5
Release:    1%{?dist}
Summary:    X transport library
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2

%description
xtrans is a library of code that is shared among various X packages to handle
network protocol transport in a modular fashion, allowing a single place to
add new transport types.   It is used by the X server, libX11, libICE, the
X font server, and related components.

%prep
%setup -q

%build
%configure \
	--enable-secure-rpc
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

#mv pc file to correct location
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/
mv %{buildroot}/%{_datadir}/pkgconfig/%{name}.pc %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_includedir}/X11/Xtrans
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/xtrans.m4
#%{_datadir}/licenses/xtrans/COPYING
#%{_datadir}/doc/xtrans/xtrans.xml

%changelog
