%define         _pkgconfigdir   %{_libdir}/pkgconfig
%define         _docdir         %{_datadir}/doc
%define         specflags       -fno-strict-aliasing
%define         qt5dir          %{_libdir}/qt5
%define		_examplesdir    %{_prefix}/%{_lib}/qt5/examples


# Conditional build:
%bcond_with	static_libs	# static libraries [incomplete support in .spec]
%bcond_without	bootstrap	# disable features to able to build without installed qt5
# -- build targets
%bcond_without	qch		# QCH documentation
%bcond_with	qm		# QM translations
# -- features
%bcond_with	cups		# CUPS printing support
%bcond_without	directfb	# DirectFB platform support
%bcond_with	egl		# EGL (EGLFS, minimal EGL) platform support
%bcond_with	gtk		# GTK+ theme integration
%bcond_with	kms		# KMS platform support
%bcond_with	pch		# pch (pre-compiled headers) in qmake
%bcond_with	systemd		# logging to journald
%bcond_without	tslib		# tslib support
%bcond_with	openvg		# OpenVG support
# -- databases
%bcond_with	freetds		# TDS (Sybase/MS SQL) plugin
%bcond_with	mysql		# MySQL plugin
%bcond_with	odbc		# unixODBC plugin
%bcond_with	pgsql		# PostgreSQL plugin
%bcond_with	sqlite2		# SQLite2 plugin
%bcond_without	sqlite		# SQLite3 plugin
%bcond_with	ibase		# ibase (InterBase/Firebird) plugin
%bcond_with	db2		# DB2 support
%bcond_with	oci		# OCI (Oracle) support
# -- SIMD CPU instructions
%bcond_without	sse2		# use SSE2 instructions
%bcond_with	sse3		# use SSE3 instructions (since: Intel middle Pentium4, AMD Athlon64)
%bcond_with	ssse3		# use SSSE3 instructions (Intel since Core2, Via Nano)
%bcond_with	sse41		# use SSE4.1 instructions (Intel since middle Core2)
%bcond_with	sse42		# use SSE4.2 instructions (the same)
%bcond_with	avx		# use AVX instructions (Intel since Sandy Bridge, AMD since Bulldozer)
%bcond_with	avx2		# use AVX2 instructions (Intel since Haswell)

%ifnarch %{ix86} %{x8664} x32 sparc sparcv9 alpha ppc
%undefine	with_ibase
%endif
%ifarch	athlon
%define		with_3dnow	1
%endif
%ifarch athlon pentium3 pentium4 %{x8664} x32
%define		with_mmx	1
%endif
%ifarch pentium4 %{x8664} x32
%define		with_sse2	1
%endif

%if %{with bootstrap}
%undefine	with_qch
%undefine	with_qm
%endif

%define		icu_abi		56
%define		next_icu_abi	%(echo $((%{icu_abi} + 1)))

%define		orgname		qtbase
Summary:	Qt5 - base components
Name:		qt5-%{orgname}
Version:	5.5.0
Release:	1%{?dist}
# See LGPL_EXCEPTION.txt for exception details
License:	LGPL v2 with Digia Qt LGPL Exception v1.1 or GPL v3
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.5/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
#Source1:	http://download.qt-project.org/official_releases/qt/5.5/%{version}/submodules/qttranslations-opensource-src-%{version}.tar.xz
# Source1-md5:	423cccbace459623a9a173cede968cbe
Patch0:		qtbase-oracle-instantclient.patch
Patch1:		%{name}-system_cacerts.patch
Patch2:		%{name}-musl-iconv-no-bom.patch
Patch3:		%{name}-musl-socklen.patch

URL:		http://qt-project.org/
%{?with_directfb:BuildRequires:	directfb}
%{?with_egl:BuildRequires:	EGL-devel}
%{?with_ibase:BuildRequires:	Firebird-devel}
%{?with_openvg:BuildRequires:	Mesa-libOpenVG-devel}
%{?with_kms:BuildRequires:	Mesa-libgbm-devel}
BuildRequires:	mesa-libgl-devel
%{?with_kms:BuildRequires:	openglesv2-devel}
BuildRequires:	alsa-lib-devel
%{?with_gtk:BuildRequires:	atk-devel}
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	dbus-devel
BuildRequires:	fontconfig-devel
%{?with_freetds:BuildRequires:	freetds-devel}
BuildRequires:	freetype-devel
%{?with_pch:BuildRequires:	gcc}
BuildRequires:	gdb
BuildRequires:	glib-devel
%{?with_gtk:BuildRequires:	gtk+2-devel}
%{?with_kms:BuildRequires:	libdrm-devel}
# see dependency on libicu version below
BuildRequires:	libicu-devel < %{next_icu_abi}
BuildRequires:	libicu-devel >= %{icu_abi}
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxcb-devel
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	openssl-devel
%{?with_oci:BuildRequires:	oracle-instantclient-devel}
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
%{?with_pgsql:BuildRequires:	postgresql-backend-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	pulseaudio-devel
%{?with_qch:BuildRequires:	qt5-assistant}
%{?with_qm:BuildRequires:	qt5-linguist}
BuildRequires:	rpm-build
BuildRequires:	sed 
%{?with_sqlite2:BuildRequires:	sqlite-devel}
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_systemd:BuildRequires:	systemd-devel}
BuildRequires:	tar
%{?with_tslib:BuildRequires:	tslib-devel}
BuildRequires:	eudev-devel
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-renderutil-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	libsm-devel
BuildRequires:	libx11-devel
BuildRequires:	libxcursor-devel
BuildRequires:	libxext-devel
BuildRequires:	libxfixes-devel
BuildRequires:	libxi-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxrender-devel
BuildRequires:	libxkbcommon-devel
BuildRequires:	libxkbcommon-x11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel

%description
Qt is a software toolkit for developing applications.

This package contains base components, like Core, Network or Xml.


%package -n qt5bootstrap-devel
Summary:	Qt5 Bootstrap library - development files
Group:		Development/Libraries
# for (subset of) Qt5Core headers
Requires:	qt5core-devel = %{version}-%{release}
Requires:	zlib-devel

%description -n qt5bootstrap-devel
Qt5 Bootstrap library (minimal part of Qt5 Core) - development files.

%package -n qt5concurrent
Summary:	Qt5 Concurrent library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}

%description -n qt5concurrent
The Qt5 Concurrent library provides high-level APIs that make it
possible to write multi-threaded programs without using low-level
threading primitives.

%package -n qt5concurrent-devel
Summary:	Qt5 Concurrent library - development files
Group:		Development/Libraries
Requires:	qt5concurrent = %{version}-%{release}
Requires:	qt5core-devel = %{version}-%{release}

%description -n qt5concurrent-devel
Header files for Qt5 Concurrent library.

%package -n qt5core
Summary:	Qt5 Core library
Group:		Libraries
Requires:	pcre
Obsoletes:	qt5-qtbase

%description -n qt5core
Qt5 Core library provides core non-GUI functionality.

%package -n qt5core-devel
Summary:	Qt5 Core library - development files
Group:		Development/Libraries
Requires:	qt5core = %{version}-%{release}
Requires:	glib-devel
Requires:	libicu-devel
Requires:	pcre-devel
Requires:	zlib-devel
Obsoletes:	qt5-qtbase-devel

%description -n qt5core-devel
Header files for Qt5 Core library.

%package -n qt5dbus
Summary:	Qt5 DBus library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}
Requires:	dbus-libs

%description -n qt5dbus
The Qt5 D-Bus library is a Unix-only library that you can use to
perform Inter-Process Communication using the D-Bus protocol.

%package -n qt5dbus-devel
Summary:	Qt5 DBus library - development files
Group:		Development/Libraries
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5dbus = %{version}-%{release}
Requires:	dbus-devel

%description -n qt5dbus-devel
Header files for Qt5 DBus library.

%package -n qt5gui
Summary:	Qt5 Gui library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}
# for:
# - ibus platforminputcontext plugin
# - qxcb platform plugin
Requires:	qt5dbus = %{version}-%{release}
# for qxcb platform plugin
Requires:	libxcb
# for compose platforminputcontext plugin
Requires:	libxkbcommon

%description -n qt5gui
The Qt5 GUI library provides the basic enablers for graphical
applications written with Qt 5.

%package -n qt5gui-generic-tslib
Summary:	Qt5 Gui generic input plugin for TSlib (touchscreen panel events)
Group:		Libraries
Requires:	qt5gui = %{version}-%{release}

%description -n qt5gui-generic-tslib
Qt5 Gui generic input plugin for TSlib (touchscreen panel events).

%package -n qt5gui-platform-directfb
Summary:	Qt5 Gui platform plugin for DirectFB
Group:		Libraries
Requires:	qt5gui = %{version}-%{release}

%description -n qt5gui-platform-directfb
Qt5 Gui platform plugin for DirectFB.

%package -n qt5gui-platform-kms
Summary:	Qt5 Gui platform plugin for KMS
Group:		Libraries
Requires:	qt5gui = %{version}-%{release}

%description -n qt5gui-platform-kms
Qt5 Gui platform plugin for KMS.

%package -n qt5gui-platform-egl
Summary:	Qt5 Gui platform plugins for EGL
Group:		Libraries
Requires:	qt5gui = %{version}-%{release}

%description -n qt5gui-platform-egl
Qt5 Gui platform plugins for EGL.

%package -n qt5gui-platformtheme-gtk2
Summary:	Qt5 Gui platform theme plugin for GTK+ 2.x
Group:		Libraries
Requires:	qt5gui = %{version}-%{release}

%description -n qt5gui-platformtheme-gtk2
Qt5 Gui platform theme plugin for GTK+ 2.x.

%package -n qt5gui-devel
Summary:	Qt5 Gui library - development files
Group:		Development/Libraries
Requires:	mesa-libgl-devel
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5gui = %{version}-%{release}
Requires:	libpng-devel

%description -n qt5gui-devel
Header files for Qt5 Gui library.

%package -n qt5network
Summary:	Qt5 Network library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}
# for bearer plugins (qconnman, qnm):
Requires:	qt5dbus = %{version}-%{release}

%description -n qt5network
The Qt5 Network library provides classes to make network programming
easier and portable.

%package -n qt5network-devel
Summary:	Qt5 Network library - development files
Group:		Development/Libraries
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5network = %{version}-%{release}
Requires:	openssl-devel

%description -n qt5network-devel
Header files for Qt5 Network library.

%package -n qt5opengl
Summary:	Qt5 OpenGL library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}
Requires:	qt5gui = %{version}-%{release}
Requires:	qt5widgets = %{version}-%{release}

%description -n qt5opengl
The Qt5 OpenGL library offers classes that make it easy to use OpenGL
in Qt 5 applications.

%package -n qt5opengl-devel
Summary:	Qt5 OpenGL library - development files
Group:		Development/Libraries
Requires:	mesa-libgl-devel
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5gui-devel = %{version}-%{release}
Requires:	qt5opengl = %{version}-%{release}
Requires:	qt5widgets-devel = %{version}-%{release}

%description -n qt5opengl-devel
Header files for Qt5 OpenGL library.

%package -n qt5openglextensions-devel
Summary:	Qt5 OpenGLExtensions library - development files
Group:		Development/Libraries
Requires:	mesa-libgl-devel
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5gui-devel = %{version}-%{release}

%description -n qt5openglextensions-devel
Qt5 OpenGLExtensions library (development files).

%package -n qt5platformsupport-devel
Summary:	Qt5 PlatformSupport library - development files
Group:		X11/Development/Libraries
Requires:	mesa-libgl-devel
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5dbus-devel = %{version}-%{release}
Requires:	qt5gui-devel = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	freetype-devel
Requires:	libx11-devel
Requires:	libxrender-devel
Requires:	libxext-devel
Requires:	eudev-devel

%description -n qt5platformsupport-devel
Qt5 PlatformSupport library (development files).

%package -n qt5printsupport
Summary:	Qt5 PrintSupport library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}
Requires:	qt5gui = %{version}-%{release}
Requires:	qt5widgets = %{version}-%{release}
%{?with_cups:Requires:	cups-lib}

%description -n qt5printsupport
The Qt5 PrintSupport library provides classes to make printing easier
and portable.

%package -n qt5printsupport-devel
Summary:	Qt5 PrintSupport library - development files
Group:		Development/Libraries
Requires:	mesa-libgl-devel
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5gui-devel = %{version}-%{release}
Requires:	qt5printSupport = %{version}-%{release}
Requires:	qt5widgets-devel = %{version}-%{release}

%description -n qt5printsupport-devel
Header files for Qt5 PrintSupport library.

%package -n qt5sql
Summary:	Qt5 Sql library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}

%description -n qt5sql
The Qt5 Sql library provides a driver layer, SQL API layer, and a user
interface layer for SQL databases.

%package -n qt5sql-devel
Summary:	Qt5 Sql library - development files
Group:		Development/Libraries
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-devel
Header files for Qt5 Sql library.

%package -n qt5sql-sqldriver-db2
Summary:	Qt5 Sql driver for IBM DB2 database
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-db2
Qt5 Sql driver for IBM DB2 database.

%package -n qt5sql-sqldriver-ibase
Summary:	Qt5 Sql driver for Firebird/InterBase database
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-ibase
Qt5 Sql driver for Firebird/InterBase database.

%package -n qt5sql-sqldriver-sqlite
Summary:	Qt5 Sql driver for SQLite 3.x database
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-sqlite
Qt5 Sql driver for SQLite 3.x database.

%package -n qt5sql-sqldriver-sqlite2
Summary:	Qt5 Sql driver for SQLite 2.x database
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-sqlite2
Qt5 Sql driver for SQLite 2.x database.

%package -n qt5sql-sqldriver-mysql
Summary:	Qt5 Sql driver for MySQL database
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-mysql
Qt5 Sql driver for MySQL database.

%package -n qt5sql-sqldriver-oci
Summary:	Qt5 Sql driver for Oracle database (using OCI interface)
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-oci
Qt5 Sql driver for Oracle database (using OCI interface).

%package -n qt5sql-sqldriver-odbc
Summary:	Qt5 Sql driver for ODBC databases
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-odbc
Qt5 Sql driver for ODBC databases.

%package -n qt5sql-sqldriver-pgsql
Summary:	Qt5 Sql driver for PostgreSQL database
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-pgsql
Qt5 Sql driver for PostgreSQL database.

%package -n qt5sql-sqldriver-tds
Summary:	Qt5 Sql driver for Sybase/MS SQL database (using TDS interface)
Group:		Libraries
Requires:	qt5sql = %{version}-%{release}

%description -n qt5sql-sqldriver-tds
Qt5 Sql driver for Sybase/MS SQL database (using TDS interface).

%package -n qt5test
Summary:	Qt5 Test library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}

%description -n qt5test
The Qt5 Test library provides classes for unit testing Qt 5
applications and libraries.

%package -n qt5test-devel
Summary:	Qt5 Test library - development files
Group:		Development/Libraries
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5test = %{version}-%{release}

%description -n qt5test-devel
Header files for Qt5 Test library.

%package -n qt5widgets
Summary:	Qt5 Widgets library
Group:		X11/Libraries
Requires:	qt5core = %{version}-%{release}
Requires:	qt5gui = %{version}-%{release}

%description -n qt5widgets
The Qt5 Widgets library extends Qt 5 GUI with C++ widget
functionality.

%package -n qt5widgets-devel
Summary:	Qt5 Widgets library - development files
Group:		X11/Development/Libraries
Requires:	mesa-libgl-devel
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5gui-devel = %{version}-%{release}
Requires:	qt5widgets = %{version}-%{release}
Requires:	libx11-devel
Requires:	libxext-devel

%description -n qt5widgets-devel
Header files for Qt5 Widgets library.

%package -n qt5xml
Summary:	Qt5 Xml library
Group:		Libraries
Requires:	qt5core = %{version}-%{release}

%description -n qt5xml
The Qt5 Xml library provides C++ implementations of the SAX and DOM
standards for XML.

%package -n qt5xml-devel
Summary:	Qt5 Xml library - development files
Group:		Development/Libraries
Requires:	qt5core-devel = %{version}-%{release}
Requires:	qt5xml = %{version}-%{release}

%description -n qt5xml-devel
Header files for Qt5 Xml library.

%package -n qt5-doc-common
Summary:	Common part of Qt5 documentation
Group:		Documentation
BuildArch:	noarch

%description -n qt5-doc-common
Common part of Qt5 documentation, global for all components.

%package doc
Summary:	HTML documentation for Qt5 application framework base components
Group:		Documentation
Requires:	qt5-doc-common = %{version}-%{release}
BuildArch:	noarch

%description doc
HTML documentation for Qt5 application framework base components.

%package doc-qch
Summary:	QCH documentation for Qt5 application framework base components
Group:		Documentation
Requires:	qt5-doc-common = %{version}-%{release}
BuildArch:	noarch

%description doc-qch
QCH documentation for Qt5 application framework base components.

%package examples
Summary:	Examples for Qt5 application framework base components
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Examples for Qt5 application framework base components.

%package -n qt5-build
Summary:	Qt5 build tools
Group:		Development/Tools

%description -n qt5-build
This package includes the Qt resource compiler (rcc), meta objects
compiler (moc), user interface compiler (uic) etc.

%package -n qt5-qmake
Summary:	Qt5 makefile generator
Group:		Development/Tools

%description -n qt5-qmake
Qt5 makefile generator.

%prep
%setup -q -n %{orgname}-opensource-src-%{version} %{?with_qm:-a1}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__sed} -i -e 's,usr/X11R6/,usr/,g' mkspecs/linux-g++-64/qmake.conf

# change QMAKE FLAGS to build
%{__sed} -i -e '
	s|^\(QMAKE_COMPILER *\)=.*gcc|\1= %{__cc}|;
	s|^\(QMAKE_CC *\)=.*gcc|\1= %{__cc}|;
	s|^\(QMAKE_CXX *\)=.*g++|\1= %{__cxx}|;
	' mkspecs/common/g++-base.conf

# define QMAKE_STRIP to true, so we get useful -debuginfo pkgs
%{__sed} -i -e '
	s|^\(QMAKE_STRIP *\)=.*|\1= :|;
	' mkspecs/common/linux.conf

%build
# pass OPTFLAGS to build qmake itself with optimization
export OPTFLAGS="%{rpmcflags}"
export PATH=$PWD/bin:$PATH

# DEFAULT OPTIONS FOR ALL BUILDS
COMMONOPT=" \
	-confirm-license \
	-opensource \
	-verbose \
	%{?debug:-debug} \
	%{!?debug:-release} \
	-prefix %{qt5dir} \
	-bindir %{qt5dir}/bin \
	-docdir %{_docdir}/qt5-doc \
	-headerdir %{_includedir}/qt5 \
	-libdir %{_libdir} \
	-plugindir %{qt5dir}/plugins \
	-datadir %{_datadir}/qt5 \
	-sysconfdir %{_sysconfdir}/qt5 \
	-examplesdir %{_examplesdir} \
%if %{with mysql}
	-I/usr/include/mysql \
%endif
%if %{with pgsql}
	-I/usr/include/postgresql/server \
%endif
	-%{!?with_cups:no-}cups \
	-%{!?with_directfb:no-}directfb \
	-dbus-linked \
	-fontconfig \
	-glib \
	-%{!?with_gtk:no-}gtkstyle \
	-iconv \
	%{?with_systemd:-journald} \
	-largefile \
	%{!?with_egl:-no-eglfs} \
	%{!?with_kms:-no-kms} \
	-no-rpath \
	-no-separate-debug-info \
	%{!?with_sse2:-no-sse2} \
	%{!?with_sse3:-no-sse3} \
	%{!?with_ssse3:-no-ssse3} \
	%{!?with_sse41:-no-sse4.1} \
	%{!?with_sse42:-no-sse4.2} \
	%{!?with_avx:-no-avx} \
	%{!?with_avx2:-no-avx2} \
	-openssl-linked \
	-optimized-qmake \
	-%{!?with_pch:no-}pch \
	-reduce-relocations \
	-sm \
	-system-freetype \
	-system-libjpeg \
	-system-libpng \
	-system-pcre \
	-system-sqlite \
	-system-xcb \
	-system-xkbcommon \
	-system-zlib \
	%{?with_tslib:-tslib} \
	-%{!?with_openvg:no-}openvg \
	-xcursor \
	-xfixes \
	-xinerama \
	-xinput2 \
	-xkb \
	-xrandr \
	-xrender \
	-xshape"

# STATIC
%if %{with static_libs}
OPT=" \
	--sql-db2=%{?with_db2:qt}%{!?with_db2:no} \
	--sql-ibase=%{?with_ibase:qt}%{!?with_ibase:no} \
	--sql-mysql=%{?with_mysql:qt}%{!?with_mysql:no} \
	--sql-oci=%{?with_oci:qt}%{!?with_oci:no} \
	--sql-odbc=%{?with_odbc:qt}%{!?with_odbc:no} \
	--sql-psql=%{?with_pgsql:qt}%{!?with_pgsql:no} \
	--sql-sqlite2=%{?with_sqlite2:qt}%{!?with_sqlite2:no} \
	--sql-sqlite=%{?with_sqlite:qt}%{!?with_sqlite:no} \
	--sql-tds=%{?with_freetds:qt}%{!?with_freetds:no} \
	-static"

./configure $COMMONOPT $OPT

%{__make} -C src
if [ ! -d staticlib ]; then
	mkdir staticlib
	cp -a lib/*.a staticlib
fi
%{__make} distclean
%endif

# SHARED
OPT=" \
	--sql-db2=%{?with_db2:plugin}%{!?with_db2:no} \
	--sql-ibase=%{?with_ibase:plugin}%{!?with_ibase:no} \
	--sql-mysql=%{?with_mysql:plugin}%{!?with_mysql:no} \
	--sql-oci=%{?with_oci:plugin}%{!?with_oci:no} \
	--sql-odbc=%{?with_odbc:plugin}%{!?with_odbc:no} \
	--sql-psql=%{?with_pgsql:plugin}%{!?with_pgsql:no} \
	--sql-sqlite2=%{?with_sqlite2:plugin}%{!?with_sqlite2:no} \
	--sql-sqlite=%{?with_sqlite:plugin}%{!?with_sqlite:no} \
	--sql-tds=%{?with_freetds:plugin}%{!?with_freetds:no} \
	-shared"

./configure $COMMONOPT $OPT

%{__make}

# use just built qdoc instead of requiring already installed qt5-build
wd="$(pwd)"
%{__sed} -i -e 's|%{qt5dir}/bin/qdoc|LD_LIBRARY_PATH='${wd}'/lib$${LD_LIBRARY_PATH:+:$$LD_LIBRARY_PATH} '${wd}'/bin/qdoc|' src/*/Makefile qmake/Makefile.qmake-docs
# build only HTML docs if without qch (which require qhelpgenerator)
%{__make} %{!?with_qch:html_}docs

%if %{with qm}
export QMAKEPATH=$(pwd)
cd qttranslations-opensource-src-%{version}
../bin/qmake
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/qt5
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_pkgconfigdir}
install -d $RPM_BUILD_ROOT/%{_libdir}/qt5/plugins/platformthemes

# for QtSolutions (qtlockedfile, qtsingleapplication, etc)
install -d $RPM_BUILD_ROOT%{_includedir}/qt5/QtSolutions

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with qm}
%{__make} -C qttranslations-opensource-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only qt and qtbase
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{assistant,designer,linguist,qmlviewer,qt_help,qtconfig,qtconnectivity,qtdeclarative,qtlocation,qtmultimedia,qtquick1,qtquickcontrols,qtscript,qtxmlpatterns}_*.qm
%else
install -d $RPM_BUILD_ROOT%{_datadir}/qt5/translations
%endif

# external plugins loaded from qtbase libs
install -d $RPM_BUILD_ROOT%{qt5dir}/plugins/iconengines

# kill unnecessary -L%{_libdir} from *.la, *.prl, *.pc
%{__sed} -i -e "s,-L%{_libdir} \?,,g" \
	$RPM_BUILD_ROOT%{_libdir}/*.prl \
	$RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# symlinks in system bin dir
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf ../%{_lib}/qt5/bin/moc moc-qt5
ln -sf ../%{_lib}/qt5/bin/qmake qmake-qt5
ln -sf ../%{_lib}/qt5/bin/uic uic-qt5
ln -sf ../%{_lib}/qt5/bin/rcc rcc-qt5
ln -sf ../%{_lib}/qt5/bin/qdbuscpp2xml qdbuscpp2xml-qt5
ln -sf ../%{_lib}/qt5/bin/qdbusxml2cpp qdbusxml2cpp-qt5
ln -sf ../%{_lib}/qt5/bin/qdoc qdoc-qt5
ln -sf ../%{_lib}/qt5/bin/qlalr qlalr-qt5
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
ifecho_tree examples %{_examplesdir}/corelib
ifecho_tree examples %{_examplesdir}/dbus
ifecho_tree examples %{_examplesdir}/gui
ifecho_tree examples %{_examplesdir}/network
ifecho_tree examples %{_examplesdir}/opengl
ifecho_tree examples %{_examplesdir}/qpa
ifecho_tree examples %{_examplesdir}/qtconcurrent
ifecho_tree examples %{_examplesdir}/qtestlib
ifecho_tree examples %{_examplesdir}/sql
ifecho_tree examples %{_examplesdir}/touch
ifecho_tree examples %{_examplesdir}/widgets
ifecho_tree examples %{_examplesdir}/xml

# find_lang --with-qm supports only PLD qt3/qt4 specific %{_datadir}/locale/*/LC_MESSAGES layout
find_qt5_qm()
{
	name="$1"
	find $RPM_BUILD_ROOT%{_datadir}/qt5/translations -name "${name}_*.qm" | \
		sed -e "s:^$RPM_BUILD_ROOT::" \
		    -e 's:\(.*/'$name'_\)\([a-z][a-z][a-z]\?\)\(_[A-Z][A-Z]\)\?\(\.qm\)$:%lang(\2\3) \1\2\3\4:'
}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n qt5concurrent -p /sbin/ldconfig
%postun	-n qt5concurrent -p /sbin/ldconfig

%post	-n qt5core -p /sbin/ldconfig
%postun	-n qt5core -p /sbin/ldconfig

%post	-n qt5dbus -p /sbin/ldconfig
%postun	-n qt5dbus -p /sbin/ldconfig

%post	-n qt5gui -p /sbin/ldconfig
%postun	-n qt5gui -p /sbin/ldconfig

%post	-n qt5network -p /sbin/ldconfig
%postun	-n qt5network -p /sbin/ldconfig

%post	-n qt5opengl -p /sbin/ldconfig
%postun	-n qt5opengl -p /sbin/ldconfig

%post	-n qt5printsupport -p /sbin/ldconfig
%postun	-n qt5printsupport -p /sbin/ldconfig

%post	-n qt5sql -p /sbin/ldconfig
%postun	-n qt5sql -p /sbin/ldconfig

%post	-n qt5test -p /sbin/ldconfig
%postun	-n qt5test -p /sbin/ldconfig

%post	-n qt5widgets -p /sbin/ldconfig
%postun	-n qt5widgets -p /sbin/ldconfig

%post	-n qt5xml -p /sbin/ldconfig
%postun	-n qt5xml -p /sbin/ldconfig

%files -n qt5bootstrap-devel
%defattr(644,root,root,755)
# static-only
%{_libdir}/libQt5Bootstrap.a
%{_libdir}/libQt5Bootstrap.prl
%{_pkgconfigdir}/Qt5Bootstrap.pc
%{qt5dir}/mkspecs/modules/qt_lib_bootstrap_private.pri

%files -n qt5concurrent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Concurrent.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Concurrent.so.5

%files -n qt5concurrent-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Concurrent.so
%{_libdir}/libQt5Concurrent.prl
%{_includedir}/qt5/QtConcurrent
%{_pkgconfigdir}/Qt5Concurrent.pc
%{_libdir}/cmake/Qt5Concurrent
%{qt5dir}/mkspecs/modules/qt_lib_concurrent.pri
%{qt5dir}/mkspecs/modules/qt_lib_concurrent_private.pri

%files -n qt5core 
%defattr(644,root,root,755)
%doc LGPL_EXCEPTION.txt header.* dist/{README,changes-*}
%attr(755,root,root) %{_libdir}/libQt5Core.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Core.so.5
%dir /etc/qt5
%dir %{qt5dir}
%dir %{qt5dir}/bin
%dir %{qt5dir}/mkspecs
%dir %{qt5dir}/mkspecs/modules
%dir %{qt5dir}/plugins
%dir %{_datadir}/qt5
%dir %{_datadir}/qt5/translations

%files -n qt5core-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Core.so
%{_libdir}/libQt5Core.prl
%dir %{_includedir}/qt5
%dir %{_includedir}/qt5/QtSolutions
%{_includedir}/qt5/QtCore
%{_pkgconfigdir}/Qt5Core.pc
%{_libdir}/cmake/Qt5
%{_libdir}/cmake/Qt5Core
%{qt5dir}/mkspecs/modules/qt_lib_core.pri
%{qt5dir}/mkspecs/modules/qt_lib_core_private.pri

%files -n qt5dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5DBus.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5DBus.so.5

%files -n qt5dbus-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5DBus.so
%{_libdir}/libQt5DBus.prl
%{_includedir}/qt5/QtDBus
%{_pkgconfigdir}/Qt5DBus.pc
%{_libdir}/cmake/Qt5DBus
%{qt5dir}/mkspecs/modules/qt_lib_dbus.pri
%{qt5dir}/mkspecs/modules/qt_lib_dbus_private.pri

%files -n qt5gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Gui.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Gui.so.5
# loaded from src/gui/kernel/qgenericpluginfactory.cpp
%dir %{qt5dir}/plugins/generic
# R: udev-libs (by all qevdev* plugins)
%attr(755,root,root) %{qt5dir}/plugins/generic/libqevdevkeyboardplugin.so
%attr(755,root,root) %{qt5dir}/plugins/generic/libqevdevmouseplugin.so
%attr(755,root,root) %{qt5dir}/plugins/generic/libqevdevtabletplugin.so
%attr(755,root,root) %{qt5dir}/plugins/generic/libqevdevtouchplugin.so
# loaded from src/gui/image/qicon.cpp
%dir %{qt5dir}/plugins/iconengines
# loaded from src/gui/image/qimage{reader,writer}.cpp
%dir %{qt5dir}/plugins/imageformats
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqgif.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqico.so
# R: libjpeg
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqjpeg.so
# loaded from src/gui/kernel/qplatforminputcontextfactory.cpp
%dir %{qt5dir}/plugins/platforminputcontexts
# R: libxkbcommon
%attr(755,root,root) %{qt5dir}/plugins/platforminputcontexts/libcomposeplatforminputcontextplugin.so
# R: Qt5DBus
%attr(755,root,root) %{qt5dir}/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so
# loaded from src/gui/kernel/qplatformintegrationfactory.cpp
%dir %{qt5dir}/plugins/platforms
# R: fontconfig freetype udev-libs
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqlinuxfb.so
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqminimal.so
# R: freetype libX11 libXrender
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqoffscreen.so
# R: Qt5DBus libxcb xcb-* xorg-* ...
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqxcb.so
# loaded from src/gui/kernel/qplatformthemefactory.cpp
%dir %{qt5dir}/plugins/platformthemes
# common for base -devel and plugin-specific files
%dir %{_libdir}/cmake/Qt5Gui

%if %{with tslib}
%files -n qt5gui-generic-tslib
%defattr(644,root,root,755)
# R: tslib
%attr(755,root,root) %{qt5dir}/plugins/generic/libqtslibplugin.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QTsLibPlugin.cmake
%endif

#%if %{with directfb}
#%files -n qt5gui-platform-directfb
#%defattr(644,root,root,755)
# R: DirectFB fontconfig freetype
#%attr(755,root,root) %{qt5dir}/plugins/platforms/libqdirectfb.so
#%{_libdir}/cmake/Qt5Gui/Qt5Gui_QDirectFbIntegrationPlugin.cmake
#%endif

%if %{with kms}
%files -n qt5gui-platform-kms
%defattr(644,root,root,755)
# R: EGL GLESv2 libdrm libgbm udev-libs
#%attr(755,root,root) %{qt5dir}/plugins/platforms/libqkms.so
#%{_libdir}/cmake/Qt5Gui/Qt5Gui_QKmsIntegrationPlugin.cmake
%endif

%if %{with egl}
%files -n qt5gui-platform-egl
%defattr(644,root,root,755)
# R: egl fontconfig freetype (for two following)
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqeglfs.so
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqminimalegl.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QEglFSIntegrationPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QMinimalEglIntegrationPlugin.cmake
%endif

%if %{with gtk}
%files -n qt5gui-platformtheme-gtk2
%defattr(644,root,root,755)
# R: gtk+2
%attr(755,root,root) %{qt5dir}/plugins/platformthemes/libqgtk2.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QGtk2ThemePlugin.cmake
%endif

%files -n qt5gui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Gui.so
%{_libdir}/libQt5Gui.prl
%{_includedir}/qt5/QtGui
%{_includedir}/qt5/QtPlatformHeaders
%{_pkgconfigdir}/Qt5Gui.pc
%{_libdir}/cmake/Qt5Gui/Qt5GuiConfig*.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QEvdevKeyboardPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QEvdevMousePlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QEvdevTabletPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QEvdevTouchScreenPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QGifPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QICOPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QJpegPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QComposePlatformInputContextPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QIbusPlatformInputContextPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QLinuxFbIntegrationPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QMinimalIntegrationPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QOffscreenIntegrationPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QXcbIntegrationPlugin.cmake
%{qt5dir}/mkspecs/modules/qt_lib_gui.pri
%{qt5dir}/mkspecs/modules/qt_lib_gui_private.pri

%files -n qt5network
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Network.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Network.so.5
# loaded from src/network/bearer/qnetworkconfigmanager_p.cpp
%dir %{qt5dir}/plugins/bearer
# R: Qt5DBus
%attr(755,root,root) %{qt5dir}/plugins/bearer/libqconnmanbearer.so
%attr(755,root,root) %{qt5dir}/plugins/bearer/libqgenericbearer.so
# R: Qt5DBus
%attr(755,root,root) %{qt5dir}/plugins/bearer/libqnmbearer.so

%files -n qt5network-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Network.so
%{_libdir}/libQt5Network.prl
%{_includedir}/qt5/QtNetwork
%{_pkgconfigdir}/Qt5Network.pc
%dir %{_libdir}/cmake/Qt5Network
%{_libdir}/cmake/Qt5Network/Qt5NetworkConfig*.cmake
%{_libdir}/cmake/Qt5Network/Qt5Network_QConnmanEnginePlugin.cmake
%{_libdir}/cmake/Qt5Network/Qt5Network_QGenericEnginePlugin.cmake
%{_libdir}/cmake/Qt5Network/Qt5Network_QNetworkManagerEnginePlugin.cmake
%{qt5dir}/mkspecs/modules/qt_lib_network.pri
%{qt5dir}/mkspecs/modules/qt_lib_network_private.pri

%files -n qt5opengl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5OpenGL.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5OpenGL.so.5

%files -n qt5opengl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5OpenGL.so
%{_libdir}/libQt5OpenGL.prl
%{_includedir}/qt5/QtOpenGL
%{_pkgconfigdir}/Qt5OpenGL.pc
%{_libdir}/cmake/Qt5OpenGL
%{qt5dir}/mkspecs/modules/qt_lib_opengl.pri
%{qt5dir}/mkspecs/modules/qt_lib_opengl_private.pri

%files -n qt5openglextensions-devel
%defattr(644,root,root,755)
# static-only
%{_libdir}/libQt5OpenGLExtensions.a
%{_libdir}/libQt5OpenGLExtensions.prl
%{_includedir}/qt5/QtOpenGLExtensions
%{_pkgconfigdir}/Qt5OpenGLExtensions.pc
%{_libdir}/cmake/Qt5OpenGLExtensions
%{qt5dir}/mkspecs/modules/qt_lib_openglextensions.pri
%{qt5dir}/mkspecs/modules/qt_lib_openglextensions_private.pri

%files -n qt5platformsupport-devel
%defattr(644,root,root,755)
# static-only
%{_libdir}/libQt5PlatformSupport.a
%{_libdir}/libQt5PlatformSupport.prl
%{_includedir}/qt5/QtPlatformSupport
%{_pkgconfigdir}/Qt5PlatformSupport.pc
%{qt5dir}/mkspecs/modules/qt_lib_platformsupport_private.pri

#%files -n qt5printsupport
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libQt5PrintSupport.so.*.*.*
#%attr(755,root,root) %{_libdir}/libQt5PrintSupport.so.5
# loaded from src/printsupport/kernel/qplatformprintplugin.cpp
#%dir %{qt5dir}/plugins/printsupport
#%if %{with cups}
#%attr(755,root,root) %{qt5dir}/plugins/printsupport/libcupsprintersupport.so
#%endif

#%files -n qt5printsupport-devel
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libQt5PrintSupport.so
#%{_libdir}/libQt5PrintSupport.prl
#%{_includedir}/qt5/QtPrintSupport
#%{_pkgconfigdir}/Qt5PrintSupport.pc
#%dir %{_libdir}/cmake/Qt5PrintSupport
#%{_libdir}/cmake/Qt5PrintSupport/Qt5PrintSupportConfig*.cmake
#%if %{with cups}
#%{_libdir}/cmake/Qt5PrintSupport/Qt5PrintSupport_QCupsPrinterSupportPlugin.cmake
#%endif
#%{qt5dir}/mkspecs/modules/qt_lib_printsupport.pri
#%{qt5dir}/mkspecs/modules/qt_lib_printsupport_private.pri

%files -n qt5sql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Sql.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Sql.so.5
# loaded from src/sql/kernel/qsqldatabase.cpp
%dir %{qt5dir}/plugins/sqldrivers
# common for base -devel and plugin-specific files
%dir %{_libdir}/cmake/Qt5Sql

%if %{with db2}
%files -n qt5sql-sqldriver-db2
%defattr(644,root,root,755)
# R: (proprietary) DB2 libs
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqldb2.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QDB2DriverPlugin.cmake
%endif

%if %{with ibase}
%files -n qt5sql-sqldriver-ibase
%defattr(644,root,root,755)
# R: Firebird-lib
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqlibase.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QIBaseDriverPlugin.cmake
%endif

%if %{with sqlite}
%files -n qt5sql-sqldriver-sqlite
%defattr(644,root,root,755)
# R: sqlite 3
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqlite.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QSQLiteDriverPlugin.cmake
%endif

%if %{with sqlite2}
%files -n qt5sql-sqldriver-sqlite2
%defattr(644,root,root,755)
# R: sqlite >= 2
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqlite2.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QSQLite2DriverPlugin.cmake
%endif

%if %{with mysql}
%files -n qt5sql-sqldriver-mysql
%defattr(644,root,root,755)
# R: mysql-libs
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqlmysql.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QMYSQLDriverPlugin.cmake
%endif

%if %{with oci}
%files -n qt5sql-sqldriver-oci
%defattr(644,root,root,755)
# R: (proprietary) Oracle libs
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqloci.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QOCIDriverPlugin.cmake
%endif

%if %{with odbc}
%files -n qt5sql-sqldriver-odbc
%defattr(644,root,root,755)
# R: unixODBC
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqlodbc.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QODBCDriverPlugin.cmake
%endif

%if %{with pgsql}
%files -n qt5sql-sqldriver-pgsql
%defattr(644,root,root,755)
# R: postgresql-libs
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqlpsql.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QPSQLDriverPlugin.cmake
%endif

%if %{with freetds}
%files -n qt5sql-sqldriver-tds
%defattr(644,root,root,755)
# R: freetds
%attr(755,root,root) %{qt5dir}/plugins/sqldrivers/libqsqltds.so
%{_libdir}/cmake/Qt5Sql/Qt5Sql_QTDSDriverPlugin.cmake
%endif

%files -n qt5sql-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Sql.so
%{_libdir}/libQt5Sql.prl
%{_includedir}/qt5/QtSql
%{_pkgconfigdir}/Qt5Sql.pc
%{_libdir}/cmake/Qt5Sql/Qt5SqlConfig*.cmake
%{qt5dir}/mkspecs/modules/qt_lib_sql.pri
%{qt5dir}/mkspecs/modules/qt_lib_sql_private.pri

%files -n qt5test
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Test.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Test.so.5

%files -n qt5test-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Test.so
%{_libdir}/libQt5Test.prl
%{_includedir}/qt5/QtTest
%{_pkgconfigdir}/Qt5Test.pc
%{_libdir}/cmake/Qt5Test
%{qt5dir}/mkspecs/modules/qt_lib_testlib.pri
%{qt5dir}/mkspecs/modules/qt_lib_testlib_private.pri

%files -n qt5widgets
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Widgets.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Widgets.so.5

%files -n qt5widgets-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Widgets.so
%{_libdir}/libQt5Widgets.prl
%{_includedir}/qt5/QtWidgets
%{_pkgconfigdir}/Qt5Widgets.pc
%dir %{_libdir}/cmake/Qt5Widgets
%{_libdir}/cmake/Qt5Widgets/Qt5WidgetsConfig*.cmake
%{_libdir}/cmake/Qt5Widgets/Qt5WidgetsMacros.cmake
%{qt5dir}/mkspecs/modules/qt_lib_widgets.pri
%{qt5dir}/mkspecs/modules/qt_lib_widgets_private.pri

%files -n qt5xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Xml.so.*.*.*
%attr(755,root,root) %{_libdir}/libQt5Xml.so.5

%files -n qt5xml-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Xml.so
%{_libdir}/libQt5Xml.prl
%{_includedir}/qt5/QtXml
%{_pkgconfigdir}/Qt5Xml.pc
%{_libdir}/cmake/Qt5Xml
%{qt5dir}/mkspecs/modules/qt_lib_xml.pri
%{qt5dir}/mkspecs/modules/qt_lib_xml_private.pri

%files -n qt5-doc-common
%defattr(644,root,root,755)
%dir %{_docdir}/qt5-doc
%{_docdir}/qt5-doc/global

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qdoc
%{_docdir}/qt5-doc/qmake
%{_docdir}/qt5-doc/qtconcurrent
%{_docdir}/qt5-doc/qtcore
%{_docdir}/qt5-doc/qtdbus
%{_docdir}/qt5-doc/qtgui
%{_docdir}/qt5-doc/qtnetwork
%{_docdir}/qt5-doc/qtopengl
%{_docdir}/qt5-doc/qtplatformheaders
%{_docdir}/qt5-doc/qtprintsupport
%{_docdir}/qt5-doc/qtsql
%{_docdir}/qt5-doc/qttestlib
%{_docdir}/qt5-doc/qtwidgets
%{_docdir}/qt5-doc/qtxml

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qdoc.qch
%{_docdir}/qt5-doc/qmake.qch
%{_docdir}/qt5-doc/qtconcurrent.qch
%{_docdir}/qt5-doc/qtcore.qch
%{_docdir}/qt5-doc/qtdbus.qch
%{_docdir}/qt5-doc/qtgui.qch
%{_docdir}/qt5-doc/qtnetwork.qch
%{_docdir}/qt5-doc/qtopengl.qch
%{_docdir}/qt5-doc/qtplatformheaders.qch
%{_docdir}/qt5-doc/qtprintsupport.qch
%{_docdir}/qt5-doc/qtsql.qch
%{_docdir}/qt5-doc/qttestlib.qch
%{_docdir}/qt5-doc/qtwidgets.qch
%{_docdir}/qt5-doc/qtxml.qch
%endif

%files examples
%dir %{_examplesdir}
%doc %{_examplesdir}/README
%{_examplesdir}/examples.pro

%files -n qt5-build
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/moc-qt5
%attr(755,root,root) %{_bindir}/qdbuscpp2xml-qt5
%attr(755,root,root) %{_bindir}/qdbusxml2cpp-qt5
%attr(755,root,root) %{_bindir}/qdoc-qt5
%attr(755,root,root) %{_bindir}/qlalr-qt5
%attr(755,root,root) %{_bindir}/rcc-qt5
%attr(755,root,root) %{_bindir}/uic-qt5
%attr(755,root,root) %{qt5dir}/bin/moc
%attr(755,root,root) %{qt5dir}/bin/qdbuscpp2xml
%attr(755,root,root) %{qt5dir}/bin/qdbusxml2cpp
%attr(755,root,root) %{qt5dir}/bin/qdoc
%attr(755,root,root) %{qt5dir}/bin/qlalr
%attr(755,root,root) %{qt5dir}/bin/rcc
%attr(755,root,root) %{qt5dir}/bin/syncqt.pl
%attr(755,root,root) %{qt5dir}/bin/uic

%files -n qt5-qmake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmake-qt5
%attr(755,root,root) %{qt5dir}/bin/qmake
%{qt5dir}/mkspecs/aix-*
%{qt5dir}/mkspecs/android-*
%{qt5dir}/mkspecs/blackberry-*
%{qt5dir}/mkspecs/common
%{qt5dir}/mkspecs/cygwin-*
%{qt5dir}/mkspecs/darwin-*
%{qt5dir}/mkspecs/devices
%{qt5dir}/mkspecs/features
%{qt5dir}/mkspecs/freebsd-*
%{qt5dir}/mkspecs/hpux-*
%{qt5dir}/mkspecs/hpuxi-*
%{qt5dir}/mkspecs/hurd-*
%{qt5dir}/mkspecs/irix-*
%{qt5dir}/mkspecs/linux-*
%{qt5dir}/mkspecs/lynxos-*
%{qt5dir}/mkspecs/macx-*
%{qt5dir}/mkspecs/netbsd-*
%{qt5dir}/mkspecs/openbsd-*
%{qt5dir}/mkspecs/qnx-*
%{qt5dir}/mkspecs/sco-*
%{qt5dir}/mkspecs/solaris-*
%{qt5dir}/mkspecs/tru64-*
%{qt5dir}/mkspecs/unixware-*
%{qt5dir}/mkspecs/unsupported
%{qt5dir}/mkspecs/win32-*
%{qt5dir}/mkspecs/wince60standard-*
%{qt5dir}/mkspecs/wince70embedded-*
%{qt5dir}/mkspecs/winphone-*
%{qt5dir}/mkspecs/winrt-*
%{qt5dir}/mkspecs/*.pri

%if 0
# unpackaged files
	/usr/lib64/cmake/Qt5Gui/Qt5Gui_QEglFSKmsIntegrationPlugin.cmake
	/usr/lib64/cmake/Qt5Gui/Qt5Gui_QEglFSX11IntegrationPlugin.cmake
	/usr/lib64/cmake/Qt5Gui/Qt5Gui_QTuioTouchPlugin.cmake
	/usr/lib64/cmake/Qt5Gui/Qt5Gui_QXcbEglIntegrationPlugin.cmake
	/usr/lib64/cmake/Qt5Gui/Qt5Gui_QXcbGlxIntegrationPlugin.cmake
	/usr/lib64/libQt5EglDeviceIntegration.prl
	/usr/lib64/libQt5EglDeviceIntegration.so
	/usr/lib64/libQt5EglDeviceIntegration.so.5
	/usr/lib64/libQt5EglDeviceIntegration.so.5.5.0
	/usr/lib64/libQt5XcbQpa.prl
	/usr/lib64/libQt5XcbQpa.so
	/usr/lib64/libQt5XcbQpa.so.5
	/usr/lib64/libQt5XcbQpa.so.5.5.0
	/usr/lib64/pkgconfig/Qt5EglDeviceIntegration.pc
	/usr/lib64/pkgconfig/Qt5XcbQpa.pc
	/usr/lib64/qt5/mkspecs/haiku-g++/qmake.conf
	/usr/lib64/qt5/mkspecs/haiku-g++/qplatformdefs.h
	/usr/lib64/qt5/mkspecs/modules/qt_lib_eglfs_device_lib_private.pri
	/usr/lib64/qt5/mkspecs/modules/qt_lib_xcb_qpa_lib_private.pri
	/usr/lib64/qt5/plugins/egldeviceintegrations/libqeglfs-kms-integration.so
	/usr/lib64/qt5/plugins/egldeviceintegrations/libqeglfs-x11-integration.so
	/usr/lib64/qt5/plugins/generic/libqtuiotouchplugin.so
	/usr/lib64/qt5/plugins/xcbglintegrations/libqxcb-egl-integration.so
	/usr/lib64/qt5/plugins/xcbglintegrations/libqxcb-glx-integration.so
	/usr/share/qt5/translations/qtwebsockets_fr.qm
%endif

%changelog
