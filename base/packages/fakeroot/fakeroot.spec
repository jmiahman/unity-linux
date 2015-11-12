Summary:	Gives a fake root environment
Name:		fakeroot
Version:	1.20.2
Release:	1%{?dist}
License:	GPL v3+
Group:		Development/Tools
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}.orig.tar.bz2
URL:		http://fakeroot.alioth.debian.org/
BuildRequires:	libacl-devel
BuildRequires:	libtool
Requires:	util-linux

Patch0: busybox-getopt.patch
Patch1: fakeroot-hide-dlsym-errors.patch
Patch2: fakeroot-no64.patch
Patch3: fakeroot-stdint.patch
Patch4: fakeroot-uclibc.patch

%define		_libdir		%{_prefix}/%{_lib}/libfakeroot

%description
fakeroot runs a command in an environment were it appears to have root
privileges for file manipulation. This is useful for allowing users to
create archives (tar, ar, .deb etc.) with files in them with root
permissions/ownership. Without fakeroot one would have to have root
privileges to create the constituent files of the archives with the
correct permissions and ownership, and then pack them up, or one would
have to construct the archives directly, without using the archiver.

fakeroot works by replacing the file manipulation library functions
(chmod(), stat() etc.) by ones that simulate the effect the real
library functions would have had, had the user really been root. These
wrapper functions are in a shared library libfakeroot.so*, which is
loaded through the LD_PRELOAD mechanism of the dynamic loader.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build

# overrides wrong symbol for musl, so hack the config script
sed -e 's/for WRAPPED in __${PRE}x${FUNC} _${PRE}x${FUNC} __${PRE}${FUNC}13 ${PRE}${FUNC}; do/for WRAPPED in ${PRE}${FUNC}; do/' \
		    -i configure

%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfakeroot.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS DEBUG README
%attr(755,root,root) %{_bindir}/faked
%attr(755,root,root) %{_bindir}/fakeroot
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/libfakeroot*.so
%{_mandir}/man1/faked.1*
%{_mandir}/man1/fakeroot.1*

%changelog
