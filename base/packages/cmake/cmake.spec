Name:		cmake	
Version:	3.3.1
Release:	1%{?dist}
Summary:	CMake is a cross-platform open-source make system

Group:		Development/Tools
License:	BSD and MIT and zlib
URL:		http://www.cmake.org
Source0:	http://www.cmake.org/files/v3.3/cmake-%{version}.tar.gz

BuildRequires:	ncurses-devel, curl-devel, expat-devel 
BuildRequires:	zlib-devel, bzip2-devel, libarchive-devel

#Requires:	

%description
CMake is used to control the software compilation process using simple 
platform and compiler independent configuration files. CMake generates 
native makefiles and workspaces that can be used in the compiler 
environment of your choice. CMake is quite sophisticated: it is possible 
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.

%prep
%setup -q


%build
./bootstrap --prefix=/usr \
	--mandir=/share/man \
	--datadir=/share/%{name} \
	--docdir=/share/doc/%{name} \
	--system-libs \
	--no-system-jsoncpp \

make %{?_smp_mflags}


%install
%make_install


%files
/usr/bin/*
/usr/share/aclocal/cmake.m4
%dir /usr/share/cmake/
%dir /usr/share/cmake/Templates/
/usr/share/cmake/Templates/*
%dir /usr/share/cmake/editors/
%dir /usr/share/cmake/editors/emacs/
%dir /usr/share/cmake/editors/vim/
/usr/share/cmake/editors/emacs/cmake-mode.el
/usr/share/cmake/editors/vim/*.vim
%dir /usr/share/cmake/include/
/usr/share/cmake/include/*.h
%dir /usr/share/cmake/Help/
%dir /usr/share/cmake/Help/variable/
/usr/share/cmake/Help/variable/*.rst
%dir /usr/share/cmake/Help/prop_gbl/
/usr/share/cmake/Help/prop_gbl/
%dir /usr/share/cmake/Help/prop_inst/
/usr/share/cmake/Help/prop_inst/
%dir /usr/share/cmake/Help/prop_test/
/usr/share/cmake/Help/prop_test/
%dir /usr/share/cmake/Help/policy/
/usr/share/cmake/Help/policy/
%dir /usr/share/cmake/Help/prop_tgt/
/usr/share/cmake/Help/prop_tgt/
%dir /usr/share/cmake/Help/manual/
/usr/share/cmake/Help/manual/
/usr/share/cmake/Help/index.rst
%dir /usr/share/cmake/Help/release/
/usr/share/cmake/Help/release/
%dir /usr/share/cmake/Help/prop_dir/
/usr/share/cmake/Help/prop_dir/
%dir /usr/share/cmake/Help/include/
/usr/share/cmake/Help/include/
%dir /usr/share/cmake/Help/command/
/usr/share/cmake/Help/command/
%dir /usr/share/cmake/Help/generator/
/usr/share/cmake/Help/generator/
%dir /usr/share/cmake/Help/prop_cache/
/usr/share/cmake/Help/prop_cache/
%dir /usr/share/cmake/Help/prop_sf/
/usr/share/cmake/Help/prop_sf/
%dir /usr/share/cmake/Help/module/
/usr/share/cmake/Help/module/
%dir /usr/share/cmake/Modules/
/usr/share/cmake/Modules/
%dir /usr/share/cmake/completions/
/usr/share/cmake/completions/

%changelog

