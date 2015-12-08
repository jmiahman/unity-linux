%define perl_vendorlib %{_datadir}/perl5/vendor_perl
%define perl_vendorarch %{_libdir}/perl5/vendor_perl


Name:		perl-IO-Socket-SSL
Version:	2.020
Release:	1%{?dist}
Summary:	Perl library for transparent SSL
Group:		Development/Libraries
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/IO-Socket-SSL/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SU/SULLR/IO-Socket-SSL-%{version}.tar.gz
Patch0:		IO-Socket-SSL-2.020-use-system-default-cipher-list.patch
Patch1:		IO-Socket-SSL-2.020-use-system-default-SSL-version.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl
BuildRequires:	perl-ExtUtils-MakeMaker
# Module Runtime
BuildRequires:	openssl >= 0.9.8
BuildRequires:	perl-Net-SSLeay >= 1.46
# Runtime
Requires:	openssl >= 0.9.8

%description
This module is a true drop-in replacement for IO::Socket::INET that
uses SSL to encrypt data before it is transferred to a remote server
or client. IO::Socket::SSL supports all the extra features that one
needs to write a full-featured SSL client or server application:
multiple SSL contexts, cipher selection, certificate verification, and
SSL version selection. As an extra bonus, it works perfectly with
mod_perl.

%prep
%setup -q -n IO-Socket-SSL-%{version}

# Use system-wide default cipher list to support use of system-wide
# crypto policy (#1076390, #1127577, CPAN RT#97816)
# https://fedoraproject.org/wiki/Changes/CryptoPolicy
%patch0

# Use system-default SSL version too
%patch1

%build
NO_NETWORK_TESTING=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

%check
make test

%clean
rm -rf %{buildroot}

%files
%doc BUGS Changes README docs/ certs/ example/
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Socket/
%doc %{perl_vendorlib}/IO/Socket/SSL.pod
%{perl_vendorlib}/IO/Socket/SSL.pm
%{perl_vendorlib}/IO/Socket/SSL/
%{_mandir}/man3/IO::Socket::SSL.3*
%{_mandir}/man3/IO::Socket::SSL::Intercept.3*
%{_mandir}/man3/IO::Socket::SSL::PublicSuffix.3*
%{_mandir}/man3/IO::Socket::SSL::Utils.3*

%changelog
