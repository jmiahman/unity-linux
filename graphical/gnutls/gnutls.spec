#
# Conditional build:
%bcond_with	dane		# libdane (DANE with DNSSEC certificate verification)
%bcond_with	openssl		# libgnutls-openssl compatibility library
%bcond_with	tpm		# TPM support in gnutls
%bcond_with	static_libs	# static libraries
%bcond_with	apidocs		# disable apidocs
#
Summary:	The GNU Transport Layer Security Library
Name:		gnutls
Version:	3.3.18
Release:	1
License:	LGPL v2.1+ (libgnutls), LGPL v3+ (libdane), GPL v3+ (openssl library and tools)
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/gcrypt/gnutls/v3.3/%{name}-%{version}.tar.xz
#Patch0:		%{name}-info.patch
#Patch1:		%{name}-link.patch
URL:		http://www.gnutls.org/
BuildRequires:	gettext
BuildRequires:	gmp-devel
%{?with_apidocs:BuildRequires:  gtk-doc}
BuildRequires:	guile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtasn1-devel
BuildRequires:	libtool
BuildRequires:	nettle-devel
BuildRequires:	p11-kit-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpm-build
BuildRequires:	sed 
BuildRequires:	tar 
BuildRequires:	texinfo
%{?with_tpm:BuildRequires:	trousers-devel >= 0.3.11}
%{?with_dane:BuildRequires:	unbound-devel}
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
%{?with_dane:Requires:	%{name}-dane = %{version}-%{release}}

%description
GnuTLS is a project that aims to develop a library which provides a
secure layer, over a reliable transport layer (ie. TCP/IP). Currently
the gnuTLS library implements the proposed standards by the IETF's TLS
working group.

%package libs
Summary:	GnuTLS shared libraries
Group:		Libraries
Requires:	libtasn1
Requires:	nettle
Requires:	p11-kit
%{?with_tpm:Requires:	trousers-libs >= 0.3.11}

%description libs
GnuTLS shared libraries.

%package devel
Summary:	Header files etc to develop gnutls applications
License:	LGPL v2.1+ (libgnutls), GPL v3+ (openssl library)
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libtasn1-devel
Requires:	nettle-devel
Requires:	p11-kit-devel
%{?with_tpm:Requires:	trousers-devel >= 0.3.11}
Requires:	zlib-devel

%description devel
Header files etc to develop gnutls applications.

%package static
Summary:	Static gnutls library
License:	LGPL v2.1+ (libgnutls), GPL v3+ (openssl library)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnutls library.

%package c++
Summary:	libgnutlsxx - C++ interface to gnutls library
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description c++
libgnutlsxx - C++ interface to gnutls library.

%package c++-devel
Summary:	Header files for libgnutlsxx, a C++ interface to gnutls library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for libgnutlsxx, a C++ interface to gnutls library.

%package c++-static
Summary:	Static version of libgnutlsxx, a C++ interface to gnutls library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static version of libgnutlsxx, a C++ interface to gnutls library.

%package dane
Summary:	DANE security library
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description dane
DANE security library.

%package dane-devel
Summary:	Header file for DANE security library
Group:		Development/Libraries
Requires:	%{name}-dane = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	unbound-devel

%description dane-devel
Header file for DANE security library.

%package dane-static
Summary:	Static DANE security library
Group:		Development/Libraries
Requires:	%{name}-dane-devel = %{version}-%{release}

%description dane-static
Static DANE security library.

%package openssl
Summary:	OpenSSL compatibility library for GnuTLS
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description openssl
OpenSSL compatibility library for GnuTLS.

%package openssl-devel
Summary:	Header file for gnutls-openssl library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-openssl = %{version}-%{release}

%description openssl-devel
Header file for gnutls-openssl library.

%package openssl-static
Summary:	Static gnutls-openssl library
Group:		Development/Libraries
Requires:	%{name}-openssl-devel = %{version}-%{release}

%description openssl-static
Static gnutls-openssl library.

#%package -n guile-gnutls
#Summary:	Guile bindings for GnuTLS
#License:	LGPL v2.1+
#Group:		Development/Languages
#Requires:	%{name}-libs = %{version}-%{release}
#Requires:	guile 

#%description -n guile-gnutls
#Guile bindings for GnuTLS.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%{__rm} po/stamp-po

%build
%configure \
	%{!?with_openssl:--disable-openssl-compatibility} \
	%{!?with_apidocs:--disable-gtk-doc} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-default-trust-store-file=/etc/ssl/ca-bundle.crt \
	%{!?with_tpm:--without-tpm} \
	--disable-openssl-compatibility \
	--disable-rpath \
	--disable-static \
	--disable-guile \
	--disable-valgrind-tests \

# docs build is broken with -jN
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# although libgnutls.la is obsoleted by pkg-config, there is
# .pc file missing for libgnutls-openssl, and it needs libgnutls.la

%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile/2.0/guile-gnutls-*.a
%endif

%{__rm} -f $RPM_BUILD_ROOT%{_infodir}/dir


%clean
rm -rf $RPM_BUILD_ROOT

%post
#[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
#[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	dane -p /sbin/ldconfig
%postun	dane -p /sbin/ldconfig

%post	openssl -p /sbin/ldconfig
%postun	openssl -p /sbin/ldconfig

#%post	-n guile-gnutls -p /sbin/ldconfig
#%postun	-n guile-gnutls -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/gnutls-*
%attr(755,root,root) %{_bindir}/ocsptool
%attr(755,root,root) %{_bindir}/psktool
%attr(755,root,root) %{_bindir}/srptool
%{?with_tpm:%attr(755,root,root) %{_bindir}/tpmtool}
%{_mandir}/man1/certtool.1*
%{_mandir}/man1/gnutls-*.1*
%{_mandir}/man1/ocsptool.1*
%{_mandir}/man1/p11tool.1*
%{_mandir}/man1/psktool.1*
%{_mandir}/man1/srptool.1*
%{_mandir}/man1/tpmtool.1*
%{_infodir}/gnutls.info*
%{_infodir}/gnutls-*.png
%{_infodir}/pkcs11-vision.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls.so.28

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls.so
%{_libdir}/libgnutls.la
%{_includedir}/gnutls
%{?with_dane:%exclude %{_includedir}/gnutls/dane.h}
%exclude %{_includedir}/gnutls/gnutlsxx.h
%{?with_openssl:%exclude %{_includedir}/gnutls/openssl.h}
%{_ilibdir}/pkgconfig/gnutls.pc
%{_mandir}/man3/gnutls_*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgnutls.a
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutlsxx.so.28

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so
%{_libdir}/libgnutlsxx.la
%{_includedir}/gnutls/gnutlsxx.h

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libgnutlsxx.a
%endif

%if %{with dane}
%files dane
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/danetool
%attr(755,root,root) %{_libdir}/libgnutls-dane.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls-dane.so.0
%{_mandir}/man1/danetool.1*

%files dane-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-dane.so
%{_libdir}/libgnutls-dane.la
%{_includedir}/gnutls/dane.h
%{_libdir}/pkgconfig/gnutls-dane.pc

%if %{with static_libs}
%files dane-static
%defattr(644,root,root,755)
%{_libdir}/libgnutls-dane.a
%endif
%endif

%if %{with openssl}
%files openssl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.27

%files openssl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so
%{_libdir}/libgnutls-openssl.la
%{_includedir}/gnutls/openssl.h

%files openssl-static
%defattr(644,root,root,755)
%{_libdir}/libgnutls-openssl.a
%endif

#%files -n guile-gnutls
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/guile/2.0/guile-gnutls-v-2.so*
#%{_datadir}/guile/site/gnutls.scm
#%{_datadir}/guile/site/gnutls
#%{_infodir}/gnutls-guile.info*

%changelog
