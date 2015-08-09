Name:		pcre
Version:	8.37	
Release:	1%{?dist}
Summary:	Perl-compatible regular expression library

Group:		System Environment/Libraries	
License:	BSD
URL:		http://www.pcre.org/

Source: 	ftp://ftp.csx.cam.ac.uk/pub/software/programming/%{name}/%{name}-%{version}.tar.bz2

Patch0:		CVE-2015-3210.patch
Patch1:		CVE-2015-3217.patch
Patch2:		CVE-2015-5073.patch

#BuildRequires:	
#Requires:	

%description
Perl-compatible regular expression library.
PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%package -n libpcrecpp
Summary: C++ bindings for %{name}
Group: Development/Libraries

%description -n libpcrecpp
C++ bindings for %{name}.

%package -n libpcre16
Summary: %{name} with 16 bit character support.
Group: Development/Libraries

%description -n libpcre16
 %{name} with 16 bit character support.

%package -n libpcre32
Summary: %{name} with 32 bit character support.
Group: Development/Libraries

%description -n libpcre32
 %{name} with 32 bit character support.

%package tools
Summary: Auxiliary utilities for %{name}.
Group: Development/Libraries

%description tools
Auxiliary utilities for %{name}.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files (Headers, libraries for dynamic linking, etc) for %{name}.


%prep
%setup -q
%patch0 -p1 -b .CVE-2015-3210
%patch1 -p1 -b .CVE-2015-3217
%patch2 -p1 -b .CVE-2015-5073

%build
./configure \
	--prefix=/usr \
	--enable-jit \
	--enable-utf8 \
	--enable-unicode-properties \
	--enable-pcre8 \
	--enable-pcre16 \
	--enable-pcre32 \
	--with-match-limit-recursion=8192 \
	--htmldir=/usr/share/doc/%{name}-%{version}/html \
	--docdir=/usr/share/doc/%{name}-%{version}

make %{?_smp_mflags}


%install
%make_install


%files
%{_libdir}/libpcreposix.so.0.0.3
%{_libdir}/libpcre.so.1
%{_libdir}/libpcre.so.1.2.5
%{_libdir}/libpcreposix.so.0

%files -n libpcrecpp
%{_libdir}/libpcrecpp.so.0
%{_libdir}/libpcrecpp.so.0.0.1

%files -n libpcre16
%{_libdir}/libpcre16.so.0
%{_libdir}/libpcre16.so.0.2.5

%files -n libpcre32
%{_libdir}/libpcre32.so.0
%{_libdir}/libpcre32.so.0.0.5

%files tools
%{_bindir}/pcregrep
%{_bindir}/pcretest

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
%{_bindir}/pcre-config

%changelog
