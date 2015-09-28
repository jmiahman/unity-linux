Name:           perl-Net-SMTP-SSL
Version:        1.03
Release:        1%{?dist}
Summary:        SSL support for Net::SMTP
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Net-SMTP-SSL/
Source0:        http://www.cpan.org/modules/by-module/Net/Net-SMTP-SSL-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Net::SMTP)
# Tests only
BuildRequires:  perl(Test::More) >= 0.47
Requires: perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
Implements the same API as Net::SMTP, but uses IO::Socket::SSL for its
network operations.

%prep
%setup -q -n Net-SMTP-SSL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/SMTP/
%{perl_vendorlib}/Net/SMTP/SSL.pm
%{_mandir}/man3/Net::SMTP::SSL.3*

%changelog
* Sun Jun 21 2015 Petr Šabata <contyk@redhat.com> - 1.03-1
- 1.03 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-2
- Perl 5.22 rebuild

* Fri Mar 27 2015 Petr Šabata <contyk@redhat.com> - 1.02-1
- 1.02 bump
- Modernize the spec

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-18
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.01-15
- Perl 5.18 rebuild

* Thu Jul 18 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.01-14
- REbuilt to perl 5.18

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Petr Pisar <ppisar@redhat.com> - 1.01-12
- Modernize spec file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.01-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.01-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-6
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.01-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 15 2008 Dan Nicholson <dbn.lists@gmail.com> 1.01-1
- Initial release
