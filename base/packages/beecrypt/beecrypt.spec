Name:		beecrypt	
Version:	4.2.1
Release:	1%{?dist}
Summary:	A general-purpose cryptography library

Group:		System Environment/Libraries
License:	LGPL2+
URL:		http://beecrypt.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:	http://repository.timesys.com/buildsources/b/beecrypt/beecrypt-4.2.1/beecrypt-4.2.1.tar.gz	

#BuildRequires:	
#Requires:	

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography
toolkit. Includes entropy sources, random generators, block ciphers, hash
functions, message authentication codes, multiprecision integer routines
and public key primitives.

%prep
%setup -q

%build
LIBS=-lgomp \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--enable-threads \
	--enable-shared \
	--without-java \
	--without-python \
	--with-cplusplus=no


make libaltdir=/usr/lib


%install
make libaltdir=/usr/lib DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la

%files
/usr/lib/libbeecrypt.so.7.0.0
/usr/lib/libbeecrypt.so.7

%changelog
