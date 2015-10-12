Name:       libxmu
Version:    1.1.2
Release:    1%{?dist}
Summary:    X.Org miscellaneous micro-utility library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.bz2

%description
X.Org damaged region extension library.

%package devel                                                          
Summary: Development tools for libXmu.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for libXmu. If you like to develop programs using libXmu, you will need
to install libXmu-devel. 

%prep
%setup -q -n libXmu-%{version}

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
%{_libdir}/*.so.*
%{_libdir}/*.so.*.*.*

%files devel
%dir %{_includedir}/X11/Xmu/
%{_includedir}/X11/Xmu/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
