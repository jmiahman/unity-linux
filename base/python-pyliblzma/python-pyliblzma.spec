%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define 	module	pyliblzma
Summary:	Platform independent python bindings for the LZMA compression library
Name:		python-%{module}
Version:	0.5.3
Release:	1
License:	LGPL v3
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pyliblzma/%{module}-%{version}.tar.bz2
# Source0-md5:	500f61116ee1ab4063b49c121786863a
URL:		https://launchpad.net/pyliblzma
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	xz-devel

%description
PylibLZMA provides a python interface for the liblzma library to read
and write data that has been compressed or can be decompressed by
Lasse Collin's xz / lzma utils.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build \
	--debug

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{python_sitearch},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc NEWS README THANKS
%attr(755,root,root) %{python_sitearch}/*.so
%{python_sitearch}/*.py[co]
%{python_sitearch}/pyliblzma-*.egg-info
