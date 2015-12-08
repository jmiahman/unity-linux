Summary: X.Org X11 Autotools macros
Name: util-macros
Version: 1.19.0
Release: 4%{?dist}
License: MIT
Group: Development/System
URL: http://www.x.org
BuildArch: noarch
Source0:  ftp://ftp.x.org/pub/individual/util/%{name}-%{version}.tar.bz2
Requires: autoconf automake libtool 

%description
X.Org X11 autotools macros required for building the various packages that
comprise the X Window System.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/
mv %{buildroot}%{_datadir}/pkgconfig/xorg-macros.pc %{buildroot}%{_libdir}/pkgconfig/xorg-macros.pc

%files
%defattr(-,root,root,-)
#%doc COPYING ChangeLog
%{_datadir}/aclocal/xorg-macros.m4
%{_libdir}/pkgconfig/xorg-macros.pc
%{_datadir}/util-macros

%changelog
