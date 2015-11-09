Name:      icu
Version:   56.1
Release:   1%{?dist}
Summary:   International Components for Unicode
Group:     Development/Tools
License:   MIT and UCD and Public Domain
URL:       http://www.icu-project.org/
Source0:   http://download.icu-project.org/files/icu4c/56.1/icu4c-56_1-src.tgz
Source1:   icu-config.sh
Autoreq: 0

BuildRequires: doxygen, autoconf, python

Requires: lib%{name} = %{version}-%{release}

#Patch1: icu.8198.revert.icu5431.patch
#Patch2: icu.8800.freeserif.crash.patch
#Patch3: icu.7601.Indic-ccmp.patch
#Patch4: gennorm2-man.patch
Patch5: icuinfo-man.patch
#Patch6: armv7hl-disable-tests.patch

Patch0:         icu-timezone.patch
Patch1:         ac264-hack.patch

%description
Tools and utilities for developing with icu.

%package -n lib%{name}
Summary: International Components for Unicode - libraries
Group:   System Environment/Libraries

%description -n lib%{name}
The International Components for Unicode (ICU) libraries provide
robust and full-featured Unicode services on a wide variety of
platforms. ICU supports the most current version of the Unicode
standard, and they provide support for supplementary Unicode
characters (needed for GB 18030 repertoire support).
As computing environments become more heterogeneous, software
portability becomes more important. ICU lets you produce the same
results across all the various platforms you support, without
sacrificing performance. It offers great flexibility to extend and
customize the supplied services.

%package  -n lib%{name}-devel
Summary:  Development files for International Components for Unicode
Group:    Development/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description -n lib%{name}-devel
Includes and definitions for developing with icu.

%package -n lib%{name}-doc
Summary: Documentation for International Components for Unicode
Group:   Documentation
BuildArch: noarch

%description -n lib%{name}-doc
%{summary}.

%{!?endian: %global endian %(%{__python} -c "import sys;print (0 if sys.byteorder=='big' else 1)")}
# " this line just fixes syntax highlighting for vim that is confused by the above and continues literal

%prep
%setup -q -n %{name}

%patch0 -p0                                                                                      
%patch1 -p1

#%patch1 -p2 -R -b .icu8198.revert.icu5431.patch
#%patch2 -p1 -b .icu8800.freeserif.crash.patch
#%patch3 -p1 -b .icu7601.Indic-ccmp.patch
#%patch4 -p1 -b .gennorm2-man.patch
%patch5 -p1 -b .icuinfo-man.patch
#%ifarch armv7hl
#%patch6 -p1 -b .armv7hl-disable-tests.patch
#%endif


%build
cd source
autoconf
CFLAGS='%optflags -fno-strict-aliasing'
CXXFLAGS='%optflags -fno-strict-aliasing'
# Endian: BE=0 LE=1
%if ! 0%{?endian}
CPPFLAGS='-DU_IS_BIG_ENDIAN=1'
%endif
#rhbz856594 do not use --disable-renaming or cope with the mess
export CC='gcc' \
 %configure --with-data-packaging=library --disable-samples
#rhbz#225896
sed -i 's|-nodefaultlibs -nostdlib||' config/mh-linux
#rhbz#681941
sed -i 's|^LIBS =.*|LIBS = -L../lib -licuuc -lpthread -lm|' i18n/Makefile
sed -i 's|^LIBS =.*|LIBS = -nostdlib -L../lib -licuuc -licui18n -lc -lgcc|' io/Makefile
sed -i 's|^LIBS =.*|LIBS = -nostdlib -L../lib -licuuc -lc|' layout/Makefile
sed -i 's|^LIBS =.*|LIBS = -nostdlib -L../lib -licuuc -licule -lc|' layoutex/Makefile
sed -i 's|^LIBS =.*|LIBS = -nostdlib -L../../lib -licutu -licuuc -lc|' tools/ctestfw/Makefile
# As of ICU 52.1 the -nostdlib in tools/toolutil/Makefile results in undefined reference to `__dso_handle'
sed -i 's|^LIBS =.*|LIBS = -L../../lib -licui18n -licuuc -lpthread -lc|' tools/toolutil/Makefile
#rhbz#813484
sed -i 's| \$(docfilesdir)/installdox||' Makefile
# There is no source/doc/html/search/ directory
sed -i '/^\s\+\$(INSTALL_DATA) \$(docsrchfiles) \$(DESTDIR)\$(docdir)\/\$(docsubsrchdir)\s*$/d' Makefile
# rhbz#856594 The configure --disable-renaming and possibly other options
# result in icu/source/uconfig.h.prepend being created, include that content in
# icu/source/common/unicode/uconfig.h to propagate to consumer packages.
test -f uconfig.h.prepend && sed -e '/^#define __UCONFIG_H__/ r uconfig.h.prepend' -i common/unicode/uconfig.h

make %{?_smp_mflags}
make %{?_smp_mflags} doc

%install
rm -rf $RPM_BUILD_ROOT source/__docs
make %{?_smp_mflags} -C source install DESTDIR=$RPM_BUILD_ROOT
make %{?_smp_mflags} -C source install-doc docdir=__docs
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so.*

#Fedora's create way of multi-arch may need for future use
#(
# cd $RPM_BUILD_ROOT%{_bindir}
# mv icu-config icu-config-%{__isa_bits}
#)
#install -p -m755 -D %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/icu-config

# not installed
rm $RPM_BUILD_ROOT/usr/lib/icu/current

%check
# test to ensure that -j(X>1) didn't "break" man pages. b.f.u #2357
if grep -q @VERSION@ source/tools/*/*.8 source/tools/*/*.1 source/config/*.1; then
    exit 1
fi
make %{?_smp_mflags} -C source check

%post -n lib%{name} -p /sbin/ldconfig

%postun -n lib%{name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/derb
%{_bindir}/genbrk
%{_bindir}/gencfu
%{_bindir}/gencnval
%{_bindir}/gendict
%{_bindir}/genrb
%{_bindir}/makeconv
%{_bindir}/pkgdata
%{_bindir}/uconv
%{_sbindir}/*
%{_mandir}/man1/derb.1*
%{_mandir}/man1/gencfu.1*
%{_mandir}/man1/gencnval.1*
%{_mandir}/man1/gendict.1*
%{_mandir}/man1/genrb.1*
%{_mandir}/man1/genbrk.1*
%{_mandir}/man1/makeconv.1*
%{_mandir}/man1/pkgdata.1*
%{_mandir}/man1/uconv.1*
%{_mandir}/man8/*.8*

%files -n lib%{name}
%defattr(-,root,root,-)
%doc license.html readme.html
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%defattr(-,root,root,-)
%{_bindir}/%{name}-config*
%{_bindir}/icuinfo
%{_mandir}/man1/%{name}-config.1*
%{_mandir}/man1/icuinfo.1*
%{_includedir}/layout
%{_includedir}/unicode
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}
#%dir %{_libdir}/%{name}/current
#%{_libdir}/%{name}/current/Makefile.inc
#%{_libdir}/%{name}/current/pkgdata.inc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/install-sh
%{_datadir}/%{name}/%{version}/mkinstalldirs
%{_datadir}/%{name}/%{version}/config
%doc %{_datadir}/%{name}/%{version}/license.html

%files -n lib%{name}-doc
%defattr(-,root,root,-)
%doc license.html readme.html
%doc source/__docs/%{name}/html/*

%changelog
