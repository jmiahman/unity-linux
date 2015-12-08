Name:		wget	
Version:	1.16.3
Release:	1%{?dist}
Summary:	A utility for retrieving files using the HTTP or FTP protocols

Group:		Applications/Internet
License:	GPLv3+
URL:		http://www.gnu.org/software/wget/
Source0:	ftp://ftp.gnu.org/gnu/wget/wget-%{version}.tar.xz

#BuildRequires:	
#Requires:	

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you are logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--with-ssl=openssl \
	--disable-nls

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

%files
/etc/wgetrc
/usr/bin/wget

%changelog
