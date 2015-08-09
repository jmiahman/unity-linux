Name:           mpc
Version:        1.0.2
Release:        1%{?dist}
Summary:        Multiprecision C library

Group:          Development/Tools
License:        LGPLv3+ and GFDL
URL:            http://www.multiprecision.org/ 
Source0:        http://www.multiprecision.org/mpc/download/mpc-%{version}.tar.gz

#BuildRequires:  
#Requires:       

%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as Mpfr.

%package devel
Summary: Header and shared development libraries for MPC
Group: Development/Libraries

%description devel
Header files and shared object symlinks for MPC is a C library.


%prep
%setup -q


%build
EGREP=egrep \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--enable-shared

make ARCH=%{_arch}
%install
%__rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%__rm $RPM_BUILD_ROOT/usr/lib/*.la


%clean
rm -rf $RPM_BUILD_ROOT

%files
#%doc README NEWS COPYING.LESSER
%{_libdir}/libmpc.so.3*

%files devel
%{_libdir}/libmpc.so
%{_includedir}/mpc.h
#%{_infodir}/*.info*

%changelog
