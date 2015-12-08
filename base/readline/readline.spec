Name:		readline
Version:	6.3
Release:	1%{?dist}
Summary:	A library for editing typed command lines

Group:		System Environment/Libraries
License:	GPLv3+
URL:		http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source0:	http://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz	

Patch1:		fix-ncurses-underlinking.patch
Patch2:		readline63-001
Patch3:		readline63-002
Patch4:		readline63-003
Patch5:		readline63-004
Patch6:		readline63-005
Patch7:		readline63-006
Patch8:		readline63-007
Patch9:		readline63-008


BuildRequires: ncurses-devel
#Requires:	

%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

%package devel
Summary: Files needed to develop programs which use the readline library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: ncurses-devel

%description devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.


%prep
%setup -q

%patch1 -p0 -b  .ncurses-underlinking
%patch2 -p0 -b	.readline63-001
%patch3 -p0 -b	.readline63-002
%patch4 -p0 -b	.readline63-003
%patch5 -p0 -b	.readline63-004
%patch6 -p0 -b	.readline63-005
%patch7 -p0 -b	.readline63-006
%patch8 -p0 -b	.readline63-007
%patch9 -p0 -b	.readline63-008

%build
./configure \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-static \
	--enable-shared

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
# verfy that its not underlinked as upstream designed it
if ! readelf -d %{buildroot}/usr/lib/libreadline.so | grep 'NEEDED.*ncurses'; then
	error "readline needs to be linked against ncurses"
	return 1
fi

%files
%{_libdir}/libreadline*.so.*
%{_libdir}/libhistory*.so.*

%files devel
%{_includedir}/readline
%{_libdir}/lib*.so

%changelog
