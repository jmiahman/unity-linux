Name:		texinfo	
Version:	5.2
Release:	1%{?dist}
Summary:	Tools needed to create Texinfo format documentation files

Group:		Applications/Publishing
License:	GPLv3+
URL:		http://www.gnu.org/software/texinfo/
Source0:	ftp://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.xz

#BuildRequires:	
#Requires:	

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
/usr/bin/*
/usr/share/texinfo/*
/usr/share/texinfo/Texinfo/*
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/*
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/*.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/*.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/*.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/Recode/*.pm
/usr/share/texinfo/lib/Unicode-EastAsianWidth/lib/Unicode/*.pm
/usr/share/texinfo/init/*.pm
/usr/share/texinfo/DebugTexinfo/*.pm
/usr/share/texinfo/Pod-Simple-Texinfo/Pod/Simple/*.pm

%changelog
