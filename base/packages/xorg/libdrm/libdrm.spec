Name:       libdrm
Version:    2.4.65
Release:    1%{?dist}
Summary:    Userspace interface to kernel DRM services.
Group:      Development/Libraries
License:    Apache License
URL:        http://dri.freedesktop.org/
Source0:    http://ftp.osuosl.org/pub/blfs/svn/l/%{name}-%{version}.tar.bz2

Patch0:	    libdrm-limits.patch

BuildRequires: libpthread-stubs eudev-devel libpciaccess-devel linux-headers

%description
Userspace interface to kernel DRM services.

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

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure \
	--enable-udev \
	--disable-manpages \
	--disable-valgrind \
                                     
# temp workaround. problem appears to be with
# uclibc open_memstream() and stdio.h        
sed -i -e 's/-Werror-implicit-function-declaration//' intel/Makefile
                                                                            
make

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
%{_includedir}/*.h
%dir %{_includedir}/libdrm/
%dir %{_includedir}/libkms/
%{_includedir}/libdrm/*.h
%{_includedir}/libkms/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
