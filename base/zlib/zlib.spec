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
	--libdir=/%{_lib} \
	--shared \

%make_build

%install
make install pkgconfigdir=/usr/lib/pkgconfig DESTDIR=%{buildroot}

%files
%doc
/%{_lib}/libz.so.?.?.?
/%{_lib}/libz.so.?
%{_mandir}/man3/zlib.?.*

%files devel
/%{_lib}/libz.a
/%{_lib}/libz.so
/usr/lib/pkgconfig/zlib.pc
%{_includedir}/zlib.h
%{_includedir}/zconf.h

%changelog
