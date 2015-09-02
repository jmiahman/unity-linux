%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-six
Version:        1.9.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/six/
Source0:        https://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
Provides:       python2-six = %{version}-%{release}

%description
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

%prep
%setup -q -n six-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}%{python_sitearch}
mkdir -p %{buildroot}%{python_sitearch}
python setup.py install --prefix=/usr --root=%{buildroot}

%files
#%{!?_licensedir:%global license %%doc}
#%license LICENSE
#%doc README documentation/index.rst
%{python_sitearch}/*

%changelog
