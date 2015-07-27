Name:		popt	
Version:	1.16	
Release:	1%{?dist}
Summary:	C library for parsing command line parameters

Group:		System Environment/Libraries
License:	MIT	
URL:		http://www.rpm5.org/
Source0:	http://rpm5.org/files/%{name}/%{name}-%{version}.tar.gz

#BuildRequires:	
#Requires:	

%description
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but
it improves on them by allowing more powerful argument expansion.
Popt can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--libdir=/lib \
	--disable-static

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/lib/*.la

%files
/lib/libpopt.so.0.0.0
/lib/libpopt.so.0

%changelog
