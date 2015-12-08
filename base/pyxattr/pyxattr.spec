Name:		pyxattr
Summary:	Extended attributes library wrapper for Python
Version:	0.5.3
Release:	1%{?dist}
License:	LGPLv2+
Group:		Development/Libraries
URL:		http://pyxattr.k1024.org/
Source:		https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
#Patch0:		0001-use-Py_ssize_t.patch
BuildRequires:	libattr-devel
BuildRequires:	python-devel, python-setuptools

%description
Python extension module wrapper for libattr. It allows to query, list,
add and remove extended attributes from files and directories.

%prep
%setup -q
#%patch0 -p1

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root="%{buildroot}" --prefix="%{_prefix}"


%check
python setup.py test

%files
%defattr(0644,root,root,0755)
%{python2_sitearch}/xattr.so
%{python2_sitearch}/*egg-info
#%license COPYING
#%doc NEWS README

%changelog
