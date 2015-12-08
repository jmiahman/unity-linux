%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global upstream_name Pygments
%global _first_letter %(echo %{upstream_name}|cut -c1 )

Name:           python-%{upstream_name}
Version:        1.6
Release:        1%{?dist}
Summary:        A syntax highlighting package written in Python.
Group:          Development/Languages

License:    BSD
URL:        http://pygments.org/
Source0:    http://pypi.python.org/packages/source/%{_first_letter}/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  python-devel python-setuptools
Requires:  python

#%filter_provides_in %{python_sitearch}/
#%filter_setup

%description
A syntax highlighting package written in Python.

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
