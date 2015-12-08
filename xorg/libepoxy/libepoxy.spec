Summary:	Epoxy - GL dispatch library
Name:		libepoxy
Version:	1.3.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/anholt/libepoxy/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		https://github.com/anholt/libepoxy

BuildRequires:	mesa-libegl-devel
BuildRequires:	mesa-libgl-devel libtool
BuildRequires:	libx11-devel python
BuildRequires:	autoconf automake util-macros

%description
Epoxy is a library for handling OpenGL function pointer management for
you.

%package devel
Summary:	Development files for libepoxy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use libepoxy.

%prep
%setup -q

%build
./autogen.sh
%configure \
	--disable-silent-rules \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--disable-static \
	--enable-shared \

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libepoxy.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_libdir}/libepoxy.so.0
%attr(755,root,root) %{_libdir}/libepoxy.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepoxy.so
%{_includedir}/epoxy
%{_libdir}/pkgconfig/epoxy.pc

%changelog
