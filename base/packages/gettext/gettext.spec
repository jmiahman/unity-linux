%define _target_platform %{_arch}-unity-linux-musl

Name:		gettext	
Version:	0.19.4
Release:	1%{?dist}
Summary:	GNU libraries and utilities for producing multi-lingual messages

Group:		Development/Tools	
License:	GPLv3+ and LGPLv2+
URL:		http://www.gnu.org/software/gettext/		
Source0:	ftp://ftp.gnu.org/gnu/gettext/%{name}-%{version}.tar.xz

#BuildRequires:	
#Requires:	

%description
The GNU gettext package provides a set of tools and documentation for
producing multi-lingual messages in programs. Tools include a set of
conventions about how programs should be written to support message
catalogs, a directory and file naming organization for the message
catalogs, a runtime library which supports the retrieval of translated
messages, and stand-alone programs for handling the translatable and
the already translated strings. Gettext provides an easy to use
library and tools for creating, using, and modifying natural language
catalogs and is a powerful and simple method for internationalizing
programs.

%package -n libintl
Group:		Development/Tools
Summary:	Tool in gettext that provides native language support.
%description -n libintl
Libintl is a library that provides native language support to programs. It is part of Gettext.

%package devel 
Group:		Development/Tools
Summary:	Development files and headers for Gettext.
                                                                                              
%description devel
Development files and headers for Gettext.


%prep
%setup -q

%build
export LIBS="-lrt" 
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--enable-threads=posix \
	--disable-java \
	--disable-static

make

%install
make -j1 DESTDIR=%{buildroot} install
%__rm $RPM_BUILD_ROOT/usr/lib/*.la

%files
%doc
/usr/bin/*
/usr/lib/*.so*
/usr/lib/gettext/*

%files -n libintl
/usr/lib/libintl.so.8.1.3
/usr/lib/libintl.so.8

%files devel
/usr/share/gettext/archive.dir.tar.xz
/usr/share/gettext/ABOUT-NLS
/usr/share/gettext/gettext.h
/usr/share/gettext/po/remove-potcdate.sin
/usr/share/gettext/po/Rules-quot
/usr/share/gettext/po/Makefile.in.in
/usr/share/gettext/po/en@quot.header
/usr/share/gettext/po/insert-header.sin
/usr/share/gettext/po/quot.sed
/usr/share/gettext/po/boldquot.sed
/usr/share/gettext/po/Makevars.template
/usr/share/gettext/po/en@boldquot.header
/usr/share/gettext/intl/plural.y
/usr/share/gettext/intl/gmo.h
/usr/share/gettext/intl/COPYING.LIB
/usr/share/gettext/intl/printf-args.h
/usr/share/gettext/intl/eval-plural.h
/usr/share/gettext/intl/l10nflist.c
/usr/share/gettext/intl/localealias.c
/usr/share/gettext/intl/vasnprintf.h
/usr/share/gettext/intl/ref-del.sin
/usr/share/gettext/intl/bindtextdom.c
/usr/share/gettext/intl/VERSION
/usr/share/gettext/intl/setlocale.c
/usr/share/gettext/intl/explodename.c
/usr/share/gettext/intl/gettextP.h
/usr/share/gettext/intl/log.c
/usr/share/gettext/intl/loadmsgcat.c
/usr/share/gettext/intl/hash-string.c
/usr/share/gettext/intl/localcharset.c
/usr/share/gettext/intl/localename.c
/usr/share/gettext/intl/printf-parse.c
/usr/share/gettext/intl/printf-parse.h
/usr/share/gettext/intl/locale.alias
/usr/share/gettext/intl/Makefile.in
/usr/share/gettext/intl/threadlib.c
/usr/share/gettext/intl/finddomain.c
/usr/share/gettext/intl/xsize.h
/usr/share/gettext/intl/printf-args.c
/usr/share/gettext/intl/plural-exp.h
/usr/share/gettext/intl/dgettext.c
/usr/share/gettext/intl/lock.c
/usr/share/gettext/intl/vasnprintf.c
/usr/share/gettext/intl/dcigettext.c
/usr/share/gettext/intl/libgnuintl.in.h
/usr/share/gettext/intl/textdomain.c
/usr/share/gettext/intl/verify.h
/usr/share/gettext/intl/dngettext.c
/usr/share/gettext/intl/export.h
/usr/share/gettext/intl/plural-exp.c
/usr/share/gettext/intl/os2compat.h
/usr/share/gettext/intl/relocatable.c
/usr/share/gettext/intl/libintl.rc
/usr/share/gettext/intl/tsearch.c
/usr/share/gettext/intl/lock.h
/usr/share/gettext/intl/version.c
/usr/share/gettext/intl/loadinfo.h
/usr/share/gettext/intl/xsize.c
/usr/share/gettext/intl/tsearch.h
/usr/share/gettext/intl/ngettext.c
/usr/share/gettext/intl/relocatable.h
/usr/share/gettext/intl/wprintf-parse.h
/usr/share/gettext/intl/config.charset
/usr/share/gettext/intl/intl-compat.c
/usr/share/gettext/intl/vasnwprintf.h
/usr/share/gettext/intl/os2compat.c
/usr/share/gettext/intl/intl-exports.c
/usr/share/gettext/intl/gettext.c
/usr/share/gettext/intl/ref-add.sin
/usr/share/gettext/intl/plural.c
/usr/share/gettext/intl/dcngettext.c
/usr/share/gettext/intl/printf.c
/usr/share/gettext/intl/localcharset.h
/usr/share/gettext/intl/langprefs.c
/usr/share/gettext/intl/dcgettext.c
/usr/share/gettext/intl/hash-string.h
/usr/share/gettext/intl/osdep.c
/usr/share/gettext/projects/GNOME/trigger
/usr/share/gettext/projects/GNOME/teams.url
/usr/share/gettext/projects/GNOME/team-address
/usr/share/gettext/projects/GNOME/teams.html
/usr/share/gettext/projects/KDE/trigger
/usr/share/gettext/projects/KDE/teams.url
/usr/share/gettext/projects/KDE/team-address
/usr/share/gettext/projects/KDE/teams.html
/usr/share/gettext/projects/TP/trigger
/usr/share/gettext/projects/TP/teams.url
/usr/share/gettext/projects/TP/team-address
/usr/share/gettext/projects/TP/teams.html
/usr/share/gettext/projects/team-address
/usr/share/gettext/projects/index
/usr/share/gettext/config.rpath
/usr/share/gettext/styles/po-emacs-x.css
/usr/share/gettext/styles/po-emacs-xterm16.css
/usr/share/gettext/styles/po-emacs-xterm256.css
/usr/share/gettext/styles/po-emacs-xterm.css
/usr/share/gettext/styles/po-vim.css
/usr/share/gettext/styles/po-default.css
/usr/share/gettext/msgunfmt.tcl
/usr/share/gettext/javaversion.class
/usr/share/aclocal/intmax.m4
/usr/share/aclocal/lib-link.m4
/usr/share/aclocal/wchar_t.m4
/usr/share/aclocal/glibc21.m4
/usr/share/aclocal/xsize.m4
/usr/share/aclocal/po.m4
/usr/share/aclocal/intdiv0.m4
/usr/share/aclocal/fcntl-o.m4
/usr/share/aclocal/stdint_h.m4
/usr/share/aclocal/gettext.m4
/usr/share/aclocal/printf-posix.m4
/usr/share/aclocal/extern-inline.m4
/usr/share/aclocal/uintmax_t.m4
/usr/share/aclocal/intlmacosx.m4
/usr/share/aclocal/lcmessage.m4
/usr/share/aclocal/lock.m4
/usr/share/aclocal/nls.m4
/usr/share/aclocal/lib-ld.m4
/usr/share/aclocal/longlong.m4
/usr/share/aclocal/glibc2.m4
/usr/share/aclocal/size_max.m4
/usr/share/aclocal/visibility.m4
/usr/share/aclocal/inttypes-pri.m4
/usr/share/aclocal/wint_t.m4
/usr/share/aclocal/codeset.m4
/usr/share/aclocal/lib-prefix.m4
/usr/share/aclocal/intldir.m4
/usr/share/aclocal/threadlib.m4
/usr/share/aclocal/intl.m4
/usr/share/aclocal/inttypes_h.m4
/usr/share/aclocal/iconv.m4
/usr/share/aclocal/progtest.m4
/usr/lib/libintl.so
/usr/lib/libgettextpo.so
/usr/lib/libgettextlib.so
/usr/lib/libasprintf.so
/usr/lib/libgettextsrc.so
/usr/include/libintl.h
/usr/include/autosprintf.h
/usr/include/gettext-po.h

%changelog
