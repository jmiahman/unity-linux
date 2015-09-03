%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global gitrev 1f9abfb5b1bb18a8f46887fa2541957e74132567
%global shortcommit %(c=%{gitrev}; echo ${c:0:7})
#%filter_provides_in %{perl_vendorarch}/.*\.so$
#%filter_provides_in %{python2_sitearch}/.*\.so$
%if 0%{?fedora}
%bcond_without python3
%filter_provides_in %{python3_sitearch}/.*\.so$
%global _cmake_opts \\\
            -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
            -DENABLE_PERL=1 \\\
            -DENABLE_PYTHON=1 \\\
            -DUSE_VENDORDIRS=1 \\\
            -DFEDORA=1 \\\
            -DENABLE_DEBIAN=1 \\\
            -DENABLE_ARCHREPO=1 \\\
            -DENABLE_LZMA_COMPRESSION=1 \\\
            -DMULTI_SEMANTICS=1 \\\
            -DENABLE_COMPLEX_DEPS=1 \\\
            %{nil}
#%else
#%bcond_with python3
#%global _cmake_opts \\\
#            -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
#            -DENABLE_LZMA_COMPRESSION=1 \\\
#            -DENABLE_RPMDB=1 \\\
#            %{nil}
%endif

%global _cmake_opts \\\
	-DENABLE_APPDATA=ON \\\
	-DENABLE_BZIP2_COMPRESSION=ON \\\
	-DENABLE_LZMA_COMPRESSION=ON \\\
	-DENABLE_APPDATA=ON \\\
	-DENABLE_PYTHON=ON \\\
	-DENABLE_RPMDB=ON \\\
	-DENABLE_RPMDB_BYRPMHEADER=ON \\\
	-DENABLE_RPMMD=ON \\\
	-DPythonLibs_FIND_VERSION=2 \\\
	-DPythonLibs_FIND_VERSION_MAJOR=2 \\\
	-DRPM5=ON \\\
	-DUSE_VENDORDIRS=ON \\\
        %{nil}

#%filter_provides_in %{ruby_vendorarch}/.*\.so$
#%filter_setup

Name:		libsolv
Version:	0.6.11
Release:	1.git%{shortcommit}%{?dist}
License:	BSD
Url:		https://github.com/openSUSE/libsolv
Source:		https://github.com/openSUSE/libsolv/archive/%{gitrev}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Group:		Development/Libraries
Summary:	Package dependency solver
BuildRequires:	cmake expat-devel rpm-devel zlib-devel
BuildRequires:	perl python-devel
BuildRequires:  xz-devel
#BuildRequires:	libdb-devel
#BuildRequires:  swig

Patch0:		libsolv-fopencookie.patch 

%description
A free package dependency solver using a satisfiability algorithm. The
library is based on two major, but independent, blocks:

- Using a dictionary approach to store and retrieve package
  and dependency information.

- Using satisfiability, a well known and researched topic, for
  resolving package dependencies.

%package devel
Summary:	A new approach to package dependency solving
Group:		Development/Libraries
Requires:	libsolv-tools%{?_isa} = %{version}-%{release}
Requires:	libsolv%{?_isa} = %{version}-%{release}
Requires:	rpm-devel%{?_isa}
Requires:	cmake

%description devel
Development files for libsolv,

%package tools
Summary:	A new approach to package dependency solving
Group:		Development/Libraries
Requires:	gzip bzip2 coreutils
Requires:	libsolv%{?_isa} = %{version}-%{release}

%description tools
Package dependency solver tools.

#%package demo
#Summary:	Applications demoing the libsolv library
#Group:		Development/Libraries
#Requires:	curl gnupg2

#%description demo
#Applications demoing the libsolv library.

%package -n python-solv
Summary:	Python bindings for the libsolv library
Group:		Development/Languages
Requires:	python
Requires:	libsolv = %{version}

%description -n python-solv
Python bindings for sat solver.

%if 0%{?fedora}
%package -n perl-solv
Summary:	Perl bindings for the libsolv library
Group:		Development/Languages
Requires:	perl
Requires:	libsolv%{?_isa} = %{version}-%{release}

%description -n perl-solv
Perl bindings for sat solver.
%endif

%prep
%setup -q -n libsolv-%{gitrev}
%patch0 -p1

%build
cmake %_cmake_opts \
        -DPythonLibs_FIND_VERSION=2 -DPythonLibs_FIND_VERSION_MAJOR=2 -DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR=/usr/lib
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
mv %{buildroot}/usr/lib64/* %{buildroot}/usr/lib/
rm -rf %{buildroot}/usr/lib64



#%check
#make ARGS="-V" test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%doc LICENSE* README BUGS
%_libdir/libsolv.so.*
%_libdir/libsolvext.so.*

%files tools
%_bindir/deltainfoxml2solv
%_bindir/dumpsolv
%_bindir/installcheck
%_bindir/mergesolv
%_bindir/repo2solv.sh
%_bindir/repomdxml2solv
%_bindir/rpmdb2solv
%_bindir/rpmmd2solv
%_bindir/rpms2solv
%_bindir/testsolv
%_bindir/updateinfoxml2solv

%files devel
#%doc examples/solv.c
%_libdir/libsolv.so
%_libdir/libsolvext.so
%_includedir/solv
%_datadir/cmake/Modules/FindLibSolv.cmake
#%{_mandir}/man?/*

#%files demo
#%_bindir/solv

%if 0%{?fedora}
%files -n perl-solv
%doc examples/p5solv
%{perl_vendorarch}/*
%endif

%files -n python-solv
#%doc examples/pysolv
%{python_sitelib}/*


%changelog
