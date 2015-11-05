%bcond_with     static_libs     # don't build static library

Summary:	A JSON implementation in C
Name:		json-c
Version:	0.12
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://s3.amazonaws.com/json-c_releases/releases/%{name}-%{version}.tar.gz

Patch0: 	size-set-but-not-used.patch

URL:		https://github.com/json-c/json-c/wiki

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%package devel
Summary:	Header files for the json-c library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the json-c library.

%package static
Summary:	Static json-c library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static json-c library.

%prep
%setup -q
%patch0 -p1

%build
# avoid "json_tokener.c:355:6: error: variable 'size' set but not used [-Werror=unused-but-set-variable]"
CFLAGS="%{rpmcflags} -Wno-unused-but-set-variable"
./configure \
	--prefix=/usr \
	%{!?with_static_libs:--disable-static} \
	--enable-shared

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%pretrans devel
# transition from 0.11-2
[ ! -L %{_includedir}/json-c ] || rm -f %{_includedir}/json-c
# transition from <= 0.10 and 0.11-2
if [ -d %{_includedir}/json -a ! -d %{_includedir}/json-c ]; then
	mv -f %{_includedir}/json %{_includedir}/json-c
	ln -sf json-c %{_includedir}/json
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README README.html
%attr(755,root,root) %{_libdir}/libjson-c.so.*.*.*
%attr(755,root,root) %{_libdir}/libjson-c.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjson-c.so
%{_includedir}/json-c
%{_libdir}/pkgconfig/json-c.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libjson-c.a
%endif

%changelog
