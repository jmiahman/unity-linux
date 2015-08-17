Name:		file	
Version:	5.24
Release:	1%{?dist}
Summary:	File type identification utility

Group: 		Applications/File
License:	BSD
URL:		http://www.darwinsys.com/file/
Source0:	http://fossies.org/linux/misc/%{name}-%{version}.tar.gz

#BuildRequires:	
#Requires:	

%description
The file command is used to identify a particular file according to the
type of data contained by the file.  File can identify many different
file types, including ELF binaries, system libraries, RPM packages, and
different graphics formats.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--datadir=/usr/share \


make %{?_smp_mflags}
make tests

%install
%make_install
rm %{buildroot}/usr/lib/*.la

%files
/usr/bin/file
/usr/lib/libmagic.so.1.0.0
/usr/lib/libmagic.so.1
%dir /usr/share/misc/
/usr/share/misc/magic.mgc

%changelog
