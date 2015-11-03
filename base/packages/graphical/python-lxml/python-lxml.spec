%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
#%{!?python3_sitearch: %global python3_sitearch %(python3 -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
#
# Conditional build:
%bcond_with	apidocs		# do not build and package API docs
%bcond_without	python2		# Python 2 package
%bcond_with	python3		# Python 3 package

%define		module	lxml
Summary:	Python 2 binding for the libxml2 and libxslt libraries
Name:		python-%{module}
Version:	3.4.4
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://lxml.de/files/%{module}-%{version}.tgz
URL:		http://lxml.de/
BuildRequires:	libxml2-devel 
BuildRequires:	libxslt-devel
%if %{with python2}
BuildRequires:	python-devel
%endif
%if %{with python3}
BuildRequires:	python3-Cython
BuildRequires:	python3-devel
%endif
BuildRequires:	rpm-build

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries.

%package -n python3-%{module}
Summary:	Python 3 binding for the libxml2 and libxslt libraries
Group:		Libraries/Python

%description -n python3-%{module}
lxml is a Pythonic binding for the libxml2 and libxslt libraries.


%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build
%endif
%if %{with python3}
%{__python3} setup.py build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%endif

%if %{with python3}
%{__python3} setup.py \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%endif

# cleanup for packaging
rm -rf docs
cp -a doc docs
# apidocs packaged separately
rm -rf docs/html
# build docs not useful at runtime
rm docs/build.txt

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc docs/* CHANGES.txt CREDITS.txt LICENSES.txt README.rst TODO.txt
%dir %{python_sitearch}/lxml
%{python_sitearch}/lxml/*.py[co]
%{python_sitearch}/lxml/lxml.etree*.h
%{python_sitearch}/lxml/includes
%{python_sitearch}/lxml/isoschematron
%dir %{python_sitearch}/lxml/html
%{python_sitearch}/lxml/html/*.py[co]
%attr(755,root,root) %{python_sitearch}/lxml/etree.so
%attr(755,root,root) %{python_sitearch}/lxml/objectify.so
%{python_sitearch}/lxml-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc docs/* CHANGES.txt CREDITS.txt LICENSES.txt README.rst TODO.txt
%dir %{python3_sitearch}/lxml
%attr(755,root,root) %{python3_sitearch}/lxml/etree.cpython-*.so
%attr(755,root,root) %{python3_sitearch}/lxml/objectify.cpython-*.so
%{python3_sitearch}/lxml/*.py
%{python3_sitearch}/lxml/__pycache__
%{python3_sitearch}/lxml/lxml.etree*.h
%{python3_sitearch}/lxml/includes
%{python3_sitearch}/lxml/isoschematron
%{python3_sitearch}/lxml/html
%{python3_sitearch}/lxml-*.egg-info
%endif

%changelog
