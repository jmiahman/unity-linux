Name:		libpng		
Version:	1.6.18
Release:	1%{?dist}
Summary:	Portable Network Graphics library

Group:		System Environment/Libraries
License:	zlib
URL:		http://www.libpng.org/pub/png/
Source0:	ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng16/libpng-%{version}.tar.gz
Patch0:		libpng-1.6.18-apng.patch	

BuildRequires: gawk zlib-devel	

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.

%package devel
Summary:       Development tools for programs to manipulate PNG image format files
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      zlib-devel pkgconfig

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

If you want to develop programs which will manipulate PNG image format
files, you should install libpng-devel.  You'll also need to install
the libpng package.

%prep
%setup -q

%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# We don't ship .la files.
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
install -Dm644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%{!?_licensedir:%global license %%doc}
#%license LICENSE
%{_libdir}/libpng16.so.*
#%{_mandir}/man5/*
%{_bindir}/pngfix

%files devel
#%doc libpng-manual.txt example.c TODO CHANGES
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/libpng*.pc
#%{_mandir}/man3/*
%{_libdir}/libpng*.a

%changelog
