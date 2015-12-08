%{!?python_sitearch: %global python_sitearch \
%(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary:	TDB - Trivial Database
Name:		tdb
Version:	1.3.7
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://www.samba.org/ftp/tdb/%{name}-%{version}.tar.gz

Patch0:		%{name}-fix-libreplace.patch

URL:		http://tdb.samba.org/
BuildRequires:	python-devel
BuildRequires:	rpm-build

%description
TDB is a Trivial Database. In concept, it is very much like GDBM, and
BSD's DB except that it allows multiple simultaneous writers and uses
locking internally to keep writers from trampling on each other. TDB
is also extremely small.

%package devel
Summary:	Header files for TDB library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for TDB library.

%package -n python-tdb
Summary:	Python bindings for TDB
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python

%description -n python-tdb
Python bindings for TDB.

%prep
%setup -q
%patch0 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--sysconfdir=/etc \
	--disable-rpath \
	--bundled-libraries=NONE \
	--builtin-libraries=replace \

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%triggerpostun -p /sbin/postshell -- tdb
#-rm -f %{_libdir}/libtdb.so.1
#/sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc docs/{README,mutex.txt,tracing.txt}
%attr(755,root,root) %{_bindir}/tdbbackup
%attr(755,root,root) %{_bindir}/tdbdump
%attr(755,root,root) %{_bindir}/tdbrestore
%attr(755,root,root) %{_bindir}/tdbtool
%attr(755,root,root) %{_libdir}/libtdb.so.*.*.*
%attr(755,root,root) %{_libdir}/libtdb.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtdb.so
%{_includedir}/tdb.h
%{_libdir}/pkgconfig/tdb.pc

%files -n python-tdb
%defattr(644,root,root,755)
%attr(755,root,root) %{python_sitearch}/tdb.so
%{python_sitearch}/_tdb_text.py
