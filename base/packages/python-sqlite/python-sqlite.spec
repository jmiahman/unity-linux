%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define		module	sqlite
Summary:	A DB API v2.0 compatible interface to SQLite
Name:		python-%{module}
Version:	2.6.3
Release:	1
License:	zlib/libpng
Group:		Development/Languages/Python
Source0:	http://pysqlite.googlecode.com/files/pysqlite-%{version}.tar.gz
# Source0-md5:	711afa1062a1d2c4a67acdf02a33d86e
URL:		http://pysqlite.googlecode.com/
BuildRequires:	python-devel
BuildRequires:	sqlite-devel
Provides:	python(sqlite)

%description
This is an extension module for the SQLite embedded relational
database. It tries to conform to the Python DB-API Spec v2 as far as
possible. One problem is that SQLite returns everything as text. This
is a result of SQLite's internal representation of data, however it
still may be possible to return data in the type specified by the
table definitions.

%prep
%setup -q -n pysqlite-%{version}

%build
#CFLAGS="%{rpmcflags}" \
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{python_sitearch},%{_examplesdir}/%{name}-%{version}}

PYTHONPATH=$RPM_BUILD_ROOT%{python_sitearch} \
	python setup.py install \
	--prefix=/usr \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{python_sitearch}/pysqlite2/test/py25
rm -rf $RPM_BUILD_ROOT%{python_sitearch}/pysqlite2/{,test/}*.py \
	$RPM_BUILD_ROOT%{_prefix}/pysqlite2-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc doc/*.txt
%dir %{python_sitearch}/pysqlite2
%{python_sitearch}/*.egg-info
%{python_sitearch}/pysqlite2/*.py[co]
%{python_sitearch}/pysqlite2/_%{module}.so
%dir %{python_sitearch}/pysqlite2/test
%{python_sitearch}/pysqlite2/test/*.py[co]
