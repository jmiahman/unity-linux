Name:		flex	
Version:	2.5.39	
Release:	1%{?dist}
Summary:	A tool for generating text-scanning programs	

Group:		Development/Tools	
License:	BSD and LGPLv2+
URL:		http://flex.sourceforge.net/
Source0:	http://fossies.org/linux/misc/%{name}-%{version}.tar.xz	

BuildRequires: m4, autoconf	
#Requires:	

%description
The flex program generates scanners.  Scanners are programs which can
recognize lexical patterns in text.  Flex takes pairs of regular
expressions and C code as input and generates a C source file as
output.  The output file is compiled and linked with a library to
produce an executable.  The executable searches through its input for
occurrences of the regular expressions.  When a match is found, it
executes the corresponding C code.  Flex was designed to work with
both Yacc and Bison, and is used by many programs as part of their
build process.

You should install flex if you are going to use your system for
application development.

# We keep the libraries in separate sub-package to allow for multilib
# installations of flex.
%package devel
Summary: Libraries for flex scanner generator
Group: Development/Tools

%description devel

This package contains the library with default implementations of
`main' and `yywrap' functions that the client binary can choose to use
instead of implementing their own.

%prep
%setup -q


%build

./configure \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--enable-shared \
	
make


%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.so' -delete
find %{buildroot} -name '*.so.2' -delete
find %{buildroot} -name '*.so.2.0.0' -delete

( cd %{buildroot}
  ln -sf flex .%{_bindir}/lex
  ln -sf flex .%{_bindir}/flex++
  ln -s flex.1 .%{_mandir}/man1/lex.1
  ln -s flex.1 .%{_mandir}/man1/flex++.1
  ln -s libfl.a .%{_libdir}/libl.a
)

%files
%defattr(-,root,root)
#%doc COPYING NEWS README
%{_bindir}/*
#%{_mandir}/man1/*
%{_includedir}/FlexLexer.h
#%{_infodir}/flex.info*

%files devel
%defattr(-,root,root)
#%doc COPYING
%{_libdir}/*.a



%changelog
