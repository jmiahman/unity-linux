%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global upstream_name docutils

Name:           python-%{upstream_name}
Version:        0.12
Release:        1%{?dist}
Summary:        Documentation Utilities for Python
Group:          Development/Languages

License:    PublicDomain
URL:        http://docutils.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  python-devel python-setuptools
Requires:  python python-pillow python-roman

#%filter_provides_in %{python_sitearch}/
#%filter_setup

%description
Documentation Utilities for Python

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=/usr --root=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc README PKG-INFO examples tests
#%{!?_licensedir:%global license %%doc}
%{python_sitearch}/*

%changelog
