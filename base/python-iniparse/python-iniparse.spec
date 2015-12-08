%{!?python_sitearch: %global python_sitearch \
%(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}


Name:           python-iniparse
Version:        0.4
Release:        1%{?dist}
Summary:        Python Module for Accessing and Modifying Configuration Data in INI files
Group:          Development/Libraries
License:        MIT and Python
URL:            http://code.google.com/p/iniparse/
Source0:        http://iniparse.googlecode.com/files/iniparse-%{version}.tar.gz
Patch0:         fix-issue-28.patch
# The patch upstream (http://code.google.com/p/iniparse/issues/detail?id=22)
# is Python3-only. The patch below uses python-six to create a version that works
# with both Python major versions and is more error-prone.

BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  python-devel
#BuildRequires:  python-test

Requires:       python-six

BuildArch: noarch

%description
iniparse is an INI parser for Python which is API compatible
with the standard library's ConfigParser, preserves structure of INI
files (order of sections & options, indentation, comments, and blank
lines are preserved when data is updated), and is more convenient to
use.

%prep
%setup -q -n iniparse-%{version}
%patch0 -p1
chmod -c -x html/index.html


%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT


python setup.py install --prefix=/usr --root=%{buildroot}
mv $RPM_BUILD_ROOT/usr/share/doc/iniparse-%{version} $RPM_BUILD_ROOT%{_pkgdocdir}

# Don't dupe the license
rm -rf $RPM_BUILD_ROOT%{_pkgdocdir}/LICENSE*
rm -rf $RPM_BUILD_ROOT%{_docdir}/python3-iniparse/LICENSE*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc %{_pkgdocdir}
#%{!?_licensedir:%global license %%doc}
#%license LICENSE LICENSE-PSF
%{python_sitearch}/*

%changelog
