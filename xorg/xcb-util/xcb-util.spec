Name:		xcb-util
Version:	0.4.0
Release:	1%{?dist}
Summary:	Utility libraries for XC Binding

Group:		Development/Libraries
License:	MIT	
URL:		http://xcb.freedesktop.org/	
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2

BuildRequires:  libxcb-devel m4 gperf

%description
The xcb-util module provides a number of libraries which sit on top 
of libxcb, the core X protocol library, and some of the extension libraries.

%package devel                                                                 
Summary: Development files for %{name}                                         
Group: Development/Libraries                                                   
Requires: %{name} = %{version}-%{release}                                      
                                                                               
%description devel                                                             
The xcb-util development package  

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -m755 -d %{buildroot}/usr/share/licenses/%{name}
install -m644 COPYING %{buildroot}/usr/share/licenses/%{name}/

%files
%{_libdir}/lib%{name}.so.*.*.*
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}.so
%{_includedir}/xcb/*.h

%changelog

