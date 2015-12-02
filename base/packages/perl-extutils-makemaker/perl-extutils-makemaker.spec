%define perl_vendorlib %{_datadir}/perl5/vendor_perl
%define perl_vendorarch %{_libdir}/perl5/vendor_perl


%global cpan_name ExtUtils-MakeMaker
%global cpan_lname extutils-makemaker
%global cpan_version 7.10

Name:           perl-%{cpan_lname}
Version:        %(echo '%{cpan_version}' | tr _ .)
Release:        1%{?dist}
Summary:        Create a module Makefile
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/%{cpan_name}/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{cpan_version}.tar.gz
# Do not set RPATH to perl shared-library modules by default. Bug #773622.
# This is copy from `perl' package. This is distributor extension.
Patch0:         %{cpan_name}-7.08-USE_MM_LD_RUN_PATH.patch
# Link to libperl.so explicitly. Bug #960048.
Patch1:         %{cpan_name}-7.08-Link-to-libperl-explicitly-on-Linux.patch
# Unbundle version modules
Patch2:         %{cpan_name}-7.04-Unbundle-version.patch
# Unbundle Encode::Locale module
Patch3:         %{cpan_name}-7.00-Unbundle-Encode-Locale.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  sed

# Do not export underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)\s*$
# Do not export private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DynaLoader|ExtUtils::MakeMaker::_version\\)

%description
This utility is designed to write a Makefile for an extension module from a
Makefile.PL. It is based on the Makefile.SH model provided by Andy
Dougherty and the perl5-porters.

%package -n perl-ExtUtils-Command
Summary:        Perl routines to replace common UNIX commands in Makefiles
License:        GPL+ or Artistic
Group:          Development/Libraries
BuildArch:      noarch
# File::Spec not used
# VMS::Feature not used

%description -n perl-ExtUtils-Command
This Perl module is used to replace common UNIX commands. In all cases the
functions work with @ARGV rather than taking arguments. This makes them
easier to deal with in Makefiles.

%prep
%setup -q -n ExtUtils-MakeMaker-%{cpan_version}

%build
BUILDING_AS_PACKAGE=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

#%check
#make test

%files
%doc Changes CONTRIBUTING README
%{_bindir}/*
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/ExtUtils/Command.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/ExtUtils::Command.*

%files -n perl-extutils-command
%dir %{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/ExtUtils/Command.pm
%{_mandir}/man3/ExtUtils::Command.*

%changelog

