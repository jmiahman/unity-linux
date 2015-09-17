Summary:	Utilities for managing processes on your system
Name:		psmisc
Version:	22.21
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/psmisc/%{name}-%{version}.tar.gz
# Source0-md5:	935c0fd6eb208288262b385fa656f1bf
URL:		http://psmisc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	ncurses-devel

%define		_bindir		/bin

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser. The pstree command displays a tree
structure of all of the running processes on your system. The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name. The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%prep
%setup -q

%build
./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --mandir=/usr/share/man \
    --infodir=/usr/share/info \
    --enable-timeout-stat \

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/fuser
%attr(755,root,root) %{_bindir}/killall
%attr(755,root,root) %{_bindir}/peekfd
%attr(755,root,root) %{_bindir}/prtstat
%attr(755,root,root) %{_bindir}/pstree
%attr(755,root,root) %{_bindir}/pstree.x11
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/peekfd.1*
%{_mandir}/man1/prtstat.1*
%{_mandir}/man1/pstree.1*

%changelog
