%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global upstream_name Sphinx

Name:           python-sphinx
Version:        1.2.2
Release:        1%{?dist}
Summary:        Python documentation generator
Group:          Development/Languages

License:    BSD and Public Domain and Python and (MIT or GPLv2)
URL:        http://sphinx.pocoo.org/
Source0:    http://pypi.python.org/packages/source/S/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  python-devel python-setuptools
Requires:  gpgme-devel

#%filter_provides_in %{python_sitearch}/gpgme/_gpgme.so
#%filter_setup

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" python setup.py build

%install
python setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc README PKG-INFO examples tests
#%{!?_licensedir:%global license %%doc}
%{_bindir}/*
%{python_sitearch}/*

%changelog
