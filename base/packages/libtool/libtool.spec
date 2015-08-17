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
/usr/bin/libtool
/usr/bin/libtoolize
/usr/lib/libltdl.la
/usr/share/libtool/config-h.in
/usr/share/libtool/COPYING.LIB
/usr/share/libtool/lt__alloc.c
/usr/share/libtool/ltdl.h
/usr/share/libtool/ltdl.mk
/usr/share/libtool/configure.ac
/usr/share/libtool/lt_error.c
/usr/share/libtool/Makefile.in
/usr/share/libtool/README
/usr/share/libtool/aclocal.m4
/usr/share/libtool/lt__argz.c
/usr/share/libtool/configure
/usr/share/libtool/slist.c
/usr/share/libtool/lt__strl.c
/usr/share/libtool/lt__dirent.c
/usr/share/libtool/lt_dlloader.c
/usr/share/libtool/Makefile.am
/usr/share/libtool/ltdl.c
/usr/share/libtool/build-aux/depcomp
/usr/share/libtool/build-aux/ltmain.sh
/usr/share/libtool/build-aux/compile
/usr/share/libtool/build-aux/config.sub
/usr/share/libtool/build-aux/config.guess
/usr/share/libtool/build-aux/install-sh
/usr/share/libtool/build-aux/missing
/usr/share/libtool/libltdl/lt__strl.h
/usr/share/libtool/libltdl/lt__dirent.h
/usr/share/libtool/libltdl/lt__argz_.h
/usr/share/libtool/libltdl/lt_dlloader.h
/usr/share/libtool/libltdl/lt_error.h
/usr/share/libtool/libltdl/lt_system.h
/usr/share/libtool/libltdl/lt__alloc.h
/usr/share/libtool/libltdl/lt__private.h
/usr/share/libtool/libltdl/lt__glibc.h
/usr/share/libtool/libltdl/slist.h
/usr/share/libtool/loaders/loadlibrary.c
/usr/share/libtool/loaders/dld_link.c
/usr/share/libtool/loaders/shl_load.c
/usr/share/libtool/loaders/preopen.c
/usr/share/libtool/loaders/dlopen.c
/usr/share/libtool/loaders/dyld.c
/usr/share/libtool/loaders/load_add_on.c
/usr/share/aclocal/ltsugar.m4
/usr/share/aclocal/ltdl.m4
/usr/share/aclocal/ltversion.m4
/usr/share/aclocal/ltoptions.m4
/usr/share/aclocal/libtool.m4
/usr/share/aclocal/lt~obsolete.m4
/usr/share/aclocal/ltargz.m4
/usr/include/ltdl.h
/usr/include/libltdl/lt_dlloader.h
/usr/include/libltdl/lt_error.h
/usr/include/libltdl/lt_system.h

%files -n libltdl
/usr/lib/libltdl.so.7                                                                                                                                       
/usr/lib/libltdl.so.7.3.1                                                                                                                                   
/usr/lib/libltdl.so

%changelog
