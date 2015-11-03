%bcond_with	static_libs	# static library
Summary:	SGI implementation of libGLU OpenGL library
Name:		glu
Version:	9.0.0
Release:	1
License:	SGI Free Software License B v2.0 (MIT-like)
Group:		Libraries
Source0:	ftp://ftp.freedesktop.org/pub/mesa/glu/glu-%{version}.tar.bz2
URL:		http://www.mesa3d.org/
BuildRequires:	opengl-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	opengl
Provides:	opengl-glu

%description
SGI implementation of libGLU OpenGL library. It implements OpenGL GLU
1.3 specifications.

%package devel
Summary:	Header files for SGI libGLU library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	opengl-devel >= 1.2
Provides:	opengl-glu-devel = 1.3

%description devel
Header files for SGI libGLU library.

%package static
Summary:	Static SGI libGLU library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	opengl-glu-static = 1.3

%description static
Static SGI libGLU library.

%prep
%setup -q -n glu-%{version}

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# there is pkg-config support; also, traditionally libGLU didn't have .la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libGLU.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLU.so.*.*.*
%attr(755,root,root) %{_libdir}/libGLU.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLU.so
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h
%{_libdir}/pkgconfig/glu.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libGLU.a
%endif
