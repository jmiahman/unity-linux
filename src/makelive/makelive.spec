Name:		makelive	
Version:	0.0.2
Release:	1%{?dist}
Summary:	makelive script

Group:		System/Applications
License:	GPL
URL:		unity-linux
Source0:	%{name}-%{version}.tar.gz

Requires:	unity-conf cdrkit	

%description
Test Package

%prep
%setup -q

%build
#No build here!

%install
mkdir -p %{buildroot}/usr/share/makelive
cp %{_builddir}/%{name}-%{version}/* %{buildroot}/usr/share/makelive/ 

%files
%dir %{_datadir}/makelive
%{_datadir}/makelive/*

%changelog

