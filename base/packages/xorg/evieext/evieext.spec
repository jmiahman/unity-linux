Name:       evieext
Version:    1.1.1
Release:    1%{?dist}
Summary:    EvIE extension headers
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/proto/%{name}-%{version}.tar.bz2

BuildRequires: util-macros

%description
Extended Visual Information Extension (XEVIE) defines a protocol for a
client to determine information about core X visuals beyond what the
core protocol provides.

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
