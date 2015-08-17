Summary: A portable x86 assembler which uses Intel-like syntax
Name: nasm
Version: 2.11.08
Release: 1%{?dist}
License: BSD
Group: Development/Languages
URL: http://www.nasm.us
Source0: http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.bz2
Source1: http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}-xdoc.tar.bz2
BuildRequires: perl(Env)
BuildRequires: autoconf
BuildRequires: asciidoc
BuildRequires: xmlto

%package doc
Summary: Documentation for NASM
BuildRequires: ghostscript, texinfo
BuildArch: noarch

%package rdoff
Summary: Tools for the RDOFF binary format, sometimes used with NASM

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%description doc
This package contains documentation for the Netwide Assembler (NASM),
in HTML, info, PostScript, and text formats.

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%prep
%setup -q
tar xjf %{SOURCE1} --strip-components 1

%build
autoreconf
%configure
make everything %{?_smp_mflags}
gzip -9f doc/nasmdoc.{ps,txt}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make INSTALLROOT=$RPM_BUILD_ROOT install install_rdf
install -d $RPM_BUILD_ROOT/%{_infodir}
install -t $RPM_BUILD_ROOT/%{_infodir} doc/info/*

%files
%doc AUTHORS CHANGES README TODO
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_mandir}/man1/nasm*
%{_mandir}/man1/ndisasm*
%{_infodir}/nasm.info*.gz

%files doc
%doc doc/html doc/nasmdoc.txt.gz doc/nasmdoc.ps.gz

%files rdoff
%{_bindir}/ldrdf
%{_bindir}/rdf2bin
%{_bindir}/rdf2ihx
%{_bindir}/rdf2com
%{_bindir}/rdfdump
%{_bindir}/rdflib
%{_bindir}/rdx
%{_bindir}/rdf2ith
%{_bindir}/rdf2srec
%{_mandir}/man1/rd*
%{_mandir}/man1/ld*

%changelog
