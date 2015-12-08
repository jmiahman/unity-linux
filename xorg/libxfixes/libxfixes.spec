Name:       libxfixes
Version:    5.0.1
Release:    1%{?dist}
Summary:    X.Org miscellaneous 'fixes' extension library.
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.bz2

%description
X.Org miscellaneous 'fixes' extension library.

%package devel                                                          
Summary: Development tools for libXfixes.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for libXfixes. If you like to develop programs using libXfixes, you will need
to install libXfixes-devel. 

%prep
%setup -q -n libXfixes-%{version} 

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
%{_libdir}/libXfixes.so.*
%{_libdir}/libXfixes.so.*.*.*

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libXfixes.so
%{_libdir}/libXfixes.a

%changelog
