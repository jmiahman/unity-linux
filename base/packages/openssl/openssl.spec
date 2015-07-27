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

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1 
%patch3 -p1 
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
export LDFLAGS="$LDFLAGS -Wa,--noexecstack"
./config --prefix=/usr \
	--libdir=lib \
	--openssldir=/etc/ssl \
	shared zlib enable-montasm enable-md2 \
	%ifarch x86_64
	enable-ec_nistp_64_gcc_128 \
	%endif
	-DOPENSSL_NO_BUF_FREELISTS

%make 
%make build-shared


%install
rm -rf %{buildroot}
make INSTALL_PREFIX=%{buildroot} MANDIR=/usr/share/man install

mkdir %{buildroot}/lib
cd %{buildroot}/lib
ln -s ../usr/lib/libcrypto.so.1.0.0 libcrypto.so.1.0.0
ln -s ../usr/lib/libssl.so.1.0.0 libssl.so.1.0.0
cd ..
ln -sf openssl %{buildroot}/usr/bin/c_rehash

%files
%doc
/etc/ssl/openssl.cnf
/etc/ssl/misc/CA.sh
/etc/ssl/misc/CA.pl
/etc/ssl/misc/c_issuer
/etc/ssl/misc/c_name
/etc/ssl/misc/c_hash
/etc/ssl/misc/tsget
/etc/ssl/misc/c_info
/usr/bin/openssl
/usr/bin/c_rehash

%files -n libcrypto
/lib/libcrypto.so.1.0.0
/usr/lib/libcrypto.so.1.0.0
/usr/lib/engines/libubsec.so
/usr/lib/engines/libatalla.so
/usr/lib/engines/libcapi.so
/usr/lib/engines/libgost.so
/usr/lib/engines/libcswift.so
/usr/lib/engines/libchil.so
/usr/lib/engines/libgmp.so
/usr/lib/engines/libnuron.so
/usr/lib/engines/lib4758cca.so
/usr/lib/engines/libsureware.so
/usr/lib/engines/libpadlock.so
/usr/lib/engines/libaep.so

%files -n libssl
/lib/libssl.so.1.0.0
/usr/lib/libssl.so.1.0.0

%changelog
