Name:		ncurses	
Version:	5.9
Release:	1%{?dist}
Summary:	Ncurses support utilities	

Group:		System Environment/Base
License:	MIT
URL:		http://invisible-island.net/ncurses/ncurses.html	
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz

Patch:		 ncurses-5.9-gcc-5.patch

Requires:	%{name}-libs

%description
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

%package terminfo
Summary: Terminal descriptions
Group: System Environment/Base

%description terminfo
This package contains additional terminal descriptions not found in
the ncurses-base package.

%package widec-libs
Summary: NCurses wide-character libraries
Group: System Environment/Base

%description widec-libs
For NCurses these wide-character libraries are usable in both multibyte and traditional 8-bit locales, while normal libraries work properly only in 8-bit locales. Wide-character and normal libraries are source-compatible, but not binary-compatible.

%package libs
Summary: NCurses libraries
Group: System Environment/Libraries

%description libs
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

This package contains the ncurses libraries.

%package terminfo-base
Summary: Descriptions of common terminals
Group: System Environment/Base
BuildArch: noarch

%description terminfo-base
This package contains descriptions of common terminals. Other terminal
descriptions are included in the ncurses-term package.

%package devel
Summary: Development files for the ncurses library
Group: Development/Libraries

%description devel
The header files and libraries for developing applications that use
the ncurses terminal handling library.

%prep
%setup -q
%patch -p1 -b .gcc-5

%build
#build
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv \
                 /usr/share/automake-1.15/$(basename $i) $i ; \
done

mkdir %{name}-build
cd %{name}-build
../configure \
	--build=%{_host} \
	--host=%{_host} \
	--mandir=/usr/share/man \
	--without-ada \
	--disable-termcap \
	--disable-rpath-hack \
	--without-cxx-binding \
	--with-terminfo-dirs="/etc/terminfo:/usr/share/terminfo" \
	--enable-pc-files \
	--with-shared

make libs
make -C progs

#wide character build
cd ..
mkdir %{name}wc-build
cd %{name}wc-build
../configure \
        --build=%{_host} \
        --host=%{_host} \
        --mandir=/usr/share/man \
        --without-ada \
        --disable-termcap \
        --disable-rpath-hack \
        --without-cxx-binding \
        --with-terminfo-dirs="/etc/terminfo:/usr/share/terminfo" \
        --enable-pc-files \
        --with-shared \
	--enable-widec \
	--without-progs

make libs
cd ..
%install
rm -rf %{buildroot}
make -j1 -C ncurses-build DESTDIR=%{buildroot} install.libs \
		install.progs install.data

make -j1 -C ncurseswc-build DESTDIR=%{buildroot} install.libs \
		install.includes install.man


for i in ansi console dumb linux rxvt screen sun vt52 vt100 vt102 \
		vt200 vt220 xterm xterm-color xterm-xfree86; do
	local termfile=$(find %{buildroot}/usr/share/terminfo/ -name $i)
	local basedir=$(basename $(dirname $termfile))	

	[ -z $termfile ] && continue

	install -d %{buildroot}/etc/terminfo/$basedir
	mv ${termfile} %{buildroot}/etc/terminfo/$basedir/
	ln -s ../../../../etc/terminfo/$basedir/$i \
		%{buildroot}/usr/share/terminfo/$basedir/$i
done


mkdir %{buildroot}%{_includedir}/ncurses
mkdir %{buildroot}%{_includedir}/ncursesw
for l in %{buildroot}%{_includedir}/*.h; do
    ln -s ../$(basename $l) %{buildroot}%{_includedir}/ncurses
    ln -s ../$(basename $l) %{buildroot}%{_includedir}/ncursesw
done

%files
/usr/bin/tic
/usr/bin/clear
/usr/bin/tset
/usr/bin/toe
/usr/bin/reset
/usr/bin/infotocap
/usr/bin/tabs
/usr/bin/captoinfo
/usr/bin/tput
/usr/bin/infocmp
%dir /usr/share/tabset
/usr/share/tabset/stdcrt
/usr/share/tabset/std
/usr/share/tabset/vt100
/usr/share/tabset/vt300

%files terminfo
%dir /usr/share/terminfo
/usr/share/terminfo/1/
/usr/share/terminfo/2/
/usr/share/terminfo/3/
/usr/share/terminfo/4/
/usr/share/terminfo/5/
/usr/share/terminfo/6/
/usr/share/terminfo/7/
/usr/share/terminfo/8/
/usr/share/terminfo/9/
/usr/share/terminfo/A/
/usr/share/terminfo/E/
/usr/share/terminfo/L/
/usr/share/terminfo/M/
/usr/share/terminfo/N/
/usr/share/terminfo/P/
/usr/share/terminfo/Q/
/usr/share/terminfo/X/
/usr/share/terminfo/a/
/usr/share/terminfo/b/
/usr/share/terminfo/c/
/usr/share/terminfo/d/
/usr/share/terminfo/e/
/usr/share/terminfo/f/
/usr/share/terminfo/g/
/usr/share/terminfo/h/
/usr/share/terminfo/i/
/usr/share/terminfo/j/
/usr/share/terminfo/k/
/usr/share/terminfo/l/
/usr/share/terminfo/m/
/usr/share/terminfo/n/
/usr/share/terminfo/o/
/usr/share/terminfo/p/
/usr/share/terminfo/q/
/usr/share/terminfo/r/
/usr/share/terminfo/s/
/usr/share/terminfo/t/
/usr/share/terminfo/u/
/usr/share/terminfo/v/
/usr/share/terminfo/w/
/usr/share/terminfo/x/
/usr/share/terminfo/z/

%files widec-libs
/usr/lib/libformw.so.5.9
/usr/lib/libncursesw.so.5.9
/usr/lib/libpanelw.so.5.9
/usr/lib/libncursesw.so.5
/usr/lib/libmenuw.so.5.9
/usr/lib/libformw.so.5
/usr/lib/libpanelw.so.5
/usr/lib/libmenuw.so.5

%files libs
%dir /usr/lib/terminfo
/usr/lib/terminfo
/usr/lib/libform.so.5
/usr/lib/libform.so.5.9
/usr/lib/libpanel.so.5
/usr/lib/libncurses.so.5
/usr/lib/libmenu.so.5
/usr/lib/libpanel.so.5.9
/usr/lib/libncurses.so.5.9
/usr/lib/libmenu.so.5.9

%files terminfo-base
/etc/terminfo/a/ansi
/etc/terminfo/r/rxvt
/etc/terminfo/d/dumb
/etc/terminfo/l/linux
/etc/terminfo/x/xterm
/etc/terminfo/x/xterm-color
/etc/terminfo/x/xterm-xfree86
/etc/terminfo/v/vt52
/etc/terminfo/v/vt200
/etc/terminfo/v/vt220
/etc/terminfo/v/vt102
/etc/terminfo/v/vt100
/etc/terminfo/s/screen
/etc/terminfo/s/sun

%dir /etc/terminfo
%dir /etc/terminfo/a
%dir /etc/terminfo/l
%dir /etc/terminfo/r
%dir /etc/terminfo/v
%dir /etc/terminfo/x
%dir /etc/terminfo/d
%dir /etc/terminfo/s

%files devel
%{_bindir}/ncurses*-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/ncurses
%dir %{_includedir}/ncursesw
%{_includedir}/ncurses/*.h
%{_includedir}/ncursesw/*.h
%{_includedir}/*.h

%changelog
