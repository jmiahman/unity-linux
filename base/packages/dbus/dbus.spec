%define _localstatedir /var
%define _mandir %{_datadir}/man
%define _docdir %{_datadir}/doc
%define _pkgconfigdir  %{_libdir}/pkgconfig

%bcond_without	X11		# X11 support

Summary:	D-BUS message bus
Name:		dbus
Version:	1.10.0
Release:	1
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	http://dbus.freedesktop.org/releases/dbus/%{name}-%{version}.tar.gz
Source1:	%{name}.initd

Patch0:		fix-int64-print.patch

URL:		http://www.freedesktop.org/Software/dbus

BuildRequires:	expat-devel 
BuildRequires:	util-linux
BuildRequires:	libx11-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto
%{?with_X11:BuildRequires:	libx11-devel}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	expat 

%description
D-BUS is a system for sending messages between applications. It is
used both for the systemwide message bus service, and as a
per-user-login-session messaging facility.

%package libs
Summary:	D-BUS library
Group:		Libraries

%description libs
D-BUS library.

%package devel
Summary:	Header files for D-BUS library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for D-BUS library.

%package x11
Summary:	X11 session support for D-BUS
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description x11
This package contains D-BUS utilities to start D-BUS service together
with user X11 session.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--with-xml=expat \
	--with-dbus-user=messagebus \
	--with-system-pid-file=/var/run/dbus.pid \
	--disable-verbose-mode \
	--disable-static \
	--enable-inotify \
	--disable-dnotify \
	--disable-tests \
	--disable-asserts \
	--disable-doxygen-docs \
	--disable-xml-docs \
	%{!?with_X11:--without-x}

make

%install
rm -rf $RPM_BUILD_ROOT

make -j1 DESTDIR=%{buildroot} install

install -Dm755 %{SOURCE1} %{buildroot}/etc/init.d/dbus


# for local configuration in dbus 1.10+
install -d $RPM_BUILD_ROOT/etc/dbus-1/session.d
install -d $RPM_BUILD_ROOT/etc/dbus-1/system.d

%clean
rm -rf $RPM_BUILD_ROOT

%pre
addgroup -S messagebus 2>/dev/null
adduser -S -H -h /dev/null -s /sbin/nologin -D messagebus -G messagebus 2>/dev/null
exit 0

%post
exec dbus-uuidgen --ensure
exit 0

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dbus-cleanup-sockets
%attr(755,root,root) %{_bindir}/dbus-daemon
%attr(755,root,root) %{_bindir}/dbus-uuidgen
%attr(755,root,root) %{_bindir}/dbus-monitor
%attr(755,root,root) %{_bindir}/dbus-run-session
%attr(755,root,root) %{_bindir}/dbus-send
%attr(755,root,root) %{_bindir}/dbus-test-tool
%attr(755,root,root) %{_bindir}/dbus-update-activation-environment
%dir %{_datadir}/dbus-1/services
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/session.conf
%{_datadir}/dbus-1/system.conf
/etc/init.d/dbus
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/session.conf
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.conf
%dir %{_localstatedir}/lib/dbus
%dir %{_localstatedir}/run/dbus

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README doc/TODO
%attr(755,root,root) %{_libdir}/libdbus-1.so.*.*.*
%{_libdir}/libdbus-1.so.3
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/session.d
%dir %{_datadir}/dbus-1/system.d
%dir /etc/dbus-1
%dir /etc/dbus-1/session.d
%dir /etc/dbus-1/system.d

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-1.so
%{_libdir}/libdbus-1.la
%dir %{_libdir}/dbus-1.0
%{_libdir}/dbus-1.0/include
%{_includedir}/dbus-1.0
%{_pkgconfigdir}/dbus-1.pc
%dir %{_docdir}/dbus
%{_docdir}/dbus/*.png
%{_docdir}/dbus/*.svg
%{_docdir}/dbus/*.txt

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dbus-launch

%changelog
