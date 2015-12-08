%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global upstream_name setuptools

Name:           python-setuptools
Version:        1.1.7
Release:        1%{?dist}
Summary:        A collection of enhancements to the Python distutils
Group:          Development/Languages

License:    PSF
URL:        http://pypi.python.org/pypi/setuptools
Source0:    http://pypi.python.org/packages/source/s/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  python-devel
Requires:  python

#%filter_provides_in %{python_sitearch}/
#%filter_setup

%description
A collection of enhancements to the Python distutils

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=/usr --root=%{buildroot}
# we don't provide a non-suffixed easy_install
echo "Removing non-suffixed easy_install ( $pkgdir/usr/bin/easy_install)"
rm %{buildroot}/usr/bin/easy_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc README PKG-INFO examples tests
#%{!?_licensedir:%global license %%doc}
%{python_sitearch}/*

%changelog
