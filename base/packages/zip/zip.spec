Summary: A file compression and packaging utility compatible with PKZIP
Name: zip
Version: 3.0
Release: 1%{?dist}
License: BSD
Group: Applications/Archiving
Source: http://downloads.sourceforge.net/infozip/zip30.tar.gz
URL: http://www.info-zip.org/Zip.html

Patch1: 10-zip-3.0-build.patch
Patch2: 20-zip-3.0-exec-stack.patch
Patch3: 30-zip-3.0-pic.patch

BuildRequires: bzip2-devel

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%package docs
Summary:  Doc files for zip
Requires: %{name} = %{version}

%description docs
Documentation files for zip

%prep
%setup -q -n zip30

%patch1 -p0 -b .build
%patch2 -p0 -b .exec-stack
%patch3 -p0 -b .pic

%build
make -f unix/Makefile prefix=%{_prefix} "CFLAGS_NOOPT=-I. -DUNIX $RPM_OPT_FLAGS" generic_gcc  %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BULD_ROOT%{_mandir}/man1

make -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} \
        MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install

%files
%doc README CHANGES TODO WHATSNEW WHERE LICENSE README.CR
%doc proginfo/algorith.txt
%{_bindir}/zipnote
%{_bindir}/zipsplit
%{_bindir}/zip
%{_bindir}/zipcloak

%files docs
%{_mandir}/man1/zip.1*                                                                            
%{_mandir}/man1/zipcloak.1*                                                                       
%{_mandir}/man1/zipnote.1*                               
%{_mandir}/man1/zipsplit.1*

%changelog
