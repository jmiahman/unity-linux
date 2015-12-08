Name:		tzdata	
Version:	2015f
%define 	_tzcodever 2013g
%define 	_ptzver 0.3
Release:	1%{?dist}
Summary:	Timezone data	

Group:		System Environment/Base
License:	Public Domain
URL:		https://www.iana.org/time-zones
Source0:	http://www.iana.org/time-zones/repository/releases/tzcode%{_tzcodever}.tar.gz	
Source1:	http://www.iana.org/time-zones/repository/releases/tzdata%{version}.tar.gz
Source2:	http://dev.alpinelinux.org/archive/posixtz/posixtz-%{_ptzver}.tar.bz2

Patch0:		0001-posixtz-fix-up-lseek.patch
Patch1:		Makefile.patch

#BuildRequires:	
#Requires:	

%description
This package contains data files with rules for various timezones around
the world.


%prep
%setup -c -T -b 0
%setup -T -D -c -b 1 -n tzdata-%{version}
%setup -T -D -b 2 -n posixtz-%{_ptzver}

cd %{_builddir}/
%patch0 -p1

cd %{_builddir}/tzdata-%{version}
%patch1 -p1

%build
cd %{_builddir}/tzdata-%{version}
make CFLAGS="$CFLAGS -DHAVE_STDINT_H=1"

cd %{_builddir}/posixtz-%{_ptzver}
make posixtz

%install
cd %{_builddir}/tzdata-%{version}
make DESTDIR=%{buildroot} install

rm -f %{builddir}/usr/share/zoneinfo/localtime
rm %{buildroot}/usr/bin/tzselect
install -Dm755 %{_builddir}/posixtz-%{_ptzver}/posixtz \
	%{buildroot}/usr/bin/posixtz

%files
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*
%{_datadir}/zoneinfo
%dir %{_datadir}/zoneinfo
%{_datadir}/zoneinfo/posix
%dir %{_datadir}/zoneinfo/posix
%changelog

