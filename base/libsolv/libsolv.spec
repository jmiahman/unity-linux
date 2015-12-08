%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global gitrev 1f9abfb5b1bb18a8f46887fa2541957e74132567
%global shortcommit %(c=%{gitrev}; echo ${c:0:7})
#%filter_provides_in %{perl_vendorarch}/.*\.so$
#%filter_provides_in %{python2_sitearch}/.*\.so$

%global _cmake_opts \\\
	-DFEDORA=1 \\\
	-DENABLE_PYTHON=1 \\\
	-DENABLE_LZMA_COMPRESSION=1 \\\
	-DENABLE_COMPLEX_DEPS=1 \\\
        %{nil}

#%filter_provides_in %{ruby_vendorarch}/.*\.so$
#%filter_setup

Name:		libsolv
Version:	0.6.14
Release:	0%{?dist}
License:	BSD
Url:		https://github.com/openSUSE/libsolv
Source0:	https://github.com/openSUSE/libsolv/archive/%{version}/%{name}-%{version}.tar.gz
Group:		Development/Libraries
Summary:	Package dependency solver
BuildRequires:	cmake expat-devel rpm-devel zlib-devel
BuildRequires:	perl python-devel
BuildRequires:  xz-devel

Patch0:		libsolv-add-portable-fopencookie.patch

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
Requires:	libsolv-tools = %{version}-%{release}
Requires:	libsolv = %{version}-%{release}
Requires:	rpm-devel
Requires:	cmake

%description devel
Development files for libsolv,

%package tools
Summary:	A new approach to package dependency solving
Group:		Development/Libraries
Requires:	gzip bzip2 coreutils
Requires:	libsolv = %{version}-%{release}

%description tools
Package dependency solver tools.

%package demo
Summary:	Applications demoing the libsolv library
Group:		Development/Libraries
Requires:	curl gnupg2

%description demo
Applications demoing the libsolv library.

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
%setup -q -n libsolv-%{version}
%patch0 -p1

%build
cmake %_cmake_opts \
        -DPythonLibs_FIND_VERSION=2 -DPythonLibs_FIND_VERSION_MAJOR=2 -DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR=/usr/lib
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make ARGS="-V" test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
#%doc LICENSE* README BUGS
%{_libdir}/libsolv.so.*
%{_libdir}/libsolvext.so.*

%files tools
%{_bindir}/deltainfoxml2solv
%{_bindir}/dumpsolv
%{_bindir}/installcheck
%{_bindir}/mergesolv
%{_bindir}/repo2solv.sh
%{_bindir}/repomdxml2solv
%{_bindir}/rpmdb2solv
%{_bindir}/rpmmd2solv
%{_bindir}/rpms2solv
%{_bindir}/testsolv
%{_bindir}/updateinfoxml2solv

%files devel
#%doc examples/solv.c
%{_libdir}/libsolv.so
%{_libdir}/libsolvext.so
%{_includedir}/solv
%{_datadir}/cmake/Modules/FindLibSolv.cmake
%{_libdir}/pkgconfig/libsolv.pc
%{_mandir}/man?/*

%files demo
%{_bindir}/solv

%if 0%{?fedora}
%files -n perl-solv
%doc examples/p5solv
%{perl_vendorarch}/*
%endif

%files -n python-solv
#%doc examples/pysolv
%{python_sitelib}/*


%changelog
