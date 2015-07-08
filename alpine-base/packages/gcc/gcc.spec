%define BUILD_GXX 1
%undefine _with_test

%define gcc_branch 4.7

Summary: C compiler from the GNU Compiler Collection.
Name: gcc
Version: 4.7.0
Release: owl1
Epoch: 1
License: GPLv3+
Group: Development/Languages
URL: http://gcc.gnu.org
Source0: gcc-%version.tar.gz
# ftp://ftp.gnu.org/gnu/gcc/gcc-%version/gcc-core-%version.tar.bz2
# Signature: ftp://ftp.gnu.org/gnu/gcc/gcc-%version/gcc-core-%version.tar.bz2.sig
Patch0: gcc-4.7.0-owl-defaults-Wl.diff

BuildRequires: binutils, gettext, bison, flex, texinfo

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

%package -n libmudflap%gcc_branch
Summary: GCC mudflap shared support libraries.
Group: System/Libraries

%description -n libmudflap%gcc_branch
This package contains GCC shared support libraries which are needed for
mudflap support.

%package -n libmudflap%gcc_branch-devel
Summary: GCC mudflap support files.
Group: Development/Libraries

%description -n libmudflap%gcc_branch-devel
This package contains headers and libraries for building mudflap-instrumented
programs.
To instrument a non-threaded program, add -fmudflap option to GCC and
when linking add -lmudflap, for threaded programs also add -fmudflapth
and -lmudflapth.

%prep
%setup -q
%{?_with_test:%setup -q -T -D -b 6}
%patch0 -p1

# Use %%optflags_lib for this entire package until we figure out how to
# properly have just gcc's libraries built with a separate set of flags.
%{expand:%%define optflags %{?optflags_lib:%optflags_lib}%{!?optflags_lib:%optflags}}

%build
# Rebuild configure(s) and Makefile(s) if templates are newer...
for f in */acinclude.m4; do
	pushd "${f%%/*}"
# Run aclocal & autoconf only if files aclocal.m4 and configure.in exist
# and acinclude.m4 is newer than aclocal.m4.
	if [ -f aclocal.m4 -a -f configure.in -a acinclude.m4 -nt aclocal.m4 ]
	then
		aclocal
		autoconf
	fi
	popd
done
for f in */Makefile.am; do
	pushd "${f%%/*}"
	[ Makefile.am -nt Makefile.in ] && automake
	popd
done

# We will build this software outside source tree as recommended by INSTALL/*
rm -rf obj-%_target_platform
mkdir obj-%_target_platform
cd obj-%_target_platform



../configure \
	--prefix=%_prefix \
	--exec-prefix=%_exec_prefix \
        --bindir=%_bindir \
        --libdir=%_libdir \
        --libexecdir=%_libdir \
        --with-slib=/%_lib \
        --infodir=%_infodir \
        --mandir=%_mandir \
	--enable-shared \
        --enable-threads=posix \
	--disable-option-checking \
        --enable-nls \
        --enable-c-mbchar \
        --enable-long-long \
        --enable-__cxa_atexit \
        --disable-multilib \
        --host=%_target_platform \
        --build=%_target_platform \
	--disable-bootstrap \
%if %BUILD_GXX
        --with-gxx-include-dir=%_includedir/c++/%version \
%endif # BUILD_GXX
%if %BUILD_GXX
        --disable-libstdcxx-pch \
%endif # BUILD_GXX
        --target=%_target_platform \
	--enable-languages=c,c++
	
#	--prefix=/usr \
#	--libexecdir=/usr/lib \
#	--enable-shared \
#   	--enable-threads=posix \
#	--enable-__cxa_atexit \
#	--enable-clocale=gnu \
#	--enable-languages=c,c++ \
#	--disable-multilib \
#	--disable-bootstrap \
#	--with-system-zlib

TARGET_OPT_FLAGS='%optflags'
TARGET_OPT_LIBFLAGS='%optflags'
#TARGET_OPT_LIBFLAGS='%{?optflags_lib:%optflags_lib}%{!?optflags_lib:%optflags}'

# Let's compile the thing
# STAGE1_CFLAGS is used for stage1 compiler
# BOOT_FLAGS is used for stage2..n compiler
# ..._FOR_TARGET is used for final compiler

#%__make bootstrap-lean \
%__make 
	STAGE1_CFLAGS="-O -fomit-frame-pointer" \
	BOOT_CFLAGS="-O -fomit-frame-pointer" \
	CFLAGS_FOR_TARGET="$TARGET_OPT_FLAGS" \
	LIBCFLAGS_FOR_TARGET="$TARGET_OPT_LIBFLAGS" \
	CXXFLAGS_FOR_TARGET="${TARGET_OPT_FLAGS//-fno-rtti/}" \
	LIBCXXFLAGS_FOR_TARGET="${TARGET_OPT_LIBFLAGS//-fno-rtti/}"

# Copy various doc files here and there.

cd ..
mkdir -p rpm-doc/gcc
install -pm 644 -p gcc/ChangeLog rpm-doc/gcc/
#install -pm 644 -p BUGS COPYING* FAQ MAINTAINERS README* gcc/SERVICE rpm-doc/gcc/
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
mv %buildroot%_libdir/libgcc_s.so.1 %buildroot/%_lib/
ln -s ../../../../../%_lib/libgcc_s.so.1 \
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
rm %buildroot%_libdir/libiberty.a
rm -f %buildroot%_libdir/*.la

%find_lang cpplib
%find_lang gcc

# autogen is needed for this
#
# %check
# cd obj-%_target_platform
# %__make -k check
# cd -

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

%files -f gcc.lang
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
%_libdir/gcc/%_target_platform/%version/cc1
%_libdir/gcc/%_target_platform/%version/collect2
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

%_libdir/gcc/%_target_platform/%version/lto1
%_libdir/gcc/%_target_platform/%version/lto-wrapper
%exclude %_libdir/gcc/%_target_platform/%version/*.la
%_libdir/gcc/%_target_platform/%version/liblto_plugin.so.0.0.0

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
/%_lib/libgcc*.so.*
%_libdir/libquadmath.so.*
%_libdir/libssp.so.*

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
%_libdir/libssp.a
%_libdir/libssp_nonshared.a

%files -n libgomp%gcc_branch
%defattr(-,root,root)
%_libdir/libgomp.so.*

%files -n libmudflap%gcc_branch
%defattr(-,root,root)
%_libdir/libmudflap.so.*
%_libdir/libmudflapth.so.*

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

%files -n libmudflap%gcc_branch-devel
%defattr(-,root,root)
%dir %_libdir/gcc/%_target_platform/%version
%dir %_libdir/gcc/%_target_platform/%version/include
%_libdir/gcc/%_target_platform/%version/include/mf-runtime.h
%dir %_libdir/gcc/%_target_platform/%version
%_libdir/libmudflap.a
%_libdir/libmudflapth.a

%changelog
