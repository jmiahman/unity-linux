Name:		attr	
Version:	2.4.47
Release:	1%{?dist}
Summary:	Utilities for managing filesystem extended attributes

Group:		System Environment/Base
License:	GPLv2+
URL:		http://acl.bestbits.at/
Source0:	http://download-mirror.savannah.gnu.org/releases/attr/attr-2.4.47.src.tar.gz	

Patch:		fix-headers.patch

#BuildRequires: libtool, autoconf, automake, bash, gzip	
#Requires:	

%description
A set of tools for manipulating extended attributes on filesystem
objects, in particular getfattr(1) and setfattr(1).
An attr(1) command is also provided which is largely compatible
with the SGI IRIX tool of the same name.

%package -n libattr
Summary: Dynamic library for extended attribute support
Group: System Environment/Libraries
License: LGPLv2+

%description -n libattr
This package contains the libattr.so dynamic library which contains
the extended attribute system calls and library functions.

%package -n libattr-devel
Summary: Files needed for building programs with libattr
Group: Development/Libraries
License: LGPLv2+
Requires: libattr = %{version}-%{release}

%description -n libattr-devel
This package contains header files and documentation needed to
develop programs which make use of extended attributes.
For Linux programs, the documented system call API is the
recommended interface, but an SGI IRIX compatibility interface
is also provided.

Currently only ext2, ext3 and XFS support extended attributes.
The SGI IRIX compatibility API built above the Linux system calls is
used by programs such as xfsdump(8), xfsrestore(8) and xfs_fsr(8).

You should install libattr-devel if you want to develop programs
which make use of extended attributes.  If you install libattr-devel,
you'll also want to install attr.


%prep
%setup -q
%patch -p1 -b .fix-headers


%build
sed -i -e '/HAVE_ZIPPED_MANPAGES/s:=.*:=false:' \
	include/builddefs.in

unset PLATFORM #184564
export OPTIMIZER=${CFLAGS}
export DEBUG=-DNDEBUG
export INSTALL_USER=root
export INSTALL_GROUP=root
./configure \
	--prefix=/ \
	--exec-prefix=/ \
	--sbindir=/bin \
	--bindir=/usr/bin \
	--libdir=/lib \
	--libexecdir=/usr/lib \
	--enable-lib64=yes \
	--includedir=/usr/include \
	--mandir=/usr/share/man \
	--datadir=/usr/share \
	--disable-gettext

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
make install-dev DESTDIR=$RPM_BUILD_ROOT
make install-lib DESTDIR=$RPM_BUILD_ROOT

# provided by man-pages
rm -r %{buildroot}/usr/share/man/man2 \
	%{buildroot}/lib/libattr.la

%files
%{_bindir}/attr
%{_bindir}/getfattr
%{_bindir}/setfattr

%files -n libattr
/lib/libattr.so.*

%files -n libattr-devel
/lib/libattr.so
%{_includedir}/attr

%changelog
