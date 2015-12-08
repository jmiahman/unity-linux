%global prever b1
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python2_shortver: %global python2_shortver %(python -c 'import sys; print(str(sys.version_info.major) + "." + str(sys.version_info.minor))')}

# tracer.so is a private object, don't include it in the provides
#%global _use_internal_dependency_generator 0
#%global __find_provides /bin/sh -c "%{_rpmconfigdir}/find-provides | grep -v -E '(tracer.so)' || /bin/true"
#%global __find_requires /bin/sh -c "%{_rpmconfigdir}/find-requires | grep -v -E '(tracer.so)' || /bin/true"

Name:           python-coverage
Summary:        Code coverage testing module for Python
Version:        4.0
Release:        0.1.%{?prever}%{?dist}
License:        BSD and (MIT or GPLv2)
Group:          System Environment/Libraries
URL:            http://nedbatchelder.com/code/modules/coverage.html
Source0:        http://pypi.python.org/packages/source/c/coverage/coverage-%{version}%{?prever}.tar.gz
BuildRequires:  python-setuptools, python-devel
Requires:       python-setuptools
Provides:	python-coverage = %{version}-%{release}

%description
Coverage.py is a Python module that measures code coverage during Python 
execution. It uses the code analysis tools and tracing hooks provided in the 
Python standard library to determine which lines are executable, and which 
have been executed.

%prep
%setup -q -n coverage-%{version}%{?prever}

find . -type f -exec chmod 0644 \{\} \;
sed -i 's/\r//g' README.txt

%build
python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --skip-build --root %{buildroot}

# rename binaries, make compat symlinks
cd %{buildroot}%{_bindir}
mv coverage python-coverage

rm -rf coverage-2* coverage2

for i in python2-coverage coverage coverage2 coverage-%{?python2_shortver}; do
  ln -s python-coverage $i
done
cd ..

%files
#%doc README.txt
%{_bindir}/coverage
%{_bindir}/coverage2
%{_bindir}/coverage-2*
%{_bindir}/python-coverage
%{_bindir}/python2-coverage
%{python_sitearch}/coverage/
%{python_sitearch}/coverage*.egg-info/

%changelog
