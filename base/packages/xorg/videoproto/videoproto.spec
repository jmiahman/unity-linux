Name:       videoproto
Version:    2.3.2
Release:    1%{?dist}
Summary:    X.Org Video extension wire protocol.
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/proto/%{name}-%{version}.tar.bz2

%description
This extension provides a protocol for a video output mechanism,
mainly to rescale video playback in the video controller hardware.

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
%{_includedir}/X11/extensions
%{_libdir}/pkgconfig/*.pc
#%{_datadir}/licenses/%{name}/COPYING
#%{_datadir}/doc/xtrans/%{name}.xml

%changelog
