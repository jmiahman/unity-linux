%bcond_with	gtk_doc		# disable gtk-doc
%bcond_with	apidocs		# disable apidocs
%bcond_with	static_libs	# don't build static library

Summary:	ASN.1 library used in GNUTLS
Name:		libtasn1
Version:	4.7
Release:	1
License:	LGPL v2.1+ (library), GPL v3+ (tools)
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/libtasn1/
BuildRequires:	docbook-xml
%{?with_apidocs:BuildRequires:	gtk-doc}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build
BuildRequires:	sed
BuildRequires:	help2man
BuildRequires:	texinfo

%description
Library 'libasn1' developed for ASN1 (Abstract Syntax Notation One)
structures management. The main features of this library are:
- on line ASN1 structure management that doesn't require any C code
  file generation.
- off line ASN1 structure management with C code file generation
  containing an array.
- DER (Distinguish Encoding Rules) encoding
- no limits for INTEGER and ENUMERATED values

%package devel
Summary:	Header files etc to develop libtasn1 applications
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc to develop libtasn1 applications.

%package static
Summary:	Static libtasn1 library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtasn1 library.

%package apidocs
Summary:	libtasn1 API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libtasn1 API documentation.

%prep
%setup -q

# remove it when non-POSIX make warnings are gone
# (after libtasn1 or gtk-doc change)
%{__sed} -i -e '/AM_INIT_AUTOMAKE/s/-Werror//' configure.ac

%build

%configure \
	%{!?with_gtk_doc:--enable-gtk-doc}%{!?with_apidocs:=no} \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{?with_apidocs:--with-html-dir=%{_gtkdocdir}} \
	--with-packager="Unity - Linux" \
	--with-packager-bug-reports="http://unity-linux.org/"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

#%post	devel -p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

#%postun	devel -p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/*.html
%attr(755,root,root) %{_bindir}/asn1*
%attr(755,root,root) %{_libdir}/libtasn1.so.*.*.*
%attr(755,root,root) %{_libdir}/libtasn1.so.6
%{_mandir}/man1/asn1*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtasn1.so
%{_libdir}/libtasn1.la
%{_includedir}/libtasn1.h
%{_libdir}/pkgconfig/libtasn1.pc
%{_infodir}/libtasn1.info*
%{_mandir}/man3/asn1_*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtasn1.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

%changelog
