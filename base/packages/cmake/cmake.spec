Name:		cmake	
Version:	3.3.1
Release:	1%{?dist}
Summary:	CMake is a cross-platform open-source make system

Group:		Development/Tools
License:	BSD and MIT and zlib
URL:		http://www.cmake.org
Source0:	http://www.cmake.org/files/v3.3/cmake-%{version}%{?rcver}.tar.gz

BuildRequires:	ncurses-devel, curl-devel, expat-devel 
BuildRequires:	zlib-devel, bzip2-devel, libarchive-devel

Requires:	

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
%doc



%changelog

