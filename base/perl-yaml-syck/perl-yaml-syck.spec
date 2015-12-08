%define 	perl_vendorarch %{_libdir}/perl5/vendor_perl
%define		pdir	YAML
%define		pnam	Syck
Summary:	YAML::Syck - fast, lightweight YAML loader and dumper
Name:		perl-yaml-syck
Version:	1.27
Release:	1%{?dist}
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/YAML/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/YAML-Syck/

BuildRequires:	perl

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.

NOTE: If you are working with other language's YAML/Syck bindings
(such as Ruby), please set $YAML::Syck::ImplicitTyping to 1 before
calling the Load/Dump functions. The default setting is for preserving
backward-compatibility with YAML.pm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=%{buildroot}

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/YAML/Syck.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/YAML
%{perl_vendorarch}/YAML/*.pm
%dir %{perl_vendorarch}/JSON
%{perl_vendorarch}/JSON/Syck.pm
%dir %{perl_vendorarch}/YAML/Dumper
%{perl_vendorarch}/YAML/Dumper/Syck.pm
%dir %{perl_vendorarch}/YAML/Loader
%{perl_vendorarch}/YAML/Loader/Syck.pm
%dir %{perl_vendorarch}/auto/YAML
%dir %{perl_vendorarch}/auto/YAML/Syck
%attr(755,root,root) %{perl_vendorarch}/auto/YAML/Syck/*.so
%{_mandir}/man3/*
