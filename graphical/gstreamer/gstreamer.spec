%define _pkgconfigdir %{_libdir}/pkgconfig
%define _aclocaldir %{_datadir}/aclocal
%define		_gstlibdir	%{_libdir}/gstreamer-%{vmajor}
%define		_gstincludedir	%{_includedir}/gstreamer-%{vmajor}


# TODO: suid/capabilities for ptp-helper?
%define		vmajor		1.0

Summary:	GStreamer Streaming-media framework runtime
Name:		gstreamer
Version:	1.6.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gstreamer/%{name}-%{version}.tar.xz
# Source0-md5:	e72e2dc2ee06bfc045bb6010c89de520
Patch0:		%{name}-without_ps_pdf.patch
Patch1:		%{name}-eps.patch
Patch2:		%{name}-inspect-rpm-format.patch
URL:		http://gstreamer.net/
BuildRequires:	bison >= 1.875
BuildRequires:	flex >= 2.5.31
BuildRequires:	gettext >= 0.17
BuildRequires:	glib-devel >= 2.32.0
BuildRequires:	gobject-introspection-devel >= 1.31.1
BuildRequires:	libcap-devel
BuildRequires:	libtool >= 2.2.6
BuildRequires:	nasm
BuildRequires:	perl
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	tar >= 1.22
BuildRequires:	xmlto
BuildRequires:	xz
Requires:	glib >= 2.32.0

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%package devel
Summary:	Include files for GStreamer streaming-media framework
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib-devel >= 2.32.0
Obsoletes:	gstreamer-plugins-bad-devel < 0.10.10

%description devel
This package contains the includes files necessary to develop
applications and plugins for GStreamer.

%package static
Summary:	GStreamer static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static versions of GStreamer libraries.

%package apidocs
Summary:	GStreamer API documentation
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
GStreamer API documentation.

%package -n bash-completion-gstreamer
Summary:	Bash completion for GStreamer utilities
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-gstreamer
Bash completion for GStreamer utilities: gst-inspect and gst-launch.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
	--disable-examples \
	--disable-pspdf \
	--disable-silent-rules \
	--disable-tests \
	--disable-docbook \
	--disable-gtk-doc \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-devel-%{version}
install -d $RPM_BUILD_ROOT%{rpmlibdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{vmajor} \
#mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
#mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/faq \
#mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/manual \
#mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/pwg \
#	$RPM_BUILD_ROOT%{_docdir}/%{name}-devel-%{version}

# no *.la for modules - shut up check files
%{__rm} $RPM_BUILD_ROOT%{_gstlibdir}/lib*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgst*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README RELEASE
%attr(755,root,root) %{_bindir}/gst-inspect-1.0
%attr(755,root,root) %{_bindir}/gst-launch-1.0
%attr(755,root,root) %{_bindir}/gst-typefind-1.0
%attr(755,root,root) %{_libdir}/libgstbase-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstbase-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstcheck-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstcheck-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstcontroller-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstcontroller-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstnet-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstnet-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstreamer-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstreamer-%{vmajor}.so.0
%dir %{_gstlibdir}
%dir /usr/libexec/gstreamer-1.0/
%attr(755,root,root) /usr/libexec/gstreamer-1.0/gst-plugin-scanner
%attr(755,root,root) /usr/libexec/gstreamer-1.0/gst-ptp-helper
%attr(755,root,root) %{_gstlibdir}/libgstcoreelements.so
%{_mandir}/man1/gst-inspect-1.0.1*
%{_mandir}/man1/gst-launch-1.0.1*
%{_mandir}/man1/gst-typefind-1.0.1*
%{_libdir}/girepository-1.0/Gst-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstBase-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstCheck-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstController-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstNet-%{vmajor}.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstbase-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstcheck-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstcontroller-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstnet-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstreamer-%{vmajor}.so
%{_docdir}/%{name}-devel-%{version}
%{_gstincludedir}
%{_gstlibdir}/include
%{_pkgconfigdir}/gstreamer-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-base-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-check-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-controller-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-net-%{vmajor}.pc
%{_aclocaldir}/gst-element-check-%{vmajor}.m4
%{_datadir}/gir-1.0/Gst-%{vmajor}.gir
%{_datadir}/gir-1.0/GstBase-%{vmajor}.gir
%{_datadir}/gir-1.0/GstCheck-%{vmajor}.gir
%{_datadir}/gir-1.0/GstController-%{vmajor}.gir
%{_datadir}/gir-1.0/GstNet-%{vmajor}.gir

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libgstbase-%{vmajor}.a
#%{_libdir}/libgstcheck-%{vmajor}.a
#%{_libdir}/libgstcontroller-%{vmajor}.a
#%{_libdir}/libgstnet-%{vmajor}.a
#%{_libdir}/libgstreamer-%{vmajor}.a

#%files apidocs
#%defattr(644,root,root,755)
#%{_gtkdocdir}/gstreamer-%{vmajor}
#%{_gtkdocdir}/gstreamer-libs-%{vmajor}
#%{_gtkdocdir}/gstreamer-plugins-%{vmajor}

#%files -n bash-completion-gstreamer
#%defattr(644,root,root,755)
#%{_datadir}/bash-completion/completions/gst-inspect-1.0
#%{_datadir}/bash-completion/completions/gst-launch-1.0
#%attr(755,root,root) %{_datadir}/bash-completion/helpers/gst
#%attr(755,root,root) %{_datadir}/bash-completion/helpers/gst-completion-helper-1.0

%changelog
