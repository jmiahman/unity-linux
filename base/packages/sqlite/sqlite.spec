%define realver 3081100
%define rpmver 3.8.11

Name:		sqlite	
Version:	%{rpmver}
Release:	1%{?dist}
Summary:	Library that implements an embeddable SQL database engine

Group:		Applications/Databases
License:	Public Domain
URL:		http://www.sqlite.org/
Source0:	https://www.sqlite.org/2015/sqlite-src-3081100.zip
Source1:	license.txt

BuildRequires:	ncurses-devel, readline-devel, musl-devel
#Requires:	

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

%package devel
Summary: Development tools for the sqlite3 embeddable SQL database engine
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files and development documentation 
for %{name}. If you like to develop programs using %{name}, you will need 
to install %{name}-devel.

%package doc
Summary: Documentation for sqlite
Group: Documentation
BuildArch: noarch

%description doc
This package contains most of the static HTML files that comprise the
www.sqlite.org website, including all of the SQL Syntax and the 
C/C++ interface specs and other miscellaneous documentation.

%package -n lemon
Summary: A parser generator
Group: Development/Tools

%description -n lemon
Lemon is an LALR(1) parser generator for C or C++. It does the same
job as bison and yacc. But lemon is not another bison or yacc
clone. It uses a different grammar syntax which is designed to reduce
the number of coding errors. Lemon also uses a more sophisticated
parsing engine that is faster than yacc and bison and which is both
reentrant and thread-safe. Furthermore, Lemon implements features
that can be used to eliminate resource leaks, making is suitable for
use in long-running programs such as graphical user interfaces or
embedded controllers.

%prep
%setup -q -a0 -n %{name}-src-%{realver}

%build
export LTLINK_EXTRAS="-ldl"
export CFLAGS="$CFLAGS -DSQLITE_ENABLE_FTS3=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_ENABLE_FTS3_PARENTHESIS -DSQLITE_SECURE_DELETE -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_ENABLE_RTREE=1 -DSQLITE_USE_URI -Iext/fts3"
./configure \
	--prefix=/usr \
	--enable-threadsafe \
	--disable-static \
	--enable-readline \
	--enable-dynamic-extensions

# rpath removal
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make libsqlite3.la
make -j1

%install
make -j1 DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la
install -Dm0644 sqlite3.1 %{buildroot}/usr/share/man/man1/sqlite3.1
install -Dm644 %{SOURCE1} %{buildroot}/usr/share/licenses/%{name}/license.txt

%files
%doc



%changelog
