%define __find_requires %{nil}
%define _sysconfdir /etc

Name:		openssl	
Version:	1.0.2d	
Release:	1%{?dist}
Summary:	Utilities from the general purpose cryptography library with TLS implementation

Group:		System Environment/Libraries
License:	OpenSSL
URL:		http://www.openssl.org
Source0:	http://www.openssl.org/source/%{name}-%{version}.tar.gz	

Patch0:		0001-fix-manpages.patch
Patch1:		0002-busybox-basename.patch
Patch2:		0003-use-termios.patch
Patch3:		0004-fix-default-ca-path-for-apps.patch
Patch4:		0005-fix-parallel-build.patch
Patch5:		0006-add-ircv3-tls-3.1-extension-support-to-s_client.patch
Patch6:		0007-reimplement-c_rehash-in-C.patch
Patch7:		0008-maintain-abi-compat-with-no-freelist-and-regular-bui.patch
Patch8:		0009-no-rpath.patch
Patch9:		0010-ssl-env-zlib.patch
Patch10:	1001-crypto-hmac-support-EVP_MD_CTX_FLAG_ONESHOT-and-set-.patch
Patch11:	1002-backport-changes-from-upstream-padlock-module.patch
Patch12:	1003-engines-e_padlock-implement-sha1-sha224-sha256-accel.patch
Patch13:	1004-crypto-engine-autoload-padlock-dynamic-engine.patch

#BuildRequires:	
#Requires:	

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.


%package -n libcrypto
Summary: Crypto library from openssl
Group: System Environment/Libraries

%description -n libcrypto
Crypto Library from OpenSSL

%package -n libssl
Summary: Crypto library from openssl
Group: System Environment/Libraries

%description -n libssl
SSL Shared Libraries

%package devel
Summary: Files for development of applications which will use OpenSSL
Group: Development/Libraries
Requires: libssl = %{version}

%description devel
OpenSSL is a toolkit for supporting cryptography. The openssl-devel
package contains include files needed to develop applications which
support various cryptographic algorithms and protocols.

%prep
%setup -q

%patch0 -p1 -b .test
%patch1 -p1
%patch2 -p1 
#%patch3 -p1 
%patch4 -p1 
%patch5 -p1 
%patch6 -p1 
%patch7 -p1 
%patch8 -p1 
%patch9 -p1 
%patch10 -p1 
%patch11 -p1 
%patch12 -p1 
%patch13 -p1 

%build
rm -rf %{_builddir}/apps/progs.h 
LDFLAGS=" -Wa,--noexecstack" \
./config \
	--prefix=/usr \
	--libdir=lib \
	--openssldir=%{_sysconfdir}/ssl \
	shared zlib enable-montasm enable-md2 \
	%ifarch x86_64
	enable-ec_nistp_64_gcc_128 \
	%endif
	-DOPENSSL_NO_BUF_FREELISTS

make depend
make 
make build-shared


%install
rm -rf %{buildroot}
make INSTALL_PREFIX=%{buildroot} MANDIR=/usr/share/man install

install -m755 %{_builddir}/%{name}-%{version}/tools/c_rehash %{buildroot}/usr/bin/
mkdir %{buildroot}/lib
mv %{buildroot}/usr/lib/libcrypto.so.1.0.0 %{buildroot}/lib/libcrypto.so.1.0.0
mv %{buildroot}/usr/lib/libssl.so.1.0.0 %{buildroot}/lib/libssl.so.1.0.0
cd %{buildroot}/
%__ln -sf /lib/libcrypto.so.1.0.0 %{buildroot}/usr/lib/libcrypto.so.1.0.0
%__ln -sf /lib/libssl.so.1.0.0 %{buildroot}/usr/lib/libssl.so.1.0.0



%files
%{_bindir}/*
%dir %{_sysconfdir}/ssl/certs
%{_sysconfdir}/ssl/openssl.cnf
%{_sysconfdir}/ssl/misc/CA.sh
%{_sysconfdir}/ssl/misc/CA.pl
%{_sysconfdir}/ssl/misc/c_issuer
%{_sysconfdir}/ssl/misc/c_name
%{_sysconfdir}/ssl/misc/c_hash
%{_sysconfdir}/ssl/misc/tsget
%{_sysconfdir}/ssl/misc/c_info
%dir %{_sysconfdir}/ssl
%dir %{_sysconfdir}/ssl/misc


%files -n libcrypto
/lib/libcrypto.so.1.0.0
%{_libdir}/libcrypto.so.1.0.0
%{_libdir}/engines/libubsec.so
%{_libdir}/engines/libatalla.so
%{_libdir}/engines/libcapi.so
%{_libdir}/engines/libgost.so
%{_libdir}/engines/libcswift.so
%{_libdir}/engines/libchil.so
%{_libdir}/engines/libgmp.so
%{_libdir}/engines/libnuron.so
%{_libdir}/engines/lib4758cca.so
%{_libdir}/engines/libsureware.so
%{_libdir}/engines/libpadlock.so
%{_libdir}/engines/libaep.so
%dir %{_libdir}/engines

%files -n libssl
/lib/libssl.so.1.0.0
%{_libdir}/libssl.so.1.0.0

%files devel
%dir /usr/include/openssl/
%{_prefix}/include/openssl/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a

%changelog
