Name:		unity-conf	
Version:	0.0.4
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
%make_install


%files
/bin/*
/etc/*
/lib/*
/sbin/*


%changelog
