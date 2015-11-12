Name:           lua51
Version:        5.1.4
Release:        1%{?dist}
Summary:        Powerful light-weight programming language
Group:          Development/Languages
License:        MIT
URL:            http://www.lua.org/
Source0:        http://www.lua.org/ftp/lua-%{version}.tar.gz
Patch0:         lua-5.1.4-autotoolize.patch
Patch1:         lua-5.1.4-lunatic.patch
BuildRequires:  readline-devel ncurses-devel
Provides:       lua = 5.1

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

%package static
Summary:        Static library for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description static
This package contains the static version of liblua for %{name}.


%prep
%setup -q -n lua-%{version}
%patch0 -p1 -z .autoxxx
%patch1 -p0 -z .lunatic
# fix perms on auto files
chmod u+x autogen.sh config.guess config.sub configure depcomp install-sh missing


%build
%configure --with-readline
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
make %{?_smp_mflags} LIBS="-lm -ldl" luac_LDADD="liblua.la -lm -ldl"
# also remove readline from lua.pc
sed -i 's/-lreadline -lncurses //g' etc/lua.pc


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_libdir}/lua/5.1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lua/5.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYRIGHT HISTORY README doc/*.html doc/*.css doc/*.gif doc/*.png
%{_bindir}/lua*
%{_libdir}/liblua-*.so
%{_mandir}/man1/lua*.1*
%dir %{_libdir}/lua
%dir %{_libdir}/lua/5.1
%dir %{_datadir}/lua
%dir %{_datadir}/lua/5.1


%files devel
%defattr(-,root,root,-)
%{_includedir}/l*.h
%{_includedir}/l*.hpp
%{_libdir}/liblua.so
%{_libdir}/pkgconfig/*.pc

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
