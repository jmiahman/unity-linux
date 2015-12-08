#
# Conditional build:
%bcond_with	qch	# documentation in QCH format

%define		orgname		qtx11extras
%define		qtbase_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 X11 Extras library
Name:		qt5-%{orgname}
Version:	5.5.0
Release:	1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt.io/official_releases/qt/5.5/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	cc5977f99ac4732950b4710cd69e148b
URL:		http://www.qt.io/
BuildRequires:	qt5core-devel >= %{qtbase_ver}
BuildRequires:	qt5gui-devel >= %{qtbase_ver}
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build
BuildRequires:	tar >= 1.22
BuildRequires:	xz

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 X11 Extras library.

%package -n	qt5x11extras
Summary:	The Qt5 X11 Extras library
Group:		Libraries
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5gui >= %{qtbase_ver}

%description -n qt5x11extras
Qt5 X11 Extras library provides classes for developing for the X11
platform.

%package -n 	qt5x11extras-devel
Summary:	Qt5 X11 Extras - development files
Group:		X11/Development/Libraries
Requires:	mesa-libgl-devel
Requires:	qt5core-devel >= %{qtbase_ver}
Requires:	qt5gui-devel >= %{qtbase_ver}
Requires:	qt5x11extras = %{version}-%{release}

%description -n qt5x11extras-devel
Qt5 X11 Extras - development files.

%description -n qt5x11extras-devel -l pl.UTF-8
Biblioteka Qt5 X11 Extras - pliki programistyczne.

%package doc
Summary:	Qt5 X11 Extras documentation in HTML format
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 X11 Extras documentation in HTML format.

%package doc-qch
Summary:	Qt5 X11 Extras documentation in QCH format
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 X11 Extras documentation in QCH format.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n qt5x11extras -p /sbin/ldconfig
%postun	-n qt5x11extras -p /sbin/ldconfig

%files -n qt5x11extras
%defattr(644,root,root,755)
%doc LGPL_EXCEPTION.txt dist/changes-*
%attr(755,root,root) %{_libdir}/libQt5X11Extras.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5X11Extras.so.5

%files -n qt5x11extras-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5X11Extras.so
%{_libdir}/libQt5X11Extras.prl
%{_includedir}/qt5/QtX11Extras
%{_libdir}/pkgconfig/Qt5X11Extras.pc
%{_libdir}/cmake/Qt5X11Extras
%{qt5dir}/mkspecs/modules/qt_lib_x11extras.pri
%{qt5dir}/mkspecs/modules/qt_lib_x11extras_private.pri

#%files doc
#%defattr(644,root,root,755)
#%{_docdir}/qt5-doc/qtx11extras

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtx11extras.qch
%endif

%changelog
