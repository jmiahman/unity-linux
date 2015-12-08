%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global upstream_name MarkupSafe
%global _first_letter %(echo %{upstream_name}|cut -c1 )

Name:           python-markupsafe
Version:        0.18
Release:        1%{?dist}
Summary:        Implements a XML/HTML/XHTML Markup safe string
Group:          Development/Languages

License:    BSD
URL:        https://github.com/mitsuhiko/markupsafe
Source0:    http://pypi.python.org/packages/source/%{_first_letter}/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  python-devel python-setuptools
Requires:  python

#%filter_provides_in %{python_sitearch}/
#%filter_setup

%description
Implements a XML/HTML/XHTML Markup safe string

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
