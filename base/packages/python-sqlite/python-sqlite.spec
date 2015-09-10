%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-sqlite
Version:        2.6.3
Release:        1%{?dist}
Summary:        Python DB-API 2.0 interface for the SQLite
Group:          Development/Libraries
License:        MIT and Python
URL:            http://code.google.com/p/pysqlite/
Source0:        https://pypi.python.org/packages/source/p/pysqlite/pysqlite-%{version}.tar.gz

BuildRequires:  python-setuptools
BuildRequires:  sqlite-devel
BuildRequires:  python-devel

%description
Python DB-API 2.0 interface for the SQLite

%prep
%setup -q -n pysqlite-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --prefix=/usr --root=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc %{_pkgdocdir}
#%{!?_licensedir:%global license %%doc}
#%license LICENSE LICENSE-PSF
%{python_sitearch}/*

%changelog
