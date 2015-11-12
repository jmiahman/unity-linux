#
# Conditional build:
%bcond_with	apidocs		# disable gtk-doc
%bcond_with	libvisual	# don't build libvisual plugin
%bcond_with	tremor		# ivorbisdec plugin (Tremor integer Ogg Vorbis decoder)
%bcond_with	v4l1		# Video4Linux 1 plugin (for Linux < 2.6.35 or so)
%bcond_with	orc             #

%define		gstname		gst-plugins-base
%define		vmajor		1.0
%define		gst_req_ver	1.6.1

Summary:	GStreamer Streaming-media framework base plugins
Name:		gstreamer-plugins-base
Version:	1.6.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-base/%{gstname}-%{version}.tar.xz
# Source0-md5:	a89933afbe45d8f8c92d89c2f1199ecb
URL:		http://gstreamer.freedesktop.org/
%{?with_apidocs:BuildRequires:	docbook-dtd412-xml}
BuildRequires:	gettext >= 0.17
BuildRequires:	glib-devel >= 2.32
BuildRequires:	gobject-introspection-devel >= 1.31.1
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.12}
BuildRequires:	iso-codes
BuildRequires:	libtool >= 2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	orc-devel >= 0.4.23
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	tar >= 1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
##
## plugins
##
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	cdparanoia3-devel >= 10.2
BuildRequires:	freetype-devel >= 2.1.2
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libtheora-devel >= 1.1
%{?with_libvisual:BuildRequires:	libvisual-devel >= 0.4.0}
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:	pango-devel >= 1.22.0
BuildRequires:	rpm-build >= 1.98
%{?with_tremor:BuildRequires:	tremor-devel}
%{?with_orc:BuildRequires:   orc-devel}
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxv-devel
# old GIR format
Requires:	glib >= 2.32
Requires:	gstreamer >= %{gst_req_ver}
Requires:	orc >= 0.4.23
Suggests:	iso-codes

%define		gstlibdir 	%{_libdir}/gstreamer-%{vmajor}
%define		gstincludedir	%{_includedir}/gstreamer-%{vmajor}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%package devel
Summary:	Include files for GStreamer streaming-media framework plugins
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib-devel >= 2.32
Requires:	gstreamer-devel >= %{gst_req_ver}

%description devel
Include files for GStreamer streaming-media framework plugins.

%package apidocs
Summary:	GStreamer streaming-media framework plugins API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GStreamer streaming-media framework plugins API documentation.

##
## Plugins
##

%package -n gstreamer-audiosink-alsa
Summary:	GStreamer plugins for the ALSA sound architecture
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-alsa
Obsoletes:	gstreamer-audiosink-alsaspdif

%description -n gstreamer-audiosink-alsa
Input and output plugin for the ALSA soundcard driver architecture.

%package -n gstreamer-audio-effects-base
Summary:	GStreamer base audio effects plugins
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-audio-effects-base
GStreamer base audio effects plugins.

%package -n gstreamer-cdparanoia
Summary:	GStreamer plugin for CD audio input using CDParanoia IV
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cdparanoia3-libs >= 10.2

%description -n gstreamer-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer.

%package -n gstreamer-ivorbisdec
Summary:	GStreamer plugin for decoding Ogg Vorbis audio files using Tremor
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-ivorbisdec
Plugin for playing Ogg Vorbis audio files using Tremor.

%package -n gstreamer-libvisual
Summary:	GStreamer libvisual plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libvisual >= 0.4.0

%description -n gstreamer-libvisual
GStreamer libvisual plugin.

%package -n gstreamer-pango
Summary:	GStreamer pango plugins
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pango >= 1:1.22.0

%description -n gstreamer-pango
This package contains textoverlay and timeoverlay GStreamer plugins.

%package -n gstreamer-theora
Summary:	GStreamer Ogg Theora plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtheora >= 1.1

%description -n gstreamer-theora
GStreamer Ogg Theora plugin.

%package -n gstreamer-video4linux
Summary:	GStreamer plugin for Video 4 Linux source
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-glib >= 143

%description -n gstreamer-video4linux
GStreamer plugin for Video 4 Linux source.

%package -n gstreamer-vorbis
Summary:	GStreamer plugin for encoding and decoding Ogg Vorbis audio files
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-vorbis
Plugins for creating and playing Ogg Vorbis audio files.

%package -n gstreamer-imagesink-x
Summary:	GStreamer XFree86/X.org output plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-imagesink-x
Standard XFree86/X.org image sink.

%package -n gstreamer-imagesink-xv
Summary:	GStreamer Xvideo output plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-imagesink-xv
XFree86/X.org image sink via Xvideo extension.

%prep
%setup -q -n %{gstname}-%{version}

%build
%configure \
	%{!?with_tremor:--disable-ivorbis} \
	%{!?with_libvisual:--disable-libvisual} \
	--disable-examples \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	%{?with_libvisual:--enable-orc} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgst*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_bindir}/gst-device-monitor-%{vmajor}
%attr(755,root,root) %{_bindir}/gst-discoverer-%{vmajor}
%attr(755,root,root) %{_bindir}/gst-play-%{vmajor}
%attr(755,root,root) %{_libdir}/libgstallocators-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstallocators-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstapp-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstapp-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstaudio-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstaudio-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstfft-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstfft-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstpbutils-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstpbutils-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstriff-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstriff-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstrtp-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstrtp-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstrtsp-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstrtsp-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstsdp-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstsdp-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgsttag-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgsttag-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstvideo-%{vmajor}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstvideo-%{vmajor}.so.0
%{_mandir}/man1/gst-device-monitor-%{vmajor}.1*
%{_mandir}/man1/gst-discoverer-%{vmajor}.1*
%{_mandir}/man1/gst-play-%{vmajor}.1*
# plugins with no external dependencies
%attr(755,root,root) %{gstlibdir}/libgstapp.so
%attr(755,root,root) %{gstlibdir}/libgstaudioconvert.so
%attr(755,root,root) %{gstlibdir}/libgstaudiorate.so
%attr(755,root,root) %{gstlibdir}/libgstaudiotestsrc.so
%attr(755,root,root) %{gstlibdir}/libgstencodebin.so
%attr(755,root,root) %{gstlibdir}/libgstgio.so
%attr(755,root,root) %{gstlibdir}/libgstplayback.so
%attr(755,root,root) %{gstlibdir}/libgstsubparse.so
%attr(755,root,root) %{gstlibdir}/libgsttcp.so
%attr(755,root,root) %{gstlibdir}/libgsttypefindfunctions.so
%attr(755,root,root) %{gstlibdir}/libgstvideoconvert.so
%attr(755,root,root) %{gstlibdir}/libgstvideorate.so
%attr(755,root,root) %{gstlibdir}/libgstvideoscale.so
%attr(755,root,root) %{gstlibdir}/libgstvideotestsrc.so
%{_libdir}/girepository-1.0/GstAllocators-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstApp-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstAudio-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstFft-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstPbutils-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstRtp-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstRtsp-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstSdp-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstTag-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstVideo-%{vmajor}.typelib
%{_datadir}/gst-plugins-base

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstallocators-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstapp-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstaudio-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstfft-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstpbutils-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstriff-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstrtp-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstrtsp-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstsdp-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgsttag-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstvideo-%{vmajor}.so
%{gstincludedir}/gst/allocators
%{gstincludedir}/gst/app
%{gstincludedir}/gst/audio
%{gstincludedir}/gst/fft
%{gstincludedir}/gst/pbutils
%{gstincludedir}/gst/riff
%{gstincludedir}/gst/rtp
%{gstincludedir}/gst/rtsp
%{gstincludedir}/gst/sdp
%{gstincludedir}/gst/tag
%{gstincludedir}/gst/video
%{_pkgconfigdir}/gstreamer-allocators-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-app-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-audio-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-fft-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-pbutils-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-plugins-base-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-riff-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-rtp-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-rtsp-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-sdp-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-tag-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-video-%{vmajor}.pc
%{_datadir}/gir-1.0/GstAllocators-%{vmajor}.gir
%{_datadir}/gir-1.0/GstApp-%{vmajor}.gir
%{_datadir}/gir-1.0/GstAudio-%{vmajor}.gir
%{_datadir}/gir-1.0/GstFft-%{vmajor}.gir
%{_datadir}/gir-1.0/GstPbutils-%{vmajor}.gir
%{_datadir}/gir-1.0/GstRtp-%{vmajor}.gir
%{_datadir}/gir-1.0/GstRtsp-%{vmajor}.gir
%{_datadir}/gir-1.0/GstSdp-%{vmajor}.gir
%{_datadir}/gir-1.0/GstTag-%{vmajor}.gir
%{_datadir}/gir-1.0/GstVideo-%{vmajor}.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-base-libs-%{vmajor}
%{_gtkdocdir}/gst-plugins-base-plugins-%{vmajor}
%endif

##
## Plugins
##

%files -n gstreamer-audiosink-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstalsa.so

%files -n gstreamer-audio-effects-base
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstadder.so
%attr(755,root,root) %{gstlibdir}/libgstaudioresample.so
%attr(755,root,root) %{gstlibdir}/libgstvolume.so

%files -n gstreamer-cdparanoia
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdparanoia.so

%if %{with tremor}
%files -n gstreamer-ivorbisdec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstivorbisdec.so
%endif

%if %{with libvisual}
%files -n gstreamer-libvisual
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstlibvisual.so
%endif

#%files -n gstreamer-pango
#%defattr(644,root,root,755)
#%attr(755,root,root) %{gstlibdir}/libgstpango.so

%files -n gstreamer-theora
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttheora.so

%if %{with v4l1}
%files -n gstreamer-video4linux
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux.so
%endif

%files -n gstreamer-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvorbis.so
%attr(755,root,root) %{gstlibdir}/libgstogg.so

%files -n gstreamer-imagesink-x
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstximagesink.so

%files -n gstreamer-imagesink-xv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstxvimagesink.so

%changelog
