#
# Conditional build:
%bcond_with	apidocs		# disable gtk-doc
%bcond_with	static_libs	# don't build static library

Summary:	ATK - Accessibility Toolkit
Name:		atk
Version:	2.18.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/atk/2.18/%{name}-%{version}.tar.xz
# Source0-md5:	fd3678f35004b4c92e3da39356996054
URL:		https://developer.gnome.org/atk/
BuildRequires:	autoconf 
BuildRequires:	automake
BuildRequires:	docbook-xml
BuildRequires:	gettext
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
%if %{with apidocs}
BuildRequires:	gtk-doc
BuildRequires:	gtk-doc-automake
%endif
BuildRequires:	libtool
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	rpm-build
BuildRequires:	tar
BuildRequires:	xz
Requires:	glib

%description
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
as tools such as screen readers and magnifiers, and alternative input
devices.

%package devel
Summary:	ATK - header files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib-devel 

%description devel
ATK - header files.

%package static
Summary:	ATK static library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
ATK static library.

%package apidocs
Summary:	ATK API documentation
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
ATK API documentation.


%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{__enable_disable apidocs gtk-doc} \
	--with-html-dir=%{_gtkdocdir} \
	%{__enable_disable static_libs static} \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libatk-1.0.la

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/atk}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libatk-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libatk-1.0.so.0
%{_libdir}/girepository-1.0/Atk-1.0.typelib

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libatk-1.0.so
%{_includedir}/atk-1.0
%{_libdir}/pkgconfig/atk.pc
%{_datadir}/gir-1.0/Atk-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libatk-1.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/atk
%endif
