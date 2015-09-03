%global libsolv_version 0.6.4-1

Name:		hawkey
Version:	0.6.0
Release:	1%{?snapshot}%{?dist}
Summary:	Library providing simplified C and Python API to libsolv
Group:		System Environment/Libraries
License:	LGPLv2+
URL:		https://github.com/rpm-software-management/%{name}
# git clone https://github.com/rpm-software-management/hawkey.git && cd hawkey && tito build --tgz
#https://github.com/rpm-software-management/hawkey/archive/hawkey-0.6.0-1.tar.gz
Source0:	https://github.com/rpm-software-management/%{name}/archive/%{name}-%{version}-1.tar.gz

Patch0:		hawkey-0.6.0-musl-add-ipc_h.patch

BuildRequires:	libsolv-devel >= %{libsolv_version}
BuildRequires:	cmake expat-devel rpm-devel zlib-devel check-devel
Requires:	libsolv >= %{libsolv_version}

# prevent provides from nonstandard paths:
#%filter_provides_in %{python_sitearch}/.*\.so$
# filter out _hawkey_testmodule.so DT_NEEDED _hawkeymodule.so:
#%filter_requires_in %{python_sitearch}/hawkey/test/.*\.so$
#%filter_setup

%description
A Library providing simplified C and Python API to libsolv.

%package devel
Summary:	A Library providing simplified C and Python API to libsolv
Group:		Development/Libraries
Requires:	hawkey = %{version}-%{release}
Requires:	libsolv-devel

%description devel
Development files for hawkey.

%package -n python-hawkey
Summary:	Python 2 bindings for the hawkey library
Group:		Development/Languages
BuildRequires:  python-devel
BuildRequires:  python-nose
BuildRequires:	python-sphinx
Requires:	%{name} = %{version}-%{release}

%description -n python-hawkey
Python 2 bindings for the hawkey library.

%prep
%setup -q -n %{name}-%{name}-%{version}-1
%patch0 -p1

%build
rm -rf %{buildroot}
export LC_ALL=en_US.UTF-8
export CFLAGS="$CFLAGS -std=gnu99"
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make %{?_smp_mflags}
make doc-man

#%check
#make ARGS="-V" test

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_libdir}/
mv %{buildroot}/usr/lib64/* %{buildroot}/usr/lib/
rm -rf %{buildroot}/usr/lib64

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%doc COPYING README.rst
%{_libdir}/libhawkey.so.*

%files devel
%{_libdir}/libhawkey.so
%{_libdir}/pkgconfig/hawkey.pc
%{_includedir}/hawkey/
#%{_mandir}/man3/hawkey.3.gz

%files -n python-hawkey
%{python_sitearch}/

%changelog
