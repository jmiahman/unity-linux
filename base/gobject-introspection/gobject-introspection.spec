Name:           gobject-introspection
Version:        1.45.4
Release:        1%{?dist}
Summary:        Introspection system for GObject-based libraries

Group:          Development/Libraries
License:        GPLv2+, LGPLv2+, MIT
URL:            http://live.gnome.org/GObjectIntrospection
#VCS:           git:git://git.gnome.org/gobject-introspection
Source0:        http://download.gnome.org/sources/gobject-introspection/1.45/%{name}-%{version}.tar.xz

Obsoletes:      gir-repository

BuildRequires:  glib-devel
BuildRequires:  python-devel
BuildRequires:  gettext
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libffi-devel
#BuildRequires:  mesa-libGL-devel
#BuildRequires:  cairo-gobject-devel
BuildRequires:  libxml2-devel
#BuildRequires:  libXfixes-devel
BuildRequires:  libx11-devel
#BuildRequires:  fontconfig-devel
#BuildRequires:  libXft-devel
BuildRequires:  freetype-devel
# Bootstrap requirements
#BuildRequires:  gnome-common
#BuildRequires:  intltool
#BuildRequires:  gtk-doc
# For doctool
#BuildRequires:  python-mako

Requires:       glib 

%description
GObject Introspection can scan C header and source files in order to
generate introspection "typelib" files.  It also provides an API to examine
typelib files, useful for creating language bindings among other
things.

%package devel
Summary: Libraries and headers for gobject-introspection
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libtool

%description devel
Libraries and headers for gobject-introspection

%prep
%setup -q

%build
(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; fi;)
%configure --disable-gtk-doc --disable-static 

make V=1

%install
%make_install

# Die libtool, die.
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%license COPYING

%{_libdir}/lib*.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/lib*.so
%dir %{_libdir}/gobject-introspection
%{_libdir}/gobject-introspection/*
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_bindir}/g-ir-*
%{_datadir}/gir-1.0
%dir %{_datadir}/gobject-introspection-1.0
%{_datadir}/gobject-introspection-1.0/*
%{_datadir}/aclocal/introspection.m4
#%{_mandir}/man1/*.gz
#%dir %{_datadir}/gtk-doc/html/gi
#%{_datadir}/gtk-doc/html/gi/*

%changelog
