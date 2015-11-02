%define _sysconfdir	/etc

Summary:	Protocol definitions and daemon for D-Bus at-spi
Name:		at-spi2-core
Version:	2.18.1
Release:	1
License:	LGPL v2+
Group:		Daemons
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-core/2.18/%{name}-%{version}.tar.xz

Patch0:		fix-buffer-overrun.patch

URL:		https://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	autoconf 
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar
BuildRequires:	libx11-devel
BuildRequires:	libxevie-devel
BuildRequires:	libxext-devel
BuildRequires:	libxi-devel
BuildRequires:	libxtst-devel
BuildRequires:	perl-xml-parser
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus

%description
at-spi allows assistive technologies to access GTK-based applications.
Essentially it exposes the internals of applications for automation,
so tools such as screen readers, magnifiers, or even scripting
interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions. It has
been completely rewritten to use D-Bus rather than ORBIT / CORBA for
its transport protocol.

%package libs
Summary:	at-spi2 core library
Group:		Libraries
Requires:	dbus-libs
Requires:	glib

%description libs
at-spi2 core library.

%package devel
Summary:	Header files for at-spi2 library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-devel
Requires:	glib-devel
Requires:	libx11-devel

%description devel
Header files for at-spi2 library.

%prep
%setup -q
%patch0 -p1

%build
DATADIRNAME="share" %configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--disable-gtk-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libexecdir}/at-spi-bus-launcher
%attr(755,root,root) %{_libexecdir}/at-spi2-registryd
%dir %{_datadir}/dbus-1/accessibility-services
%{_datadir}/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
%{_datadir}/dbus-1/services/org.a11y.Bus.service
%dir %{_sysconfdir}/at-spi2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/at-spi2/accessibility.conf
%{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatspi.so.*.*.*
%attr(755,root,root) %{_libdir}/libatspi.so.0
%{_libdir}/girepository-1.0/Atspi-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatspi.so
%{_includedir}/at-spi-2.0
%{_datadir}/gir-1.0/Atspi-2.0.gir
%{_libdir}/pkgconfig/atspi-2.pc

%changelog
