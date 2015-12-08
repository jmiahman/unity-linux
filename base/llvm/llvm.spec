%bcond_without  clang

Name:           llvm
Version:        3.6.2
Release:        1%{?dist}
Summary:        The Low Level Virtual Machine

Group:          Development/Languages
License:        NCSA
URL:            http://llvm.org/

# source archives
Source0:        http://llvm.org/releases/%{version}/llvm-%{version}.src.tar.xz
Source1:        http://llvm.org/releases/%{version}/cfe-%{version}.src.tar.xz

Source2:	http://llvm.org/releases/%{version}/clang-tools-extra-%{version}.src.tar.xz
Source3:	http://llvm.org/releases/%{version}/compiler-rt-%{version}.src.tar.xz
Source4:	http://llvm.org/releases/%{version}/polly-%{version}.src.tar.xz

Patch0:		llvm-0001-fix-shared-build.patch
Patch1:		llvm-0002-musl-triple.patch
Patch2:		llvm-0003-musl-hacks.patch

Patch3:		compiler-rt-0001-musl-no-dlvsym.patch
Patch4:		compiler-rt-0002-musl-no-sanitizers.patch
Patch5:		compiler-rt-0003-off_t.patch

Patch6:		clang-0001-fix-stdint.h.patch
Patch7:		clang-0002-fix-unwind-header.patch
Patch8:	 	clang-0003-add-unity-linux-distro.patch
Patch9: 	clang-0004-unity-use-z-relro.patch
Patch10:	clang-0005-unity-hash-style-gnu.patch
Patch11:	clang-0006-musl-unity-triple.patch
Patch12:	clang-0007-musl-dynamic-linker-paths.patch
Patch13:	clang-0008-unity-PIE-by-default.patch
Patch14:	clang-0009-pass-host-triple-to-compiler-rt.patch
Patch15:	clang-0010-unity-use-z-now.patch
Patch16:	clang-0011-unity-SSP-by-default.patch


BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  groff
BuildRequires:  libffi-devel
BuildRequires:  libtool libltdl
BuildRequires:  binutils-devel
BuildRequires:  ncurses-devel
BuildRequires:  zip
BuildRequires:  python-sphinx
Requires:       %{name}-libs = %{version}-%{release}

%description
LLVM is a compiler infrastructure designed for compile-time,
link-time, runtime, and idle-time optimization of programs from
arbitrary programming languages.  The compiler infrastructure includes
mirror sets of programming tools as well as libraries with equivalent
functionality.


%package devel
Summary:        Libraries and header files for LLVM
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}
Requires:       libffi-devel
Requires:       libstdc++-devel >= 3.4
Requires:       ncurses-devel
#Requires(posttrans): /usr/sbin/alternatives
#Requires(postun):    /usr/sbin/alternatives

%description devel
This package contains library and header files needed to develop new
native programs that use the LLVM infrastructure.


#%package docs
#Summary:        Documentation for LLVM
#Group:          Documentation
#BuildArch:      noarch
#Requires:       %{name} = %{version}-%{release}
# might seem redundant, but needed to kill off the old arch-ed -doc subpackage

#%description docs
#Documentation for the LLVM compiler infrastructure.


%package libs
Summary:        LLVM shared libraries
Group:          System Environment/Libraries

%description libs
Shared libraries for the LLVM compiler infrastructure.


%package static
Summary:        LLVM static libraries
Group:          Development/Languages
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static libraries for the LLVM compiler infrastructure.  Not recommended
for general consumption.


%package -n clang
Summary:        A C language family front-end for LLVM
License:        NCSA
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}
# clang requires gcc, clang++ requires libstdc++-devel
Requires:       libstdc++-devel
Requires:       gcc-c++

%description -n clang
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extensible.


%Package -n clang-libs
Summary:        Runtime library for clang
Group:          System Environment/Libraries

%description -n clang-libs
Runtime library for clang.


%package -n clang-devel
Summary:        Header files for clang
Group:          Development/Languages
Requires:       clang = %{version}-%{release}

%description -n clang-devel
This package contains header files for the Clang compiler.


%package -n clang-analyzer
Summary:        A source code analysis framework
License:        NCSA
Group:          Development/Languages
BuildArch:      noarch
Requires:       clang = %{version}-%{release}
# not picked up automatically since files are currently not instaled
# in standard Python hierarchies yet
Requires:       python

%description -n clang-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%if %{with lldb}
%package -n lldb
Summary:        Next generation high-performance debugger
License:        NCSA
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}
BuildRequires:  swig
BuildRequires:  libedit-devel
BuildRequires:  python-devel

%description -n lldb
LLDB is a next generation, high-performance debugger. It is built as a set
of reusable components which highly leverage existing libraries in the
larger LLVM Project, such as the Clang expression parser and LLVM
disassembler.

%package -n lldb-devel
Summary:        Header files for LLDB
Group:          Development/Languages
Requires:       lldb = %{version}-%{release}

%description -n lldb-devel
This package contains header files for the LLDB debugger.
%endif


%prep
%setup -q -a1 -a2 -a3 -a4 -n llvm-%{version}.src
rm -rf tools/clang tools/lldb projects/compiler-rt
mv cfe-*/ tools/clang
mv compiler-rt-*/ projects/compiler-rt
%if %{with lldb}
mv lldb-*/ tools/lldb
%endif

%patch0 -p1
%patch1 -p1
%patch2 -p1

cd projects/compiler-rt/

%patch3 -p1
%patch4 -p1
%patch5 -p1

cd ../../
cd tools/clang/

%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

cd ../../

%if %{with lldb}
cd tools/lldb
# careful when recreating this patch...
%patch200 -p1 -b .python
%patch202 -p1
sed -i s/@lib@/%{_lib}/g scripts/Python/modules/readline/Makefile
cd ../../
%endif



# fix library paths
sed -i 's|/lib /usr/lib $lt_ld_extra|%{_libdir} $lt_ld_extra|' configure
sed -i 's|(PROJ_prefix)/lib|(PROJ_prefix)/%{_lib}/%{name}|g' Makefile.config.in
sed -i 's|/lib\>|/%{_lib}/%{name}|g' tools/llvm-config/llvm-config.cpp
sed -ri "/ifeq.*CompilerTargetArch/s#i386#i686#g" projects/compiler-rt/make/platform/clang_linux.mk

%build
%ifarch s390
# Decrease debuginfo verbosity to reduce memory consumption in linker
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

mkdir build
cd build
ln -sf ../configure .
# clang is lovely and all, but unity builds with gcc
# -fno-devirtualize shouldn't be necessary, but gcc has scary template-related
# bugs that make it so.  gcc 5 ought to be fixed.
export CC=gcc
export CXX=g++
export CFLAGS="%{optflags} -DLLDB_DISABLE_PYTHON -DHAVE_PROCESS_VM_READV"
export CXXFLAGS="%{optflags} -DLLDB_DISABLE_PYTHON -DHAVE_PROCESS_VM_READV"
%configure \
  --with-extra-options="-fno-devirtualize" \
  --with-extra-ld-options=-Wl,-Bsymbolic \
  --libdir=%{_libdir}/%{name} \
  --disable-polly \
  --disable-libcpp \
  --enable-cxx11 \
  --enable-clang-arcmt \
  --enable-clang-static-analyzer \
  --enable-clang-rewriter \
  --enable-optimized \
  --disable-profiling \
  --disable-assertions \
  --disable-werror \
  --disable-expensive-checks \
  --enable-debug-runtime \
  --enable-keep-symbols \
  --enable-jit \
  --enable-docs \
  --disable-doxygen \
  --enable-threads \
  --enable-pthreads \
  --enable-zlib \
  --enable-pic \
  --enable-shared \
  --disable-embed-stdcxx \
  --enable-timestamps \
  --enable-backtraces \
  --enable-targets=x86,powerpc,arm,aarch64,cpp,nvptx,systemz,r600 \
  --enable-bindings=none \
  --enable-libffi \
  --enable-ltdl-install \
  \
%ifarch armv7hl armv7l
  --with-cpu=cortex-a8 \
  --with-tune=cortex-a8 \
  --with-arch=armv7-a \
  --with-float=hard \
  --with-fpu=vfpv3-d16 \
  --with-abi=aapcs-vfp \
%endif
  \
  --with-binutils-include=%{_includedir} \
  --with-optimize-option=-O3

make %{?_smp_mflags} REQUIRES_RTTI=1 VERBOSE=1
#make REQUIRES_RTTI=1 VERBOSE=1

%install
cd build
make install DESTDIR=%{buildroot} PROJ_docsdir=/moredocs
cd -

# you have got to be kidding me
rm -f %{buildroot}%{_bindir}/FileCheck
rm -f %{buildroot}%{_bindir}/count
rm -f %{buildroot}%{_bindir}/not
rm -f %{buildroot}%{_bindir}/verify-uselistorder
rm -f %{buildroot}%{_bindir}/obj2yaml
rm -f %{buildroot}%{_bindir}/yaml2obj

#cd %{buildroot}%{_includedir}/llvm/Config
#cp -p %{SOURCE10} config.h
#cp -p %{SOURCE11} llvm-config.h
#cd ../../../

# Create ld.so.conf.d entry
#mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
#cat >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf << EOF
#%{_libdir}/%{name}
#EOF

%if %{with clang}
# Static analyzer not installed by default:
# http://clang-analyzer.llvm.org/installation#OtherPlatforms

# scan-view
mkdir -p %{buildroot}%{_libexecdir}/clang-analyzer/
cp -pr tools/clang/tools/scan-view %{buildroot}%{_libexecdir}/clang-analyzer/

# scan-build
mkdir -p %{buildroot}%{_libexecdir}/clang-analyzer/scan-build
for file in c++-analyzer ccc-analyzer scan-build scanview.css sorttable.js; do
  cp -p tools/clang/tools/scan-build/$file %{buildroot}%{_libexecdir}/clang-analyzer/scan-build/
done

# scan-build manual page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p tools/clang/tools/scan-build/scan-build.1 %{buildroot}%{_mandir}/man1/

# scan-build requires clang in search path
ln -sf ../../../bin/clang %{buildroot}%{_libexecdir}/clang-analyzer/scan-build/clang

ln -sf %{_libexecdir}/clang-analyzer/scan-view/scan-view %{buildroot}%{_bindir}/scan-view
ln -sf %{_libexecdir}/clang-analyzer/scan-build/scan-build %{buildroot}%{_bindir}/scan-build
%endif

# Get rid of erroneously installed example files.
rm %{buildroot}%{_libdir}/%{name}/*LLVMHello.*

# remove executable bit from static libraries
find %{buildroot}%{_libdir} -name "*.a" -type f -print0 | xargs -0 chmod -x

# Install man page for LLDB
%if %{with lldb}
mkdir -p %{buildroot}%{_mandir}/man1
cp tools/lldb/docs/lldb.1 %{buildroot}%{_mandir}/man1/
%endif

# Install documentation documentation
find %{buildroot}/moredocs/ -name "*.tar.gz" -print0 | xargs -0 rm -rf
mkdir -p %{buildroot}%{_docdir}

# llvm-doc
#mkdir -p %{buildroot}%{llvmdocdir %{name}-doc}
#cp -ar examples %{buildroot}%{llvmdocdir %{name}-doc}/examples
#find %{buildroot}%{llvmdocdir %{name}-doc} -name Makefile -o -name CMakeLists.txt -o -name LLVMBuild.txt -print0 | xargs -0 rm -f

# llvm-apidoc
#%if %{with doxygen}
#mv %{buildroot}/moredocs/html/doxygen %{buildroot}%{llvmdocdir %{name}-apidoc}
#%endif

# llvm-ocaml-doc
#%if %{with ocaml}
#mv %{buildroot}/moredocs/ocamldoc/html %{buildroot}%{llvmdocdir %{name}-ocaml-doc}
#%endif

# clang
#%if %{with clang}
#cd tools/clang/docs/
#make -f Makefile.sphinx man
#cd -
#cp tools/clang/docs/_build/man/clang.1 %{buildroot}%{_mandir}/man1/clang.1

#mkdir -p %{buildroot}%{llvmdocdir clang}
#for f in LICENSE.TXT NOTES.txt README.txt CODE_OWNERS.TXT; do
#  cp tools/clang/$f %{buildroot}%{llvmdocdir clang}/
#done
#%endif

# clang-apidoc
#%if %{with clang}
#%if %{with doxygen}
#cp -ar tools/clang/docs/doxygen/html %{buildroot}%{llvmdocdir clang-apidoc}
#%endif
#%endif

# lldb
#%if %{with lldb}
#mkdir -p %{buildroot}%{llvmdocdir lldb}
#cp tools/lldb/LICENSE.TXT %{buildroot}%{llvmdocdir lldb}/
#%endif

# delete the rest of installed documentation (because it's bad)
rm -rf %{buildroot}/moredocs

# install CMake modules
mkdir -p %{buildroot}%{_datadir}/llvm/cmake/
cp -p cmake/modules/*.cmake %{buildroot}%{_datadir}/llvm/cmake/

# remove RPATHs
file %{buildroot}%{_bindir}/* | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d
file %{buildroot}%{_libdir}/%{name}/*.so | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d

%check
# the Koji build server does not seem to have enough RAM
# for the default 16 threads

# the || : is wrong, i know, but the git snaps fail to make check due to
# broken makefiles in the doc dirs.

# LLVM test suite failing on ARM, PPC64 and s390(x)
#mkdir -p %{buildroot}%{llvmdocdir %{name}-devel}
#cd build
#make -k check LIT_ARGS="-v -j4" | tee %{buildroot}%{llvmdocdir %{name}-devel}/testlog-%{_arch}.txt || :
#cd -

%if %{with clang}
# clang test suite failing on PPC and s390(x)
# FIXME:
# unexpected failures on all platforms with GCC 4.7.0.
# capture logs
#mkdir -p %{buildroot}%{llvmdocdir clang-devel}
#cd build
#make -C tools/clang/test TESTARGS="-v -j4" | tee %{buildroot}%{llvmdocdir clang-devel}/testlog-%{_arch}.txt || :
#cd -
%endif


%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%if %{with clang}
%post -n clang-libs -p /sbin/ldconfig
%postun -n clang-libs -p /sbin/ldconfig
%endif

%if %{with lldb}
%post -n lldb -p /sbin/ldconfig
%postun -n lldb -p /sbin/ldconfig
%endif


#%posttrans devel
# link llvm-config to the platform-specific file;
# use ISA bits as priority so that 64-bit is preferred
# over 32-bit if both are installed
#
# XXX ew alternatives though. seems like it'd be better to install a
# shell script that cases on $(arch) and calls out to the appropriate
# llvm-config-%d.
#alternatives \
#  --install \
#  %{_bindir}/llvm-config \
##  llvm-config \

#%postun devel
#if [ $1 -eq 0 ]; then
#  alternatives --remove llvm-config \
#fi
#exit 0


%files
%doc CREDITS.TXT
%doc README.txt
%dir %{_datadir}/llvm
%{_bindir}/bugpoint
%{_bindir}/llc
%{_bindir}/lli
%{_bindir}/lli-child-target
%exclude %{_bindir}/llvm-config
%{_bindir}/llvm*
%{_bindir}/macho-dump
%{_bindir}/opt
%if %{with clang}
%exclude %{_mandir}/man1/clang.1*
#%exclude %{_mandir}/man1/scan-build.1*
%endif
%if %{with lldb}
#%exclude %{_mandir}/man1/lldb.1*
%endif
#%doc %{_mandir}/man1/*.1*

%files devel
#%doc %{llvmdocdir %{name}-devel}/
%{_bindir}/llvm-config
%{_includedir}/%{name}
%{_includedir}/%{name}-c
%{_datadir}/llvm/cmake

%files libs
%doc LICENSE.TXT
#%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%dir %{_libdir}/%{name}
%if %{with clang}
%exclude %{_libdir}/%{name}/libclang.so
%endif
%if %{with lldb}
%exclude %{_libdir}/%{name}/liblldb.so
%endif
%{_libdir}/%{name}/*.so

%files static
%{_libdir}/%{name}/*.a

%if %{with clang}
%files -n clang
#%doc %{llvmdocdir clang}/
%{_bindir}/clang*
%{_bindir}/c-index-test
%{_prefix}/lib/clang
#%doc %{_mandir}/man1/clang.1*

%files -n clang-libs
%{_libdir}/%{name}/libclang.so

%files -n clang-devel
#%doc %{llvmdocdir clang-devel}/
%{_includedir}/clang
%{_includedir}/clang-c

%files -n clang-analyzer
#%{_mandir}/man1/scan-build.1*
%{_bindir}/scan-build
%{_bindir}/scan-view
%{_libexecdir}/clang-analyzer
%endif

%if %{with lldb}
%files -n lldb
#%doc %{llvmdocdir lldb}/
%{_bindir}/lldb
%{_bindir}/lldb-*
%{_libdir}/%{name}/liblldb.so
# XXX double check this
#{python2_sitearch}/*
#%doc %{_mandir}/man1/lldb.1*

%files -n lldb-devel
%{_includedir}/lldb
%endif

#%files docs
#%doc %{llvmdocdir %{name}-doc}/

%changelog
