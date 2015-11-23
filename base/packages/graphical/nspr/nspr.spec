Summary:	Netscape Portable Runtime (NSPR)
Name:		nspr
Version:	4.10.10
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	cf43d04668ab20f12cd0b5fa24315354

Patch0:		%{name}-fix-getproto.patch
Patch1:		%{name}-pc.patch

URL:		http://www.mozilla.org/projects/nspr/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	sed >= 4.0

%description
Libraries that implement cross-platform runtime services from
Netscape.

%package devel
Summary:	NSPR library header files for development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the NSPR library from Netscape.

%package static
Summary:	Static NSPR library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static NSPR library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd nspr
cp -f /usr/share/automake*/config.sub build/autoconf
autoconf
CFLAGS="$CFLAGS -D_PR_POLL_AVAILABLE -D_PR_HAVE_OFF64_T -D_PR_INET6 -D_PR_HAVE_INET_NTOP -D_PR_HAVE_GETHOSTBYNAME2 -D_PR_HAVE_GETADDRINFO -D_PR_INET6_PROBE" \
../nspr/configure \
	--prefix=/usr \
	--includedir=%{_includedir}/nspr \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-ipv6 \
	--enable-optimize \

make CC="${CC:-gcc}" CXX="${CXX:-g++}"

%install
rm -rf $RPM_BUILD_ROOT

cd nspr
make install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnspr4.so
%attr(755,root,root) %{_libdir}/libplc4.so
%attr(755,root,root) %{_libdir}/libplds4.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nspr-config
%{_includedir}/nspr
%{_aclocaldir}/nspr.m4
%{_libdir}/pkgconfig/mozilla-nspr.pc
%{_libdir}/pkgconfig/nspr.pc

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libnspr4.a
#%{_libdir}/libplc4.a
#%{_libdir}/libplds4.a

%changelog
