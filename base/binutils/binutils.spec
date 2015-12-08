%define _target_platform %{_arch}-unity-linux-musl
%define _libiberty 1

Name:           binutils
Version:        2.25 
Release:        1%{?dist}
Summary:        Tools necessary to build programs 

Group:          Development/Tools 
License:        GPLv3+
URL:            http://sources.redhat.com/binutils
Source0:        http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2

Patch0:		binutils-ld-fix-static-linking.patch
Patch1: 	hash-style-gnu.patch
Patch2:		binutils-2.20.51.0.2-libtool-lib64.patch

BuildRequires: gettext, flex, bison, zlib-devel
Requires: coreutils
Requires(post): /usr/bin/install-info
Requires(preun): /usr/bin/install-info
Requires(post): coreutils

%description
Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes
of an object or archive file), strings (for listing printable strings
from files), strip (for discarding symbols), and addr2line (for
converting addresses to file and line).

%package devel
Summary: BFD and opcodes static and dynamic libraries and header files
Group: System Environment/Libraries

%description devel
This package contains BFD and opcodes static and dynamic libraries.

%prep
%setup -q
%patch0 -p1 -b .fix-static-linking
%patch1 -p1 -b .hash-style-gnu
%patch2 -p1 -b .libtool_64


%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--target=%{_target_platform} \
	--with-build-sysroot=%{buildroot} \
	--with-sysroot=/ \
	--prefix=/usr \
	--libdir=%{_libdir} \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--enable-multilib \
	--enable-shared \
	--enable-ld=default \
	--enable-gold=yes \
	--enable-64-bit-bfd \
	--enable-plugins \
	%if %{_libiberty} == 1
	--enable-install-libiberty \
	%endif
        %if %{_libiberty} == 0
        --disable-install-libiberty \
        %endif
	--disable-werror \
	--disable-nls \

make libdir=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Remove libtool files, which reference the .so libs
rm -f %{buildroot}%{_libdir}/libbfd.la
rm -f %{buildroot}%{_libdir}/libopcodes.la

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%dir %{_prefix}/%{_target_platform}
%dir %{_prefix}/%{_target_platform}/bin/
%dir %{_prefix}/%{_target_platform}/lib/
%dir %{_prefix}/%{_target_platform}/lib/ldscripts/
%{_prefix}/%{_target_platform}/bin/*
%{_prefix}/%{_target_platform}/lib/ldscripts/*
%{_libdir}/*%{version}.so
%{_mandir}/man1/*
%{_infodir}
%{_infodir}/[^b]*info*
%{_infodir}/binutils*info*

%files devel
%defattr(-,root,root,-)
%exclude %{_libdir}/*%{version}.so
%{_includedir}/*.h
%dir %{_includedir}/libiberty
%{_includedir}/libiberty/*.h
%{_prefix}/lib/lib*.a
%{_libdir}/lib*.a
%{_libdir}/libbfd.so
%{_libdir}/libopcodes.so
%{_infodir}/bfd*info*

%changelog
* Mon Nov 30 2015 JMiahMan <JMiahMan@unity-linux.org> 2.25.1-1
- Initial build for Unity-Linux
