Name:       mcpp
Version:    2.7.2
Release:    1%{?dist}
Summary:    A portable C preprocessor.
Group:      Development/Languages
License:    BSD-style-license
URL:        mcpp.sourceforge.net
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Patch0:     01-zeroc-fixes.patch
Patch1:     02-gniibe-fixes.patch

Requires:   %{name}-libs = %{version}

%description
A portable C/C++ preprocessor supporting 
several compiler-systems on UNIX and Windows.

%package libs
Summary: Libraries for %{name}.                                            
Group: Development/Languages                                                       
                                                                                   
%description libs        
This package contains the library files                
for %{name}.           

%package devel                                                          
Summary: Development tools for %{name}.
Group: Development/Languages                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel. 

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure \
	--enable-mcpplib \
	--disable-static \

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

%files libs
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}.so.*.*.*

%files devel
%{_includedir}/*.h
%{_libdir}/lib%{name}.so

%changelog
