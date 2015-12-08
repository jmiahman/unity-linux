
Name:    openjpeg
Version: 1.5.1
Release: 1%{?dist}
Summary: JPEG 2000 command line tools
Group : System Environment/Libraries

License: BSD
URL:     http://code.google.com/p/openjpeg/

Source0: http://downloads.sourceforge.net/openjpeg.mirror/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: automake libtool
BuildRequires: doxygen
BuildRequires: libtiff-devel
BuildRequires: lcms2-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel

Requires: %{name}-libs = %{version}-%{release}

%description
OpenJPEG is an open-source JPEG 2000 codec written in C. It has been
developed in order to promote the use of JPEG 2000, the new still-image
compression standard from the Joint Photographic Experts Group (JPEG).

%package libs
Summary: JPEG 2000 codec runtime library
%description libs
The %{name}-libs package contains runtime libraries for applications that use
OpenJPEG.

%package  devel
Summary:  Development files for %{name} 
Requires: %{name}-libs = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use OpenJPEG.

%prep
%setup -q 

%build

cmake . \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DOPENJPEG_INSTALL_LIB_DIR=lib \
	-DOPENJPEG_INSTALL_PACKAGE_DIR=/usr/lib/%{name}-1.5 \

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# continue to ship compat header symlink
ln -s openjpeg-1.5/openjpeg.h %{buildroot}%{_includedir}/openjpeg.h

%files
%{_bindir}/image_to_j2k
%{_bindir}/j2k_dump
%{_bindir}/j2k_to_image
#%{_mandir}/man1/*image_to_j2k.1*
#%{_mandir}/man1/*j2k_dump.1*
#%{_mandir}/man1/*j2k_to_image.1*

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
#%doc CHANGES LICENSE
%{_libdir}/libopenjpeg.so.1*
%{_libdir}/libopenjpeg.so.5
#%{_mandir}/man3/*libopenjpeg.3*

%files devel
%{_includedir}/openjpeg-1.5/
%{_includedir}/openjpeg.h
%{_libdir}/libopenjpeg.so
%{_libdir}/pkgconfig/libopenjpeg1.pc
%{_libdir}/openjpeg-1.5/

%changelog
