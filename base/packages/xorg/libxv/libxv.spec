Name:       libxv
Version:    1.0.10
Release:    1%{?dist}
Summary:    X.Org Video extension library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXv-%{version}.tar.bz2

BuildRequires: xproto videoproto libx11-devel libxext-devel

%description
X.Org Video extension library.

%package devel                                                          
Summary: Development tools for libXv.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for libXv. If you like to develop programs using libXv, you will need
to install libXv-devel. 

%prep
%setup -q -n libXv-%{version} 

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
%{_libdir}/libXv.so.*
%{_libdir}/libXv.so.*.*.*

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libXv.so
%{_libdir}/libXv.a

%changelog
