%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name: python-pycairo
Version: 1.10.0
Release: 1%{?dist}
License: MPLv1.1 or LGPLv2
Group: Development/Languages
Summary: Python bindings for the cairo library
URL: http://cairographics.org/pycairo
Source: http://cairographics.org/releases/py2cairo-%{version}.tar.bz2

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cairo-devel
BuildRequires: libtool
BuildRequires: libxcb-devel
BuildRequires: pkgconfig
#BuildRequires: pytest
BuildRequires: python-devel
#BuildRequires: python-xpyb-devel
#BuildRequires: lyx-fonts
#Requires: python-xpyb

%description
Python bindings for the cairo library.

%package devel
Summary: Libraries and headers for pycairo
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: cairo-devel
Requires: pkgconfig
Requires: python-devel

%description devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with pycairo.

%prep
%setup -q -n py2cairo-%{version}
# fix broken tarball
touch ChangeLog
# we install examples into docdir, so remove executable bit
find examples -type f | xargs chmod -x

%build
# fix broken tarball
autoreconf -i
%configure --enable-xcb --enable-xpyb
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f

#%check
#cd test
#PYTHONPATH=$RPM_BUILD_ROOT%{python_sitearch} py.test

%files
%license COPYING*
%doc AUTHORS NEWS README
%doc examples doc/faq.rst doc/overview.rst doc/README
%{python_sitearch}/cairo/

%files devel
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/pycairo.pc

%changelog
* Wed Dec 09 2015 JMiahMan <JMiahMan@unity-linux.org> - 1.10.0-1
- Initial Build

