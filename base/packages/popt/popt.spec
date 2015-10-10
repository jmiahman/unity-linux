Name:		popt	
Version:	1.16	
Release:	1%{?dist}
Summary:	C library for parsing command line parameters

Group:		System Environment/Libraries
License:	MIT	
URL:		http://www.rpm5.org/
Source0:	http://rpm5.org/files/%{name}/%{name}-%{version}.tar.gz

#BuildRequires:	
Requires:	libintl

%description
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but
it improves on them by allowing more powerful argument expansion.
Popt can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--libdir=/lib \
	--disable-static

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/lib/*.la

mkdir -p $RPM_BUILD_ROOT%{_libdir}
cd $RPM_BUILD_ROOT/%{_lib}
ln -sf ../../%{_lib}/$(ls libpopt.so.?.?.?) $RPM_BUILD_ROOT%{_libdir}/libpopt.so
cd ..


%files
/lib/libpopt.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libpopt.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/popt.h

%changelog
