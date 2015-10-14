Name:       pixman
Version:    0.32.8
Release:    1%{?dist}
Summary:    The X.Org Pixman library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2

Patch0:     float-header-fix.patch

BuildRequires: perl

%description
Pixman is a low-level software library for pixel manipulation, 
providing features such as image compositing and trapezoid rasterization.

%package devel                                                          
Summary: Development tools for %{name}.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel. 

%prep
%setup -q -n %{name}-%{version} 
%patch0 -p1

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
%{_libdir}/lib%{name}-1.so.*
%{_libdir}/lib%{name}-1.so.*.*.*

%files devel
%dir %{_includedir}/pixman-1/
%{_includedir}/pixman-1/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}-1.so

%changelog
