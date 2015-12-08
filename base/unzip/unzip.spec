Summary: A utility for unpacking zip files
Name: unzip
Version: 6.0
Release: 1%{?dist}
License: BSD
Group: Applications/Archiving
Source0: http://downloads.sourceforge.net/infozip/unzip60.tar.gz
# Not sent to upstream.
Patch1: unzip-6.0-bzip2-configure.patch
# Upstream plans to do this in zip (hopefully also in unzip).
Patch2: unzip-6.0-exec-shield.patch
# Upstream plans to do similar thing.
Patch3: unzip-6.0-close.patch
# Details in rhbz#532380.
# Reported to upstream: http://www.info-zip.org/board/board.pl?m-1259575993/
Patch4: unzip-6.0-attribs-overflow.patch
# Not sent to upstream, as it's Fedora/RHEL specific.
# Modify the configure script not to request the strip of binaries.
Patch5: unzip-6.0-nostrip.patch
Patch6: unzip-6.0-manpage-fix.patch
# Update match.c with recmatch() from zip 3.0's util.c
# This also resolves the license issue in that old function.
# Original came from here: https://projects.parabolagnulinux.org/abslibre.git/plain/libre/unzip-libre/match.patch
Patch7: unzip-6.0-fix-recmatch.patch
# Update process.c
Patch8: unzip-6.0-symlink.patch
# change using of macro "case_map" by "to_up"
Patch9: unzip-6.0-caseinsensitive.patch
# downstream fix for "-Werror=format-security"
# upstream doesn't want hear about this option again
Patch10: unzip-6.0-format-secure.patch
Patch11: unzip-6.0-valgrind.patch
Patch12: unzip-6.0-x-option.patch
Patch13: unzip-6.0-overflow.patch
Patch14: unzip-6.0-cve-2014-8139.patch
Patch15: unzip-6.0-cve-2014-8140.patch
Patch16: unzip-6.0-cve-2014-8141.patch
Patch17: unzip-6.0-overflow-long-fsize.patch
# Fix heap overflow and infinite loop when invalid input is given (#1260947)
Patch18: unzip-6.0-heap-overflow-infloop.patch

# support non-{latin,unicode} encoding
Patch19: unzip-6.0-alt-iconv-utf8.patch
Patch20: unzip-6.0-alt-iconv-utf8-print.patch

URL: http://www.info-zip.org/UnZip.html
BuildRequires:  bzip2-devel

%description
The unzip utility is used to list, test, or extract files from a zip
archive.  Zip archives are commonly found on MS-DOS systems.  The zip
utility, included in the zip package, creates zip archives.  Zip and
unzip are both compatible with archives created by PKWARE(R)'s PKZIP
for MS-DOS, but the programs' options and default behaviors do differ
in some respects.

Install the unzip package if you need to list, test or extract files from
a zip archive.

%prep
%setup -q -n unzip60
%patch1 -p1 -b .bzip2-configure
%patch2 -p1 -b .exec-shield
%patch3 -p1 -b .close
%patch4 -p1 -b .attribs-overflow
%patch5 -p1 -b .nostrip
%patch6 -p1 -b .manpage-fix
%patch7 -p1 -b .recmatch
%patch8 -p1 -b .symlink
%patch9 -p1 -b .caseinsensitive
%patch10 -p1 -b .format-secure
%patch11 -p1 -b .valgrind
%patch12 -p1 -b .x-option
%patch13 -p1 -b .overflow
%patch14 -p1 -b .cve-2014-8139
%patch15 -p1 -b .cve-2014-8140
%patch16 -p1 -b .cve-2014-8141
%patch17 -p1 -b .overflow-long-fsize
%patch18 -p1 -b .heap-overflow-infloop
%patch19 -p1 -b .utf
%patch20 -p1 -b .utf-print


%build
# IZ_HAVE_UXUIDGID is needed for right functionality of unzip -X
# NOMEMCPY solve problem with memory overlapping - decomression is slowly,
# but successfull.
make -f unix/Makefile CF_NOOPT="-I. -DUNIX $RPM_OPT_FLAGS -DNOMEMCPY -DIZ_HAVE_UXUIDGID" generic_gcc %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1 INSTALL="cp -p" install

%files
%defattr(-,root,root)
%doc README BUGS LICENSE
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Wed Dec 02 2015 JMiahMan <JMiahMan@unity-linux.org> - 6.0-1
- Initial build for Unity-Linux
