#
# Conditional build:
%bcond_without	bootstrap	# disable features to able to build without installed qt5
# -- build targets
%bcond_with	qch		# QCH documentation
%bcond_with	qm		# QM translations
%bcond_with	qtdeclarative	# Quick2 plugin for Qt5Declarative
%bcond_with	qtwebkit	# WebKit plugin for Qt5Declarative

%if %{with bootstrap}
%undefine	with_qch
%undefine	with_qm
%undefine	with_qtwebkit
%endif

%define		orgname		qttools
%define		qtbase_ver		%{version}
%define		qttools_ver		5.2
%define		qtdeclarative_ver	5.5
%define		qtwebkit_ver		5.5
Summary:	Development tools for Qt 5
Name:		qt5-%{orgname}
Version:	5.5.0
Release:	1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt.io/official_releases/qt/5.5/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	535ff9df9d83e9bde08ee3913b751d07
#Source1:	http://download.qt.io/official_releases/qt/5.5/%{version}/submodules/qttranslations-opensource-src-%{version}.tar.xz
# Source1-md5:	1f89d53fe759db123b4b6d9de9d9e8c9
URL:		http://www.qt.io/
BuildRequires:	mesa-libgl-devel
BuildRequires:	qt5core-devel >= %{qtbase_ver}
BuildRequires:	qt5dbus-devel >= %{qtbase_ver}
BuildRequires:	qt5gui-devel >= %{qtbase_ver}
BuildRequires:	qt5network-devel >= %{qtbase_ver}
#BuildRequires:	qt5printsupport-devel >= %{qtbase_ver}
%{?with_qtdeclarative:BuildRequires:	qt5quick-devel >= %{qtdeclarative_ver}}
BuildRequires:	qt5sql-devel >= %{qtbase_ver}
%{?with_qtwebkit:BuildRequires:	qt5webKit-devel >= %{qtwebkit_ver}}
BuildRequires:	qt5widgets-devel >= %{qtbase_ver}
BuildRequires:	qt5xml-devel >= %{qtbase_ver}
%{?with_qch:BuildRequires:	qt5-assistant >= %{qttools_ver}}
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-doc-common >= %{qtbase_ver}
%{?with_qm:BuildRequires:	qt5-linguist >= %{qttools_ver}}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build
BuildRequires:	tar >= 1.22
BuildRequires:	xz
# pixeltool: Core, Gui, Widgets
# qtpaths: Core
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5gui >= %{qtbase_ver}
Requires:	qt5widgets >= %{qtbase_ver}

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains additional tools for building Qt applications.

%package -n qt5-assistant
Summary:	Qt documentation browser
Group:		X11/Development/Tools
# assistant: Core, Gui, Help, Network, PrintSupport, Sql, Widgets
# qcollectiongenerator: Core, Gui, Help
# qhelpconverter: Core, Gui, Widgets
# qhelpgenerator: Core, Gui, Help; sqldriver-sqlite3 to work
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5help = %{version}-%{release}
Requires:	qt5gui >= %{qtbase_ver}
Requires:	qt5network >= %{qtbase_ver}
Requires:	qt5printsupport >= %{qtbase_ver}
Requires:	qt5sql >= %{qtbase_ver}
Requires:	qt5sql-sqldriver-sqlite3 >= %{qtbase_ver}
Requires:	qt5widgets >= %{qtbase_ver}

%description -n qt5-assistant
Qt Assistant is a tool for browsing on-line documentation with
indexing, bookmarks and full-text search.

%package -n qt5-designer
Summary:	IDE used for GUI designing with Qt 5 library
Group:		X11/Applications
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5designer = %{version}-%{release}
Requires:	qt5gui >= %{qtbase_ver}
Requires:	qt5network >= %{qtbase_ver}
Requires:	qt5printsupport >= %{qtbase_ver}
Requires:	qt5widgets >= %{qtbase_ver}
Requires:	qt5xml >= %{qtbase_ver}

%description -n qt5-designer
An advanced tool used for GUI designing with Qt 5 library.

%package -n qt5-linguist
Summary:	Translation helper for Qt 5
Group:		X11/Development/Tools
# lconvert,lrelease,lupdate: Core, Xml
# linguist: Core, Gui, PrintSupport, Widgets, Xml
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5gui >= %{qtbase_ver}
Requires:	Qt5printsupport >= %{qtbase_ver}
Requires:	qt5widgets >= %{qtbase_ver}
Requires:	qt5xml >= %{qtbase_ver}

%description -n qt5-linguist
Translation helper for Qt 5.

%package -n qt5-qdbus
Summary:	Qt5 DBus tools
Group:		X11/Applications
# qdbus: Core, DBus, Xml
# qdbusviewer: Core, DBus, Gui, Widgets, Xml
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5dbus >= %{qtbase_ver}
Requires:	qt5gui >= %{qtbase_ver}
Requires:	qt5widgets >= %{qtbase_ver}
Requires:	qt5xml >= %{qtbase_ver}

%description -n qt5-qdbus
This package contains the qdbus and qdbusviewer tools.

%package -n qt5clucene
Summary:	Qt5 CLucene library
Group:		Libraries
Requires:	qt5core >= %{qtbase_ver}

%description -n qt5clucene
The Qt5 CLucene library provides Qt API to CLucene, a C++ port of
Lucene high-performance, full-featured text search engine.

%package -n qt5clucene-devel
Summary:	Qt5 CLucene library - development files
Group:		Development/Libraries
Requires:	qt5cLucene = %{version}-%{release}
Requires:	qt5core-devel >= %{qtbase_ver}

%description -n qt5clucene-devel
Header files for Qt5 CLucene library.

%package -n qt5designer
Summary:	Qt5 Designer libraries
Group:		X11/Libraries
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5gui >= %{qtbase_ver}
Requires:	qt5widgets >= %{qtbase_ver}
Requires:	qt5xml >= %{qtbase_ver}

%description -n qt5designer
The Qt5 Designer libraries provide classes to create your own custom
widget plugins for Qt Designer and classes to access Qt Designer
components.

%package -n qt5designer-devel
Summary:	Qt5 Designer libraries - development files
Group:		X11/Development/Libraries
Requires:	mesa-libgl-devel
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5designer = %{version}-%{release}
Requires:	qt5gui >= %{qtbase_ver}
Requires:	qt5widgets >= %{qtbase_ver}
Requires:	qt5xml >= %{qtbase_ver}

%description -n qt5designer-devel
Header files for Qt5 Designer libraries.

%package -n qt5designer-plugin-qquickwidget
Summary:	QQuickWidget (Quick2) plugin for Qt5 Designer
Group:		X11/Libraries
Requires:	qt5designer = %{version}-%{release}
Requires:	qt5quick >= %{qtdeclarative_ver}

%description -n qt5designer-plugin-qquickwidget
QQuickWidget (Quick2) plugin for Qt5 Designer.

%package -n qt5designer-plugin-qwebview
Summary:	QWebView plugin for Qt5 Designer
Group:		X11/Libraries
Requires:	qt5designer = %{version}-%{release}
Requires:	qt5webKit >= %{qtwebkit_ver}

%description -n qt5designer-plugin-qwebview
QWebView plugin for Qt5 Designer.

%package -n qt5help
Summary:	Qt5 Help library
Group:		X11/Libraries
Requires:	qt5cLucene = %{version}-%{release}
Requires:	qt5core >= %{qtbase_ver}
Requires:	qt5gui >= %{qtbase_ver}
Requires:	qt5network >= %{qtbase_ver}
Requires:	qt5sql >= %{qtbase_ver}
Requires:	qt5widgets >= %{qtbase_ver}

%description -n qt5help
Qt5 Help library provides classes for integrating online documentation
in applications.


%package -n qt5help-devel
Summary:	Qt5 Help library - development files
Group:		X11/Development/Libraries
Requires:	qt5clucene-devel = %{version}-%{release}
Requires:	qt5core-devel >= %{qtbase_ver}
Requires:	qt5gui-devel >= %{qtbase_ver}
Requires:	qt5help = %{version}-%{release}
Requires:	qt5network-devel >= %{qtbase_ver}
Requires:	qt5sql-devel >= %{qtbase_ver}
Requires:	qt5widgets-devel >= %{qtbase_ver}

%description -n qt5help-devel
Header files for Qt5 Help library.

%package -n qt5uitools-devel
Summary:	Qt5 Ui Tools library - development files
Group:		X11/Development/Libraries
Requires:	OpenGL-devel
Requires:	qt5core-devel >= %{qtbase_ver}
Requires:	qt5gui-devel >= %{qtbase_ver}
Requires:	qt5widgets-devel >= %{qtbase_ver}

%description -n qt5uitools-devel
Header files and static Qt5 Ui Tools library.

Qt5 Ui Tools library provides classes to handle forms created with Qt
Designer.


%package doc
Summary:	Qt5 Tools documentation in HTML format
Group:		X11/Development/Libraries
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 Tools documentation in HTML format.

%package doc-qch
Summary:	Qt5 Tools documentation in QCH format
Group:		X11/Development/Libraries
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 Tools documentation in QCH format.

%package examples
Summary:	Qt5 Tools examples
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 Tools - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version} %{?with_qm:-a1}

%build
qmake-qt5
%{__make}

# build only HTML docs if without qch (which needs already installed qhelpgenerator)
%{__make} %{!?with_qch:html_}docs

%if %{with qm}
cd qttranslations-opensource-src-%{version}
qmake-qt5
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with qm}
%{__make} -C qttranslations-opensource-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only assistant, designer, linguist, qt_help, qtconfig here
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{qmlviewer,qtbase,qtconnectivity,qtdeclarative,qtlocation,qtmultimedia,qtquick1,qtquickcontrols,qtscript,qtwebsockets,qtxmlpatterns}_*.qm
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/qt_{??,??_??}.qm
# qtconfig build is currently disabled (see src/src.pro)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/qtconfig_*.qm
%endif

# kill unnecessary -L%{_libdir} from *.la, *.prl, *.pc
%{__sed} -i -e "s,-L%{_libdir} \?,,g" \
	$RPM_BUILD_ROOT%{_libdir}/*.{la,prl} \
	$RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# symlinks in system bin dir
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf ../%{_lib}/qt5/bin/assistant assistant-qt5
ln -sf ../%{_lib}/qt5/bin/designer designer-qt5
ln -sf ../%{_lib}/qt5/bin/lconvert lconvert-qt5
ln -sf ../%{_lib}/qt5/bin/linguist linguist-qt5
ln -sf ../%{_lib}/qt5/bin/lrelease lrelease-qt5
ln -sf ../%{_lib}/qt5/bin/lupdate lupdate-qt5
ln -sf ../%{_lib}/qt5/bin/pixeltool pixeltool-qt5
ln -sf ../%{_lib}/qt5/bin/qcollectiongenerator qcollectiongenerator-qt5
ln -sf ../%{_lib}/qt5/bin/qdbus qdbus-qt5
ln -sf ../%{_lib}/qt5/bin/qdbusviewer qdbusviewer-qt5
ln -sf ../%{_lib}/qt5/bin/qhelpconverter qhelpconverter-qt5
ln -sf ../%{_lib}/qt5/bin/qhelpgenerator qhelpgenerator-qt5
ln -sf ../%{_lib}/qt5/bin/qtdiag qtdiag-qt5
ln -sf ../%{_lib}/qt5/bin/qtpaths qtpaths-qt5
ln -sf ../%{_lib}/qt5/bin/qtplugininfo qtplugininfo-qt5
cd -

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/assistant
ifecho_tree examples %{_examplesdir}/qt5/designer
ifecho_tree examples %{_examplesdir}/qt5/help
ifecho_tree examples %{_examplesdir}/qt5/linguist
ifecho_tree examples %{_examplesdir}/qt5/uitools


%if %{with qm}
find_qt5_qm assistant >> assistant.lang
find_qt5_qm designer >> designer.lang
find_qt5_qm linguist >> linguist.lang
find_qt5_qm qt_help >> qt_help.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n qt5clucene -p /sbin/ldconfig
%postun	-n qt5clucene -p /sbin/ldconfig

%post	-n qt5designer -p /sbin/ldconfig
%postun	-n qt5designer -p /sbin/ldconfig

%post	-n qt5help -p /sbin/ldconfig
%postun	-n qt5help -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LGPL_EXCEPTION.txt dist/changes-*
%attr(755,root,root) %{_bindir}/pixeltool-qt5
%attr(755,root,root) %{_bindir}/qtdiag-qt5
%attr(755,root,root) %{_bindir}/qtpaths-qt5
%attr(755,root,root) %{_bindir}/qtplugininfo-qt5
%attr(755,root,root) %{qt5dir}/bin/pixeltool
%attr(755,root,root) %{qt5dir}/bin/qtdiag
%attr(755,root,root) %{qt5dir}/bin/qtpaths
%attr(755,root,root) %{qt5dir}/bin/qtplugininfo

%files -n qt5-assistant 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/assistant-qt5
%attr(755,root,root) %{_bindir}/qcollectiongenerator-qt5
%attr(755,root,root) %{_bindir}/qhelpconverter-qt5
%attr(755,root,root) %{_bindir}/qhelpgenerator-qt5
%attr(755,root,root) %{qt5dir}/bin/assistant
%attr(755,root,root) %{qt5dir}/bin/qcollectiongenerator
%attr(755,root,root) %{qt5dir}/bin/qhelpconverter
%attr(755,root,root) %{qt5dir}/bin/qhelpgenerator

%files -n qt5-designer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/designer-qt5
%attr(755,root,root) %{qt5dir}/bin/designer

%files -n qt5-linguist
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lconvert-qt5
%attr(755,root,root) %{_bindir}/linguist-qt5
%attr(755,root,root) %{_bindir}/lrelease-qt5
%attr(755,root,root) %{_bindir}/lupdate-qt5
%attr(755,root,root) %{qt5dir}/bin/lconvert
%attr(755,root,root) %{qt5dir}/bin/linguist
%attr(755,root,root) %{qt5dir}/bin/lrelease
%attr(755,root,root) %{qt5dir}/bin/lupdate
%{_datadir}/qt5/phrasebooks
%{_libdir}/cmake/Qt5LinguistTools

%files -n qt5-qdbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qdbus-qt5
%attr(755,root,root) %{_bindir}/qdbusviewer-qt5
%attr(755,root,root) %{qt5dir}/bin/qdbus
%attr(755,root,root) %{qt5dir}/bin/qdbusviewer

%files -n qt5clucene
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5CLucene.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5CLucene.so.5

%files -n qt5clucene-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5CLucene.so
%{_libdir}/libQt5CLucene.prl
%{_includedir}/qt5/QtCLucene
%{_libdir}/pkgconfig/Qt5CLucene.pc
%{qt5dir}/mkspecs/modules/qt_lib_clucene_private.pri

%files -n qt5designer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Designer.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Designer.so.5
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so.5

%dir %{qt5dir}/plugins/designer
%attr(755,root,root) %{qt5dir}/plugins/designer/libcontainerextension.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libcustomwidgetplugin.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libtaskmenuextension.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libworldtimeclockplugin.so

# common for base -devel and plugin-specific files (from other source packages)
%dir %{_libdir}/cmake/Qt5Designer

%files -n qt5designer-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Designer.so
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so
%{_libdir}/libQt5Designer.prl
%{_libdir}/libQt5DesignerComponents.prl
%{_includedir}/qt5/QtDesigner
%{_includedir}/qt5/QtDesignerComponents
%{_libdir}/pkgconfig/Qt5Designer.pc
%{_libdir}/pkgconfigQt5DesignerComponents.pc
%{_libdir}/cmake/Qt5Designer/Qt5DesignerConfig*.cmake
%{_libdir}/cmake/Qt5Designer/Qt5Designer_AnalogClockPlugin.cmake
%{_libdir}/cmake/Qt5Designer/Qt5Designer_MultiPageWidgetPlugin.cmake
%{_libdir}/cmake/Qt5Designer/Qt5Designer_TicTacToePlugin.cmake
%{_libdir}/cmake/Qt5Designer/Qt5Designer_WorldTimeClockPlugin.cmake
%{qt5dir}/mkspecs/modules/qt_lib_designer.pri
%{qt5dir}/mkspecs/modules/qt_lib_designer_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_designercomponents_private.pri

%if %{with qtdeclarative}
%files -n Qt5Designer-plugin-qquickwidget
%defattr(644,root,root,755)
%attr(755,root,root) %{qt5dir}/plugins/designer/libqquickwidget.so
%{_libdir}/cmake/Qt5Designer/Qt5Designer_QQuickWidgetPlugin.cmake
%endif

%if %{with qtwebkit}
%files -n Qt5Designer-plugin-qwebview
%defattr(644,root,root,755)
%attr(755,root,root) %{qt5dir}/plugins/designer/libqwebview.so
%{_libdir}/cmake/Qt5Designer/Qt5Designer_QWebViewPlugin.cmake
%endif

%files -n qt5help
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Help.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Help.so.5

%files -n qt5help-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Help.so
%{_libdir}/libQt5Help.prl
%{_includedir}/qt5/QtHelp
%{_libdir}/pkgconfig/Qt5Help.pc
%{_libdir}/cmake/Qt5Help
%{qt5dir}/mkspecs/modules/qt_lib_help.pri
%{qt5dir}/mkspecs/modules/qt_lib_help_private.pri

%files -n qt5uitools-devel
%defattr(644,root,root,755)
# static-only
%{_libdir}/libQt5UiTools.a
%{_libdir}/libQt5UiTools.prl
%{_includedir}/qt5/QtUiPlugin
%{_includedir}/qt5/QtUiTools
%{_libdir}/pkgconfig/Qt5UiTools.pc
%{_libdir}/cmake/Qt5UiPlugin
%{_libdir}/cmake/Qt5UiTools
%{qt5dir}/mkspecs/modules/qt_lib_uiplugin.pri
%{qt5dir}/mkspecs/modules/qt_lib_uitools.pri
%{qt5dir}/mkspecs/modules/qt_lib_uitools_private.pri

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtassistant
%{_docdir}/qt5-doc/qtdesigner
%{_docdir}/qt5-doc/qthelp
%{_docdir}/qt5-doc/qtlinguist
%{_docdir}/qt5-doc/qtuitools

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtassistant.qch
%{_docdir}/qt5-doc/qtdesigner.qch
%{_docdir}/qt5-doc/qthelp.qch
%{_docdir}/qt5-doc/qtlinguist.qch
%{_docdir}/qt5-doc/qtuitools.qch
%endif

%changelog
