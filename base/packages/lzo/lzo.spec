Name:           lzo
Version:        2.08
Release:        1%{?dist}
Summary:        Data compression library with very fast (de)compression
Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.oberhumer.com/opensource/lzo/
Source0:        http://www.oberhumer.com/opensource/lzo/download/%{name}-%{version}.tar.gz
Patch0:         lzo-2.08-configure.patch
BuildRequires:  zlib-devel

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory. In addition there are slower
compression levels achieving a quite competitive compression ratio
while still decompressing at this very high speed.


%package minilzo
Summary:        Mini version of lzo for apps which don't need the full version
Group:          System Environment/Libraries

%description minilzo
A small (mini) version of lzo for embedding into applications which don't need
full blown lzo compression support.


%package devel
Summary:        Development files for the lzo library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-minilzo = %{version}-%{release}
Requires:       zlib-devel

%description devel
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
This package contains development files needed for lzo.


%prep
%setup -q
%patch0 -p1 -z .configure
# mark asm files as NOT needing execstack
for i in asm/i386/src_gas/*.S; do
  echo '.section .note.GNU-stack,"",@progbits' >> $i
done


%build
%configure --disable-dependency-tracking --disable-static --enable-shared
make %{?_smp_mflags}
# build minilzo too (bz 439979)
gcc %{optflags} -fpic -Iinclude/lzo -o minilzo/minilzo.o -c minilzo/minilzo.c
gcc -g -shared -Wl,-z,now -o libminilzo.so.0 -Wl,-soname,libminilzo.so.0 minilzo/minilzo.o


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
install -m 755 libminilzo.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libminilzo.so.0 $RPM_BUILD_ROOT%{_libdir}/libminilzo.so
install -p -m 644 minilzo/minilzo.h $RPM_BUILD_ROOT%{_includedir}/lzo

#Remove doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/lzo

%check
make check test


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post minilzo -p /sbin/ldconfig

%postun minilzo -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%doc AUTHORS THANKS NEWS
%{_libdir}/liblzo2.so.*

%files minilzo
%defattr(-,root,root,-)
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%doc minilzo/README.LZO
%{_libdir}/libminilzo.so.0

%files devel
%defattr(-,root,root,-)
#%doc doc/LZOAPI.TXT doc/LZO.FAQ doc/LZO.TXT
%{_includedir}/lzo
%{_libdir}/lib*lzo*.so


%changelog

