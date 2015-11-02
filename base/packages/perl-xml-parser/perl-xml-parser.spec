%define         perl_vendorarch %{_libdir}/perl5/vendor_perl

Name:           perl-xml-parser
Version:        2.44
Release:        1%{?dist}
Summary:        Perl module for parsing XML documents

Group:          Development/Libraries
License:        GPL+ or Artistic
Url:            http://search.cpan.org/dist/XML-Parser/
Source0:        http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/XML-Parser-%{version}.tar.gz

Requires:       perl

%description
This module provides ways to parse XML documents. It is built on top
of XML::Parser::Expat, which is a lower level interface to James
Clark's expat library. Each call to one of the parsing methods creates
a new instance of XML::Parser::Expat which is then used to parse the
document. Expat options may be provided when the XML::Parser object is
created. These options are then passed on to the Expat object on each
parse call. They can also be given as extra arguments to the parse
methods, in which case they override options given at XML::Parser
creation time.

%prep
%setup -q -n XML-Parser-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}

%check
make test

%files
%doc README Changes samples/
%{perl_vendorarch}/XML/
%{perl_vendorarch}/auto/XML/
%{_mandir}/man3/*.3*

%changelog
