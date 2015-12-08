%define		dbus_version	1.8
%define		expat_version	1.95.5
%define		glib2_version	2.32
Summary:	GLib-based library for using D-BUS
Name:		dbus-glib
Version:	0.104
Release:	1
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	http://dbus.freedesktop.org/releases/dbus-glib/%{name}-%{version}.tar.gz
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	dbus-devel >= %{dbus_version}
%{?with_apidocs:BuildRequires:	docbook-xml}
BuildRequires:	expat-devel >= %{expat_version}
BuildRequires:	gettext
BuildRequires:	glib-devel >= %{glib2_version}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build
Requires:	dbus-libs >= %{dbus_version}

%description
D-BUS add-on library to integrate the standard D-BUS library with the
GLib thread abstraction and main loop.

%package devel
Summary:	Header files for GLib-based library for using D-BUS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= %{dbus_version}
Requires:	glib-devel >= %{glib2_version}

%description devel
Header files for GLib-based library for using D-BUS.

%prep
%setup -q

%build

%configure \
	--prefix=/usr \
	--disable-gtk-doc \
	--disable-silent-rules \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--enable-static=no \
	--enable-bash-completion=no \

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
# AFL not in common-licenses, so COPYING included
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libdbus-glib-1.so.*.*.*
%attr(755,root,root) %{_libdir}/libdbus-glib-1.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dbus-binding-tool
%attr(755,root,root) %{_libdir}/libdbus-glib-1.so
%{_libdir}/libdbus-glib-1.la
%{_mandir}/man1/dbus-binding-tool.1*
%{_includedir}/dbus-1.0/dbus/dbus-glib*.h
%{_includedir}/dbus-1.0/dbus/dbus-gtype-specialized.h
%{_includedir}/dbus-1.0/dbus/dbus-gvalue-parse-variant.h
%{_libdir}/pkgconfig/dbus-glib-1.pc

%changelog
