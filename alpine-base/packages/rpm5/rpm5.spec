Name:           rpm
Version:        5.4.15
Release:        1%{?dist}
Summary:        The RPM package management system.

Group:          System Environment/Base
License:        LGPL
URL:            rpm5.org
Source0:        http://translationproject.org/extra/rpm-5.4.15.tar.gz
Source1:	http://optware.kupper.org/sources/db-5.2.42.tar.gz
Source2:	configure-db3
Source3:        configure.ac

Patch0:		rpm-musl-5.4.patch
Patch1:		rpm-musl-name.patch
Patch2:		rpm-macro.patch

#BuildRequires:  
#Requires:       

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

%description 	build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

#--------------------------------------------------------------------

%package	devel
Summary:        Development files for %{name}
Group:          System Environment/Base
License:        LGPL
Requires:       %{name} = %{version}

%description	devel
Development files and headers for %{name}.

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build

tar xzvf %{SOURCE1} 
mv db-5.2.42 db
mkdir db3
cp %{SOURCE2} db3/configure

export CFLAGS="-D_GNU_SOURCE -D__musl__ -Os"
cp %{SOURCE3} .
autoconf

./configure \
	--prefix='/usr' \
	--disable-openmp \
	--disable-nls \
	--with-file=external \
	--with-db=internal \
	--without-lua \
	--with-neon \
	--with-openssl \
	--with-pcre=external \
	--without-selinux \
	--with-xz=external \
	--with-beecrypt=external \
	--with-zlib \
	--without-db-tools-integrated \
	--enable-debug

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


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
%{_usrlibrpm}/rpm.*
%{_usrlibrpm}/tgpg
%{_usrlibrpm}/rpmpopt

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

%files devel
%{_includedir}/rpm
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
