%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \

Name:           libjpeg-turbo
Version:        1.4.1
Release:        1%{?dist}
Summary:        A MMX/SSE2 accelerated library for manipulating JPEG image files
Group:		System Environment/Libraries
License:        IJG
URL:            http://sourceforge.net/projects/libjpeg-turbo
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  nasm

%description
The libjpeg-turbo package contains a library of functions for manipulating JPEG
images.

%package devel
Summary:        Headers for the libjpeg-turbo library
Requires:       libjpeg-turbo = %{version}-%{release}

%description devel
This package contains header files necessary for developing programs which will
manipulate JPEG files using the libjpeg-turbo library.

%package utils
Summary:        Utilities for manipulating JPEG images
Requires:       libjpeg-turbo = %{version}-%{release}

%description utils
The libjpeg-turbo-utils package contains simple client programs for accessing
the libjpeg functions. It contains cjpeg, djpeg, jpegtran, rdjpgcom and
wrjpgcom. Cjpeg compresses an image file into JPEG format. Djpeg decompresses a
JPEG file into a regular image file. Jpegtran can perform various useful
transformations on JPEG files. Rdjpgcom displays any text comments included in a
JPEG file. Wrjpgcom inserts text comments into a JPEG file.

%prep
%setup -q

%build

./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \
	--with-jpeg8 \

make %{?_smp_mflags}

%install
make -j1 DESTDIR=%{buildroot} docdir=/usr/share/doc/%{name} install
find %{buildroot} -name "*.la" -delete

# Fix perms
chmod -x README-turbo.txt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
#%doc README README-turbo.txt ChangeLog.txt
%{_libdir}/libjpeg.so.8*
%{_libdir}/libturbojpeg.so.0*

%files devel
#%doc coderules.txt jconfig.txt libjpeg.txt structure.txt example.c
%{_includedir}/*.h
%{_libdir}/libjpeg.so
%{_libdir}/libturbojpeg.so


%files utils
#%doc usage.txt wizard.txt
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/rdjpgcom
%{_bindir}/wrjpgcom
#%{_mandir}/man1/cjpeg.1*
#%{_mandir}/man1/djpeg.1*
#%{_mandir}/man1/jpegtran.1*
#%{_mandir}/man1/rdjpgcom.1*
#%{_mandir}/man1/wrjpgcom.1*

%changelog
