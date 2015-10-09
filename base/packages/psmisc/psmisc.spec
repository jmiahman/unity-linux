Summary:	Utilities for managing processes on your system
Name:		psmisc
Version:	22.21
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/psmisc/%{name}-%{version}.tar.gz

Patch0: 	psmisc-limits.patch

# Source0-md5:	935c0fd6eb208288262b385fa656f1bf
URL:		http://psmisc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	ncurses-devel

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser. The pstree command displays a tree
structure of all of the running processes on your system. The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name. The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%package docs                                                                               
Summary:        Docs for %{name}                                                  
License:        LGPL v2.1+                                                                  
Group:          Applications/System                                                         
Requires:       %{name} = %{version}-%{release}                                             
                                                                                            
%description docs                                                                           
Documentation files for the %{name} package

%prep
%setup -q
%patch0 -p1

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
%{_bindir}/fuser
%{_bindir}/killall
%{_bindir}/prtstat
%{_bindir}/pstree
%{_bindir}/pstree.x11

%files docs
%doc AUTHORS ChangeLog README
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/prtstat.1*
%{_mandir}/man1/pstree.1*

%changelog
