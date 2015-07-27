Name:           m4
Version:        1.4.17 
Release:        1%{?dist}
Summary:        GNU macro processor

Group:          Applications/Text
License:        GPLv3+
URL:            http://www.gnu.org/software/m4/
Source0:        http://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz

#BuildRequires:  
#Requires:       

%description
A GNU implementation of the traditional UNIX macro processor.  M4 is
useful for writing text files which can be logically parsed, and is used
by many programs as part of their build process.  M4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts, but
not for running configure scripts.

%prep
%setup -q
chmod 644 COPYING

%build
export LIBS="-lrt" 
./configure \
	--build=%{_build} \
	--host=%{_host} \
	--prefix=/usr \
										make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/lib/charset.alias

%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/m4
%{_infodir}/*
%{_mandir}/man1/m4.1*


%changelog
