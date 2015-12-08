Summary: Utility for modifying/upgrading files
Name: patch
Version: 2.7.5
Release: 0%{?dist}
License: GPLv3+
URL: http://www.gnu.org/software/patch/patch.html
Group: Development/Tools
Source: ftp://ftp.gnu.org/gnu/patch/patch-%{version}.tar.xz

#BuildRequires: ed

%description
The patch program applies diff files to originals.  The diff command
is used to compare an original to a changed file.  Diff lists the
changes made to the file.  A person who has the original file can then
use the patch command with the diff file to add the changes to their
original file (patching the file).

Patch should be installed because it is a common way of upgrading
applications.

%prep
%setup -q

%build
CFLAGS=`echo $CFLAGS|sed -e 's|-fstack-protector||g'`

./configure \
	--prefix=/usr \
	--disable-silent-rules \
	--mandir=/usr/share/man

make %{?_smp_mflags}

#%check
#make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*

%changelog
