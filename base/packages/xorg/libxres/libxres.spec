Name:       libxres
Version:    1.0.7
Release:    1%{?dist}
Summary:    X.Org Resource extension library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.bz2

BuildRequires: xproto resourceproto
BuildRequires: libx11-devel libxext-devel

%description
X.Org Resource extension library.

%package devel                                                          
Summary: Development tools for %{name}.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel. 

%prep
%setup -q -n libXres-%{version}

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure \
	--sysconfdir=/etc \
                                     
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
%{_libdir}/libXRes.so
%{_includedir}/X11/extensions/XRes.h
%{_libdir}/pkgconfig/xres.pc
%{_mandir}/man3/XRes*.3*

%changelog
