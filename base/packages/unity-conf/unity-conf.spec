Name:		unity-conf	
Version:	001
Release:	1%{?dist}
Summary:	Some configure scripts

Group:		None
License:	GPL
URL:		http://www.url.com
Source0:	%{name}-%{version}.tar.gz

#BuildRequires:	
#Requires:	

%description
Stuff


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog
