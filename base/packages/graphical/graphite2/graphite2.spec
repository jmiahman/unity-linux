Summary:	Font rendering capabilities for complex non-Roman writing systems
Name:		graphite2
Version:	1.3.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tgz
# Source0-md5:	7cda6fc6bc197b216777b15ce52c38a8

Patch0:		cmake.patch  
Patch1:		graphite2-1.2.0-cmakepath.patch

URL:		http://graphite.sil.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
# the rest for tests only
BuildRequires:	freetype-devel
BuildRequires:	glib-devel
BuildRequires:	libicu-devel

%description
Graphite is a project within SIL's Non-Roman Script Initiative and
Language Software Development groups to provide rendering capabilities
for complex non-Roman writing systems. Graphite can be used to create
"smart fonts" capable of displaying writing systems with various
complex behaviors. With respect to the Text Encoding Model, Graphite
handles the "Rendering" aspect of writing system implementation.

%package devel
Summary:	Header files for graphite2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for graphite2 library.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build

cmake -G "Unix Makefiles" .. \
	-DCMAKE_C_FLAGS:STRING="${CFLAGS}" \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DGRAPHITE2_COMPARE_RENDERER=OFF \
	-DGRAPHITE2_NFILEFACE=ON \
	-DGRAPHITE2_NSEGCACHE=ON
# fix unwanted -O3 cflag (taken form Debian)
find . -type f ! -name "rules" ! -name "changelog" -exec sed -i -e 's/\-O3//g' {} \;

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# cmake's fake (with no dependencies); also obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgraphite2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*.txt
%attr(755,root,root) %{_libdir}/libgraphite2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite2.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgraphite2.so
%{_includedir}/graphite2
%{_libdir}/pkgconfig/graphite2.pc

%changelog
