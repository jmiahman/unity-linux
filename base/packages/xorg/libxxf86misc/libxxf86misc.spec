Name:       libxxf86misc
Version:    1.0.3
Release:    1%{?dist}
Summary:    X.Org XFree86 miscellaneous extension library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXxf86misc-%{version}.tar.bz2

BuildRequires: xf86miscproto libxext-devel libx11-devel

%description
X.Org XFree86 miscellaneous extension library.

%package devel                                                          
Summary: Development tools for %{name}.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel. 

%prep
%setup -q -n libXxf86misc-%{version}

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
%{_libdir}/libXxf86misc.so.*
%{_libdir}/libXxf86misc.so.*.*.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libXxf86misc.so
%{_libdir}/libXxf86misc.a

%changelog
