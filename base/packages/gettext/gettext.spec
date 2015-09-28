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
	--mandir=%{_datadir}/man \
	--enable-threads=posix \
	--disable-java \
	--disable-static

make

%install
make -j1 DESTDIR=%{buildroot} install
%__rm $RPM_BUILD_ROOT/usr/lib/*.la

%files
%doc
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/gettext/*

%files -n libintl
%{_libdir}/libintl.so.8.1.3
%{_libdir}/libintl.so.8

%files devel
%{_datadir}/gettext/archive.dir.tar.xz
%{_datadir}/gettext/ABOUT-NLS
%{_datadir}/gettext/gettext.h
%{_datadir}/gettext/po/remove-potcdate.sin
%{_datadir}/gettext/po/Rules-quot
%{_datadir}/gettext/po/Makefile.in.in
%{_datadir}/gettext/po/en@quot.header
%{_datadir}/gettext/po/insert-header.sin
%{_datadir}/gettext/po/quot.sed
%{_datadir}/gettext/po/boldquot.sed
%{_datadir}/gettext/po/Makevars.template
%{_datadir}/gettext/po/en@boldquot.header
%{_datadir}/gettext/intl/plural.y
%{_datadir}/gettext/intl/gmo.h
%{_datadir}/gettext/intl/COPYING.LIB
%{_datadir}/gettext/intl/printf-args.h
%{_datadir}/gettext/intl/eval-plural.h
%{_datadir}/gettext/intl/l10nflist.c
%{_datadir}/gettext/intl/localealias.c
%{_datadir}/gettext/intl/vasnprintf.h
%{_datadir}/gettext/intl/ref-del.sin
%{_datadir}/gettext/intl/bindtextdom.c
%{_datadir}/gettext/intl/VERSION
%{_datadir}/gettext/intl/setlocale.c
%{_datadir}/gettext/intl/explodename.c
%{_datadir}/gettext/intl/gettextP.h
%{_datadir}/gettext/intl/log.c
%{_datadir}/gettext/intl/loadmsgcat.c
%{_datadir}/gettext/intl/hash-string.c
%{_datadir}/gettext/intl/localcharset.c
%{_datadir}/gettext/intl/localename.c
%{_datadir}/gettext/intl/printf-parse.c
%{_datadir}/gettext/intl/printf-parse.h
%{_datadir}/gettext/intl/locale.alias
%{_datadir}/gettext/intl/Makefile.in
%{_datadir}/gettext/intl/threadlib.c
%{_datadir}/gettext/intl/finddomain.c
%{_datadir}/gettext/intl/xsize.h
%{_datadir}/gettext/intl/printf-args.c
%{_datadir}/gettext/intl/plural-exp.h
%{_datadir}/gettext/intl/dgettext.c
%{_datadir}/gettext/intl/lock.c
%{_datadir}/gettext/intl/vasnprintf.c
%{_datadir}/gettext/intl/dcigettext.c
%{_datadir}/gettext/intl/libgnuintl.in.h
%{_datadir}/gettext/intl/textdomain.c
%{_datadir}/gettext/intl/verify.h
%{_datadir}/gettext/intl/dngettext.c
%{_datadir}/gettext/intl/export.h
%{_datadir}/gettext/intl/plural-exp.c
%{_datadir}/gettext/intl/os2compat.h
%{_datadir}/gettext/intl/relocatable.c
%{_datadir}/gettext/intl/libintl.rc
%{_datadir}/gettext/intl/tsearch.c
%{_datadir}/gettext/intl/lock.h
%{_datadir}/gettext/intl/version.c
%{_datadir}/gettext/intl/loadinfo.h
%{_datadir}/gettext/intl/xsize.c
%{_datadir}/gettext/intl/tsearch.h
%{_datadir}/gettext/intl/ngettext.c
%{_datadir}/gettext/intl/relocatable.h
%{_datadir}/gettext/intl/wprintf-parse.h
%{_datadir}/gettext/intl/config.charset
%{_datadir}/gettext/intl/intl-compat.c
%{_datadir}/gettext/intl/vasnwprintf.h
%{_datadir}/gettext/intl/os2compat.c
%{_datadir}/gettext/intl/intl-exports.c
%{_datadir}/gettext/intl/gettext.c
%{_datadir}/gettext/intl/ref-add.sin
%{_datadir}/gettext/intl/plural.c
%{_datadir}/gettext/intl/dcngettext.c
%{_datadir}/gettext/intl/printf.c
%{_datadir}/gettext/intl/localcharset.h
%{_datadir}/gettext/intl/langprefs.c
%{_datadir}/gettext/intl/dcgettext.c
%{_datadir}/gettext/intl/hash-string.h
%{_datadir}/gettext/intl/osdep.c
%{_datadir}/gettext/projects/GNOME/trigger
%{_datadir}/gettext/projects/GNOME/teams.url
%{_datadir}/gettext/projects/GNOME/team-address
%{_datadir}/gettext/projects/GNOME/teams.html
%{_datadir}/gettext/projects/KDE/teams.url
%{_datadir}/gettext/projects/KDE/trigger
%{_datadir}/gettext/projects/KDE/team-address
%{_datadir}/gettext/projects/KDE/teams.html
%{_datadir}/gettext/projects/TP/trigger
%{_datadir}/gettext/projects/TP/teams.url
%{_datadir}/gettext/projects/TP/team-address
%{_datadir}/gettext/projects/TP/teams.html
%{_datadir}/gettext/projects/team-address
%{_datadir}/gettext/projects/index
%{_datadir}/gettext/config.rpath
%{_datadir}/gettext/styles/po-emacs-x.css
%{_datadir}/gettext/styles/po-emacs-xterm16.css
%{_datadir}/gettext/styles/po-emacs-xterm256.css
%{_datadir}/gettext/styles/po-emacs-xterm.css
%{_datadir}/gettext/styles/po-vim.css
%{_datadir}/gettext/styles/po-default.css
%{_datadir}/gettext/msgunfmt.tcl
%{_datadir}/gettext/javaversion.class
%{_datadir}/aclocal/intmax.m4
%{_datadir}/aclocal/lib-link.m4
%{_datadir}/aclocal/wchar_t.m4
%{_datadir}/aclocal/glibc21.m4
%{_datadir}/aclocal/xsize.m4
%{_datadir}/aclocal/po.m4
%{_datadir}/aclocal/intdiv0.m4
%{_datadir}/aclocal/fcntl-o.m4
%{_datadir}/aclocal/stdint_h.m4
%{_datadir}/aclocal/gettext.m4
%{_datadir}/aclocal/printf-posix.m4
%{_datadir}/aclocal/extern-inline.m4
%{_datadir}/aclocal/uintmax_t.m4
%{_datadir}/aclocal/intlmacosx.m4
%{_datadir}/aclocal/lcmessage.m4
%{_datadir}/aclocal/lock.m4
%{_datadir}/aclocal/nls.m4
%{_datadir}/aclocal/lib-ld.m4
%{_datadir}/aclocal/longlong.m4
%{_datadir}/aclocal/glibc2.m4
%{_datadir}/aclocal/size_max.m4
%{_datadir}/aclocal/visibility.m4
%{_datadir}/aclocal/inttypes-pri.m4
%{_datadir}/aclocal/wint_t.m4
%{_datadir}/aclocal/codeset.m4
%{_datadir}/aclocal/lib-prefix.m4
%{_datadir}/aclocal/intldir.m4
%{_datadir}/aclocal/threadlib.m4
%{_datadir}/aclocal/intl.m4
%{_datadir}/aclocal/inttypes_h.m4
%{_datadir}/aclocal/iconv.m4
%{_datadir}/aclocal/progtest.m4
%{_libdir}/libintl.so
%{_libdir}/libgettextpo.so
%{_libdir}/libgettextlib.so
%{_libdir}/libasprintf.so
%{_libdir}/libgettextsrc.so
%dir %{_libdir}/gettext
%dir %{_datadir}/gettext
%dir %{_datadir}/gettext/intl
%dir %{_datadir}/gettext/po
%dir %{_datadir}/gettext/projects/KDE
%dir %{_datadir}/gettext/projects/GNOME
%dir %{_datadir}/gettext/projects/TP
%dir %{_datadir}/gettext/projects
%dir %{_datadir}/gettext/projects
%dir %{_datadir}/gettext/styles
%{_includedir}/libintl.h
%{_includedir}/autosprintf.h
%{_includedir}/gettext-po.h

%changelog
