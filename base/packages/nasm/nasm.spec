Summary: A portable x86 assembler which uses Intel-like syntax
Name: nasm
Version: 2.11.08
Release: 1%{?dist}
License: BSD
Group: Development/Languages
URL: http://www.nasm.us
Source0: http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.bz2
Source1: http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}-xdoc.tar.bz2
#BuildRequires: perl(Env)
#BuildRequires: autoconf
#BuildRequires: asciidoc
#BuildRequires: xmlto

#%package doc
#Summary: Documentation for NASM
#BuildRequires: ghostscript, texinfo
#BuildArch: noarch

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

#%description doc
#This package contains documentation for the Netwide Assembler (NASM),
#in HTML, info, PostScript, and text formats.

%prep
%setup -q
tar xjf %{SOURCE1} --strip-components 1

%build
autoreconf
%configure
make nasmlib.o %{?_smp_mflags}
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make INSTALLROOT=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT/%{_infodir}
install -t $RPM_BUILD_ROOT/%{_infodir} doc/info/*

%files
#%doc AUTHORS CHANGES README TODO
%{_bindir}/nasm
%{_bindir}/ndisasm
#%{_mandir}/man1/nasm*
#%{_mandir}/man1/ndisasm*

#%files doc
#%doc doc/html doc/nasmdoc.txt.gz doc/nasmdoc.ps.gz

%changelog
