Summary:	A freely licensed alternative to the GLUT library
Name:		freeglut
Version:	2.6.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/freeglut/%{name}-%{version}.tar.gz
URL:		http://freeglut.sourceforge.net/
BuildRequires:	opengl-glu-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxext-devel
BuildRequires:	libxi-devel
BuildRequires:	libxxf86vm-devel
Provides:	opengl-glut = 4.0

%description
Freeglut, the Free OpenGL Utility Toolkit, is meant to be a free
alternative to Mark Kilgard's GLUT library. It is distributed under an
X-Consortium style license (see COPYING for details), to offer you a
chance to use and/or modify the source.

It makes use of OpenGL, GLU, and pthread libraries. The library does
not make use of any GLUT code and is not 100% compatible. Code
recompilation and/or slight modifications might be required for your
applications to work with freeglut.

%package devel
Summary:	Header files for freeglut library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	opengl-glu-devel
Requires:	libxext-devel
Requires:	libxi-devel
Requires:	libxxf86vm-devel
Provides:	opengl-glut-devel

%description devel
Header files for freeglut library.

%prep
%setup -q

%build
sed -i "s/smooth_opengl3 //" progs/demos/Makefile.*
libtoolize --force && autoreconf -vfi


%configure \
	--disable-warnings \
	--disable-static

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
%doc AUTHORS COPYING ChangeLog FrequentlyAskedQuestions NEWS README TODO doc/{freeglut.html,index.html,progress.html,*.png}
%lang(fr) %doc LISEZ_MOI
%attr(755,root,root) %{_libdir}/libglut.so.*.*.*
%attr(755,root,root) %{_libdir}/libglut.so.3

%files devel
%defattr(644,root,root,755)
%doc doc/{freeglut_user_interface.html,structure.html}
%attr(755,root,root) %{_libdir}/libglut.so
%{_libdir}/libglut.la
%{_includedir}/GL/freeglut*.h
%{_includedir}/GL/glut.h

%changelog
