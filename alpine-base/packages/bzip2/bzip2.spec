Name:		bzip2	
Version:	1.0.6
Release:	1%{?dist}
Summary:	A file compression utility

Group:		Applications/File
License:	BSD
URL:		http://sources.redhat.com/bzip2
Source0:	http://www.bzip.org/%{version}/%{name}-%{version}.tar.gz

Patch0:		bzip2-1.0.4-makefile-CFLAGS.patch
Patch1:		bzip2-1.0.6-saneso.patch
Patch2:		bzip2-1.0.4-man-links.patch
Patch3:		bzip2-1.0.2-progress.patch
Patch4:		bzip2-1.0.3-no-test.patch
Patch5:		bzip2-1.0.4-POSIX-shell.patch

#BuildRequires:	
#Requires:	

%description
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities
of the best techniques available.  However, bzip2 has the added benefit
of being approximately two times faster at compression and six times
faster at decompression than those techniques.  Bzip2 is not the
fastest compression utility, but it does strike a balance between speed
and compression capability.

Install bzip2 if you need a compression utility.

%package devel
Summary: Libraries and header files for apps which will use bzip2
Group: Development/Libraries

%description devel

Header files and a library of bzip2 functions, for developing apps
which will use the library.


%prep
%setup -q

%patch0 -p1 -b	.makefile-CFLAGS
%patch1 -p1 -b  .saneso
%patch2 -p1 -b  .man-links
%patch3 -p1 -b  .progress
%patch4 -p1 -b  .no-test
%patch5 -p1 -b  .POSIX-shell

sed -i \
	-e 's:\$(PREFIX)/man:\$(PREFIX)/share/man:g' \
	-e 's:ln -s -f $(PREFIX)/bin/:ln -s :' \
Makefile

sed -i \
	-e "s:1\.0\.4:%{version}:" \
	bzip2.1 bzip2.txt Makefile-libbz2_so manual.*

%build
make -f Makefile-libbz2_so all
make all

%install
make PREFIX=%{buildroot}/usr install
install -D libbz2.so.%{version} %{buildroot}/usr/lib/libbz2.so.%{version}
ln -s libbz2.so.%{version} %{buildroot}/usr/lib/libbz2.so
ln -s libbz2.so.%{version} %{buildroot}/usr/lib/libbz2.so.1

%files
/usr/bin/bzgrep
/usr/bin/bzdiff
/usr/bin/bzmore
/usr/bin/bunzip2
/usr/bin/bzegrep
/usr/bin/bzip2
/usr/bin/bzcmp
/usr/bin/bzless
/usr/bin/bzfgrep
/usr/bin/bzip2recover
/usr/bin/bzcat

%files devel
/usr/lib/libbz2.so
/usr/lib/libbz2.a
/usr/include/bzlib.h

%changelog
