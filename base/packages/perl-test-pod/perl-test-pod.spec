%define		perl_vendorlib %{_datadir}/perl5/vendor_perl
%define		pdir	Test
%define		pnam	Pod
Summary:	Test::Pod Perl module - check for POD errors in files
Name:		perl-test-pod
Version:	1.48
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/Test-Pod/
BuildRequires:	perl
BuildArch:	noarch

%description
Check POD files for errors or warnings in a test file, using
Pod::Checker to do the heavy lifting.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor 
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Pod.pm
%{_mandir}/man3/Test::Pod.3pm*
