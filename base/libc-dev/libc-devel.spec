Name:		libc-devel	
Version:	0.7
Release:	1%{?dist}
Summary:	Meta package to pull in correct libc and missing headers

Group:		Development/C	
License:	GPL
URL:		http://unity-linux.org
Source0:	sys-cdefs.h	
Source1:	sys-queue.h
Source2:	sys-tree.h

BuildRequires:	musl-devel
Requires:	musl-devel

%description
This is a meta package that pulls in the correct libc and some missing headers in Musl

%prep
#nothing here

%build
# Nothing here

%install
install -D %{SOURCE0} %{buildroot}/usr/include/sys/cdefs.h
install -D %{SOURCE1} %{buildroot}/usr/include/sys/queue.h
install -D %{SOURCE2} %{buildroot}/usr/include/sys/tree.h

%files
%{_includedir}/sys/*.h

%changelog

