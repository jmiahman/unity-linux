%define _target_platform %{_arch}-unity-linux-musl
%define _luaver 5.2

Name:		lua%{_luaver}	
Version:	5.2.4
Release:	1%{?dist}
Summary:	Powerful light-weight programming language	

Group:		Development/Languages
License:	MIT
URL:		http://www.lua.org/
Source0:	http://www.lua.org/ftp/lua-%{version}.tar.gz

Patch0:		lua-5.2-make.patch
Patch1:		lua-5.2-module_paths.patch

BuildRequires:	libtool, autoconf, automake
#Requires:	

%description
Lua is a powerful light-weight programming language designed for
extending applications. Lua is also frequently used as a
general-purpose, stand-alone language. Lua is free software.
Lua combines simple procedural syntax with powerful data description
constructs based on associative arrays and extensible semantics. Lua
is dynamically typed, interpreted from bytecodes, and has automatic
memory management with garbage collection, making it ideal for
configuration, scripting, and rapid prototyping.

%package devel
Summary:        Development files for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains development files for %{name}.


%prep
%setup -q -n lua-%{version}

%patch0 -p1
%patch1 -p1

%build
# disable readline
sed -i -e '/#define LUA_USE_READLINE/d' src/luaconf.h

# we use libtool
cat >configure.ac <<EOF
top_buildir=.

AC_INIT(src/luaconf.h)
AC_PROG_LIBTOOL
AC_OUTPUT()
EOF

libtoolize --force --install && aclocal && autoconf

./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	
cd src
make V=%{version} \
	CFLAGS=" -DLUA_USE_LINUX -DLUA_COMPAT_ALL" \
	SYSLDFLAGS=$LDFLAGS \
	RPATH="/usr/lib" \
	LIB_LIBS="-lpthread -lm -ldl" \
	unity_all

%install
rm -rf %{buildroot}

make V=%{version} \
	INSTALL_TOP=%{buildroot}/usr \
	INSTALL_INC=%{buildroot}/usr/include/%{name} \
	INSTALL_LIB=%{buildroot}/usr/lib/%{name} \
	unity_install 

rm %{buildroot}/usr/lib/%{name}/*.la

for i in %{buildroot}/usr/bin/* ; do
	mv $i ${i}%{_luaver}
done


for i in %{buildroot}/usr/lib/%{name}/*.so.*; do
	ln -s %{name}/${i##*/} %{buildroot}/usr/lib/${i##*/}
done


install -D -m 644 doc/lua.1 %{buildroot}/usr/share/man/man1/lua%{_luaver}.1 \
	&& install -D -m 644 doc/luac.1 \
		%{buildroot}/usr/share/man/man1/luac%{_luaver}.1 \

install -d %{buildroot}/usr/lib/pkgconfig

cat > %{buildroot}/usr/lib/pkgconfig/lua%{_luaver}.pc <<EOF
# lua.pc -- pkg-config data for Lua

# vars from install Makefile

# grep '^V=' ../Makefile
V= %{_luaver}
# grep '^R=' ../Makefile
R= %{version}

# grep '^INSTALL_.*=' ../Makefile | sed 's/INSTALL_TOP/prefix/'
prefix= /usr
INSTALL_BIN= \${prefix}/bin
INSTALL_INC= \${prefix}/include
INSTALL_LIB= \${prefix}/lib
INSTALL_MAN= \${prefix}/man/man1
INSTALL_LMOD= \${prefix}/share/lua/\${V}
INSTALL_CMOD= \${prefix}/lib/lua/\${V}

# canonical vars
exec_prefix=\${prefix}
libdir=\${exec_prefix}/lib/%{name}
includedir=\${prefix}/include/%{name}

Name: Lua
Description: An Extensible Extension Language
Version: \${R}
Requires:
Libs: -L\${libdir} -llua -lm
Cflags: -I\${includedir}

# (end of lua%{_luaver}.pc)
EOF

#We need to make and own these folders as lua proper
mkdir -p %{buildroot}/usr/lib/lua
mkdir -p %{buildroot}/usr/share/lua

%files
/usr/bin/luac5.2
/usr/bin/lua5.2
%dir /usr/lib/lua5.2
%dir /usr/lib/lua
%dir /usr/share/lua
/usr/lib/liblua-5.2.so.0.0.0
/usr/lib/liblua-5.2.so.0
/usr/lib/lua5.2/liblua-5.2.so.0.0.0
/usr/lib/lua5.2/liblua-5.2.so.0

%files devel
/usr/lib/pkgconfig/lua5.2.pc
/usr/lib/lua5.2/liblua.a
/usr/lib/lua5.2/liblua.so
%dir /usr/include/lua5.2/ 
/usr/include/lua5.2/luaconf.h
/usr/include/lua5.2/lualib.h
/usr/include/lua5.2/lua.hpp
/usr/include/lua5.2/lua.h
/usr/include/lua5.2/lauxlib.h

%changelog

