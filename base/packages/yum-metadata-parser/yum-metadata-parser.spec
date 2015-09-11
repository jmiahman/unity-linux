%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary:	A fast metadata parser for yum
Name:		yum-metadata-parser
Version:	1.1.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://yum.baseurl.org/download/yum-metadata-parser/%{name}-%{version}.tar.gz
# Source0-md5:	05289971e5cfde532631f2a99f6c58c7
URL:		http://yum.baseurl.org/
BuildRequires:	glib-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel 
BuildRequires:	rpm-build
BuildRequires:	sqlite-devel
Requires:	python

%description
Fast metadata parser for yum implemented in C.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README AUTHORS ChangeLog
%{python_sitearch}/*.py*
%{python_sitearch}/*.egg-info
%attr(755,root,root) %{python_sitearch}/*.so

%changelog
