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
	--mandir=/usr/share/man

make %{?_smp_mflags}


%install
%make_install


%files
/usr/bin/xmlwf
/usr/lib/libexpat.so.1
/usr/lib/libexpat.so.1.6.0

%files devel
/usr/include/*.h

%changelog
