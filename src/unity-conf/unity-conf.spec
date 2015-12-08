%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64

Name:		unity-conf	
Version:	0.0.5
Release:	1%{?dist}
Summary:	Unity CLI configuration management scripts

Group:		Applications/System
License:	GPL
URL:		http://www.url.com
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	make
Requires:	blkid syslinux-extlinux
Requires:	tzdata sfdisk tar

%description
Unity CLI configuration management scripts

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%{_bindir}/*
/etc/*
%{_libdir}/*
%{_sbindir}/*


%changelog
* Tue Dec 08 2015 JMiahMan <JMiahMan@unity-linux.com> - 0.0.5-1
- Initial build for Unity-Linux
