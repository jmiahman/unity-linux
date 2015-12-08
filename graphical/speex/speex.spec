%bcond_with	static_libs	# don't build static library

Summary:	An open-source, patent-free speech codec
Name:		speex
Version:	1.2
%define	subver	rc2
%define	rel	2
Release:	%{subver}.%{rel}
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/speex/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	6ae7db3bab01e1d4b86bacfa8ca33e81
URL:		http://www.speex.org/
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	speexdsp-devel

%description
Speex is a patent-free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package devel
Summary:	Speex library - development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	Speex-devel

%description devel
Speex library - development files.

%package static
Summary:	Speex static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	Speex-static

%description static
Speex static library.

%package progs
Summary:	speexdec and speexenc utilities
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Obsoletes:	Speex-progs

%description progs
Utilities for the Speex codec: speexdec (decodes a Speex file and
produces a WAV or raw file) and speexenc (encodes file from WAV or raw
format using Speex).

%prep
%setup -q -n %{name}-%{version}%{subver}

%build
%configure \
	--with-ogg-libraries=%{_libdir} \
	%{!?with_static_libs:--disable-static} \
	--enable-binaries
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA=

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libspeex.so.*.*.*
%attr(755,root,root) %{_libdir}/libspeex.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/manual.pdf
%attr(755,root,root) %{_libdir}/libspeex.so
%{_libdir}/libspeex.la
# note: dir shared with speexdsp-devel
%dir %{_includedir}/speex
%{_includedir}/speex/speex.h
%{_includedir}/speex/speex_bits.h
%{_includedir}/speex/speex_callbacks.h
%{_includedir}/speex/speex_config_types.h
%{_includedir}/speex/speex_header.h
%{_includedir}/speex/speex_stereo.h
%{_includedir}/speex/speex_types.h
%{_datadir}/aclocal/speex.m4
%{_libdir}/pkgconfig/speex.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libspeex.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/speexdec
%attr(755,root,root) %{_bindir}/speexenc
%{_mandir}/man1/speexdec.1*
%{_mandir}/man1/speexenc.1*
