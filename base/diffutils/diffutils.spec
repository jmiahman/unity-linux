Summary: A GNU collection of diff utilities
Name: diffutils
Version: 3.3
Release: 1%{?dist}
Group: Applications/Text
URL: http://www.gnu.org/software/diffutils/diffutils.html
Source: ftp://ftp.gnu.org/gnu/diffutils/diffutils-%{version}.tar.xz
License: GPLv3+

%description
Diffutils includes four utilities: diff, cmp, diff3 and sdiff. Diff
compares two files and shows the differences, line by line.  The cmp
command shows the offset and line numbers where two files differ, or
cmp can show the characters that differ between the two files.  The
diff3 command shows the differences between three files.  Diff3 can be
used when two people have made independent changes to a common
original; diff3 can produce a merged file that contains both sets of
changes and warnings about conflicts.  The sdiff command can be used
to merge two files interactively.

Install diffutils if you need to compare text files.

%prep
%setup -q

%build
./configure \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info

make 

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%check
# Disable update-copyright gnulib test (bug #1239428).
#>gnulib-tests/test-update-copyright.sh
#make check

%files
/usr/bin/*

%changelog
