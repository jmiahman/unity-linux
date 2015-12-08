%define _target_platform %{_arch}-unity-linux-musl

Name:		libtool	
Version:	2.4.6
Release:	1%{?dist}
Summary:	The GNU Portable Library Tool

Group:		Development/Tools
License:	GPLv2+ and LGPLv2+ and GFDL
URL:		http://www.gnu.org/software/libtool/
Source0:	http://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz

#BuildRequires:	
#Requires:	

%description
GNU Libtool is a set of shell scripts which automatically configure UNIX and
UNIX-like systems to generically build shared libraries. Libtool provides a
consistent, portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, but do not use
the rest of the GNU Autotools (such as GNU Autoconf and GNU Automake), you
should install the libtool package.

The libtool package also includes all files needed to integrate the GNU
Portable Library Tool (libtool) and the GNU Libtool Dynamic Module Loader
(ltdl) into a package built using the GNU Autotools (including GNU Autoconf
and GNU Automake).

%package -n libltdl
Summary:  Runtime libraries for GNU Libtool Dynamic Module Loader
Group:    System Environment/Libraries
License:  LGPLv2+


%description -n libltdl
The libtool-ltdl package contains the GNU Libtool Dynamic Module Loader, a
library that provides a consistent, portable interface which simplifies the
process of using dynamic modules.

These runtime libraries are needed by programs that link directly to the
system-installed ltdl libraries; they are not needed by software built using
the rest of the GNU Autotools (including GNU Autoconf and GNU Automake).

%prep
%setup -q

%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--disable-static \

make %{?_smp_mflags}


%install
%make_install


%files
%{_bindir}/libtool
%{_bindir}/libtoolize
%{_libdir}/libltdl.la
%{_datadir}/libtool/config-h.in
%{_datadir}/libtool/COPYING.LIB
%{_datadir}/libtool/lt__alloc.c
%{_datadir}/libtool/ltdl.h
%{_datadir}/libtool/ltdl.mk
%{_datadir}/libtool/configure.ac
%{_datadir}/libtool/lt_error.c
%{_datadir}/libtool/Makefile.in
%{_datadir}/libtool/README
%{_datadir}/libtool/aclocal.m4
%{_datadir}/libtool/lt__argz.c
%{_datadir}/libtool/configure
%{_datadir}/libtool/slist.c
%{_datadir}/libtool/lt__strl.c
%{_datadir}/libtool/lt__dirent.c
%{_datadir}/libtool/lt_dlloader.c
%{_datadir}/libtool/Makefile.am
%{_datadir}/libtool/ltdl.c
%{_datadir}/libtool/build-aux/*
%{_datadir}/libtool/libltdl/lt__strl.h
%{_datadir}/libtool/libltdl/lt__dirent.h
%{_datadir}/libtool/libltdl/lt__argz_.h
%{_datadir}/libtool/libltdl/lt_dlloader.h
%{_datadir}/libtool/libltdl/lt_error.h
%{_datadir}/libtool/libltdl/lt_system.h
%{_datadir}/libtool/libltdl/lt__alloc.h
%{_datadir}/libtool/libltdl/lt__private.h
%{_datadir}/libtool/libltdl/lt__glibc.h
%{_datadir}/libtool/libltdl/slist.h
%{_datadir}/libtool/loaders/loadlibrary.c
%{_datadir}/libtool/loaders/dld_link.c
%{_datadir}/libtool/loaders/shl_load.c
%{_datadir}/libtool/loaders/preopen.c
%{_datadir}/libtool/loaders/dlopen.c
%{_datadir}/libtool/loaders/dyld.c
%{_datadir}/libtool/loaders/load_add_on.c
%{_datadir}/aclocal/ltsugar.m4
%{_datadir}/aclocal/ltdl.m4
%{_datadir}/aclocal/ltversion.m4
%{_datadir}/aclocal/ltoptions.m4
%{_datadir}/aclocal/libtool.m4
%{_datadir}/aclocal/lt~obsolete.m4
%{_datadir}/aclocal/ltargz.m4
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/build-aux/
%dir %{_datadir}/%{name}/libltdl/
%dir %{_datadir}/%{name}/loaders/
%dir %{_includedir}/libltdl/
%{_includedir}/ltdl.h
%{_includedir}/libltdl/lt_dlloader.h
%{_includedir}/libltdl/lt_error.h
%{_includedir}/libltdl/lt_system.h

%files -n libltdl
%{_libdir}/libltdl.so.7
%{_libdir}/libltdl.so.7.3.1
%{_libdir}/libltdl.so

%changelog
