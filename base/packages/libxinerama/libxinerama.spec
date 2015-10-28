Summary:	Xinerama extension library
Name:		libxinerama
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2
# Source0-md5:	9336dc46ae3bf5f81c247f7131461efd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed
BuildRequires:	libxext-devel
BuildRequires:	xineramaproto
BuildRequires:	util-macros

%description
Xinerama extension library.

%package devel
Summary:	Header files for libXinerama library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxext-devel
Requires:	xineramaproto

%description devel
Xinerama extension library.

This package contains the header files needed to develop programs that
use libXinerama.

%prep
%setup -q -n libXinerama-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXinerama.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXinerama.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXinerama.so
%{_libdir}/libXinerama.la
%{_includedir}/X11/extensions/Xinerama.h
%{_includedir}/X11/extensions/panoramiXext.h
%{_pkgconfigdir}/xinerama.pc
%{_mandir}/man3/Xinerama*.3*

%changelog
