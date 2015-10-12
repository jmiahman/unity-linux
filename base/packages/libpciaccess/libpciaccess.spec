Name:       libpciaccess
Version:    0.13.4
Release:    1%{?dist}
Summary:    X.Org PCI access library.
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2

Patch0:	    fix-arm.patch
Patch1:     libpciaccess-limits.patch

%description
The libpciaccess package contains a library for 
portable PCI access routines across multiple operating systems.

%package devel                                                          
Summary: Development tools for %{name}.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%{_libdir}/libpciaccess.so.0
%{_libdir}/libpciaccess.so.0.*.*

%files devel
%{_includedir}/pciaccess.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpciaccess.so
%{_libdir}/libpciaccess.a

%changelog
