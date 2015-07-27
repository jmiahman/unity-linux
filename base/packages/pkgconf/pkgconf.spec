Name:		pkgconf		
Version:	0.9.11
Release:	1%{?dist}
Summary:	development framework configuration tools

Group:		Development/Tools
License:	ISC
URL:		https://github.com/pkgconf/pkgconf
Source0:	http://rabbit.dereferenced.org/~nenolod/distfiles/pkgconf-%{version}.tar.bz2

#BuildRequires:	
#Requires:	

%description


%prep
%setup -q


%build
./configure \
	--build=%{_build} \
	--host=%{_host} \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var 

%make
%make check

%install
%make_install
%__ln -s pkgconf $RPM_BUILD_ROOT/usr/bin/pkg-config

%files
%{_bindir}/pkgconf
%{_bindir}/pkg-config
/usr/share/aclocal/pkg.m4

%changelog
