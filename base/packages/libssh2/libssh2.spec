Name:		libssh2
Version:	1.6.0
Release:	1%{?dist}
Summary:	A library implementing the SSH2 protocol
Group:		System Environment/Libraries
License:	BSD
URL:		http://www.libssh2.org/
Source0:	http://libssh2.org/download/libssh2-%{version}.tar.gz
Patch0:		libssh2-1.4.2-utf8.patch
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/man

BuildRequires:	openssh-server

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package	devel
Summary:	Development files for libssh2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The libssh2-devel package contains libraries and header files for
developing applications that use libssh2.

%package	docs
Summary:	Documentation for libssh2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	docs
The libssh2-docs package contains man pages and examples for
developing applications that use libssh2.

%prep
%setup -q

# Make sure things are UTF-8...
%patch0 -p1

%build
%configure --disable-static --enable-shared
make %{?_smp_mflags}

# Avoid polluting libssh2.pc with linker options (#947813)
sed -i -e 's|[[:space:]]-Wl,[^[:space:]]*||' libssh2.pc

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} \;

# clean things up a bit for packaging
make -C example clean
rm -rf example/.deps
find example/ -type f '(' -name '*.am' -o -name '*.in' ')' -exec rm -v {} \;

# avoid multilib conflict on libssh2-devel
mv -v example example.%{_arch}

%check
echo "Running tests for %{_arch}"
# The SSH test will fail if we don't have /dev/tty, as is the case in some
# versions of mock (#672713)
if [ ! -c /dev/tty ]; then
	echo Skipping SSH test due to missing /dev/tty
	echo "exit 0" > tests/ssh2.sh
fi
# Apparently it fails in the arm buildsystem too
%ifarch %{arm}
echo Skipping SSH test on arm
echo "exit 0" > tests/ssh2.sh
%endif
# mansyntax check fails on PPC* and aarch64 with some strange locale error
make -C tests check

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%if 0%{?_licensedir:1}
%license COPYING
%else
%doc COPYING
%endif
%doc docs/AUTHORS ChangeLog NEWS README RELEASE-NOTES
%{_libdir}/libssh2.so.1
%{_libdir}/libssh2.so.1.*

%files docs
%doc docs/BINDINGS docs/HACKING docs/TODO
%{_mandir}/man3/libssh2_*.3*

%files devel
%doc example.%{_arch}/
%{_includedir}/libssh2.h
%{_includedir}/libssh2_publickey.h
%{_includedir}/libssh2_sftp.h
%{_libdir}/libssh2.so
%{_libdir}/pkgconfig/libssh2.pc

%changelog
