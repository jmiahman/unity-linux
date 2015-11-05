%bcond_with     static_libs     # don't build static library

Summary:	WebRTC Audio Processing library
Name:		webrtc-audio-processing
Version:	0.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/%{name}-%{version}.tar.xz
# Source0-md5:	da25bb27812c8404060d4cc0dc712f04
URL:		http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/

BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	tar
BuildRequires:	xz

%description
WebRTC is an open source project that enables web browsers with
Real-Time Communications (RTC) capabilities via simple Javascript
APIs. The WebRTC components have been optimized to best serve this
purpose. WebRTC implements the W3C's proposal for video conferencing
on the web.

%package devel
Summary:	Header files for WebRTC Audio Processing library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the header files needed to develop programs
which make use of WebRTC Audio Processing library.

%package static
Summary:	Static WebRTC Audio Processing library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WebRTC Audio Processing library.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS PATENTS README
%attr(755,root,root) %{_libdir}/libwebrtc_audio_processing.so.*.*.*
%attr(755,root,root) %{_libdir}/libwebrtc_audio_processing.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebrtc_audio_processing.so
%{_includedir}/webrtc_audio_processing
%{_libdir}/pkgconfig/webrtc-audio-processing.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwebrtc_audio_processing.a
%endif

%changelog
