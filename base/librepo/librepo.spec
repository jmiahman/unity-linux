%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           librepo
Version:        1.7.15
Release:        1%{?dist}
Summary:        Repodata downloading library

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://github.com/Tojaj/librepo
# Use the following commands to generate the tarball:
#  git clone https://github.com/Tojaj/librepo.git
#  cd librepo
#  utils/make_tarball.sh %{gitrev}
Source0:        https://github.com/Tojaj/librepo/archive/librepo-%{version}.tar.gz

#BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  glib-devel
BuildRequires:  gpgme-devel
BuildRequires:  libattr-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel

# prevent provides from nonstandard paths:
#%filter_provides_in %{python_sitearch}/.*\.so$
#%filter_setup

%description
A library providing C and Python (libcURL like) API to downloading repository
metadata.

%package devel
Summary:        Repodata downloading library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for librepo.

%package -n python-librepo
Summary:        Python bindings for the librepo library
Group:          Development/Languages
BuildRequires:  pygpgme
BuildRequires:  python-devel
BuildRequires:  python-sphinx
BuildRequires:  pyxattr
Requires:       %{name} = %{version}-%{release}

%description -n python-librepo
Python bindings for the librepo library.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
rm -rf %{buildroot}
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mv %{buildroot}/usr/lib64/* %{buildroot}/usr/lib/
rm -rf %{buildroot}/usr/lib64

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%doc COPYING README.md
%{_libdir}/librepo.so.*

%files devel
%{_libdir}/librepo.so
%{_libdir}/pkgconfig/librepo.pc
%{_includedir}/librepo/

%files -n python-librepo
%{python_sitearch}/librepo/

%changelog
