%bcond_with     static_libs     # static library

Summary:	GIF-manipulation library
Name:		giflib
Version:	5.1.1
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/giflib/%{name}-%{version}.tar.bz2

Patch0:		xmlto-skip-validation.patch

URL:		http://sourceforge.net/projects/giflib/
BuildRequires:	libtool
BuildRequires:	rpm-build
BuildRequires:	sed
BuildRequires:	xmlto

%description
GIF loading and saving shared library. This version uses LZW
compression (warning: patent/license issues in some countries).

%package devel
Summary:	GIF-manipulation library header files and documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libungif-devel

%description devel
Libraries and headers needed for developing programs that use libgif
to load and save GIF image files.

%package static
Summary:	GIF-manipulation static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libungif-static

%description static
Static libraries needed for developing programs that use libgif to
load and save GIF image files.

%package progs
Summary:	Programs for converting and transforming GIF images
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Provides:	libungif-progs

%description progs
This package contains various programs for manipulating GIF image
files.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
# these are unpackged examples
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/gifbg.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/gifcolor.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/gifhisto.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/gifwedge.1

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libgif.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libungif.so
ln -sf libgif.a $RPM_BUILD_ROOT%{_libdir}/libungif.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgif.so.*.*.*
%attr(755,root,root) %{_libdir}/libgif.so.7

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt doc/{gif_lib,intro}.html doc/whatsinagif
%attr(755,root,root) %{_libdir}/libgif.so
%attr(755,root,root) %{_libdir}/libungif.so
%{_libdir}/libgif.la
%{_includedir}/gif_lib.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgif.a
%{_libdir}/libungif.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gif2rgb
%attr(755,root,root) %{_bindir}/gifbuild
%attr(755,root,root) %{_bindir}/gifclrmp
%attr(755,root,root) %{_bindir}/gifecho
%attr(755,root,root) %{_bindir}/giffix
%attr(755,root,root) %{_bindir}/gifinto
%attr(755,root,root) %{_bindir}/giftext
%attr(755,root,root) %{_bindir}/giftool
%{_mandir}/man1/gif2rgb.1*
%{_mandir}/man1/gifbuild.1*
%{_mandir}/man1/gifclrmp.1*
%{_mandir}/man1/gifecho.1*
%{_mandir}/man1/giffix.1*
%{_mandir}/man1/gifinto.1*
%{_mandir}/man1/giflib.1*
%{_mandir}/man1/giftext.1*
%{_mandir}/man1/giftool.1*

%changelog
