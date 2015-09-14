Name:		texinfo	
Version:	5.2
Release:	1%{?dist}
Summary:	Tools needed to create Texinfo format documentation files

Group:		Applications/Publishing
License:	GPLv3+
URL:		http://www.gnu.org/software/texinfo/
Source0:	ftp://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.xz

Provides:	info

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. The GNU
Project uses the Texinfo file format for most of its documentation.

Install texinfo if you want a documentation system for producing both
online and print documentation from the same source file and/or if you
are going to write documentation for the GNU Project.

%prep
%setup -q


%build
./configure \
	--build=%{_build} \
	--host=%{_host} \
	--prefix=/usr

make

%install
%make_install

rm -f ${RPM_BUILD_ROOT}/usr/share/info/dir
rm -rf ${RPM_BUILD_ROOT}/usr/lib/charset.alias

%files
%{bindir}/*
%{_datadir}/texinfo/*
%{_datadir}/texinfo/Texinfo/*
%{_datadir}/texinfo/lib/Text-Unidecode/lib/Text/*
%{_datadir}/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/*.pm
%{_datadir}/texinfo/lib/libintl-perl/lib/Locale/*.pm
%{_datadir}/texinfo/lib/libintl-perl/lib/Locale/RecodeData/*.pm
%{_datadir}/texinfo/lib/libintl-perl/lib/Locale/Recode/*.pm
%{_datadir}/texinfo/lib/Unicode-EastAsianWidth/lib/Unicode/*.pm
%{_datadir}/texinfo/init/*.pm
%{_datadir}/texinfo/DebugTexinfo/*.pm
%{_datadir}/texinfo/Pod-Simple-Texinfo/Pod/Simple/*.pm
%dir %{_datadir}/texinfo

%changelog
