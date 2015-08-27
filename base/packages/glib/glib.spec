%define _target_platform %{_arch}-unity-linux-musl

Name:		glib	
Version:	2.44.1
Release:	1%{?dist}
Summary:	A library of handy utility functions

Group:		System Environment/Libraries
License:	LGPLv2+
URL:		http://www.gtk.org/
Source0:	http://fossies.org/linux/misc/glib-%{version}.tar.gz

BuildRequires:	perl, gettext-devel, zlib-devel, libtool
BuildRequires:	bzip2-devel, libffi-devel	

%description
GLib is a handy library of utility functions. This C library is
designed to solve some portability problems and provide other useful
functionality that most programs require.

%package devel
Summary: Libraries and header files for %{name} development 
Group:	 Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
%{summary}.

%prep
%setup -q


%build
# workaround packaing issue. gtk-doc.make timestamp was newer than
# Makefile.am, which triggers automake re-run
touch -r docs/reference/glib/Makefile.am gtk-doc.make

./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--disable-gtk-doc \
	--disable-compile-warnings \

make

%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/lib/charset.alias
rm %{buildroot}/usr/lib/*.la

%files
#%doc COPYING
#%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib*.so.*

%files devel
%{_bindir}/*
%{_libdir}/lib*.so
%{_libdir}/glib-2.0/
%{_libdir}/pkgconfig/*
%{_includedir}/*
#%{_mandir}/man1/*
%{_datadir}/aclocal/*

%changelog
