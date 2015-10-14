Name:       xauth
Version:    1.0.8
Release:    1%{?dist}
Summary:    X.Org authorization settings program.
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/app/xauth-%{version}.tar.bz2

%description
The xauth program is used to edit and display the authorization 
information used in connecting to the X server. 

%prep
%setup -q -n xauth-%{version}

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
%{_bindir}/*

%changelog
