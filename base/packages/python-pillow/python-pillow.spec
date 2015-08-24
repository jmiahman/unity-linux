%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global upstream_name Pillow
%global _first_letter %(echo %{upstream_name}|cut -c1 )

Name:           python-%{upstream_name}
Version:        2.8.1
Release:        1%{?dist}
Summary:	A Python Imaging Library 
Group:          Development/Languages

License:    BSD
URL:        http://python-imaging.github.io/
Source0:    http://pypi.python.org/packages/source/%{_first_letter}/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  python-devel python-setuptools libpng-devel
BuildRequires:	libjpeg-turbo-devel freetype-devel libtiff-devel
Buildrequires:	lcms2-devel
#libwebp-dev
#openjpeg-dev

Requires:  python

#%filter_provides_in %{python_sitearch}/
#%filter_setup

%description
A Python Imaging Library

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=/usr --root=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc README PKG-INFO examples tests
#%{!?_licensedir:%global license %%doc}
%{python_sitearch}/*

%changelog
