%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global upstream_name Jinja2
%global _first_letter %(echo %{upstream_name}|cut -c1 )

Name:           python-%{upstream_name}
Version:        2.7.3
Release:        1%{?dist}
Summary:        A small but fast and easy to use stand-alone python template engine
Group:          Development/Languages

License:    BSD
URL:        http://jinja.pocoo.org/
Source0:    http://pypi.python.org/packages/source/%{_first_letter}/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  python-devel python-setuptools
Requires:  python python-markupsafe

#%filter_provides_in %{python_sitearch}/
#%filter_setup

%description
A small but fast and easy to use stand-alone python template engine

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
