%define BUILD_GXX 0
%undefine _with_test

%define gcc_branch 5.1
%define with_musl 1
%define gcc_stage 3

%define _languages 'c,c++'

Summary:	C compiler from the GNU Compiler Collection.
Name:		gcc
Version:	5.1.0
Release:	1%{?dist}
License:	GPLv3+
Group:		Development/Languages
URL:		http://gcc.gnu.org
Source0:	http://mirrors.axint.net/repos/gnu.org/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2

Patch0:		005_all_gcc-spec-env.patch
Patch1:		010_all_default-fortify-source.patch
Patch2:		011_all_default-warn-format-security.patch
Patch3:		012_all_default-warn-trampolines.patch
Patch4:		020_all_msgfmt-libstdc++-link.patch
Patch5:		050_all_libiberty-asprintf.patch
Patch6:		051_all_libiberty-pic.patch
Patch7:		053_all_libitm-no-fortify-source.patch
Patch8:		067_all_gcc-poison-system-directories.patch
Patch9:		074_all_gcc5_isl-dl.patch
Patch10:	086_all_gcc5-pie-copy-relocs-pr65780.patch
Patch11:	090_all_pr55930-dependency-tracking.patch
Patch12:	101_all_gcc49_configure.patch
Patch13:	102_all_gcc48_config.in.patch
Patch14:	103_all_gcc49_Makefile.in.patch
Patch15:	105_all_gcc48_gcc.c.patch
Patch16:	116_all_gcc47_nopie_option.patch
Patch17:	120_all_gcc49_config_crtbeginp.patch
Patch18:	124_all_gcc49_invoke.texi.patch
Patch19:	134_all_gcc48_config_i386.patch
Patch20:	135_all_gcc48_config_arm.patch
Patch21:	140_all_gcc49_config_esp.patch
Patch22:	141_all_gcc49_config_esp_alpine.patch
Patch23:	201-libitm.patch
Patch24:	202-musl-config-v3.patch
Patch25:	204-arm.patch
Patch26:	209-x86-v3.patch
Patch27:	210-fixincludes.patch
Patch28:	211-unwind.patch
Patch29:	212-gthr.patch
Patch30:	213-posix_memalign.patch
Patch31:	214-stdint.patch
Patch32:        libgcc-always-build-gcceh.a.patch
Patch33:        gcc-4.8-musl-libssp.patch
Patch34:        gcc-4.9-musl-fortify.patch
Patch35:        boehm-gc-musl.patch
Patch36:        gcc-pure64.patch
Patch37:        fix-gcj-musl.patch
Patch38:        fix-gcj-iconv-musl.patch
Patch39:        gcc-4.8-build-args.patch
Patch40:        fix-cxxflags-passing.patch
Patch41:        ada-fixes.patch
Patch42:        ada-musl.patch
Patch43:        ada-no-pie.patch
Patch44:        ada-shared.patch


#BuildRequires: binutils, gettext, bison, flex, texinfo

%description
The gcc package contains C compiler from the GNU Compiler Collection,
as well as documentation which is not limited to just the C compiler.

%package -n cpp
Summary: GNU C preprocessor.
Group: Development/Languages

%description -n cpp
cpp (or cccp) is the GNU C Compatible Compiler Preprocessor.  cpp is a
macro processor which is used automatically by the C compiler to
transform program source before actual compilation.  cpp may also be
used independently from the C compiler and the C language.

%package -n libgcc
Summary: GCC shared support library.
Group: System Environment/Libraries

%description -n libgcc
This package contains GCC shared support library which is needed
e.g. for exception handling support.

%package -n libgcc%gcc_branch-plugin-devel
Summary: GCC plugin header files.
Group: Development/Libraries

%description -n libgcc%gcc_branch-plugin-devel
This package contains header files required to build GCC plugins.

%if %BUILD_GXX
%package c++
Summary: C++ support for gcc.
Group: Development/Languages

%description c++
This package contains the C++ compiler from the GNU Compiler Collection.
It includes support for most of the current C++ specification, including
templates and exception handling.  It does include the static standard
C++ library and C++ header files.  The library for dynamically linking
programs is available as a separate binary package.

%package -n libstdc++
Summary: GNU C++ library.
Group: System Environment/Libraries

%description -n libstdc++
The libstdc++ package contains the GCC Standard C++ Library.

%package -n libstdc++-devel
Summary: Header files and libraries for C++ development.
Group: Development/Libraries

%description -n libstdc++-devel
Header files and libraries needed for C++ development.
%endif

####################################################################
# OpenMP library

%package -n libgomp%gcc_branch
Summary: GCC OpenMP shared support library.
Group: System/Libraries

%description -n libgomp%gcc_branch
This package contains GCC OpenMP shared support library.

%package -n libgomp%gcc_branch-devel
Summary: GCC OpenMP support files.
Group: Development/Libraries

%description -n libgomp%gcc_branch-devel
This package contains GCC OpenMP headers and library.

####################################################################
# mudflap library

#%package -n libmudflap%gcc_branch
#Summary: GCC mudflap shared support libraries.
#Group: System/Libraries

#%description -n libmudflap%gcc_branch
#This package contains GCC shared support libraries which are needed for
#mudflap support.

#%package -n libmudflap%gcc_branch-devel
#Summary: GCC mudflap support files.
#Group: Development/Libraries

#%description -n libmudflap%gcc_branch-devel
#This package contains headers and libraries for building mudflap-instrumented
#programs.
#To instrument a non-threaded program, add -fmudflap option to GCC and
#when linking add -lmudflap, for threaded programs also add -fmudflapth
#and -lmudflapth.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
#%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
#%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
#%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
#%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1

%build
# Rebuild configure(s) and Makefile(s) if templates are newer...
for f in */acinclude.m4; do
	cd "${f%%/*}"
# Run aclocal & autoconf only if files aclocal.m4 and configure.in exist
# and acinclude.m4 is newer than aclocal.m4.
	if [ -f aclocal.m4 -a -f configure.in -a acinclude.m4 -nt aclocal.m4 ]
	then
		aclocal
		autoconf
	fi
	cd ..
done

# We will build this software outside source tree as recommended by INSTALL/*
rm -rf obj-%_target_platform
mkdir obj-%_target_platform
cd obj-%_target_platform

#Alpine
	../configure --prefix=/usr \
		--mandir=/usr/share/man \
		--infodir=/usr/share/info \
		--build=%_target_platform \
		--host=%_target_platform \
		--target=%_target_platform \
		--with-pkgversion="Unity %{version}" \
		--enable-checking=release \
		--disable-fixed-point \
		--disable-libstdcxx-pch \
		--disable-multilib \
		--disable-nls \
		--disable-werror \
		%{_symvers} \
		--enable-__cxa_atexit \
		--enable-esp \
		--enable-cloog-backend \
		--enable-languages=%{_languages} \
		--with-system-zlib \
		%if %with_musl
		--disable-libssp \
		--disable-libmudflap \
		--disable-libsanitizer \
		--disable-symvers \
		%endif
		%if %{gcc_stage} == 1
		--with-newlib \
		--without-headers \
		--disable-shared \
		--enable-threads=no \
		%endif
		%if %{gcc_stage} == 2
		--with-newlib \
		--disable-shared \
		--enable-threads=no \
		%endif
		%if %{gcc_stage} == 3
		--enable-shared \
		--enable-threads \
		--enable-tls \
		%endif


export ADA_CFLAGS='-fno-stack-check'

%make

cd ..
mkdir -p rpm-doc/gcc
install -pm 644 -p gcc/ChangeLog rpm-doc/gcc/
install -pm 644 -p COPYING* MAINTAINERS README* rpm-doc/gcc/

%if %BUILD_GXX
mkdir -p rpm-doc/g++
install -pm 644 -p gcc/cp/{ChangeLog,NEWS} rpm-doc/g++/

mkdir -p rpm-doc/libstdc++
install -pm 644 -p libstdc++-v3/{ChangeLog,README} rpm-doc/libstdc++/
%endif

find rpm-doc -type f \( -iname '*changelog*' -not -name '*.bz2' \) -print0 |
	xargs -r0 bzip2 -9 --

%install
rm -rf %buildroot

%__make -C obj-%_target_platform DESTDIR=%buildroot install

# Relocate libgcc shared library from %_libdir/ to /%_lib/.
mkdir %buildroot/%_lib
ln -s ../../../../../%_libdir/libgcc_s.so.1 \
	%buildroot%_libdir/gcc/%_target_platform/%version/libgcc_s.so
#mesut
#rm %buildroot%_libdir/libgcc_s.so

# Fix some things.
ln -s gcc %buildroot%_bindir/cc
echo ".so gcc.1" > %buildroot%_mandir/man1/cc.1

%if %BUILD_GXX
echo ".so g++.1" > %buildroot%_mandir/man1/c++.1
%endif

# Remove unpackaged files
rm %buildroot%_infodir/dir
rm %buildroot%_infodir/gccinstall.info*
#rm %buildroot%_libdir/libiberty.a
rm -f %buildroot%_libdir/*.la

%post
/sbin/install-info --info-dir=%_infodir %_infodir/gcc.info
/sbin/install-info --info-dir=%_infodir %_infodir/gccint.info
%_libdir/gcc/%_target_platform/%version/install-tools/mkheaders
chmod -R go+rX %_libdir/gcc/%_target_platform/%version/include/*

%preun
if [ $1 -eq 0 ]; then
	/sbin/install-info --delete --info-dir=%_infodir %_infodir/gccint.info
	/sbin/install-info --delete --info-dir=%_infodir %_infodir/gcc.info
	if [ -d %_libdir/gcc/%_target_platform/%version/include ]; then
		rm -rf %_libdir/gcc/%_target_platform/%version/include/*
	fi
fi

%post -n libgcc -p /sbin/ldconfig
%postun -n libgcc -p /sbin/ldconfig

%post -n cpp
/sbin/install-info --info-dir=%_infodir %_infodir/cpp.info
/sbin/install-info --info-dir=%_infodir %_infodir/cppinternals.info

%preun -n cpp
if [ $1 -eq 0 ]; then
	/sbin/install-info --delete --info-dir=%_infodir %_infodir/cppinternals.info
	/sbin/install-info --delete --info-dir=%_infodir %_infodir/cpp.info
fi

%if %BUILD_GXX
%post -n libstdc++ -p /sbin/ldconfig
%postun -n libstdc++ -p /sbin/ldconfig
%endif

%files 
%defattr(-,root,root)
%_bindir/cc
%_bindir/gcc
%_bindir/gcov
%_bindir/%_target_platform-gcc
%_bindir/%_target_platform-gcc-%version
%_infodir/gcc.info*
%_infodir/gccint.info*
%dir %_libdir/gcc
%dir %_libdir/gcc/%_target_platform
%dir %_libdir/gcc/%_target_platform/%version
#%_libdir/gcc/%_target_platform/%version/cc1
#%_libdir/gcc/%_target_platform/%version/collect2
%_libdir/gcc/%_target_platform/%version/crt*.o
%_libdir/gcc/%_target_platform/%version/libgcc*.a
%_libdir/gcc/%_target_platform/%version/libgcc*.so
%_libdir/gcc/%_target_platform/%version/libgcov*.a

%_libdir/gcc/%_target_platform/%version/include

%_libdir/gcc/%_target_platform/%version/include-fixed
%_libdir/gcc/%_target_platform/%version/install-tools

%_mandir/man1/cc.1*
%_mandir/man1/gcc.1*
%_mandir/man1/gcov.1*
%_mandir/man7/fsf-funding.7*
%_mandir/man7/gfdl.7*
%_mandir/man7/gpl.7*
%doc rpm-doc/gcc/*

#%_libdir/gcc/%_target_platform/%version/lto1
#%_libdir/gcc/%_target_platform/%version/lto-wrapper
#%exclude %_libdir/gcc/%_target_platform/%version/*.la
#%_libdir/gcc/%_target_platform/%version/liblto_plugin.so.0.0.0

%files -n cpp
%defattr(-,root,root)
%_bindir/cpp
%_infodir/cpp.info*
%_infodir/cppinternals.info*
%dir %_libdir/gcc
%dir %_libdir/gcc/%_target_platform
%_mandir/man1/cpp.1*

%files -n libgcc
%defattr(-,root,root)
/%_libdir/libgcc*.so.*
%_libdir/libquadmath.so.*
#%_libdir/libssp.so.*

%if %BUILD_GXX
%files c++ -f cpplib.lang
%defattr(-,root,root)
%_bindir/?++
%_bindir/%_target_platform-?++
%dir %_libdir/gcc
%dir %_libdir/gcc/%_target_platform
%_libdir/gcc/%_target_platform/%version/cc1plus
%_mandir/man1/?++.1*
%doc rpm-doc/g++/*

%files -n libstdc++
%defattr(-,root,root)
%_libdir/libstdc++.so.6*
%_datadir/locale/*/LC_MESSAGES/libstdc++.mo
%doc rpm-doc/libstdc++/*
%doc libstdc++-v3/doc/html
%exclude %_datadir/gcc-%version/python

%files -n libstdc++-devel
%defattr(-,root,root)
%_includedir/c++/%version
%_libdir/libs*++.a
%_libdir/libstdc++.so
%endif

%files -n libgcc%gcc_branch-plugin-devel
%defattr(-,root,root)
%_libdir/gcc/%_target_platform/%version/plugin
%_infodir/libquadmath.info*
%_libdir/libquadmath.a
#%_libdir/libssp.a
#%_libdir/libssp_nonshared.a

%files -n libgomp%gcc_branch
%defattr(-,root,root)
%_libdir/libgomp.so.*

#%files -n libmudflap%gcc_branch
#%defattr(-,root,root)
#%_libdir/libmudflap.so.*
#%_libdir/libmudflapth.so.*

%files -n libgomp%gcc_branch-devel
%defattr(-,root,root)
%dir %_libdir/gcc/%_target_platform/%version
%dir %_libdir/gcc/%_target_platform/%version/include
%_libdir/gcc/%_target_platform/%version/plugin
%_libdir/gcc/%_target_platform/%version/include/omp.h
%dir %_libdir/gcc/%_target_platform/%version
%_infodir/libgomp*.info*
%_libdir/libgomp.a
%_libdir/libgomp.so
%_libdir/libgomp.spec

#%files -n libmudflap%gcc_branch-devel
#%defattr(-,root,root)
#%dir %_libdir/gcc/%_target_platform/%version
#%dir %_libdir/gcc/%_target_platform/%version/include
#%_libdir/gcc/%_target_platform/%version/include/mf-runtime.h
#%dir %_libdir/gcc/%_target_platform/%version
#%_libdir/libmudflap.a
#%_libdir/libmudflapth.a

%changelog
