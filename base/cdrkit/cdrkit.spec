Name:		cdrkit	
Version:	1.1.11
Release:	1%{?dist}
Summary:	A collection of CD/DVD utilities

Group:		Applications/System
License:	GPLv2
URL:		http://cdrkit.org/
Source0:	http://ftp.cc.uoc.gr/mirrors/linux/frugalware/frugalware-current/source/apps/cdrkit/cdrkit-%{version}.tar.gz

BuildRequires:	libcap-devel, bzip2-devel, zlib-devel
Requires:	file, bzip2

%description
cdrkit is a collection of CD/DVD utilities.

%prep
%setup -q


%build
sed -i -e "s!define HAVE_RCMD 1!undef HAVE_RCMD!g" include/xconfig.h.in
export CFLAGS="$CFLAGS -D__THROW=''"
make

%install
make PREFIX=%{buildroot}/usr install
cd %{buildroot}/usr/bin
ln -s wodim cdrecord
ln -s readom readcd
ln -s genisoimage mkisofs
ln -s genisoimage mkhybrid
ln -s icedax cdda2wav
cd %{buildroot}/usr/share/man/man1
ln -s wodim.1 cdrecord.1
ln -s readom.1 readcd.1
ln -s genisoimage.1 mkisofs.1
ln -s genisoimage.1 mkhybrid.1
ln -s icedax.1 cdda2wav.1

%files
/usr/sbin/*
/usr/bin/*

%changelog

