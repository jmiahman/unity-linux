
%define _privlib /usr/share/perl5/core_perl
%define _archlib /usr/lib/perl5/core_perl
%define _vendorlib /usr/share/perl5/vendor_perl
%define _vendorarch /usr/lib/perl5/vendor_perl

Name:		perl
Version:	5.22.0
Release:        1%{?dist}
Summary:	Practical Extraction and Report Language

Group:		Development/Languages
License:	(GPL+ or Artistic) and (GPLv2+ or Artistic) and Copyright Only and HSRL and Public Domain and UCD
URL:		http://www.perl.org/
Source0:	http://www.cpan.org/src/5.0/perl-%{version}.tar.xz

#BuildRequires:
#Requires:

%description
Perl is a high-level programming language with roots in C, sed, awk and shell
scripting.  Perl is good at handling processes and files, and is especially
good at handling text.  Perl's hallmarks are practicality and efficiency.
While it is used to do a lot of different things, Perl's most common
applications are system administration utilities and web programming.

Install this package if you want to program in Perl or enable your system to
handle Perl scripts with %{_bindir}/perl interpreter.

If your script requires some Perl modules, you can install them with
"perl(MODULE)" where "MODULE" is a name of required module. E.g. install
"perl(Test::More)" to make Test::More Perl module available.

If you need all the Perl modules that come with upstream Perl sources, so
called core modules, install perl-core package.

If you only need perl run-time as a shared library, i.e. Perl interpreter
embedded into another application, the only essential package is perl-libs.

Perl header files can be found in perl-devel package.

%package -n miniperl
Summary:        miniperl is a mini version of the perl executable.
Group:          Development/Languages
License:        GPL+ or Artistic

%description -n miniperl
miniperl is a mini version of the perl executable, used in building perl itself.

%prep
%setup -q

%build
export BUILD_ZLIB=False
export BUILD_BZIP2=0

sed -i -e 's/less -R/less/g' ./Configure
sed -i -e 's/libswanted="\(.*\) nsl\(.*\)"/libswanted="\1\2"/g' ./Configure

./Configure -des \
	-Dcccdlflags='-fPIC' \
	-Dcccdlflags='-fPIC' \
	-Dccdlflags='-rdynamic' \
	-Dprefix=/usr \
	-Dprivlib=%{_privlib} \
	-Darchlib=%{_archlib} \
	-Dvendorprefix=/usr \
	-Dvendorlib=%{_vendorlib} \
	-Dvendorarch=%{_vendorarch} \
	-Dsiteprefix=/usr/local \
	-Dsitelib=/usr/local/share/perl5/site_perl \
	-Dsitearch=/usr/local/lib/perl5/site_perl \
	-Dlocincpth=' ' \
	-Doptimize=${CFLAGS} \
	-Duselargefiles \
	-Dusethreads \
	-Duseshrplib \
	-Dd_semctl_semun \
	-Dman1dir=/usr/share/man/man1 \
	-Dman3dir=/usr/share/man/man3 \
	-Dinstallman1dir=/usr/share/man/man1 \
	-Dinstallman3dir=/usr/share/man/man3 \
	-Dman1ext='1' \
	-Dman3ext='3pm' \
	-Dinc_version_list=none \
	-Dcf_by='Unity' \
	-Ud_csh \
	-Dusenm

make libperl.so
make miniperl
make

%install
make install DESTDIR=%{buildroot}

cp -f miniperl %{buildroot}/usr/bin

%files
/usr/bin/*
%exclude %{_bindir}/miniperl
/usr/lib/perl5/core_perl/*
/usr/share/perl5/core_perl/*

%files -n miniperl
/usr/bin/miniperl

%changelog
