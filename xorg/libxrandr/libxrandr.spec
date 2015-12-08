Summary:	X Randr extension library
Name:		libxrandr
Version:	1.5.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrandr-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxrender-devel
BuildRequires:	randrproto
BuildRequires:	renderproto
BuildRequires:	xextproto
BuildRequires:	util-macros
Requires:	libx11

%description
X Resize and Rotate extension library.

%package devel
Summary:	Header files for libXrandr library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxext-devel
Requires:	libxrender-devel
Requires:	randrproto

%description devel
X Resize and Rotate extension library.

This package contains the header files needed to develop programs that
use libXrandr.

%prep
%setup -q -n libXrandr-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake} --add-missing
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
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libXrandr.so.*.*.*
%{_libdir}/libXrandr.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXrandr.so
%{_libdir}/libXrandr.la
%{_includedir}/X11/extensions/Xrandr.h
%{_pkgconfigdir}/xrandr.pc
%{_mandir}/man3/XRR*.3*
%{_mandir}/man3/Xrandr.3*

%changelog
