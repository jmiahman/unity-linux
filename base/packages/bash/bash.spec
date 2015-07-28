%define patchleveltag .39
%define baseversion 4.3

Name:		bash
Version:	%{baseversion}%{patchleveltag}
Release:	1%{?dist}
Summary:	The GNU Bourne Again shell	

Group:		System Environment/Shells
License:	GPLv3+
URL:		http://www.gnu.org/software/bash
Source0:	ftp://ftp.gnu.org/gnu/bash/bash-%{baseversion}.tar.gz

Patch1:   bash43-001
Patch2:   bash43-002
Patch3:   bash43-003
Patch4:   bash43-004
Patch5:   bash43-005
Patch6:   bash43-006
Patch7:   bash43-007
Patch8:   bash43-008
Patch9:   bash43-009
Patch10:   bash43-010
Patch11:   bash43-011
Patch12:   bash43-012
Patch13:   bash43-013
Patch14:   bash43-014
Patch15:   bash43-015
Patch16:   bash43-016
Patch17:   bash43-017
Patch18:   bash43-018
Patch19:   bash43-019
Patch20:   bash43-020
Patch21:   bash43-021
Patch22:   bash43-022
Patch23:   bash43-023
Patch24:   bash43-024
Patch25:   bash43-025
Patch26:   bash43-026
Patch27:   bash43-027
Patch28:   bash43-028
Patch29:   bash43-029
Patch30:   bash43-030
Patch31:   bash43-031
Patch32:   bash43-032
Patch33:   bash43-033
Patch34:   bash43-034
Patch35:   bash43-035
Patch36:   bash43-036
Patch37:   bash43-037
Patch38:   bash43-038
Patch39:   bash43-039
Patch40:   bash-noinfo.patch
Patch41:   privmode-setuid-fail.patch


BuildRequires: readline-devel, ncurses-devel, bison, flex
#Requires:	

%description
The GNU Bourne Again shell (Bash) is a shell or command language
interpreter that is compatible with the Bourne shell (sh). Bash
incorporates useful features from the Korn shell (ksh) and the C shell
(csh). Most sh scripts can be run by bash without modification.

%prep
%setup -q -n %{name}-%{baseversion}

%patch1 -p0 -b .bash43-001
%patch2 -p0 -b .bash43-002
%patch3 -p0 -b .bash43-003
%patch4 -p0 -b .bash43-004
%patch5 -p0 -b .bash43-005
%patch6 -p0 -b .bash43-006
%patch7 -p0 -b .bash43-007
%patch8 -p0 -b .bash43-008
%patch9 -p0 -b .bash43-009
%patch10 -p0 -b .bash43-010
%patch11 -p0 -b .bash43-011
%patch12 -p0 -b .bash43-012
%patch13 -p0 -b .bash43-013
%patch14 -p0 -b .bash43-014
%patch15 -p0 -b .bash43-015
%patch16 -p0 -b .bash43-016
%patch17 -p0 -b .bash43-017
%patch18 -p0 -b .bash43-018
%patch19 -p0 -b .bash43-019
%patch20 -p0 -b .bash43-020
%patch21 -p0 -b .bash43-021
%patch22 -p0 -b .bash43-022
%patch23 -p0 -b .bash43-023
%patch24 -p0 -b .bash43-024
%patch25 -p0 -b .bash43-025
%patch26 -p0 -b .bash43-026
%patch27 -p0 -b .bash43-027
%patch28 -p0 -b .bash43-028
%patch29 -p0 -b .bash43-029
%patch30 -p0 -b .bash43-030
%patch31 -p0 -b .bash43-031
%patch32 -p0 -b .bash43-032
%patch33 -p0 -b .bash43-033
%patch34 -p0 -b .bash43-034
%patch35 -p0 -b .bash43-035
%patch36 -p0 -b .bash43-036
%patch37 -p0 -b .bash43-037
%patch38 -p0 -b .bash43-038
%patch39 -p0 -b .bash43-039
%patch40 -p0 -b .bash-noinfo
%patch41 -p0 -b .privmode-setuid-fail



%build
./configure \
	--prefix=/usr \
	--bindir=/bin \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--with-curses \
	--disable-nls \
	--enable-readline \
	--without-bash-malloc \
	--with-installed-readline

make y.tab.c 
make builtins/libbuiltins.a 
make
%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/locale

%files
/bin/bashbug
/bin/bash

%changelog
