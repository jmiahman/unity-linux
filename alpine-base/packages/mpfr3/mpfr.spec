Name:           mpfr
Version:        3.1.3 
Release:        1%{?dist}
Summary:        A C library for multiple-precision floating-point computations

Group:          System Environment/Libraries
License:        LGPLv3+ and GPLv3+ and GFDL 

URL:            http://www.mpfr.org/ 
Source0:        http://www.mpfr.org/mpfr-current/%{name}-%{version}.tar.xz

#BuildRequires:  
#Requires:       

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.


%package devel
Summary: Development tools A C library for mpfr library
Group: Development/Libraries

%description devel
Header files and documentation for using the MPFR 
multiple-precision floating-point library in applications.

If you want to develop applications which will use the MPFR library,
you'll need to install the mpfr-devel package.  You'll also need to
install the mpfr package.

%prep
%setup -q

%build
./configure \
	--build=%{_build} \
	--host=%{_host} \
	--prefix=/usr \
	--enable-shared \
make

%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT


%clean
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install
%__rm $RPM_BUILD_ROOT/usr/lib/*.la



%files
%defattr(-,root,root,-)
%doc COPYING COPYING.LESSER NEWS README
%{_libdir}/libmpfr.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libmpfr.so
%{_includedir}/*.h
%{_infodir}/mpfr.info*

%changelog
