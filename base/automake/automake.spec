

Name:		automake
Version:	1.15
Release:	1%{?dist}
Summary:	A GNU tool for automatically creating Makefiles	

Group:		Development/Tools
License:	GPLv2+ and GFDL and Public Domain and MIT
URL:		http://www.gnu.org/software/%{name}/
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz	

#BuildRequires:	
#Requires:	

%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

You should install Automake if you are developing software and would
like to use its ability to automatically generate GNU standard
Makefiles.

%prep
%setup -q


%build
./configure \
	--host=%{_target_platform} \
	--build=%{_target_platform} \
	--prefix=/usr \

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

%files
/usr/bin/%{name}-%{version}
/usr/bin/%{name}
/usr/bin/aclocal
/usr/bin/aclocal-%{version}
/usr/share/%{name}-%{version}/depcomp
/usr/share/%{name}-%{version}/tap-driver.sh
/usr/share/%{name}-%{version}/mdate-sh
/usr/share/%{name}-%{version}/compile
/usr/share/%{name}-%{version}/COPYING
/usr/share/%{name}-%{version}/config.sub
/usr/share/%{name}-%{version}/ylwrap
/usr/share/%{name}-%{version}/texinfo.tex
/usr/share/%{name}-%{version}/config.guess
/usr/share/%{name}-%{version}/install-sh
/usr/share/%{name}-%{version}/py-compile
/usr/share/%{name}-%{version}/INSTALL
/usr/share/%{name}-%{version}/missing
/usr/share/%{name}-%{version}/mkinstalldirs
/usr/share/%{name}-%{version}/ar-lib
/usr/share/%{name}-%{version}/test-driver
/usr/share/%{name}-%{version}/Automake/Version.pm
/usr/share/%{name}-%{version}/Automake/ItemDef.pm
/usr/share/%{name}-%{version}/Automake/FileUtils.pm
/usr/share/%{name}-%{version}/Automake/XFile.pm
/usr/share/%{name}-%{version}/Automake/Config.pm
/usr/share/%{name}-%{version}/Automake/ChannelDefs.pm
/usr/share/%{name}-%{version}/Automake/RuleDef.pm
/usr/share/%{name}-%{version}/Automake/DisjConditions.pm
/usr/share/%{name}-%{version}/Automake/Item.pm
/usr/share/%{name}-%{version}/Automake/Condition.pm
/usr/share/%{name}-%{version}/Automake/Options.pm
/usr/share/%{name}-%{version}/Automake/Channels.pm
/usr/share/%{name}-%{version}/Automake/Configure_ac.pm
/usr/share/%{name}-%{version}/Automake/General.pm
/usr/share/%{name}-%{version}/Automake/Wrap.pm
/usr/share/%{name}-%{version}/Automake/Getopt.pm
/usr/share/%{name}-%{version}/Automake/Language.pm
/usr/share/%{name}-%{version}/Automake/VarDef.pm
/usr/share/%{name}-%{version}/Automake/Variable.pm
/usr/share/%{name}-%{version}/Automake/Rule.pm
/usr/share/%{name}-%{version}/Automake/Location.pm
/usr/share/%{name}-%{version}/am/progs.am
/usr/share/%{name}-%{version}/am/remake-hdr.am
/usr/share/%{name}-%{version}/am/check2.am
/usr/share/%{name}-%{version}/am/texinfos.am
/usr/share/%{name}-%{version}/am/vala.am
/usr/share/%{name}-%{version}/am/depend.am
/usr/share/%{name}-%{version}/am/yacc.am
/usr/share/%{name}-%{version}/am/lex.am
/usr/share/%{name}-%{version}/am/data.am
/usr/share/%{name}-%{version}/am/compile.am
/usr/share/%{name}-%{version}/am/distdir.am
/usr/share/%{name}-%{version}/am/libtool.am
/usr/share/%{name}-%{version}/am/dejagnu.am
/usr/share/%{name}-%{version}/am/texi-vers.am
/usr/share/%{name}-%{version}/am/configure.am
/usr/share/%{name}-%{version}/am/header-vars.am
/usr/share/%{name}-%{version}/am/install.am
/usr/share/%{name}-%{version}/am/header.am
/usr/share/%{name}-%{version}/am/library.am
/usr/share/%{name}-%{version}/am/texibuild.am
/usr/share/%{name}-%{version}/am/scripts.am
/usr/share/%{name}-%{version}/am/ltlib.am
/usr/share/%{name}-%{version}/am/java.am
/usr/share/%{name}-%{version}/am/inst-vars.am
/usr/share/%{name}-%{version}/am/mans-vars.am
/usr/share/%{name}-%{version}/am/libs.am
/usr/share/%{name}-%{version}/am/mans.am
/usr/share/%{name}-%{version}/am/program.am
/usr/share/%{name}-%{version}/am/lisp.am
/usr/share/%{name}-%{version}/am/lang-compile.am
/usr/share/%{name}-%{version}/am/ltlibrary.am
/usr/share/%{name}-%{version}/am/clean-hdr.am
/usr/share/%{name}-%{version}/am/depend2.am
/usr/share/%{name}-%{version}/am/check.am
/usr/share/%{name}-%{version}/am/clean.am
/usr/share/%{name}-%{version}/am/subdirs.am
/usr/share/%{name}-%{version}/am/tags.am
/usr/share/%{name}-%{version}/am/footer.am
/usr/share/%{name}-%{version}/am/python.am
/usr/share/aclocal/README
/usr/share/aclocal-%{version}/depend.m4
/usr/share/aclocal-%{version}/obsolete.m4
/usr/share/aclocal-%{version}/ar-lib.m4
/usr/share/aclocal-%{version}/depout.m4
/usr/share/aclocal-%{version}/auxdir.m4
/usr/share/aclocal-%{version}/prog-cc-c-o.m4
/usr/share/aclocal-%{version}/as.m4
/usr/share/aclocal-%{version}/maintainer.m4
/usr/share/aclocal-%{version}/options.m4
/usr/share/aclocal-%{version}/mkdirp.m4
/usr/share/aclocal-%{version}/lead-dot.m4
/usr/share/aclocal-%{version}/gcj.m4
/usr/share/aclocal-%{version}/dmalloc.m4
/usr/share/aclocal-%{version}/amversion.m4
/usr/share/aclocal-%{version}/init.m4
/usr/share/aclocal-%{version}/vala.m4
/usr/share/aclocal-%{version}/sanity.m4
/usr/share/aclocal-%{version}/python.m4
/usr/share/aclocal-%{version}/silent.m4
/usr/share/aclocal-%{version}/lex.m4
/usr/share/aclocal-%{version}/strip.m4
/usr/share/aclocal-%{version}/install-sh.m4
/usr/share/aclocal-%{version}/extra-recurs.m4
/usr/share/aclocal-%{version}/substnot.m4
/usr/share/aclocal-%{version}/lispdir.m4
/usr/share/aclocal-%{version}/make.m4
/usr/share/aclocal-%{version}/cond.m4
/usr/share/aclocal-%{version}/upc.m4
/usr/share/aclocal-%{version}/cond-if.m4
/usr/share/aclocal-%{version}/runlog.m4
/usr/share/aclocal-%{version}/tar.m4
/usr/share/aclocal-%{version}/missing.m4
/usr/share/aclocal-%{version}/internal/ac-config-macro-dirs.m4
%dir /usr/share/aclocal-%{version}
%dir /usr/share/aclocal-%{version}/internal
%dir /usr/share/%{name}-%{version}
%dir /usr/share/%{name}-%{version}/Automake
%dir /usr/share/%{name}-%{version}/am

%changelog
