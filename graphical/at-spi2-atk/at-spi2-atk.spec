%define         _pkgconfigdir   %{_libdir}/pkgconfig
#
# Conditional build:
%bcond_with	static_libs	# static library
#
Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Name:		at-spi2-atk
Version:	2.18.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-atk/2.18/%{name}-%{version}.tar.xz
URL:		https://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	at-spi2-core-devel
BuildRequires:	atk-devel
BuildRequires:	autoconf 
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build
BuildRequires:	tar
BuildRequires:	libx11-devel
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	atk
Requires:	at-spi2-core
Requires:	dbus

%description
This package provides a GTK+ module that bridges ATK to the new D-Bus
based at-spi.

%package libs
Summary:	Shared atk-bridge library
Group:		Libraries
Requires:	at-spi2-core-libs
Requires:	atk
Requires:	dbus-libs
Requires:	glib

%description libs
Shared atk-bridge library, providing ATK/D-Bus bridge.

%package devel
Summary:	Header files for atk-bridge library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	at-spi2-core-devel
Requires:	glib-devel

%description devel
Header files for atk-bridge library.

%package static
Summary:	Static atk-bridge library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static atk-bridge library.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/modules/libatk-bridge.la \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/module/libatk-bridge.a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libatk-bridge.so
%dir %{_libdir}/gnome-settings-daemon-3.0
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files libs
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so
%{_includedir}/at-spi2-atk
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libatk-bridge-2.0.a
%endif
