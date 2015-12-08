%bcond_with		apidocs		# do not build and package API docs
%define _pkgconfigdir %{_libdir}/pkgconfig

Summary:	Theora - video codec intended for use within Ogg multimedia streaming system
Name:		libtheora
Version:	1.1.1
Release:	1%{?dist}
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.bz2
# Source0-md5:	292ab65cedd5021d6b7ddd117e07cd8e
Patch0:		link.patch
Patch1:		libpng16.patch
URL:		http://www.theora.org/
BuildRequires:	sdl-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libogg-devel >= 1.1
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1.0.1
BuildRequires:	pkgconfig
BuildRequires:	rpm >= 4.4.9-56
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex-bibtex
BuildRequires:	tetex-latex-ltablex
BuildRequires:	transfig
%endif
Requires:	libogg >= 1.1
Requires:	libvorbis >= 1.0.1
Provides:	libtheora-mmx

%define		no_install_post_check_so	1

%description
Theora is Xiph.Org's first publicly released video codec, intended for
use within the Ogg's project's Ogg multimedia streaming system. Theora
is derived directly from On2's VP3 codec; Currently the two are nearly
identical, varying only in framing headers, but Theora will diverge
and improve from the main VP3 development lineage as time progresses.

%package devel
Summary:	Header files for Theora library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel >= 1.1
Provides:	libtheora-mmx-devel

%description devel
Header files for Theora library.

%package static
Summary:	Static Theora library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libtheora-mmx-static
Obsoletes:	libtheora-mmx-static

%description static
Static Theora library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure

%{__make}
%if %{with apidocs}
%{__make} -C doc/spec
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/libtheora-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING LICENSE README
%attr(755,root,root) %{_libdir}/libtheora.so.*.*.*
%attr(755,root,root) %{_libdir}/libtheora.so.0
%attr(755,root,root) %{_libdir}/libtheoradec.so.*.*.*
%attr(755,root,root) %{_libdir}/libtheoradec.so.1
%attr(755,root,root) %{_libdir}/libtheoraenc.so.*.*.*
%attr(755,root,root) %{_libdir}/libtheoraenc.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/{color.html,draft-ietf-avt-rtp-theora-00.txt,vp3-format.txt} doc/libtheora/html doc/spec/Theora.pdf
%attr(755,root,root) %{_libdir}/libtheora.so
%attr(755,root,root) %{_libdir}/libtheoradec.so
%attr(755,root,root) %{_libdir}/libtheoraenc.so
%{_libdir}/libtheora.la
%{_libdir}/libtheoradec.la
%{_libdir}/libtheoraenc.la
%{_includedir}/theora
%{_pkgconfigdir}/theora.pc
%{_pkgconfigdir}/theoradec.pc
%{_pkgconfigdir}/theoraenc.pc

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libtheora.a
#%{_libdir}/libtheoradec.a
#%{_libdir}/libtheoraenc.a

%changelog
