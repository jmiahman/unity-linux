%define _target_platform %{_arch}-unity-linux-musl

Name:		curl		
Version:	7.44.0
Release:	1%{?dist}
Summary:	A utility for getting files from remote servers (FTP, HTTP, and others)

Group:		Applications/Internet
License:	MIT
URL:		http://curl.haxx.se/
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.lzma

BuildRequires:	zlib-devel, openssl-devel, libssh2-devel	
Requires:	ca-certificates
Requires:	libcurl  = %{version}-%{release}

%description
curl is a command line tool for transferring data with URL syntax, supporting
FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
SMTP, POP3 and RTSP.  curl supports SSL certificates, HTTP POST, HTTP PUT, FTP
uploading, HTTP form based upload, proxies, cookies, user+password
authentication (Basic, Digest, NTLM, Negotiate, kerberos...), file transfer
resume, proxy tunneling and a busload of other useful tricks. 

%package -n libcurl
Summary: A library for getting files from web servers
Group: Development/Libraries
Requires: libssh2

%description -n libcurl
libcurl is a free and easy-to-use client-side URL transfer library, supporting
FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
SMTP, POP3 and RTSP. libcurl supports SSL certificates, HTTP POST, HTTP PUT,
FTP uploading, HTTP form based upload, proxies, cookies, user+password
authentication (Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer
resume, http proxy tunneling and more.

%package -n libcurl-devel
Summary: Files needed for building applications with libcurl
Group: Development/Libraries
Requires: libcurl = %{version}-%{release}
Provides: curl-devel = %{version}-%{release}

%description -n libcurl-devel
The libcurl-devel package includes header files and libraries necessary for
developing programs which use the libcurl library. It contains the API
documentation of the library, too.



%prep
%setup -q


%build

./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--without-libidn \
	--enable-ipv6 \
	--disable-ldap \

make

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libcurl -p /sbin/ldconfig

%postun -n libcurl -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
#%doc CHANGES README*
#%doc docs/BUGS docs/FAQ docs/FEATURES
#%doc docs/MANUAL docs/RESOURCES
#%doc docs/TheArtOfHttpScripting docs/TODO
%{_bindir}/curl
#%{_mandir}/man1/curl.1*

%files -n libcurl
%defattr(-,root,root,-)
#%license COPYING
%{_libdir}/libcurl.so.*

%files -n libcurl-devel
%defattr(-,root,root,-)
#%doc docs/examples/*.c docs/examples/Makefile.example docs/INTERNALS
#%doc docs/CONTRIBUTE docs/libcurl/ABI
%{_bindir}/curl-config*
%{_includedir}/curl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#%{_mandir}/man1/curl-config.1*
#%{_mandir}/man3/*
%{_datadir}/aclocal/libcurl.m4

%changelog

