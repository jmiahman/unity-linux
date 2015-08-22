
Name:		gc
Version:	7.4.2
Release:	1%{?dist}
Summary:	A garbage collector for C and C++	

Group:		Development/Libraries		
License:	GPL
URL:		http://hboehm.info/gc/
Source0:	http://hboehm.info/gc/gc_source/gc-%{version}.tar.gz

Patch0: 	fix-boehm-gc.patch

BuildRequires:	libatomic_ops-devel linux-headers
#Requires:	

%description
A garbage collector that can be used as a garbage 
collecting replacement for C malloc or C++ new.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q 

%patch0 -p1

%build
export CFLAGS="$CFLAGS -D_GNU_SOURCE -DNO_GETCONTEXT -DUSE_MMAP -DHAVE_DL_ITERATE_PHDR"
./configure \
	--prefix=/usr \
	--disable-static \
	--datadir=/usr/share/doc/gc \
	--enable-cplusplus \

make %{?_smp_mflags}


%install
make -j1 DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%license COPYING COPYING.LESSER
%{_libdir}/libcord.so.*
%{_libdir}/libgc.so.*
%{_libdir}/libgccpp.so.*

%files devel
#%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_includedir}/gc/*.h
%dir %{_includedir}/gc/
#%{_mandir}/*/*

%changelog
