%define _target_platform %{_arch}-unity-linux-musl

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
Provides: pkgconfig

%description


%prep
%setup -q


%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var 

%make
%make check

%install
%__rm -rf %{buildroot}
%make_install
%__ln -s pkgconf $RPM_BUILD_ROOT/usr/bin/pkg-config
mkdir -p %{buildroot}/usr/lib/pkgconfig

%files
%dir /usr/lib/pkgconfig
%{_bindir}/pkgconf
%{_bindir}/pkg-config
/usr/share/aclocal/pkg.m4

%changelog
