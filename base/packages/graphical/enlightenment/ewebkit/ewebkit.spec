#
# Conditional build:
%bcond_with	elementary	# MiniBrowser build (needs Elementary); not installed anyway
#
%define		efl_ver	1.8
%define		rel 4
Summary:	WebKit-EFL - Web content engine for EFL applications
Name:		ewebkit
Version:	0.1.0
%define	svnrev	164189
%define	subver	r%{svnrev}
Release:	0.%{subver}.%{rel}
License:	BSD
Group:		Libraries
#Source0:	webkit-%{subver}.tar.xz
# official snapshots
Source0:	http://download.enlightenment.org/rel/libs/webkit-efl/webkit-efl-%{svnrev}.tar.xz
# Source0-md5:	731513fc042ec8e03840bc1ab6a66771
Patch0:		%{name}-lib.patch
Patch1:		%{name}-werror.patch
Patch2:		%{name}-include.patch
Patch3:		%{name}-build.patch
Patch4:		%{name}-x32.patch
Patch5:		%{name}-glib.patch
Patch6:		%{name}-link.patch
Patch7:		gstreamer-headers.patch
URL:		http://trac.enlightenment.org/e/wiki/EWebKit
BuildRequires:	mesa-libgl-devel
BuildRequires:	atk-devel >= 2.10.0
BuildRequires:	bison >= 2.4.1
BuildRequires:	cairo-devel >= 1.10.2
BuildRequires:	cmake >= 2.8.3
BuildRequires:	dbus-devel
BuildRequires:	e_dbus-devel >= 1.7
BuildRequires:	ecore-devel >= %{efl_ver}
BuildRequires:	ecore-evas-devel >= %{efl_ver}
BuildRequires:	ecore-file-devel >= %{efl_ver}
BuildRequires:	ecore-imf-devel >= %{efl_ver}
BuildRequires:	ecore-imf-evas-devel >= %{efl_ver}
BuildRequires:	ecore-input-devel >= %{efl_ver}
BuildRequires:	ecore-x-devel >= %{efl_ver}
BuildRequires:	edje >= %{efl_ver}
BuildRequires:	edje-devel >= %{efl_ver}
BuildRequires:	eet-devel >= %{efl_ver}
BuildRequires:	eeze-devel >= %{efl_ver}
BuildRequires:	efreet-devel >= %{efl_ver}
BuildRequires:	eina-devel >= %{efl_ver}
%{?with_elementary:BuildRequires:	elementary-devel >= %{efl_ver}}
BuildRequires:	enchant-devel
BuildRequires:	eo-devel >= %{efl_ver}
BuildRequires:	evas-devel >= %{efl_ver}
BuildRequires:	flex >= 2.5.34
BuildRequires:	fontconfig-devel >= 2.8.0
BuildRequires:	freetype-devel >= 2.4.2
BuildRequires:	glib-devel >= 2.36.0
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.0.5
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.5
#BuildRequires:	gtk+2-devel >= 2.10
BuildRequires:	harfbuzz-devel >= 0.9.18
BuildRequires:	harfbuzz-icu-devel >= 0.9.18
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	pango-devel
BuildRequires:	perl >= 5.10.0
BuildRequires:	python >= 2.6.0
BuildRequires:	ruby >= 1.8.7
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	atk >= 2.10.0
Requires:	cairo >= 1.10.2
Requires:	e_dbus >= 1.7
Requires:	ecore >= %{efl_ver}
Requires:	ecore-evas >= %{efl_ver}
Requires:	ecore-file >= %{efl_ver}
Requires:	ecore-imf >= %{efl_ver}
Requires:	ecore-imf-evas >= %{efl_ver}
Requires:	ecore-input >= %{efl_ver}
Requires:	ecore-x >= %{efl_ver}
Requires:	edje-libs >= %{efl_ver}
Requires:	efreet >= %{efl_ver}
Requires:	eeze >= %{efl_ver}
Requires:	eina >= %{efl_ver}
Requires:	evas >= %{efl_ver}
Requires:	fontconfig-libs >= 2.8.0
Requires:	freetype >= 2.1.0
Requires:	glib >= 2.36.0
Requires:	gstreamer >= 1.0.5
Requires:	gstreamer-plugins-base >= 1.0.5
Requires:	harfbuzz >= 0.9.18
Requires:	harfbuzz-icu >= 0.9.18
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7

# __once_call, __once_called non-function symbols from libstdc++
%define		skip_post_check_so	libewebkit.*

%description
WebKit-EFL - Web content engine for EFL applications.

%package devel
Summary:	Header files for WebKit-EFL library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.10.2
Requires:	ecore-devel >= 1.2.0
Requires:	ecore-input-devel >= 1.2.0
Requires:	evas-devel >= 1.0.0
Requires:	harfbuzz-devel
Requires:	libsoup-devel >= 2.42.0
Requires:	libstdc++-devel

%description devel
Header files for WebKit-EFL library.

%prep
%setup -q -n efl-webkit
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
# replace -g2 with -g1 to not run into 4 GB ar format limit
# https://bugs.webkit.org/show_bug.cgi?id=91154
# http://sourceware.org/bugzilla/show_bug.cgi?id=14625
CFLAGS="%(echo %{rpmcflags} | sed 's/ -g2/ -g1/g')"
CXXFLAGS="%(echo %{rpmcxxflags} | sed 's/ -g2/ -g1/g') -Wno-deprecated-declarations"
%cmake . \
%ifarch x32
	-DENABLE_JIT=OFF \
%endif
	-DPORT=Efl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog Source/WebKit/LICENSE
%attr(755,root,root) %{_bindir}/PluginProcess
%attr(755,root,root) %{_bindir}/WebProcess
%attr(755,root,root) %{_libdir}/libewebkit.so.*.*.*
%attr(755,root,root) %{_libdir}/libewebkit.so.0
%attr(755,root,root) %{_libdir}/libewebkit2.so.*.*.*
%attr(755,root,root) %{_libdir}/libewebkit2.so.0
%{_datadir}/ewebkit-0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libewebkit.so
%attr(755,root,root) %{_libdir}/libewebkit2.so
%{_includedir}/ewebkit-0
%{_includedir}/ewebkit2-0
%{_libdir}/pkgconfig/ewebkit.pc
%{_libdir}/pkgconfig/ewebkit2.pc
%{_libdir}/cmake/EWebKit
%{_libdir}/cmake/EWebKit2

%changelog

