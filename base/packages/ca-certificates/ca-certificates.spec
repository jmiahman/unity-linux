Name:		ca-certificates
Version:	20150916
Release:	1%{?dist}
Summary:	A CA root certificate bundle

Group:		System Environment/Base
License:	GPL-v2+ and MPL-2.0
URL:		http://www.linuxfromscratch.org/blfs/view/svn/postlfs/cacerts.html
Source0:	http://anduin.linuxfromscratch.org/sources/other/certdata.txt
Source1:	make-ca
Source2:	make-cert
Source3:	remove-expired-certs



BuildRequires:	perl
Requires:	openssl perl

BuildArch: noarch

%description
This package includes PEM files of CA certificates to allow SSL-based applications to check 
for the authenticity of SSL connections. It includes, among others, certificate authorities 
used by the Debian infrastructure and those shipped with Mozilla's browsers.

%prep
#%setup -q


%build
#nother here

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -d %{buildroot}/usr/bin
install -m755 %{SOURCE1} %{buildroot}/usr/bin
install -m755 %{SOURCE2} %{buildroot}/usr/bin
install -m755 %{SOURCE3} %{buildroot}/usr/bin

%post
cp %{SOURCE0} .
make-ca
remove-expired-certs certs
install -d /etc/ssl/certs
cp -v certs/*.pem /etc/ssl/certs
c_rehash
install BLFS-ca-bundle*.crt /etc/ssl/ca-bundle.crt
ln -sfv ../ca-bundle.crt /etc/ssl/certs/ca-certificates.crt

%files
/usr/bin/*

%changelog

