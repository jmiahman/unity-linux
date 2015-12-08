#
# Conditional build:
%bcond_with	static_libs	# don't build static library
#
Summary:	SpeexDSP - speech processing library that goes along with the Speex codec
Name:		speexdsp
Version:	1.2
%define	subver	rc3
%define	rel	3
Release:	0.%{subver}.%{rel}
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/speex/%{name}-%{version}%{subver}.tar.gz
URL:		http://www.speex.org/
BuildRequires:	libtool
BuildRequires:	sed

%description
SpeexDSP is a speech processing library that goes along with the Speex
codec.

%package devel
Summary:	SpeexDSP library - development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
SpeexDSP library - development files.

%package static
Summary:	SpeexDSP static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SpeexDSP static library.

%prep
%setup -q -n %{name}-%{version}%{subver}

# make it not depend on caller's configure checks
%{__sed} -i -e 's/defined HAVE_STDINT_H/1/' include/speex/speexdsp_config_types.h.in

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
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
%attr(755,root,root) %{_libdir}/libspeexdsp.so.*.*.*
%attr(755,root,root) %{_libdir}/libspeexdsp.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/manual.pdf
%attr(755,root,root) %{_libdir}/libspeexdsp.so
%{_libdir}/libspeexdsp.la
# note: dir shared with speex-devel
%dir %{_includedir}/speex
%{_includedir}/speex/speex_echo.h
%{_includedir}/speex/speex_jitter.h
%{_includedir}/speex/speex_preprocess.h
%{_includedir}/speex/speex_resampler.h
%{_includedir}/speex/speexdsp_*.h
%{_libdir}/pkgconfig/speexdsp.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libspeexdsp.a
%endif
