Name:		bison	
Version:	3.0.4
Release:	1%{?dist}
Summary:	A GNU general-purpose parser generator	

URL:		http://www.gnu.org/software/bison/
License:	GPLv3+
Group:		Development/Tools
Source0: 	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz

#BuildRequires:	
#Requires:	

%description
Bison is a general purpose parser generator that converts a grammar
description for an LALR(1) context-free grammar into a C program to
parse that grammar. Bison can be used to develop a wide range of
language parsers, from ones used in simple desk calculators to complex
programming languages. Bison is upwardly compatible with Yacc, so any
correctly written Yacc grammar should work with Bison without any
changes. If you know Yacc, you shouldn't have any trouble using
Bison. You do need to be very proficient in C programming to be able
to use Bison. Bison is only needed on systems that are used for
development.

If your system will be used for C development, you should install
Bison.

%package devel
Summary: -ly library for development using Bison-generated parsers
Group: Development/Libraries

%description devel
The bison-devel package contains the -ly library sometimes used by
programs using Bison-generated parsers.  If you are developing programs
using Bison, you might want to link with this library.  This library
is not required by all Bison-generated parsers, but may be employed by
simple programs to supply minimal support for the generated parsers.


%prep
%setup -q


%build
%configure

make %{?_smp_mflags}


%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS TODO COPYING
%{_mandir}/*/bison*
%{_datadir}/bison
%{_infodir}/bison.info*
%{_bindir}/bison
%{_datadir}/aclocal/bison*.m4
%{_bindir}/yacc
   /usr/lib64/charset.alias
%{_datadir}/doc/bison/examples/calc++/calc++-driver.cc
%{_datadir}/doc/bison/examples/calc++/calc++-driver.hh
%{_datadir}/doc/bison/examples/calc++/calc++-parser.yy
%{_datadir}/doc/bison/examples/calc++/calc++-scanner.ll
%{_datadir}/doc/bison/examples/calc++/calc++.cc
%{_datadir}/doc/bison/examples/mfcalc/calc.h
%{_datadir}/doc/bison/examples/mfcalc/mfcalc.y
%{_datadir}/doc/bison/examples/rpcalc/rpcalc.y
%{_datadir}/info/dir
%{_datadir}/locale/*/LC_MESSAGES/*.mo


%files devel
%doc COPYING
%defattr(-,root,root)
%{_libdir}/liby.a

%changelog
