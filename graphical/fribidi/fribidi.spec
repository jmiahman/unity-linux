#
# Conditional build:
%bcond_without	glib		# Glib usage
%bcond_with	static_libs	# static library
#
Summary:	GNU FriBidi - library implementing the Unicode BiDi algorithm
Name:		fribidi
Version:	0.19.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://fribidi.org/download/%{name}-%{version}.tar.bz2
URL:		http://fribidi.freedesktop.org/
%{?with_glib:BuildRequires:	glib-devel}
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_glib:Requires:	glib}

%description
GNU FriBidi is a free Implementation of the Unicode BiDi algorithm.

%package devel
Summary:	Header files for FriBidi library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_glib:Requires:	glib-devel}

%description devel
The fribidi-devel package includes header files for the fribidi
package.

%package static
Summary:	Static FriBidi library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FriBidi library.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-glib%{!?with_glib:=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/fribidi
%attr(755,root,root) %{_libdir}/libfribidi.so.*.*.*
%attr(755,root,root) %{_libdir}/libfribidi.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfribidi.so
%{_libdir}/libfribidi.la
%{_includedir}/fribidi
%{_libdir}/pkgconfig/fribidi.pc
%{_mandir}/man3/fribidi_*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfribidi.a
%endif

%changelog
