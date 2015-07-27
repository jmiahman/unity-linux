Name:		zlib	
Version:	1.2.8
Release:	1%{?dist}
Summary:	The compression and decompression library

Group:		System Environment/Libraries
License:	zlib and Boost
URL:		http://www.zlib.net/
Source0:	http://www.zlib.net/zlib-%{version}.tar.xz

#BuildRequires:
#Requires:	

%description
Zlib is a general-purpose, patent-free, lossless data compression
library which is used by many different programs.

%package devel
Summary: Header files and libraries for Zlib development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The zlib-devel package contains the header files and libraries needed
to develop programs that use the zlib compression and decompression
library.

%prep
%setup -q


%build
export CFLAGS="$CFLAGS -O2"
./configure \
	--prefix=/usr \
	--libdir=/lib \
	--shared \

%make


%install
make install pkgconfigdir=/usr/lib/pkgconfig DESTDIR=%{buildroot}


%files
%doc
/lib/libz.so.1.2.8
/lib/libz.so.1

%files devel
/lib/libz.a
/lib/libz.so
/usr/lib/pkgconfig/zlib.pc
/usr/include/zlib.h
/usr/include/zconf.h

%changelog
