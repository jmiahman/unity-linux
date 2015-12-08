%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64
%define _lib /lib64
%global _default_patch_fuzz 2

%define patchleveltag .10
%define baseversion 2.7

Name:		python2	
Version:	%{baseversion}%{patchleveltag}
#Version:	2.7.10
Release:	0%{?dist}
Summary:	An interpreted, interactive, object-oriented programming language	

Group:		Development/Languages
License:	Python
URL:		http://www.python.org/
Source0:	http://ftp.osuosl.org/pub/blfs/conglomeration/Python/Python-%{version}.tar.xz

Patch0:		musl-find_library.patch
Patch1:		unchecked-ioctl.patch	
Patch4:		00187-add-RPATH-to-pyexpat.patch
Patch5:		python-2.6-rpath.patch
Patch6:		python-2.6.4-distutils-rpath.patch
Patch7:		python-pythonpath.patch
Patch8:		python-ac_fixes.patch

Patch9:		python-2.7.1-config.patch
Patch10:	00144-no-gdbm.patch
Patch11:	00146-hashlib-fips.patch
Patch12:	00165-crypt-module-salt-backport.patch

Patch13:	python-2.7.3-lib64.patch
Patch14:	python-2.7-lib64-sysconfig.patch
Patch15:	lib64-fix-for-test_install.patch

BuildRequires:	expat-devel, openssl-devel, zlib-devel, ncurses-devel
BuildRequires:  bzip2-devel, gdbm-devel, sqlite-devel, libffi-devel
BuildRequires:  readline-devel

%description
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

Programmers can write new built-in modules for Python in C or C++.
Python can be used as an extension language for applications that need
a programmable interface.

Note that documentation for Python is provided in the python-docs
package.

This package provides the "python" executable; most of the actual
implementation is within the "python-libs" package.

%package tests
Summary: The test modules from the main python package
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description tests
The test modules from the main python package: %{name}
These have been removed to save space, as they are never or almost
never used in production.

You might want to install the python-test package if you're developing python
code that uses more than just unittest and/or test_support.py.

%package gdbm
Summary: GNU dbm database support for Python 
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description gdbm
GNU dbm database support for Python

%package devel
Summary: The libraries and header files needed for Python development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.
This package contains the header files and libraries needed to do
these types of tasks.

Install python-devel if you want to develop Python extensions.  The
python package will also need to be installed.  You'll probably also
want to install the python-docs package, which contains Python
documentation.

%prep
%setup -q -n Python-%{version}


%patch0 -p1 -b .find_library
%patch1 -p1 -b .unchecked-ioctl
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

sed -i -e 's#db_setup_debug = False#db_setup_debug = True#g' setup.py

# remove if Lib/plat-linux3 exists
[ -d Lib/plat-linux3 ] && exit 1
cp -a Lib/plat-linux2 Lib/plat-linux3
rm -r Modules/expat Modules/zlib

%build
aclocal
autoconf

#This also is a hack.. find out why _hashlib needs it forced
export LDFLAGS="$LDFLAGS -lz"

%configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--libdir=%{_libdir} \
	--enable-shared \
	--with-threads \
	--enable-ipv6 \
	--with-system-ffi \
	--disable-xdr \
	--with-system-zlib \
	--with-system-expat \
	--enable-unicode=ucs4

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make -j1 DESTDIR=%{buildroot} install
#install -Dm644 LICENSE %{buildroot}/usr/share/licenses/%{name}g/LICENSE
rm %{buildroot}%{_bindir}/2to3

%files
%license LICENSE
%{_mandir}/man*/python.*
%{_mandir}/man*/python2.*
%{_bindir}/*
%{_libdir}/libpython%{baseversion}.so.1.0
%dir %{_libdir}/python%{baseversion}/
%{_libdir}/python%{baseversion}/*
%dir %{_libdir}/python%{baseversion}/sqlite3
%{_libdir}/python%{baseversion}/sqlite3/*

#Exclude testing folders
%exclude %{_libdir}/python%{baseversion}/sqlite3/test
%exclude %{_libdir}/python%{baseversion}/unittest/test/
%exclude %{_libdir}/python%{baseversion}/email/test/
%exclude %{_libdir}/python%{baseversion}/ctypes/test/
%exclude %{_libdir}/python%{baseversion}/bsddb/test/
%exclude %{_libdir}/python%{baseversion}/test/
%exclude %{_libdir}/python%{baseversion}/lib-tk/test/

%files gdbm
%{_libdir}/python%{baseversion}/lib-dynload/gdbm*.so

%files tests
%{_libdir}/python%{baseversion}/sqlite3/test
%{_libdir}/python%{baseversion}/unittest/test/
%{_libdir}/python%{baseversion}/email/test/
%{_libdir}/python%{baseversion}/ctypes/test/
%{_libdir}/python%{baseversion}/bsddb/test/
%{_libdir}/python%{baseversion}/test/
%{_libdir}/python%{baseversion}/lib-tk/test/

%files devel
%{_bindir}/%{name}*-config
%dir %{_includedir}/python%{baseversion}
%dir %{_libdir}/python%{baseversion}/config
%dir %{_libdir}/python%{baseversion}/distutils
%{_libdir}/python2.7/config/*
%{_libdir}/python2.7/distutils/*
%{_includedir}/python%{baseversion}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpython%{baseversion}.so

%changelog
