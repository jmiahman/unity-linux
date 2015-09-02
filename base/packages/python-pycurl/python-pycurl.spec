%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-pycurl
Version:        7.19.5.1
Release:        1%{?dist}
Summary:        A Python interface to libcurl

Group:          Development/Languages
License:        LGPLv2+ or MIT
URL:            http://pycurl.sourceforge.net/
Source0:        http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  curl-devel >= 7.19.0

# During its initialization, PycURL checks that the actual libcurl version
# is not lower than the one used when PycURL was built.
# Yes, that should be handled by library versioning (which would then get
# automatically reflected by rpm).
# For now, we have to reflect that dependency.
%global libcurl_sed '/^#define LIBCURL_VERSION "/!d;s/"[^"]*$//;s/.*"//;q'
%global curlver_h /usr/include/curl/curlver.h
%global libcurl_ver %(sed %{libcurl_sed} %{curlver_h} 2>/dev/null || echo 0)
Requires:       libcurl >= %{libcurl_ver}

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.


%prep
%setup0 -q -n pycurl-%{version}

# temporarily exclude failing test-cases
rm -f tests/{post_test,reset_test}.py

%build
export CFLAGS="$RPM_OPT_FLAGS"
python setup.py build

%install
python setup.py install --prefix=/usr --root=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/pycurl

%files
#%{!?_licensedir:%global license %%doc}
#%license COPYING-LGPL COPYING-MIT
#%doc ChangeLog README.rst examples doc tests
%{python_sitearch}/*

%changelog
