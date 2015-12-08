%bcond_with     static_libs     # don't build static library

%define		_aclocaldir	%{_datadir}/aclocal
%define		_pkgconfigdir	%{_libdir}/pkgconfig
%define		_docdir		%{_datadir}/doc

Summary:	The Vorbis General Audio Compression Codec
Name:		libvorbis
Version:	1.3.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
URL:		http://www.vorbis.com/

BuildRequires:	gcc 
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar
BuildRequires:	xz
Requires:	libogg

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

%package devel
Summary:	Development files for Ogg Vorbis library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel 

%description devel
The libvorbis-devel package contains the header files and
documentation needed to develop applications with libvorbis.

%package static
Summary:	Static development library for Ogg Vorbis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The libvorbis-static package contains the static libraries of
libvorbis.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} devel-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING README
%attr(755,root,root) %{_libdir}/libvorbis.so.*.*.*
%attr(755,root,root) %{_libdir}/libvorbis.so.0
%attr(755,root,root) %{_libdir}/libvorbisenc.so.*.*.*
%attr(755,root,root) %{_libdir}/libvorbisenc.so.2
%attr(755,root,root) %{_libdir}/libvorbisfile.so.*.*.*
%attr(755,root,root) %{_libdir}/libvorbisfile.so.3

%files devel
%defattr(644,root,root,755)
%doc devel-docs/*
%attr(755,root,root) %{_libdir}/libvorbis.so
%attr(755,root,root) %{_libdir}/libvorbisenc.so
%attr(755,root,root) %{_libdir}/libvorbisfile.so
%{_libdir}/libvorbis.la
%{_libdir}/libvorbisenc.la
%{_libdir}/libvorbisfile.la
%{_includedir}/vorbis
%{_aclocaldir}/vorbis.m4
%{_pkgconfigdir}/vorbis.pc
%{_pkgconfigdir}/vorbisenc.pc
%{_pkgconfigdir}/vorbisfile.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libvorbis.a
%{_libdir}/libvorbisenc.a
%{_libdir}/libvorbisfile.a
%endif

%changelog
