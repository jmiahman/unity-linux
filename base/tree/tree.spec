Name:		tree
Version:	1.6.0
Release:	1%{?dist}
Summary:	A recursive directory indented listing of files

Group: 		Applications/File
License:	GPL
URL:		http://mama.indstate.edu/users/ice/tree/
Source0:	http://mama.indstate.edu/users/ice/tree/src/%{name}-%{version}.tgz

BuildRequires: musl-devel
Requires: musl	

%description
Tree is a recursive directory indented
listing of files

%package docs
Summary:  Doc files for %{name}
Requires: %{name} = %{version}

%description docs
Documentation for tree, a recursive 
directory indented listing of files

%prep
%setup -q


%build

make %{?_smp_mflags}

%install
make prefix=%{buildroot}/usr MANDIR=%{buildroot}%{_datadir}/man/man1 install

%files
/usr/bin/tree

%files docs
%{_datadir}/man/man1/*

%changelog
