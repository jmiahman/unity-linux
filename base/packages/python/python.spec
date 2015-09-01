%define _target_platform %{_arch}-unity-linux-musl

%define patchleveltag .10
%define baseversion 2.7

Name:		python	
Version:	%{baseversion}%{patchleveltag}
Release:	1%{?dist}
Summary:	An interpreted, interactive, object-oriented programming language	

Group:		Development/Languages
License:	Python
URL:		http://www.python.org/
Source0:	http://ftp.osuosl.org/pub/blfs/conglomeration/Python/Python-%{version}.tar.xz

Patch0:		find_library.patch
Patch1:		unchecked-ioctl.patch	
Patch2:		python-2.7.1-config.patch
Patch3:		00146-hashlib-fips.patch
Patch4:		00187-add-RPATH-to-pyexpat.patch
Patch5:		python-2.6-rpath.patch
Patch6:		python-2.6.4-distutils-rpath.patch

BuildRequires:	expat-devel, openssl-devel, zlib-devel, ncurses-devel
BuildRequires:  bzip2-devel, gdbm-devel, sqlite, libffi-devel
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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
#rm -r Modules/expat Modules/zlib

#Die local die! Dirty Dirty Hack.. fix later
sed -i "s%/usr/local/%/usr/%g" $(grep -H -r '/usr/local/' ./ | cut -d: -f1)

#This also is a hack.. find out why _hashlib needs it forced
export LDFLAGS="$LDFLAGS -lz"

./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--enable-shared \
	--with-threads \
	--enable-ipv6 \
	--with-system-ffi \
	--with-system-zlib \
	--with-system-expat \
	--enable-unicode=ucs4

make %{?_smp_mflags}


%install
make -j1 DESTDIR=%{buildroot} install
install -Dm644 LICENSE %{buildroot}/usr/share/licenses/%{name}g/LICENSE
rm %{buildroot}/usr/bin/2to3

%files
/usr/bin/*
/usr/lib/libpython%{baseversion}.so.1.0
%dir /usr/lib/python%{baseversion}/
/usr/lib/python%{baseversion}/*

#Exclude testing folders
%exclude /usr/lib/python%{baseversion}/sqlite3/test
%exclude /usr/lib/python%{baseversion}/unittest/test/
%exclude /usr/lib/python%{baseversion}/email/test/
%exclude /usr/lib/python%{baseversion}/ctypes/test/
%exclude /usr/lib/python%{baseversion}/bsddb/test/
%exclude /usr/lib/python%{baseversion}/test/
%exclude /usr/lib/python%{baseversion}/lib-tk/test/

%files gdbm
/usr/lib/python%{baseversion}/lib-dynload/gdbm*.so

%files tests
/usr/lib/python%{baseversion}/sqlite3/test
/usr/lib/python%{baseversion}/unittest/test/
/usr/lib/python%{baseversion}/email/test/
/usr/lib/python%{baseversion}/ctypes/test/
/usr/lib/python%{baseversion}/bsddb/test/
/usr/lib/python%{baseversion}/test/
/usr/lib/python%{baseversion}/lib-tk/test/

%files devel
/usr/bin/%{name}*-config
%dir /usr/include/python%{baseversion}
%dir /usr/lib/python%{baseversion}/config
%dir /usr/lib/python%{baseversion}/distutils
/usr/lib/python2.7/config/*
/usr/lib/python2.7/distutils/*
/usr/include/python%{baseversion}/*.h
/usr/lib/pkgconfig/*.pc
/usr/lib/libpython%{baseversion}.so

%changelog
