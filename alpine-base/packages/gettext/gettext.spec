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
Group:          Development/Tools

%description -n libintl
Libintl is a library that provides native language support to programs. It is part of Gettext.

%prep
%setup -q

%build
export LIBS="-lrt" 
./configure \
	--build=%{_build} \
	--host=%{_host} \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--enable-threads=posix \
	--disable-java \
	--disable-static
										%make

%install
make -j1 DESTDIR=$RPM_BUILD_ROOT install
%__rm $RPM_BUILD_ROOT/usr/lib/*.la

%files
%doc
/usr/bin/*
/usr/lib/*.so*
/usr/lib/gettext/*

%files -n libintl
/usr/lib/libintl.so.8.1.3
/usr/lib/libintl.so.8


%changelog
