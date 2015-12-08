Name:       libxt
Version:    1.1.5
Release:    1%{?dist}
Summary:    X.Org toolkit intrinsics library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXt-%{version}.tar.bz2

BuildRequires: xproto libx11-devel libsm-devel
BuildRequires: libice-devel e2fsprogs-devel

%description
libXt provides the X Toolkit Intrinsics, an abstract widget 
library upon which other toolkits are based.

%package devel                                                          
Summary: Development tools for libXt.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for libXt. If you like to develop programs using libXt, you will need
to install libXt-devel. 

%prep
%setup -q -n libXt-%{version}

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
%{_libdir}/libXt.so.*
%{_libdir}/libXt.so.*.*.*

%files devel
%{_includedir}/X11/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libXt.so
%{_libdir}/libXt.a

%changelog
