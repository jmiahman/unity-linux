Summary:	help2man - automatic manual page generation
Name:		help2man
Version:	1.47.2
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.debian.org/debian/pool/main/h/help2man/%{name}_%{version}.tar.xz
URL:		http://www.gnu.org/software/help2man/

BuildRequires:	perl
Requires:	perl

%description
help2man is a tool for automatically generating simple manual pages
from program output. This program is intended to provide an easy way
for software authors to include a manual page in their distribution
without having to maintain that document. Given a program which
produces reasonably standard `--help' and `--version' outputs,
help2man can re-arrange that output into something which resembles a
manual page.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%post	-p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

#%postun	-p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

%files 
%defattr(644,root,root,755)
%doc NEWS README THANKS debian/changelog
%attr(755,root,root) %{_bindir}/help2man
%{_infodir}/help2man.info*
%{_mandir}/man1/help2man.1*

%changelog
