Summary: an X.Org utility for making makefile dependencies
Name: makedepend
Version: 1.0.4
Release: 1%{?dist}
License: MIT
Group: Development/System
URL: http://www.x.org
BuildArch: noarch
Source0:  ftp://ftp.x.org/pub/individual/util/%{name}-%{version}.tar.bz2
Requires: autoconf automake libtool 

%description
%{name} is an X.Org utility for making makefile dependencies.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%defattr(-,root,root,-)
#%doc COPYING ChangeLog
%{_bindir}/*
#%{_datadir}/man/man1/%{name}

%changelog
