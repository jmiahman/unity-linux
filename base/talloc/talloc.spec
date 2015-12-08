%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:		talloc
Version:	2.1.4
Release:	1%{?dist}
Summary:	The talloc library

Group:		System Environment/Daemons
License:	LGPLv3+
URL:		http://talloc.samba.org/
Source0:	http://samba.org/ftp/talloc/talloc-%{version}.tar.gz
Patch0:		always-libs.patch
Patch1:		fix-libreplace.patch
BuildRequires:	python-devel

%description
A library that implements a hierarchical allocator with destructors.

%package -n python-talloc
Group: Development/Libraries
Summary: Python bindings for the Talloc library
Requires: python
Requires: talloc = %{version}-%{release}

%description -n python-talloc
Python libraries for creating bindings using talloc

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%configure \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \
	--bundled-libraries=NONE \
	--builtin-libraries=replace \
	--disable-rpath \
	--disable-rpath-install \
	--without-gettext \

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libtalloc.so.*
%{_libdir}/libtalloc.so.*.*.*

%files -n python-talloc
%{python_sitearch}/*.so
%{_libdir}/libpytalloc-util.so.*
%{_libdir}/libpytalloc-util.so.*.*.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h

%changelog

