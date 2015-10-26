Name:       libdmx
Version:    1.1.3
Release:    1%{?dist}
Summary:    DMX extension library
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libdmx-%{version}.tar.bz2

BuildRequires:	libxext-devel
BuildRequires:	dmxproto
BuildRequires:	util-macros

%description
DMX (Distributed Multihead X) extension library.

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
%{_libdir}/libdmx.so.*.*.*
%{_libdir}/libdmx.so.*

%files devel
%{_libdir}/libdmx.so
%{_includedir}/X11/extensions/dmxext.h
%{_pkgconfigdir}/dmx.pc
%{_mandir}/man3/DMX*.3*

%changelog
