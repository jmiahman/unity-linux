Name:		doxygen	
Version:	1.8.9.1
Release:	1%{?dist}
Summary:	A documentation system for C/C++	

Group:		Development/Tools	
License:	GPL+
URL:		http://www.stack.nl/~dimitri/doxygen/index.html
Source0:	http://ftp.stack.nl/pub/users/dimitri/doxygen-%{version}.src.tar.gz

BuildRequires:	flex, bison, coreutils, perl, python
#Requires:	

%description
Doxygen can generate an online class browser (in HTML) and/or a
reference manual (in LaTeX) from a set of documented source files. The
documentation is extracted directly from the sources. Doxygen can
also be configured to extract the code structure from undocumented
source files.

%prep
%setup -q


%build

sed -i -e 's:^\(TMAKE_CFLAGS_RELEASE\t*\)= .*$:\1= $(ECFLAGS):' \
	-e 's:^\(TMAKE_CXXFLAGS_RELEASE\t*\)= .*$:\1= $(ECXXFLAGS):' \
	-e 's:^\(TMAKE_LFLAGS_RELEASE\s*\)=.*$:\1= $(ELDFLAGS):' \
                tmake/lib/*/tmake.conf

# fix final DESTDIR issue
sed -i -e "s:\$(INSTALL):\$(DESTDIR)/\$(INSTALL):g" \
	addon/doxywizard/Makefile.in

export ECFLAGS="$CFLAGS" ECXXFLAGS="$CXXFLAGS" ELDFLAGS="$LDFLAGS"

./configure \
	--prefix=/usr \
	
make

%install
make DESTDIR=%{buildroot} MAN1DIR=share/man/man1 install


%files
#%doc LANGUAGE.HOWTO README.md examples
#%doc html
%{_bindir}/doxygen
#%{_mandir}/man1/doxygen.1*

%changelog

