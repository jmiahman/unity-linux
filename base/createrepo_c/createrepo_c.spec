%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64

Summary:        Creates a common metadata repository
Name:           createrepo_c
Version:        0.9.1
Release:        1%{?dist}
License:        GPLv2
Group:          System Environment/Base
Source0:        https://github.com/rpm-software-management/createrepo_c/archive/0.9.1.tar.gz
URL:            https://github.com/Tojaj/createrepo_c

Patch0:		createrepo_c-0.9.1-replace-on_exit-with-portable-atexit.patch

BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  file-devel
BuildRequires:  glib-devel >= 2.22.0
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  python-devel
BuildRequires:  python-nose
BuildRequires:  python-sphinx
BuildRequires:  rpm-devel >= 4.8.0-28
BuildRequires:  sqlite-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  bash-completion

%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package libs
Summary:    Library for repodata manipulation
Group:      Development/Libraries

%description libs
Libraries for applications using the createrepo_c library
for easy manipulation with a repodata.


%package devel
Summary:    Library for repodata manipulation
Group:      Development/Libraries
Requires:   pkgconfig >= 1:0.14
Requires:   %{name}-libs =  %{version}-%{release}

%description devel
This package contains the createrepo_c C library and header files.
These development files are for easy manipulation with a repodata.

%package -n python-createrepo_c
Summary:    Python bindings for the createrepo_c library
Group:      Development/Languages
Requires:   %{name}-libs = %{version}-%{release}

%description -n python-createrepo_c
Python bindings for the createrepo_c library.

%prep
%setup -q 
%patch0 -p1

%build
%cmake .
make %{?_smp_mflags} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
make doc-c

#%check
#make tests
#make ARGS="-V" test

%install
make install DESTDIR=$RPM_BUILD_ROOT/

%post -n %{name}-libs -p /sbin/ldconfig

%postun -n %{name}-libs -p /sbin/ldconfig

%files
%doc README.md
%doc COPYING
%_mandir/man8/createrepo_c.8.*
%_mandir/man8/mergerepo_c.8.*
%_mandir/man8/modifyrepo_c.8.*
%_mandir/man8/sqliterepo_c.8.*
%{_bindir}/createrepo_c
%{_bindir}/mergerepo_c
%{_bindir}/modifyrepo_c
%{_bindir}/sqliterepo_c
%{_datadir}/bash-completion/completions/*

%files libs
%doc COPYING
%{_libdir}/libcreaterepo_c.so.*

%files devel
%{_libdir}/libcreaterepo_c.so
%{_libdir}/pkgconfig/createrepo_c.pc
%{_includedir}/createrepo_c/*
%doc COPYING
%doc doc/html

%files -n python-createrepo_c
%{python_sitearch}/createrepo_c/

%changelog
* Mon Nov 30 2015 JMiahMan <JMiahMan@unity-linux.org> - 0.9.1-1
- Initial build for Unity Linux
