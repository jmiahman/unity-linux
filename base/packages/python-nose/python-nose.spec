%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_version: %global python_version %(echo `python -c "import sys; print(sys.version)"` | cut -d '.' -f1-2)}

%global upstream_name nose

# Enable building without docs to avoid a circular dependency between this and python-sphinx
%global with_docs 0

Name:           python-nose
Version:        1.3.7
Release:        1%{?dist}
Summary:        Discovery-based unittest extension for Python

Group:          Development/Languages
License:        LGPLv2+ and Public Domain
URL:            http://somethingaboutorange.com/mrl/projects/nose/
Source0:        http://pypi.python.org/packages/source/n/nose/nose-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
Provides:       python-%{upstream_name} = %{version}-%{release}

BuildRequires:  python-setuptools
BuildRequires:  hd2u
BuildRequires:  python-coverage >= 3.4-1
Requires:       python-setuptools

%description
nose extends the test loading and running features of unittest, making
it easier to write, find and run tests.

By default, nose will run tests in files or directories under the
current working directory whose names include "test" or "Test" at a
word boundary (like "test_this" or "functional_test" or "TestClass"
but not "libtest"). Test output is similar to that of unittest, but
also includes captured stdout output from failing tests, for easy
print-style debugging.

These features, and many more, are customizable through the use of
plugins. Plugins included with nose provide support for doctest, code
coverage and profiling, flexible attribute-based test selection,
output capture and more.

%package docs
Summary:        Nose Documentation
Group:          Documentation
BuildRequires:  python-sphinx
Requires: python-nose

%description docs
Documentation for Nose

%prep
%setup -q -n %{upstream_name}-%{version}

dos2unix examples/attrib_plugin.py

%build
python setup.py build

%install
rm -rf %{buildroot}
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).

python setup.py install --skip-build --root %{buildroot} \
           --install-data=%{_datadir}

%if 0%{?with_docs}
pushd doc
make html
rm -rf .build/html/.buildinfo .build/html/_sources
mv .build/html ..
rm -rf .build
popd
%endif # with_docs
cp -a doc reST
rm -rf reST/.static reST/.templates


#%check
#python selftest.py

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
#%doc AUTHORS CHANGELOG lgpl.txt NEWS README.txt
%{_bindir}/nosetests
%{_bindir}/nosetests-%{python_version}
#%{_mandir}/man1/nosetests.1.gz
%{python_sitelib}/nose*

#%files docs
#%defattr(-,root,root,-)
##%doc reST examples
#%if 0%{?with_docs}
#%doc html
#%endif # with_docs

%changelog
