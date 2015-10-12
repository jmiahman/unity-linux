Name:       xf86dgaproto
Version:    2.1
Release:    1%{?dist}
Summary:    X.Org Direct Graphics Access extension wire protocol.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/proto/%{name}-%{version}.tar.bz2

%description
This package provides development headers describing the wire protocol for the 
XFree86-DGA extension, which provides direct, framebuffer-like, graphics access.

%prep
%setup -q

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

#mv pc file to correct location
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_includedir}/X11/extensions/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
