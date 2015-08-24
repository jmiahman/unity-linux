%define _target_platform %{_arch}-unity-linux-musl

Name:		libarchive	
Version:	3.1.2
Release:	1%{?dist}
Summary:	A library for handling streaming archive formats

Group:		System Environment/Libraries	
License:	BSD
URL:		http://libarchive.org
Source0:	http://www.libarchive.org/downloads/libarchive-%{version}.tar.gz

BuildRequires:	zlib-devel, bzip2-devel, xz-devel, libacl-devel, openssl-devel, expat-devel
#Requires:	

Patch0:		CVE-2013-0211.patch
Patch1:		CVE-2015-2304.patch

%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     bsdtar
Summary:        Manipulate tape archives
Group:          Applications/File
Requires:       %{name} = %{version}-%{release}

%description -n bsdtar
The bsdtar package contains standalone bsdtar utility split off regular
libarchive packages.


%package -n     bsdcpio
Summary:        Copy files to and from archives
Group:          Applications/File
Requires:       %{name} = %{version}-%{release}

%description -n bsdcpio
The bsdcpio package contains standalone bsdcpio utility split off regular
libarchive packages.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--without-xml2 \

make

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/usr/lib/*.la


%files
%defattr(-,root,root,-)
#%license COPYING
#%doc README NEWS
%{_libdir}/libarchive.so.13*
#%{_mandir}/*/cpio.*
#%{_mandir}/*/mtree.*
#%{_mandir}/*/tar.*

%files devel
%defattr(-,root,root,-)
#%doc
%{_includedir}/*.h
#%{_mandir}/*/archive*
#%{_mandir}/*/libarchive*
%{_libdir}/libarchive.so
%{_libdir}/pkgconfig/libarchive.pc

%files -n bsdtar
%defattr(-,root,root,-)
#%license COPYING
#%doc README NEWS
%{_bindir}/bsdtar
#%{_mandir}/*/bsdtar*

%files -n bsdcpio
%defattr(-,root,root,-)
#%license COPYING
#%doc README NEWS
%{_bindir}/bsdcpio
#%{_mandir}/*/bsdcpio*


%changelog
