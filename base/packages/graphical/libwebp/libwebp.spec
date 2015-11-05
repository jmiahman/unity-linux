%bcond_with     static_libs     # don't build static library
%bcond_without	opengl	# OpenGL-based visualizer

Summary:	WebP image codec libraries
Name:		libwebp
Version:	0.4.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.webmproject.org/releases/webp/%{name}-%{version}.tar.gz
URL:		https://developers.google.com/speed/webp/
%{?with_opengl:BuildRequires:	mesa-libgl-devel}
%{?with_opengl:BuildRequires:	freeglut-devel}
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool

%description
WebP image codec libraries.

%package devel
Summary:	Header files for WebP libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for WebP libraries.

%if %{with static_libs}
%package static
Summary:	Static WebP libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WebP libraries.
%endif

%package progs
Summary:	WebP image codec tools
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
WebP image codec tools.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static} \
	--disable-silent-rules \
	--enable-libwebpdemux \
	--enable-libwebpmux \
	--enable-libwebpdecoder
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwebp*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS PATENTS README
%attr(755,root,root) %{_libdir}/libwebp.so.*.*.*
%attr(755,root,root) %{_libdir}/libwebp.so.5
%attr(755,root,root) %{_libdir}/libwebpdemux.so.*.*.*
%attr(755,root,root) %{_libdir}/libwebpdemux.so.1
%attr(755,root,root) %{_libdir}/libwebpmux.so.*.*.*
%attr(755,root,root) %{_libdir}/libwebpmux.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebp.so
%attr(755,root,root) %{_libdir}/libwebpdemux.so
%attr(755,root,root) %{_libdir}/libwebpmux.so
%{_includedir}/webp
%{_pkgconfigdir}/libwebp.pc
%{_pkgconfigdir}/libwebpdemux.pc
%{_pkgconfigdir}/libwebpmux.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwebp.a
%{_libdir}/libwebpdemux.a
%{_libdir}/libwebpmux.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cwebp
%attr(755,root,root) %{_bindir}/dwebp
%attr(755,root,root) %{_bindir}/gif2webp
%{?with_opengl:%attr(755,root,root) %{_bindir}/vwebp}
%attr(755,root,root) %{_bindir}/webpmux
%{_mandir}/man1/cwebp.1*
%{_mandir}/man1/dwebp.1*
%{_mandir}/man1/gif2webp.1*
%{?with_opengl:%{_mandir}/man1/vwebp.1*}
%{_mandir}/man1/webpmux.1*
