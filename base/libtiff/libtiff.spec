%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \


Summary:       Library of functions for manipulating TIFF format image files
Name:          libtiff
Version:       4.0.4
Release:       1%{?dist}
License:       libtiff
Group:         System Environment/Libraries
URL:           http://www.remotesensing.org/libtiff/

Source:        ftp://ftp.remotesensing.org/pub/libtiff/tiff-%{version}.tar.gz

Patch0:        libtiff-am-version.patch
Patch1:        libtiff-make-check.patch

BuildRequires: zlib-devel libjpeg-turbo-devel 
BuildRequires: libtool automake autoconf pkgconfig

%description
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.

%package devel
Summary:       Development tools for programs which will use the libtiff library
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description devel
This package contains the header files and documentation necessary for
developing programs which will manipulate TIFF format image files
using the libtiff library.

If you need to develop programs which will manipulate TIFF format
image files, you should install this package.  You'll also need to
install the libtiff package.

%package tools
Summary:    Command-line utility programs for manipulating TIFF files
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains command-line programs for manipulating TIFF format
image files using the libtiff library.

%prep
%setup -q -n tiff-%{version}

%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-cxx \

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# remove what we didn't want installed
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%doc COPYRIGHT README RELEASE-DATE VERSION
%{_libdir}/libtiff.so.*

%files devel
#%doc TODO ChangeLog html
%{_includedir}/*
%{_libdir}/libtiff.so
%{_libdir}/pkgconfig/libtiff*.pc
#%{_mandir}/man3/*
%{_libdir}/*.a

%files tools
%{_bindir}/*
#%{_mandir}/man1/*

%changelog
