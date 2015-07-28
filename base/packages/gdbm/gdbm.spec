Name:		gdbm
Version:	1.11
Release:	1%{?dist}
Summary:	A GNU set of database routines which use extensible hashing

Group:		System Environment/Libraries
License:	GPLv3+
URL:		http://www.gnu.org/software/gdbm/
Source0:	http://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

Patch0: gdbm-1.10-zeroheaders.patch


BuildRequires: libtool, gettext	
#Requires:	

%description
Gdbm is a GNU database indexing library, including routines which use
extensible hashing.  Gdbm works in a similar way to standard UNIX dbm
routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

If you're a C developer and your programs need access to simple
database routines, you should install gdbm.  You'll also need to
install gdbm-devel.

%package devel
Summary: Development libraries and header files for the gdbm library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Gdbm-devel contains the development libraries and header files for
gdbm, the GNU database system.  These libraries and header files are
necessary if you plan to do development using the gdbm database.

Install gdbm-devel if you are developing C programs which will use the
gdbm database library.  You'll also need to install the gdbm package.


%prep
%setup -q

%patch0 -p1 -b .zeroheaders


%build
./configure \
	--prefix=/usr \
	--enable-libgdbm-compat \
	--disable-largefile \
	--disable-dependency-tracking \
	--enable-fast-install

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la

%files
/usr/bin/gdbm_dump
/usr/bin/gdbm_load
/usr/bin/gdbmtool
/usr/lib/libgdbm.so.4.0.0
/usr/lib/libgdbm_compat.so.4.0.0
/usr/lib/libgdbm.so.4
/usr/lib/libgdbm_compat.so.4

%files devel
%{_libdir}/libgdbm.so
%{_libdir}/libgdbm_compat.so
%{_includedir}/*

%changelog
