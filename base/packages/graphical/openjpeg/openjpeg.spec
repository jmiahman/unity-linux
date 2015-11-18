%define 	_includedir	/usr/include

Summary:	An open-source JPEG 2000 codec
Name:		openjpeg
Version:	2.1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/openjpeg.mirror/openjpeg-%{version}.tar.gz
# Source0-md5:	f6419fcc233df84f9a81eb36633c6db6
Patch0:		CVE-2015-6581.patch
Patch1:		fix-use-after-free.patch

URL:		http://www.openjpeg.org/
BuildRequires:	cmake >= 2.8.2
BuildRequires:	doxygen
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig >= 0.22
BuildRequires:	zlib-devel

%description
The OpenJPEG 2 library is an open-source JPEG 2000 codec written in C
language. It has been developed in order to promote the use of JPEG
2000, the new still-image compression standard from the Joint
Photographic Experts Group (JPEG).

%package devel
Summary:	Header file for OpenJPEG 2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header file needed for developing programs
using the OpenJPEG 2 library.

%package progs
Summary:	OpenJPEG 2 codec programs
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
OpenJPEG 2 codec programs.

%prep
%setup -q -n openjpeg-%{version}
#%patch0 -p1
#%patch1 -p1

%build
%cmake . \
	-DBUILD_DOC=ON \
	-DOPENJPEG_INSTALL_LIB_DIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as doc
#%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/openjpeg-2.1
#%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/html

ln -sf %{_includedir}/openjpeg-2.1/* %{buildroot}%{_includedir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE NEWS README THANKS
%attr(755,root,root) %{_libdir}/libopenjp2.so.*.*.*
%attr(755,root,root) %{_libdir}/libopenjp2.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenjp2.so
%{_includedir}/openjpeg-2.1
%{_includedir}/*.h
%dir %{_libdir}/openjpeg-2.1
%{_libdir}/openjpeg-2.1/OpenJPEG*.cmake
%{_libdir}/pkgconfig/libopenjp2.pc
%{_mandir}/man3/libopenjp2.3*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/opj_compress
%attr(755,root,root) %{_bindir}/opj_decompress
%attr(755,root,root) %{_bindir}/opj_dump
%{_mandir}/man1/opj_compress.1*
%{_mandir}/man1/opj_decompress.1*
%{_mandir}/man1/opj_dump.1*

%changelog
