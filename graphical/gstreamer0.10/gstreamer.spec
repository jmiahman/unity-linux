Summary:	GStreamer Streaming-media framework runtime
Name:		gstreamer
Version:	0.10.36
Release:	7
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz

#Patch0:		gstreamer-without_ps_pdf.patch
#Patch1:		gstreamer-eps.patch
#Patch2:		gstreamer-inspect-rpm-format.patch
Patch3:		bison3.patch

URL:		http://gstreamer.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel >= 0.6.8
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	nasm
BuildRequires:	perl
BuildRequires:	pkgconfig 
BuildRequires:	python
BuildRequires:	tar
BuildRequires:	xmlto
BuildRequires:	xz
Requires:	glib

%define		__gst_inspect	%{_bindir}/gst-inspect-0.10
%define		vmajor		%(echo %{version} | cut -d. -f1,2)
%define		_gstlibdir	%{_libdir}/gstreamer-%{vmajor}
%define		_gstincludedir	%{_includedir}/gstreamer-%{vmajor}

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
Requires:	glib-devel
Requires:	libxml2-devel

%description devel
This package contains the includes files necessary to develop
applications and plugins for GStreamer.

%package static
Summary:	GStreamer static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static versions of GStreamer libraries.

%prep
%setup -q -n gstreamer-%{version}
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
%patch3 -p1

%build
# po/Makefile.in.in is modified
#{__gettextize}
%{__libtoolize}
%{__aclocal} -I common/m4 -I m4 -I .
%{__autoconf}
%{__autoheader}
%{__automake} --add-missing
%configure \
	--disable-examples \
	--disable-pspdf \
	--disable-silent-rules \
	--disable-tests \
	--disable-docbook \
	--disable-gtk-doc \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


# no *.la for modules - shut up check files
%{__rm} $RPM_BUILD_ROOT%{_gstlibdir}/lib*.la
# *.la for libs kept - no .private dependencies in *.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
# generic launchers
%attr(755,root,root) %{_bindir}/gst-feedback
%attr(755,root,root) %{_bindir}/gst-inspect
%attr(755,root,root) %{_bindir}/gst-launch
%attr(755,root,root) %{_bindir}/gst-typefind
%attr(755,root,root) %{_bindir}/gst-xmlinspect
%attr(755,root,root) %{_bindir}/gst-xmllaunch
# versioned
%attr(755,root,root) %{_bindir}/gst-feedback-0.10
%attr(755,root,root) %{_bindir}/gst-inspect-0.10
%attr(755,root,root) %{_bindir}/gst-launch-0.10
%attr(755,root,root) %{_bindir}/gst-typefind-0.10
%attr(755,root,root) %{_bindir}/gst-xmlinspect-0.10
%attr(755,root,root) %{_bindir}/gst-xmllaunch-0.10
%attr(755,root,root) %{_libdir}/libgstbase-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstbase-0.10.so.0
%attr(755,root,root) %{_libdir}/libgstcheck-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstcheck-0.10.so.0
%attr(755,root,root) %{_libdir}/libgstcontroller-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstcontroller-0.10.so.0
%attr(755,root,root) %{_libdir}/libgstdataprotocol-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstdataprotocol-0.10.so.0
%attr(755,root,root) %{_libdir}/libgstnet-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstnet-0.10.so.0
%attr(755,root,root) %{_libdir}/libgstreamer-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstreamer-0.10.so.0
%dir %{_gstlibdir}
#%attr(755,root,root) %{_gstlibdir}/gst-plugin-scanner
%attr(755,root,root) %{_gstlibdir}/libgstcoreelements.so
%attr(755,root,root) %{_gstlibdir}/libgstcoreindexers.so
%{_mandir}/man1/gst-feedback-0.10.1*
%{_mandir}/man1/gst-inspect-0.10.1*
%{_mandir}/man1/gst-launch-0.10.1*
%{_mandir}/man1/gst-typefind-0.10.1*
%{_mandir}/man1/gst-xmlinspect-0.10.1*
%{_mandir}/man1/gst-xmllaunch-0.10.1*
%{_libdir}/girepository-1.0/Gst-0.10.typelib
%{_libdir}/girepository-1.0/GstBase-0.10.typelib
%{_libdir}/girepository-1.0/GstCheck-0.10.typelib
%{_libdir}/girepository-1.0/GstController-0.10.typelib
%{_libdir}/girepository-1.0/GstNet-0.10.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstbase-0.10.so
%attr(755,root,root) %{_libdir}/libgstcheck-0.10.so
%attr(755,root,root) %{_libdir}/libgstcontroller-0.10.so
%attr(755,root,root) %{_libdir}/libgstdataprotocol-0.10.so
%attr(755,root,root) %{_libdir}/libgstnet-0.10.so
%attr(755,root,root) %{_libdir}/libgstreamer-0.10.so
%{_libdir}/libgstbase-0.10.la
%{_libdir}/libgstcheck-0.10.la
%{_libdir}/libgstcontroller-0.10.la
%{_libdir}/libgstdataprotocol-0.10.la
%{_libdir}/libgstnet-0.10.la
%{_libdir}/libgstreamer-0.10.la
%{_gstincludedir}
%{_pkgconfigdir}/gstreamer-0.10.pc
%{_pkgconfigdir}/gstreamer-base-0.10.pc
%{_pkgconfigdir}/gstreamer-check-0.10.pc
%{_pkgconfigdir}/gstreamer-controller-0.10.pc
%{_pkgconfigdir}/gstreamer-dataprotocol-0.10.pc
%{_pkgconfigdir}/gstreamer-net-0.10.pc
%{_aclocaldir}/gst-element-check-0.10.m4
%{_datadir}/gir-1.0/Gst-0.10.gir
%{_datadir}/gir-1.0/GstBase-0.10.gir
%{_datadir}/gir-1.0/GstCheck-0.10.gir
%{_datadir}/gir-1.0/GstController-0.10.gir
%{_datadir}/gir-1.0/GstNet-0.10.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgstbase-0.10.a
%{_libdir}/libgstcheck-0.10.a
%{_libdir}/libgstcontroller-0.10.a
%{_libdir}/libgstdataprotocol-0.10.a
%{_libdir}/libgstnet-0.10.a
%{_libdir}/libgstreamer-0.10.a

%changelog
