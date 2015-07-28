Name:		tar	
Version:	1.28
Release:	1%{?dist}
Summary:	A GNU file archiving program

Group:		Applications/Archiving
License:	GPLv3+	
URL:		http://www.gnu.org/software/tar/	
Source0:	ftp://ftp.gnu.org/gnu/tar/%{name}-%{version}.tar.xz

#BuildRequires: autoconf automake texinfo gettext libacl-devel rsh
#Requires:	

%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.

If you want to use tar for remote backups, you also need to install
the rmt package on the remote box.

%prep
%setup -q


%build
# For now
FORCE_UNSAFE_CONFIGURE=1 \
./configure \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--with-lzma="xz --format=lzma"

make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -rf %{buildroot}/usr/lib/charset.alias

mkdir %{buildroot}/bin
mv %{buildroot}/usr/bin/tar %{buildroot}/bin/
ln -s /bin/tar %{buildroot}/usr/bin/tar

%files
/bin/tar
/usr/libexec/rmt
/usr/bin/tar

%changelog
