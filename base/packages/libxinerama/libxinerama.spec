Name:       libxinerama
Version:    1.1.3
Release:    1%{?dist}
Summary:    X.Org Xinerama extension library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2

BuildRequires: xineramaproto libx11-devel libxext-devel

%description
The X.Org Xinerama extension library.

%package devel                                                          
Summary: Development tools for libXinerama.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for libXinerama. If you like to develop programs using libXinerama, you will need
to install libXinerama-devel. 

%prep
%setup -q -n libXinerama-%{version} 

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
%{_libdir}/libXinerama.so.*
%{_libdir}/libXinerama.so.*.*.*

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libXinerama.so
%{_libdir}/libXinerama.a

%changelog
