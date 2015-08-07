Name:		acl
Version:	2.2.52
Release:	1%{?dist}
Summary:	Access control list utilities	

Group:		System Environment/Base
License:	GPLv2+
URL:		http://acl.bestbits.at/
Source0:	http://download-mirror.savannah.gnu.org/releases/acl/acl-2.2.52.src.tar.gz	

BuildRequires: gawk, gettext, libattr-devel, libtool
Requires: libacl

%description
This package contains the getfacl and setfacl utilities needed for
manipulating access control lists.

%package -n libacl
Summary: Dynamic library for access control list support
License: LGPLv2+
Group: System Environment/Libraries

%description -n libacl
This package contains the libacl.so dynamic library which contains
the POSIX 1003.1e draft standard 17 functions for manipulating access
control lists.

%package -n libacl-devel
Summary: Files needed for building programs with libacl
License: LGPLv2+
Group: Development/Libraries
Requires: libacl = %{version}-%{release}, libattr-devel

%description -n libacl-devel
This package contains header files and documentation needed to develop
programs which make use of the access control list programming interface
defined in POSIX 1003.1e draft standard 17.

%prep
%setup -q


%build
sed -i -e '/^as_dummy=/s:=":="$PATH$PATH_SEPARATOR:' \
		configure # hack PATH with AC_PATH_PROG

sed -i -e "/^PKG_DOC_DIR/s:@pkg_name@:%{name}:" \
		-e '/HAVE_ZIPPED_MANPAGES/s:=.*:=false:' \
		include/builddefs.in \


unset PLATFORM
export OPTIMIZER=${CFLAGS}
export DEBUG=-DNDEBUG
CONFIG_SHELL=/bin/sh ./configure \
	--prefix=/usr \
	--libdir=/lib \
	--libexecdir=/usr/lib \
	--disable-gettext

make %{?_smp_mflags}


%install
make DIST_ROOT=%{buildroot} install install-lib install-dev
rm %{buildroot}/usr/lib/*.la %{buildroot}/lib/*.la %{buildroot}/lib/*.a \

chown -R root:root %{buildroot}/*


%files
%{_bindir}/chacl
%{_bindir}/getfacl
%{_bindir}/setfacl

%files -n libacl
/lib/libacl.so.*

%files -n libacl-devel
/lib/libacl.so
%{_includedir}/acl
%{_includedir}/sys/acl.h

%changelog
