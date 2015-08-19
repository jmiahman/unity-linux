#%{!?luaver: %global luaver %(lua5.2 -e "print(string.sub(_VERSION, 5))")}
%define luaver 5.2
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-posix
Version:        33.3.1
Release:        1%{?dist}
Summary:        A POSIX library for Lua
Group:          Development/Libraries
License:        Public Domain
URL:            http://luaforge.net/projects/luaposix/
Source0:        https://github.com/luaposix/luaposix/archive/release-v%{version}.tar.gz

Patch0: 	fix-sched-header.patch

BuildRequires:  lua5.2-devel
BuildRequires:  ncurses-devel
#BuildRequires:	lua-lunit
Requires:       lua5.2

%description
This is a POSIX library for Lua which provides access to many POSIX features
to Lua programs.

%prep
%setup -q -n luaposix-release-v%{version}
%patch0 -p1

%build
LUA=lua%{luaver} LUA_INCLUDE=$(pkg-config lua%{luaver} --cflags) \
./configure --prefix=/usr \
	--libdir=/usr/lib/lua/%{luaver} \
	--datadir=/usr/share/lua/%{luaver} \

make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT luadir=/usr/share/lua/%{luaver} install


%check
make V=1 check


%clean
rm -rf $RPM_BUILD_ROOT


%files
#%doc AUTHORS ChangeLog COPYING NEWS README
#%{_defaultdocdir}/luaposix/
%{lualibdir}/*
%dir %{lualibdir}
%dir %{luapkgdir}
%{luapkgdir}/*.lua
%{luapkgdir}/posix/

%changelog
