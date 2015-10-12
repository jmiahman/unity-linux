Name:		xcb-utils	
Version:	0.4.0
Release:	1%{?dist}
Summary:	Utility libraries for XC Binding

Group:		
License:	
URL:		
Source0:	

BuildRequires:	
Requires:	

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

