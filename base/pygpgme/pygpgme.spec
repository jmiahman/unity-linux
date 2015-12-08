%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           pygpgme
Version:        0.3
Release:        1%{?dist}
Summary:        Python module for working with OpenPGP messages

Group:          Development/Languages
License:        LGPL
URL:            https://pypi.python.org/pypi/pygpgme
Source0:        https://pypi.python.org/packages/source/p/pygpgme/pygpgme-0.3.tar.gz
Patch0:         pygpgme-pubkey-hash-algo.patch
Patch1:         pygpgme-no-encrypt-to.patch
BuildRequires:  python-devel
BuildRequires:  gpgme-devel

#%filter_provides_in %{python_sitearch}/gpgme/_gpgme.so
#%filter_setup

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%prep
%setup -q
%patch0 -p0 -b .pubkey-hash-algo
%patch1 -p0 -b .no-encrypt-to

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" python setup.py build

%install
python setup.py install --skip-build --root $RPM_BUILD_ROOT
chmod 0755 $RPM_BUILD_ROOT%{python_sitearch}/gpgme/_gpgme.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc README PKG-INFO examples tests
#%{!?_licensedir:%global license %%doc}
#%license lgpl-2.1.txt
%{python_sitearch}/*

%changelog
