%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64
%define _lib /lib64

Name:		expat	
Version:	2.1.0
Release:	1%{?dist}
Summary:	An XML Parser library written in C

Group:		System Environment/Libraries
License:	MIT
URL:		http://www.libexpat.org/
Source0:	http://fossies.org/linux/www/%{name}-%{version}.tar.gz		
#BuildRequires:	
#Requires:	

%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package devel
Summary:  Libraries and header files to develop applications using expat
Group: Development/Libraries
Requires: expat = %{version}

%description devel
The expat-devel package contains the libraries, include files and documentation
to develop XML applications with expat.

%prep
%setup -q

%build

./configure \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--libdir=%{_libdir} \
	--disable-static

make %{?_smp_mflags}


%install
%make_install

rm -rf %{buildroot}/%{_libdir}/libexpat.la

%files
%{_bindir}/xmlwf
%{_libdir}/libexpat.so.1
%{_libdir}/libexpat.so.1.6.0
%{_mandir}/man*/*.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h

%changelog
* Mon Dec 07 2015 JMiahMan <JMiahMan@unity-linux.org> - 2.1.0-1
- Rebuild for rpm4

