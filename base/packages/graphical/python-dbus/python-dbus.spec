%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
#%{!?python3_sitearch: %global python3_sitearch %(python3 -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

#
# Conditional build:
%bcond_without  python2         # Python 2.x module
%bcond_with     python3         # Python 3.x module
#
%define		rname		dbus-python
#
Summary:	Python library for using D-BUS
Name:		python-dbus
Version:	1.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://dbus.freedesktop.org/releases/dbus-python/%{rname}-%{version}.tar.gz
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	cpp
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_python2:BuildRequires:	python-devel}
%{?with_python3:BuildRequires:	python3-devel}
BuildRequires:	rpm-build
Requires:	dbus-glib
Requires:	dbus-libs
Requires:	python-lxml

%description
D-BUS add-on library to integrate the standard D-BUS library with
Python.

%package devel
Summary:	C API for _dbus_bindings module
License:	AFL v2.1 or LGPL v2.1
Group:		Development/Libraries
Requires:	dbus-devel

%description devel
C API for _dbus_bindings module.

%package -n python3-dbus
Summary:	Python 3 library for using D-BUS
Group:		Libraries/Python
Requires:	dbus-glib
Requires:	dbus-libs

%description -n python3-dbus
D-BUS add-on library to integrate the standard D-BUS library with
Python 3.

%prep
%setup -qn %{rname}-%{version}

%build

%if %{with python3}
mkdir py3
cd py3
../configure \
	--prefix=/usr
	PYTHON=%{__python3} \
	PYTHON_LIBS=-lpython3
%{__make}
cd ..
%endif

%if %{with python2}
mkdir py2
cd py2
../configure \
	--prefix=/usr
	PYTHON=%{__python} \
	PYTHON_LIBS=-lpython
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

# use sitedir instead of sitescriptdir to match PyQt4 dbus/mainloop dir
%if %{with python2}
%{__make} -C py2 install \
	pythondir=%{python_sitearch} \
	DESTDIR=$RPM_BUILD_ROOT

%endif

%if %{with python3}
%{__make} -C py3 install \
	pythondir=%{python3_sitearch} \
	DESTDIR=$RPM_BUILD_ROOT

%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README doc/*.txt
%dir %{python_sitearch}/dbus
%{python_sitearch}/dbus/*.py[co]
%dir %{python_sitearch}/dbus/mainloop
%{python_sitearch}/dbus/mainloop/*.py[co]
%attr(755,root,root) %{python_sitearch}/_dbus_bindings.so
%attr(755,root,root) %{python_sitearch}/_dbus_glib_bindings.so
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%if %{with python3}
%files -n python3-dbus
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README doc/*.txt
%dir %{python3_sitearch}/dbus
%{python3_sitearch}/dbus/__pycache__
%{python3_sitearch}/dbus/*.py
%dir %{python3_sitearch}/dbus/mainloop
%{python3_sitearch}/dbus/mainloop/__pycache__
%{python3_sitearch}/dbus/mainloop/*.py
%attr(755,root,root) %{python3_sitearch}/_dbus_bindings.so
%attr(755,root,root) %{python3_sitearch}/_dbus_glib_bindings.so
%endif

%changelog
