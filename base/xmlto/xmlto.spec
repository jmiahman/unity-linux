Summary:	A tool for converting XML files to various formats
Name:		xmlto
Version:	0.0.26
Release:	1%{?dist}
License:	GPL v2
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/x/m/xmlto/%{name}-%{version}.tar.gz
URL:		http://cyberelk.net/tim/software/xmlto/
BuildRequires:	docbook-xml
BuildRequires:	docbook-xsl
BuildRequires:	libxslt
BuildRequires:	util-linux
Requires:	docbook-xml
Requires:	docbook-xsl
Requires:	libxslt
# for getopt
Requires:	util-linux

%description
This is a package for converting XML files to various formats using
XSL stylesheets.

%prep
%setup -q

%build
./configure \
	--prefix=/usr \
	--mandir=/usr/share/man \

make -j1

%install
rm -rf $RPM_BUILD_ROOT

make -j1 DESTDIR=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xmlif
%attr(755,root,root) %{_bindir}/xmlto
%{_datadir}/%{name}
%{_mandir}/man1/xmlif.1*
%{_mandir}/man1/xmlto.1*
