#
# Conditional build:
%bcond_with	static_libs	# don't build static library
%bcond_with	xmms		# don't build XMMS plugin

%define         _aclocaldir     %{_datadir}/aclocal
%define         _pkgconfigdir   %{_libdir}/pkgconfig
%define         _docdir         %{_datadir}/doc

Summary:	Free Lossless Audio Codec
Name:		flac
Version:	1.3.1
Release:	1
License:	BSD (libFLAC/libFLAC++), GPL v2+ (programs and plugins)
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/flac/%{name}-%{version}.tar.xz
Patch0:		%{name}-sigemptyset.patch
URL:		http://xiph.org/flac/

BuildRequires:	gettext
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
%{?with_xmms:BuildRequires:	rpm-build}
BuildRequires:	tar
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRequires:	xz

%description
FLAC is an Open Source lossless audio codec developed by Josh Coalson.

%package devel
Summary:	FLAC - development files
License:	BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel

%description devel
The package contains the development header files for FLAC libraries.

%package static
Summary:	FLAC - static libraries
License:	BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The package contains FLAC static libraries.

%package c++
Summary:	FLAC++ - C++ API for FLAC codec
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
FLAC++ - C++ API for FLAC codec.

%description c++ -l pl.UTF-8
FLAC++ - API C++ do kodeka FLAC.

%package c++-devel
Summary:	Header files for FLAC++ library
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for FLAC++ library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FLAC++.

%package c++-static
Summary:	Static FLAC++ library
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static FLAC++ library.

%package -n xmms-input-flac
Summary:	Free Lossless Audio Codec - XMMS plugin
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description -n xmms-input-flac
FLAC input plugin for XMMS.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	%{!?with_xmms:--disable-xmms-plugin} \
	--enable-ogg \
	--disable-sse \
	--disable-rpath \
	--with-pic

%{__make}

rm -rf doc-html
cp -a doc/html doc-html
# no makefiles in doc dirs
find doc-html -name 'Makefile*' | xargs %{__rm}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{with xmms}
%{__rm} $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.a
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.Xiph README
%attr(755,root,root) %{_bindir}/flac
%attr(755,root,root) %{_bindir}/metaflac
%attr(755,root,root) %{_libdir}/libFLAC.so.*.*.*
%attr(755,root,root) %{_libdir}/libFLAC.so.8
%{_mandir}/man1/flac.1*
%{_mandir}/man1/metaflac.1*

%files devel
%defattr(644,root,root,755)
%doc doc-html/{*.html,images}
%attr(755,root,root) %{_libdir}/libFLAC.so
%{_libdir}/libFLAC.la
%{_includedir}/FLAC
%{_pkgconfigdir}/flac.pc
%{_aclocaldir}/libFLAC.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libFLAC.a
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFLAC++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libFLAC++.so.6

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFLAC++.so
%{_libdir}/libFLAC++.la
%{_includedir}/FLAC++
%{_pkgconfigdir}/flac++.pc
%{_aclocaldir}/libFLAC++.m4

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libFLAC++.a
%endif

%if %{with xmms}
%files -n xmms-input-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_input_plugindir}/libxmms-flac.so
%endif
