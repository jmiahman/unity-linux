#%define _target_platform %{_arch}-unity-linux-musl
%global _arch %(uname -m)

# build against xz?
%bcond_without xz
# just for giggles, option to build with internal Berkeley DB
%bcond_with int_bdb
# run internal testsuite?
%bcond_with check
# build with plugins?
%bcond_without plugins
# build with sanitizers?
%bcond_with sanitizer
# build with libarchive? (needed for rpm2archive)
%bcond_without libarchive
# build with libimaevm.so
%bcond_without libimaevm
%bcond_with int_bdb

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define rpmhome /usr/lib/rpm

%define rpmver 4.12.0.1

%define bdbname db
%define bdbver 5.3.28
%define dbprefix db

Summary: The RPM package management system
Name: rpm
Version: 4.12.0.1
Release: 2%{?dist}
Group: System Environment/Base
Url: http://www.rpm.org/
Source0: http://rpm.org/releases/rpm-4.12.x/%{name}-%{version}.tar.bz2
%if %{with int_bdb}
#Source1: db-%{bdbver}.tar.gz
%else
BuildRequires: db-devel
Requires: db
%endif

#Patch to run on MUSL
Patch0: rpm-4.14.x-portable-definitions.patch
# Disable autoconf config.site processing (#962837)
#Patch1: rpm-4.11.x-siteconfig.patch
# Fedora specspo is setup differently than what rpm expects, considering
# this as Fedora-specific patch for now
#Patch2: rpm-4.9.90-fedora-specspo.patch
# In current Fedora, man-pages pkg owns all the localized man directories
#Patch3: rpm-4.9.90-no-man-dirs.patch
# gnupg2 comes installed by default, avoid need to drag in gnupg too
#Patch4: rpm-4.8.1-use-gpg2.patch
# Temporary band-aid for rpm2cpio whining on payload size mismatch (#1142949)
#Patch5: rpm-4.12.0-rpm2cpio-hack.patch

# Patches already upstream:
#Patch100: rpm-4.13.0-rc1-Fix-new-richdep-syntax.patch
#Patch101: rpm-4.13.0-selinux--permissive-scriptlets.patch
#Patch102: rpm-4.13.0-non-numeric-epoch.patch
#Patch103: rpm-4.13.0-wrong-version-macro.patch
#Patch104: rpm-4.13.0-memory-error.patch
#Patch105: rpm-4.13.0-rpmdeps-weakdep-support.patch
#Patch106: rpm-4.13.0-autopatch-fix.patch
#Patch107: rpm-4.13.0-ignore-sigpipe.patch
#Patch108: rpm-4.13.0-unsupported-keys.patch
#Patch109: rpm-4.13.0-fix-crash-on-corrupted.patch

# These are not yet upstream
#Patch302: rpm-4.7.1-geode-i686.patch
# Probably to be upstreamed in slightly different form
#Patch304: rpm-4.9.1.1-ld-flags.patch
# Compressed debuginfo support (#833311)
#Patch305: rpm-4.10.0-dwz-debuginfo.patch
# Minidebuginfo support (#834073)
#Patch306: rpm-4.10.0-minidebuginfo.patch
# Fix CRC32 after dwz (#971119)
#Patch307: rpm-4.11.1-sepdebugcrcfix.patch
# Fix race condidition where unchecked data is exposed in the file system
#Patch308: rpm-4.12.0.x-CVE-2013-6435.patch
# Add check against malicious CPIO file name size
#Patch309: rpm-4.12.0.x-CVE-2014-8118.patch

# Partially GPL/LGPL dual-licensed and some bits with BSD
# SourceLicense: (GPLv2+ and LGPLv2+ with exceptions) and BSD 
License: GPLv2+

Requires: coreutils
%if %{without int_bdb}
# db recovery tools, rpmdb_util symlinks
Requires: %{_bindir}/%{dbprefix}_stat
%endif
Requires: popt
Requires: curl

%if %{with check}
BuildRequires: fakechroot
%endif

# XXX generally assumed to be installed but make it explicit as rpm
# is a bit special...
BuildRequires: gawk
BuildRequires: readline-devel zlib-devel
## The popt version here just documents an older known-good version
BuildRequires: popt-devel
BuildRequires: file-devel
BuildRequires: gettext-devel
BuildRequires: ncurses-devel
BuildRequires: bzip2-devel >= 0.9.0c-2
BuildRequires: python-devel >= 2.6
BuildRequires: libcap-devel
BuildRequires: libacl-devel
%if ! %{without xz}
BuildRequires: xz-devel
%endif
%if ! %{without libarchive}
BuildRequires: libarchive-devel
%endif
# Only required by sepdebugcrcfix patch
BuildRequires: binutils-devel
# Couple of patches change makefiles so, require for now...
BuildRequires: automake libtool

#%if %{with plugins}
BuildRequires: dbus-devel
#%endif

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package libs
Summary:  Libraries for manipulating RPM packages
Group: Development/Libraries
License: GPLv2+ and LGPLv2+ with exceptions
Requires: rpm = %{version}-%{release}
Requires: libcap

%description libs
This package contains the RPM shared libraries.

%package build-libs
Summary:  Libraries for building and signing RPM packages
Group: Development/Libraries
License: GPLv2+ and LGPLv2+ with exceptions
Requires: rpm-libs = %{version}-%{release}
Requires: %{_bindir}/gpg2

%description build-libs
This package contains the RPM shared libraries for building and signing
packages.

%package devel
Summary:  Development files for manipulating RPM packages
Group: Development/Libraries
License: GPLv2+ and LGPLv2+ with exceptions
Requires: rpm = %{version}-%{release}
Requires: rpm-libs = %{version}-%{release}
Requires: rpm-build-libs = %{version}-%{release}
Requires: popt-devel

%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

%package build
Summary: Scripts and executable programs used to build packages
Group: Development/Tools
Requires: rpm = %{version}-%{release}
Requires: findutils sed grep gawk diffutils file patch
Requires: tar unzip gzip bzip2 cpio xz
Requires: pkgconfig

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

%package sign
Summary: Package signing support
Group: System Environment/Base
Requires: rpm-build-libs = %{version}-%{release}

%description sign
This package contains support for digitally signing RPM packages.

%package python
Summary: Python 2 bindings for apps which will manipulate RPM packages
Group: Development/Libraries
Requires: rpm = %{version}-%{release}

%description python
The rpm-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python 2
programs that will manipulate RPM packages and databases.

%package python3
Summary: Python 3 bindings for apps which will manipulate RPM packages
Group: Development/Libraries
Requires: rpm = %{version}-%{release}

%description python3
The rpm-python3 package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python 3
programs that will manipulate RPM packages and databases.

%package apidocs
Summary: API documentation for RPM libraries
Group: Documentation
BuildArch: noarch

%description apidocs
This package contains API documentation for developing applications
that will manipulate RPM packages and databases.

%package cron
Summary: Create daily logs of installed packages.
Group: System Environment/Base
BuildArch: noarch
Requires: crontabs logrotate rpm = %{version}-%{release}

%description cron
This package contains a cron job which creates daily logs of installed
packages on a system.

%if %{with plugins}
%package plugin-selinux
Summary: Rpm plugin for SELinux functionality
Group: System Environment/Base
Requires: rpm-libs = %{version}-%{release}

%description plugin-selinux
%{summary}

%package plugin-syslog
Summary: Rpm plugin for syslog functionality
Group: System Environment/Base
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-syslog
%{summary}

%package plugin-systemd-inhibit
Summary: Rpm plugin for systemd inhibit functionality
Group: System Environment/Base
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-systemd-inhibit
%{summary}

%package plugin-ima
Summary: Rpm plugin ima file signatures
Group: System Environment/Base
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-ima
%{summary}

%endif

%prep
%setup -n %{name}-%{rpmver}

%patch0 -p1

%if %{with int_bdb}
ln -s db-%{bdbver} db
%endif

%build
#Remove OLD config.sub
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done


%if %{without int_bdb}
#CPPFLAGS=-I%{_includedir}/db%{bdbver} 
#LDFLAGS=-L%{_libdir}/db%{bdbver}
%endif
#CPPFLAGS="$CPPFLAGS `pkg-config --cflags nss` -DLUA_COMPAT_APIINTCASTS"
#CFLAGS="$RPM_OPT_FLAGS %{?sanitizer_flags} -DLUA_COMPAT_APIINTCASTS"
#export CPPFLAGS CFLAGS LDFLAGS

autoreconf -i -f

# Using configure macro has some unwanted side-effects on rpm platform
# setup, use the old-fashioned way for now only defining minimal paths.
LDFLAGS="$LDFLAGS -lintl" \
./configure \
    --prefix=%{_usr} \
    --sysconfdir=%{_sysconfdir} \
    --localstatedir=%{_var} \
    --sharedstatedir=%{_var}/lib \
    --libdir=%{_libdir} \
    --build=%{_target_platform} \
    --host=%{_target_platform} \
    --with-vendor=redhat \
    --with-external-db \
    --without-lua \
    --with-beecrypt \
    --without-selinux \
    --with-cap \
    --with-acl \
    --disable-python

make %{?_smp_mflags}

cd python
%{__python} setup.py build
#%{__python3} setup.py build
cd ..

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR="$RPM_BUILD_ROOT" install

# We need to build with --enable-python for the self-test suite, but we
# actually package the bindings built with setup.py (#531543#c26)
rm -rf $RPM_BUILD_ROOT/%{python_sitearch}
cd python
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
# %{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
cd ..


# Save list of packages through cron
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily
install -m 755 scripts/rpm.daily ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/rpm

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -m 644 scripts/rpm.log ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/rpm

mkdir -p ${RPM_BUILD_ROOT}/usr/lib/tmpfiles.d
echo "r /var/lib/rpm/__db.*" > ${RPM_BUILD_ROOT}/usr/lib/tmpfiles.d/rpm.conf

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
mkdir -p $RPM_BUILD_ROOT%{rpmhome}/macros.d

mkdir -p $RPM_BUILD_ROOT/var/lib/rpm
for dbi in \
    Basenames Conflictname Dirnames Group Installtid Name Obsoletename \
    Packages Providename Requirename Triggername Sha1header Sigmd5 \
    __db.001 __db.002 __db.003 __db.004 __db.005 __db.006 __db.007 \
    __db.008 __db.009
do
    touch $RPM_BUILD_ROOT/var/lib/rpm/$dbi
done

# plant links to relevant db utils as rpmdb_foo for documention compatibility
%if %{without int_bdb}
for dbutil in dump load recover stat upgrade verify
do
    ln -s ../../bin/%{dbprefix}_${dbutil} $RPM_BUILD_ROOT/%{rpmhome}/rpmdb_${dbutil}
done
%endif


find $RPM_BUILD_ROOT -name "*.la"|xargs rm -f

# These live in perl-generators now
rm -f $RPM_BUILD_ROOT/%{rpmhome}/{perldeps.pl,perl.*}
rm -f $RPM_BUILD_ROOT/%{_fileattrsdir}/perl*
# Axe unused cruft
rm -f $RPM_BUILD_ROOT/%{rpmhome}/{tcl.req,osgideps.pl}

%if %{with check}
%check
make check
[ "$(ls -A tests/rpmtests.dir)" ] && cat tests/rpmtests.log
%endif

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post build-libs -p /sbin/ldconfig
%postun build-libs -p /sbin/ldconfig

%posttrans
# XXX this is klunky and ugly, rpm itself should handle this
dbstat=/usr/lib/rpm/rpmdb_stat
if [ -x "$dbstat" ]; then
    if "$dbstat" -e -h /var/lib/rpm 2>&1 | grep -q "doesn't match library version \| Invalid argument"; then
        rm -f /var/lib/rpm/__db.* 
    fi
fi
exit 0

%files 
%defattr(-,root,root,-)
#%license COPYING
%doc GROUPS CREDITS doc/manual/[a-z]*

/usr/lib/tmpfiles.d/rpm.conf
%dir %{_sysconfdir}/rpm

%attr(0755, root, root) %dir /var/lib/rpm
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/rpm/*

/bin/rpm
%{_bindir}/rpm2archive
%{_bindir}/rpm2cpio
%{_bindir}/rpmdb
%{_bindir}/rpmkeys
%{_bindir}/rpmquery
%{_bindir}/rpmverify

%{_mandir}/man8/rpm.8*
%{_mandir}/man8/rpmdb.8*
%{_mandir}/man8/rpmkeys.8*
%{_mandir}/man8/rpm2cpio.8*

# XXX this places translated manuals to wrong package wrt eg rpmbuild
%{_mandir}/fr/man[18]/*.[18]*
%{_mandir}/ko/man[18]/*.[18]*
%{_mandir}/ja/man[18]/*.[18]*
%{_mandir}/pl/man[18]/*.[18]*
%{_mandir}/ru/man[18]/*.[18]*
%{_mandir}/sk/man[18]/*.[18]*

%{_datadir}/locale/*/LC_MESSAGES/rpm.mo

%attr(0755, root, root) %dir %{rpmhome}
%{rpmhome}/macros
%{rpmhome}/macros.d
%{rpmhome}/rpmpopt*
%{rpmhome}/rpmrc

%{rpmhome}/rpmdb_*
%{rpmhome}/rpm.daily
%{rpmhome}/rpm.log
%{rpmhome}/rpm.supp
%{rpmhome}/rpm2cpio.sh
%{rpmhome}/tgpg

%{rpmhome}/platform

%dir %{rpmhome}/fileattrs

%files libs
%defattr(-,root,root)
%{_libdir}/librpmio.so.*
%{_libdir}/librpm.so.*
%if %{with plugins}
%dir %{_libdir}/rpm-plugins

%files plugin-syslog
%{_libdir}/rpm-plugins/syslog.so

#%files plugin-selinux
#%{_libdir}/rpm-plugins/selinux.so

%files plugin-systemd-inhibit
%{_libdir}/rpm-plugins/systemd_inhibit.so

#%files plugin-ima
#%{_libdir}/rpm-plugins/ima.so
%endif

%files build-libs
%defattr(-,root,root)
%{_libdir}/librpmbuild.so.*
%{_libdir}/librpmsign.so.*

%files build
%defattr(-,root,root)
%{_bindir}/rpmbuild
%{_bindir}/gendiff
%{_bindir}/rpmspec

%{_mandir}/man1/gendiff.1*
%{_mandir}/man8/rpmbuild.8*
%{_mandir}/man8/rpmdeps.8*
%{_mandir}/man8/rpmspec.8*

%{rpmhome}/brp-*
%{rpmhome}/check-*
#%{rpmhome}/debugedit
#%{rpmhome}/sepdebugcrcfix
#%{rpmhome}/find-debuginfo.sh
%{rpmhome}/find-lang.sh
%{rpmhome}/*provides*
%{rpmhome}/*requires*
%{rpmhome}/*deps*
%{rpmhome}/*.prov
%{rpmhome}/*.req
%{rpmhome}/config.*
%{rpmhome}/mkinstalldirs
%{rpmhome}/macros.p*
%{rpmhome}/fileattrs/*

%files sign
%defattr(-,root,root)
%{_bindir}/rpmsign
%{_mandir}/man8/rpmsign.8*

%files python
%defattr(-,root,root)
%{python_sitearch}/rpm
%{python_sitearch}/rpm_python-%{version}-py2.7.egg-info

#%files python3
#%defattr(-,root,root)
#%{python3_sitearch}/rpm
#%{python3_sitearch}/rpm_python-%{eggver}-py%{python3_version}.egg-info

%files devel
%defattr(-,root,root)
%{_mandir}/man8/rpmgraph.8*
%{_bindir}/rpmgraph
%{_libdir}/librp*[a-z].so
%{_libdir}/pkgconfig/rpm.pc
%{_includedir}/rpm

%files cron
%defattr(-,root,root)
%{_sysconfdir}/cron.daily/rpm
%config(noreplace) %{_sysconfdir}/logrotate.d/rpm

%files apidocs
%defattr(-,root,root)
#%license COPYING
%doc doc/librpm/html/*

%changelog
* Wed Dec 02 2015 JMiahMan <JMiahMan@unity-linux.org> - 4.12.0.1-2
- removed requires for db5.3 and replace it just with db

* Mon Nov 30 2015 JMiahMan <JMiahMan@unity-linux.org> - 4.12.0.1-1
- Initial build for Unity-Linux

