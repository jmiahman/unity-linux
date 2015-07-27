Name:		xz	
Version:	5.2.1
Release:	1%{?dist}
Summary:	LZMA compression utilities

Group:		Applications/File
License:	GPLv2+ and Public Domain
URL:		http://tukaani.org/%{name}/
Source0:	http://tukaani.org/%{name}/%{name}-%{version}.tar.xz

#BuildRequires:	
#Requires:	

%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as
part of 7-Zip. It provides high compression ratio while keeping the
decompression speed fast.

%package 	libs
Summary:	Libraries for decoding LZMA compression
Group:		System Environment/Libraries
License:	Public Domain

%description 	libs
Libraries for decoding files compressed with LZMA or XZ utils.


%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--disable-rpath \
	--disable-werror \

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/lzdiff
/usr/bin/xzegrep
/usr/bin/lzless
/usr/bin/xzdiff
/usr/bin/lzgrep
/usr/bin/xzless
/usr/bin/xzmore
/usr/bin/lzcat
/usr/bin/xz
/usr/bin/xzfgrep
/usr/bin/lzcmp
/usr/bin/unlzma
/usr/bin/lzfgrep
/usr/bin/lzmainfo
/usr/bin/lzegrep
/usr/bin/unxz
/usr/bin/xzgrep
/usr/bin/xzcmp
/usr/bin/lzmadec
/usr/bin/xzcat
/usr/bin/xzdec
/usr/bin/lzma
/usr/bin/lzmore

%files libs
/usr/lib/liblzma.so.5
/usr/lib/liblzma.so.5.2.1

%changelog
