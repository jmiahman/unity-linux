#
# Conditional build:
%bcond_with	static_libs	# don't build static library
%bcond_with	apidocs		# do not build and package API docs
%bcond_with	python		# smixer-python binding
%bcond_with	resmgr		# Resource Manager support

%define		_sysconfdir	/etc

Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Name:		alsa-lib
Version:	1.0.29
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
Source1:	%{name}-modprobe.conf
Source2:	%{name}-asound.conf

Patch0:		alsa-lib_pcm_h.patch
Patch1:		alsa-lib_mixed_types.patch

URL:		http://www.alsa-project.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
%if %{with python}
BuildRequires:	python-devel
%endif
%{?with_resmgr:BuildRequires:	resmgr-devel}

%description
Advanced Linux Sound Architecture (ALSA) - Library

Features:
- general
	- modularized architecture
	- support for versioned and exported symbols
	- full proc filesystem support - /proc/sound
- ISA soundcards
	- support for 128k ISA DMA buffer
- mixer
	- new enhanced API for applications
	- support for unlimited number of channels
	- volume can be set in three ways (percentual (0-100), exact and
	  decibel)
	- support for mute (and hardware mute if hardware supports it)
	- support for mixer events
		- this allows two or more applications to be synchronized
- digital audio (PCM)
	- new enhanced API for applications
	- full real duplex support
	- full duplex support for SoundBlaster 16/AWE soundcards
	- digital audio data for playback and record should be read back using
	  proc filesystem
- OSS/Lite compatibility
	- full mixer compatibity
	- full PCM (/dev/dsp) compatibility

%package devel
Summary:	Advanced Linux Sound Architecture (ALSA) - header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Advanced Linux Sound Architecture (ALSA) - header files.

%package static
Summary:	Advanced Linux Sound Architecture (ALSA) - static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Advanced Linux Sound Architecture (ALSA) - static library.

%package apidocs
Summary:	ALSA Library API documentation
Group:		Documentation
BuildArch:	noarch

%description apidocs
API and internal documentation for ALSA Library.

%package smixer-python
Summary:	Python binding module for ALSA Mixer Interface
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description smixer-python
Python binding module for ALSA Mixer Interface.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
configure_opts="\
	--prefix=/usr \
	--disable-silent-rules \
	%{!?with_python:--disable-python} \
	%{?with_resmgr:--enable-resmgr} \
	--disable-static \
	--enable-rawmidi \
	--enable-seq \
	--enable-aload \
	--disable-dependency-tracking \
	--without-versioned \
"

%if %{with static_libs}
install -d build-static
cd build-static
../configure $configure_opts \
	--disable-shared \
	--enable-static
%{__make}
cd ..
%endif

install -d build-shared
cd build-shared
../configure $configure_opts \
	--enable-shared \
	--disable-static

%{__make}
%{?with_apidocs:%{__make} doc}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/alsa
install -d $RPM_BUILD_ROOT/etc/modprobe.d

%if %{with static_libs}
%{__make} -C build-static/src install-libLTLIBRARIES \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build-shared install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libasound.so.* $RPM_BUILD_ROOT/%{_lib}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libasound.so
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib}; echo libasound.so.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libasound.so

install -D utils/alsa.m4 $RPM_BUILD_ROOT%{_aclocaldir}/alsa.m4
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/alsa-base.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/asound.conf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/alsa-lib/smixer/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/asoundrc.txt
%attr(755,root,root) %{_bindir}/aserver
%attr(755,root,root) /%{_lib}/libasound.so.*.*.*
%attr(755,root,root) /%{_lib}/libasound.so.2
%dir %{_libdir}/alsa-lib
%dir %{_libdir}/alsa-lib/smixer
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-ac97.so
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-hda.so
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-sbase.so
%{_datadir}/alsa
%dir %{_sysconfdir}/alsa
%config(noreplace) %{_sysconfdir}/asound.conf
%config(noreplace) %{_sysconfdir}/modprobe.d/alsa-base.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasound.so
%{_libdir}/libasound.la
%{_includedir}/sys/asoundlib.h
%{_includedir}/alsa
%{_datadir}/aclocal/alsa.m4
%{_libdir}/pkgconfig/alsa.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libasound.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build-shared/doc/doxygen/html/*
%endif

%if %{with python}
%files smixer-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-python.so
%endif
