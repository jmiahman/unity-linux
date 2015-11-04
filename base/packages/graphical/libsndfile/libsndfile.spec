%define         _aclocaldir     %{_datadir}/aclocal
%define         _pkgconfigdir   %{_libdir}/pkgconfig
%define         _docdir         %{_datadir}/doc

%bcond_with	regtest		# build sndfile-regtest program
%bcond_with	octave		# don't build octave binding
%bcond_with	static_libs	# don't build static library
%bcond_with	tests		# don't build tests

%ifarch x32
%undefine	with_octave
%endif

Summary:	C library for reading and writing files containing sampled sound
Name:		libsndfile
Version:	1.0.25
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.mega-nerd.com/libsndfile/files/%{name}-%{version}.tar.gz
URL:		http://www.mega-nerd.com/libsndfile/
BuildRequires:	alsa-lib-devel
BuildRequires:	flac-devel 
BuildRequires:	libogg-devel
%{?with_tests:BuildRequires:	libstdc++-devel}
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
%{?with_octave:BuildRequires:	octave-devel}
BuildRequires:	pkgconfig
BuildRequires:	sed
%{?with_regtest:BuildRequires:	sqlite3-devel}
Requires:	flac
Requires:	libogg
Requires:	libvorbis

%description
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

%package devel
Summary:	libsndfile header files and development documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	flac-devel
Requires:	libogg-devel
Requires:	libvorbis-devel

%description devel
Header files and development documentation for libsndfile.

%package static
Summary:	libsndfile static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libsndfile static libraries.

%package progs
Summary:	libsndfile utility programs
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description progs
libsndfile utility programs:
- sndfile-convert - convert a sound files from one format to another
- sndfile-info - display information about a sound file
- sndfile-play - play a sound file

%package -n octave-sndfile
Summary:	sndfile module for Octave
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave

%description -n octave-sndfile
A couple of script files for loading, saving, and playing sound files
from within Octave.

%prep
%setup -q

%if %{without tests}
%{__sed} -i 's, tests$,,' Makefile.am
%endif

%build
ac_cv_sys_largefile_CFLAGS="-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" \
%configure \
	--disable-silent-rules \
	%{!?with_regtest:--disable-sqlite} \
	%{!?with_static_libs:--disable-static} \
	--enable-largefile

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libsndfile1-dev

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libsndfile.so.*.*.*
%attr(755,root,root) %{_libdir}/libsndfile.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/*.html doc/*.jpg doc/new_file_type.HOWTO
%attr(755,root,root) %{_libdir}/libsndfile.so
%{_libdir}/libsndfile.la
%{_includedir}/sndfile.h*
%{_pkgconfigdir}/sndfile.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libsndfile.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sndfile-*
%{_mandir}/man1/sndfile-*.1*

%if %{with octave}
%files -n octave-sndfile
%defattr(644,root,root,755)
%{_datadir}/octave/site/m/sndfile_*.m
%dir %{_libdir}/octave/*/site/oct/*/sndfile
%{_libdir}/octave/*/site/oct/*/sndfile/PKG_ADD
%attr(755,root,root) %{_libdir}/octave/*/site/oct/*/sndfile/sndfile.oct
%endif

%changelog
