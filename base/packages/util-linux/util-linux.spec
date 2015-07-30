Name:		util-linux	
Version:	2.26.2
Release:	1%{?dist}
Summary:	A collection of basic system utilities

Group:		System Environment/Base	
License:	GPLv2 and GPLv2+ and LGPLv2+ and BSD with advertising and Public Domain	
URL:		http://en.wikipedia.org/wiki/Util-linux
Source0:	ftp://ftp.kernel.org/pub/linux/utils/util-linux/v2.26/util-linux-%{version}.tar.xz

BuildRequires: zlib-devel, sed, ncurses-devel, tar 
BuildRequires: autoconf, automake, libtool 
BuildRequires: python-devel, linux-headers

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, Util-linux contains the fdisk configuration tool and the login
program.


%package -n blkid
Summary: Block device identification tool.
Group: Development/Libraries
License: LGPLv2+

%description -n blkid
Block device identification tool.


%package -n libblkid
Summary:  Block device identification library from util-linux.
Group: Development/Libraries
License: LGPLv2+
Requires: libfdisk = %{version}-%{release}
Requires: pkgconfig

%description -n libblkid
Block device identification library from util-linux.


%package -n libuuid
Summary: DCE compatible Universally Unique Identifier library.
Group: Development/Libraries
License: LGPLv2+

%description -n libuuid
DCE compatible Universally Unique Identifier library.


%package -n sfdisk
Summary: Partition table manipulator from util-linux.
Group: Development/Libraries
License: LGPLv2+
Requires: pkgconfig

%description -n sfdisk
Partition table manipulator from util-linux.

%package -n cfdisk
Summary: Curses based partition table manipulator from util-linux.
Group: Development/Libraries
License: LGPLv2+
Requires: pkgconfig

%description -n cfdisk
Curses based partition table manipulator from util-linux.


%package -n libmount
Summary: Device mounting library
Group: Development/Libraries
License: LGPLv2+
Requires: libblkid = %{version}-%{release}
Requires: libuuid = %{version}-%{release}

%description -n libmount
This is the device mounting library, part of util-linux.


%package -n libmount-devel
Summary: Device mounting library
Group: Development/Libraries
License: LGPLv2+
Requires: libmount = %{version}-%{release}
Requires: pkgconfig

%description -n libmount-devel
This is the device mounting development library and headers,
part of util-linux.


%package -n libblkid
Summary: Block device ID library
Group: Development/Libraries
License: LGPLv2+
Requires: libuuid = %{version}-%{release}

%description -n libblkid
This is block device identification library, part of util-linux.


%package -n libblkid-devel
Summary: Block device ID library
Group: Development/Libraries
License: LGPLv2+
Requires: libblkid = %{version}-%{release}
Requires: pkgconfig

%description -n libblkid-devel
This is the block device identification development library and headers,
part of util-linux.


%package -n mcookie
Summary: Generate magic cookies for xauth
Group: Development/Libraries
License: LGPLv2+

%description -n mcookie
Mcookie generates a 128-bit random hexadecimal number for use with the X authority system.

%package -n python-libmount
Summary: A wrapper around libmount
Group: Development/Libraries
License: BSD
Requires: libmount = %{version}-%{release}
Requires: pkgconfig

%description -n  python-libmount
A wrapper around libmount, for reading and manipulating filesystem tables

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--enable-raw \
	--disable-uuidd \
	--disable-nls \
	--disable-tls \
	--disable-kill \
	--with-ncurses \
	--disable-login \
	--disable-last \
	--disable-sulogin \
	--disable-su \
	--enable-chsh \

make %{?_smp_mflags}


%install
make -j1 install DESTDIR=%{buildroot}
# use pkg-config
rm -f %{buildroot}/usr/lib/*.la \
	%{buildroot}/usr/lib/python*/site-packages/libmount/*.la

%files

%files -n blkid

%files -n libblkid

%files -n libuuid

%files -n sfdisk

%files -n cfdisk

%files -n libmount
 
%files -n libmount-devel

%files -n libblkid

%files -n libblkid-devel

%files -n mcookie

%files -n python-libmount

%changelog
