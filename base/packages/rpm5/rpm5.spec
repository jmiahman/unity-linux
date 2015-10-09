Name:           rpm
Version:        5.4.15
Release:        1%{?dist}
Summary:        The RPM package management system.

Group:          System Environment/Base
License:        LGPL
URL:            rpm5.org
Source0:        https://translationproject.org/extra/rpm-5.4.15.tar.gz
#Source1:	http://optware.kupper.org/sources/db-5.2.42.tar.gz

Patch0:		rpm-db5.2.patch
Patch1:		rpm-musl-5.4.patch
Patch2:		rpm-musl-name.patch
Patch3:		rpm-macro.patch
Patch4:		rpm-5.4.10-fix-a-couple-of-debugedit-memleaks.patch
Patch5:		rpm-fix-missing-types-in-headers.patch
Patch6:		rpm-5.4.9-mire-fix-strings-lacking-null-terminator.patch
Patch7:		rpm-5.4.9-fix-verify-segfault.patch


BuildRequires: expat-devel, python-devel 
Requires: expat sqlite libxml2 
Requires: libstdc++ db5.2-sql bzip2 libgcc

%description
RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

#--------------------------------------------------------------------

%package	libs
Summary:	Libraries for manipulating RPM packages.
Group:		System Environment/Base

%description	libs
This package contains the %{name} shared libraries.

#--------------------------------------------------------------------

%package	build
Summary:	Scripts and executable programs used to build packages.
Group:		System Environment/Base
Requires:	%{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description 	build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

#--------------------------------------------------------------------

%package	python
Summary:	Python 2 bindings for apps which will manipulate RPM packages
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description python
The rpm-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python 2
programs that will manipulate RPM packages and databases.

#--------------------------------------------------------------------

%package	devel
Summary:        Development files for %{name}
Group:          System Environment/Base
License:        LGPL
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description	devel
Development files and headers for %{name}.

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
rm -rf %{builddir}

#tar xzvf %{SOURCE1} 
#mv db-5.2.42 db
#mkdir db3
#cp %{SOURCE2} db3/configure

export CFLAGS="-D_GNU_SOURCE -D__musl__ -Os"
autoconf

./configure \
	--prefix=/usr \
	--disable-silent-rules \
	--enable-static \
	--enable-shared \
	--disable-openmp \
	--disable-nls \
	--with-file=external \
        --with-db=external \
	--with-bzip2=external \
	--without-path-versioned \
	--with-popt=external \
	--with-dbapi=db \
	--without-lua \
	--with-neon \
	--with-openssl \
	--with-pcre=internal \
	--without-selinux \
	--with-xz=external \
	--with-beecrypt=external \
	--with-zlib \
	--without-db-tools-integrated \
	--with-python='2.7' \
	--enable-debug

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
#This is needed for macros
mkdir -p %{buildroot}/var/spool/repackage/

%clean
rm -rf $RPM_BUILD_ROOT

#--------------------------------------------------------------------

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/rpm
%{_bindir}/rpm2cpio
%{_bindir}/gendiff
%{_usrlibrpm}/macros
%dir /var/spool/repackage
%{_usrlibrpm}/rpm.*
%{_usrlibrpm}/tgpg
%{_usrlibrpm}/rpmpopt
%dir %{_libdir}/rpm

#--------------------------------------------------------------------

%files libs
%{_libdir}/librpm-5.4.so
%{_libdir}/librpmconstant-5.4.so
%{_libdir}/librpmdb-5.4.so
%{_libdir}/librpmio-5.4.so
%{_libdir}/librpmmisc-5.4.so
%{_libdir}/librpmbuild-5.4.so

#--------------------------------------------------------------------

%files build
%{_bindir}/rpmbuild
%{_usrlibrpmbin}/
%{_usrlibrpm}/brp-*
%{_usrlibrpm}/check-files
%{_usrlibrpm}/cross-build
%{_usrlibrpm}/find-debuginfo.sh
%{_usrlibrpm}/find-lang.sh
%{_usrlibrpm}/find-prov.pl
%{_usrlibrpm}/find-provides.perl
%{_usrlibrpm}/find-req.pl
%{_usrlibrpm}/find-requires.perl
%{_usrlibrpm}/getpo.sh
%{_usrlibrpm}/http.req
%{_usrlibrpm}/javadeps.sh

%{_usrlibrpm}/executabledeps.sh
%{_usrlibrpm}/libtooldeps.sh
%{_usrlibrpm}/perldeps.pl
%{_usrlibrpm}/perl.prov
%{_usrlibrpm}/perl.req
%{_usrlibrpm}/php.prov
%{_usrlibrpm}/php.req
%{_usrlibrpm}/pkgconfigdeps.sh
%{_usrlibrpm}/pythondeps.sh

%{_usrlibrpm}/u_pkg.sh
%{_usrlibrpm}/vpkg-provides.sh
%{_usrlibrpm}/vpkg-provides2.sh

#--------------------------------------------------------------------

%files python
%defattr(-,root,root)
/usr/lib/python2.7/site-packages/rpm

#--------------------------------------------------------------------

%files devel
%{_includedir}/rpm/*.h
%dir %{_includedir}/rpm/
%{_libdir}/librpm.a
%{_libdir}/librpm.la
%{_libdir}/librpm.so
%{_libdir}/librpmconstant.a
%{_libdir}/librpmconstant.la
%{_libdir}/librpmconstant.so
%{_libdir}/librpmdb.a
%{_libdir}/librpmdb.la
%{_libdir}/librpmdb.so
%{_libdir}/librpmio.a
%{_libdir}/librpmio.la
%{_libdir}/librpmio.so
%{_libdir}/librpmmisc.a
%{_libdir}/librpmmisc.la
%{_libdir}/librpmmisc.so
%{_libdir}/librpmbuild.a
%{_libdir}/librpmbuild.la
%{_libdir}/librpmbuild.so
%{_libdir}/pkgconfig/rpm.pc

#--------------------------------------------------------------------

%changelog
