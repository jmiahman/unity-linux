#For some reason we have an issue with the ice-9 module in 2.0.11 so wait to build

Name:		guile
#Version:	2.0.11
Version:	1.8.8
Release:	1%{?dist}
Summary:	Guile is a portable, embeddable Scheme implementation written in C

Group:		Development/Libraries		
License:	GPL
URL:		http://www.gnu.org/software/guile/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz

#Patch0: 	strtol_l.patch
Patch0:		fix-defines.patch

BuildRequires:	gmp-devel libtool ncurses-devel gc-devel
BuildRequires:	texinfo libunistring-devel libffi-devel

%description
Guile is a library designed to help programmers create 
flexible applications. Using Guile in an application allows 
the application's functionality to be extended by users or 
other programmers with plug-ins, modules, or scripts.

%package        libs                                                                                                                                                                                          
Summary:        Libraries for %{name}                                                                                                                                                                  
Requires:       %{name} = %{version}-%{release}     
                                                    
%description    libs                                                                                                                                                                                          
This package contains libraries in order                                                                                                                                                
to run applications that use %{name}.

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

#Remove OLD config.sub
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv \
		 /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure \
	--prefix=/usr \
	--disable-static \
	--disable-error-on-warning \

sed -i 's|" $sys_lib_dlsearch_path "|" $sys_lib_dlsearch_path %{_libdir} "|' \
    libtool

make -j1

%install
make -j1 DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
#%license COPYING COPYING.LESSER
%{_bindir}/*
%dir %{_datadir}/guile/
%{_datadir}/guile/*
#%{_libdir}/guile/*

%files libs
%{_libdir}/libguile*.so.*

%files devel
#%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/guile.m4
%{_includedir}/*.h
%dir %{_includedir}/libguile/
%{_includedir}/libguile/*.h
%{_includedir}/guile/*.h
%dir %{_includedir}/guile/
#%{_mandir}/*/*

%changelog
