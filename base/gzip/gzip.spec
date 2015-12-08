Name:		gzip	
Version:	1.6
Release:	1%{?dist}
Summary:	The GNU data compression program	

Group:		Applications/File
License:	GPLv3+ and GFDL	
URL:		http://www.gzip.org/		
Source0:	http://ftp.gnu.org/gnu/gzip/gzip-%{version}.tar.gz

#BuildRequires:	
#Requires:	

%description
The gzip package contains the popular GNU gzip data compression
program. Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a
very commonly used data compression program.

%prep
%setup -q


%build
export DEFS="NO_ASM"
./configure \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}/usr/lib/charset.alias

mkdir -p %{buildroot}/bin
mv %{buildroot}/usr/bin/gzip %{buildroot}/usr/bin/gunzip %{buildroot}/bin/
ln -s /bin/gzip %{buildroot}/usr/bin/gzip
ln -s /bin/gunzip %{buildroot}/usr/bin/gunzip
ln -sf /bin/gunzip %{buildroot}/usr/bin/uncompress

%files
/bin/gzip
/bin/gunzip
/usr/bin/zmore
/usr/bin/zcmp
/usr/bin/uncompress
/usr/bin/zless
/usr/bin/zgrep
/usr/bin/zforce
/usr/bin/gzip
/usr/bin/zegrep
/usr/bin/gunzip
/usr/bin/zfgrep
/usr/bin/zdiff
/usr/bin/gzexe
/usr/bin/znew
/usr/bin/zcat

%changelog
