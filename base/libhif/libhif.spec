

Summary:   Simple package library built on top of hawkey and librepo
Name:      libhif
Version:   0.2.1
Release:   1%{?dist}
License:   LGPLv2+
Group:     Development/Libraries
URL:       https://github.com/hughsie/libhif
Source0:   http://people.freedesktop.org/~hughsient/releases/libhif-%{version}.tar.xz

BuildRequires: glib-devel
BuildRequires: libtool
#BuildRequires: docbook-utils
#BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel
BuildRequires: hawkey-devel >= 0.4.6
BuildRequires: rpm-devel >= 4.11.0
BuildRequires: librepo-devel >= 1.7.11
BuildRequires: libsolv-devel

# Bootstrap build requirements
BuildRequires: automake autoconf libtool

%description
This library provides a simple interface to hawkey and librepo and is currently
used by PackageKit and rpm-ostree.

%package devel
Summary: GLib Libraries and headers for libhif
Requires: %{name} = %{version}-%{release}

%description devel
GLib headers and libraries for libhif.

%prep
%setup -q

%build
%configure \
        --disable-gtk-doc \
        --disable-static \
        --disable-silent-rules \
	--disable-gtk-doc \
	--enable-dnf-yumdb \

make %{?_smp_mflags}

%install

make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/bin/
%__cp %{_builddir}/%{name}-%{version}/libhif/hif-cmd %{buildroot}/usr/bin/

rm -f $RPM_BUILD_ROOT%{_libdir}/libhif*.la
rm -rf $RPM_BUILD_ROOT/usr/share/gtk-doc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%doc README.md AUTHORS NEWS COPYING
%{_bindir}/*
%{_libdir}/libhif.so.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/libhif.so
%{_libdir}/pkgconfig/libhif.pc
%dir %{_includedir}/libhif
%{_includedir}/libhif/*.h
#%{_datadir}/gtk-doc
%{_datadir}/gir-1.0/*.gir

%changelog
* Mon Nov 30 2015 JMiahMan <JMiahMan@unity-linux.org> - 0.2.1-1
- Initial release for Unity-Linux
