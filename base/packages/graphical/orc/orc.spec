#
# Conditional build:
%bcond_with	static_libs	# static libraries build
%bcond_with     apidocs         # disable gtk-doc

%define _pkgconfigdir %{_libdir}/pkgconfig
%define _aclocaldir %{_datadir}/aclocal


%define	libver	0.4
Summary:	The Oil Runtime Compiler
Name:		orc
Version:	0.4.24
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.xz
URL:		http://code.entropywave.com/projects/orc/
%{?with_apidocs:buildrequires: gtk-doc}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar
#BuildRequires:	which
BuildRequires:	xz

%description
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data. The "language" is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package devel
Summary:	Header files for orc library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for orc library.

%package static
Summary:	Static orc library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static orc library.

%description static -l pl.UTF-8
Statyczna biblioteka orc.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--disable-static} \
	%{?with_apidocs:--disable-gtk-docs}
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
%doc COPYING README TODO
%attr(755,root,root) %{_bindir}/orc-bugreport
%attr(755,root,root) %{_bindir}/orcc
%attr(755,root,root) %{_libdir}/liborc-%{libver}.so.*.*.*
%attr(755,root,root) %{_libdir}/liborc-%{libver}.so.0
%attr(755,root,root) %{_libdir}/liborc-test-%{libver}.so.*.*.*
%attr(755,root,root) %{_libdir}/liborc-test-%{libver}.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborc-%{libver}.so
%attr(755,root,root) %{_libdir}/liborc-test-%{libver}.so
%{_libdir}/liborc-%{libver}.la
%{_libdir}/liborc-test-%{libver}.la
%{_includedir}/orc-%{libver}
%{_pkgconfigdir}/orc-%{libver}.pc
%{_aclocaldir}/orc.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liborc-%{libver}.a
%{_libdir}/liborc-test-%{libver}.a
%endif
