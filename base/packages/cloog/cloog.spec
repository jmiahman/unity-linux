Name:		cloog	
Version:	0.18.1
Release:	1%{?dist}
Summary:	The Chunky Loop Generator

Group:		System Environment/Libraries		
License:	GPLv2+
URL:		http://www.cloog.org
Source0:	http://gcc.fyxm.net/infrastructure/%{name}-%{version}.tar.gz	

#BuildRequires:	gmp-dev, isl-dev
#Requires:	

%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package devel
Summary:        Development tools for the Chunky Loop Generator
Group:          Development/Libraries

%description devel
The header files and dynamic shared libraries of the Chunky Loop Generator.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \
	--with-sysroot=%{buildroot} \
	--with-isl=system

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} INSTALL="install -D" install
rm -f %{buildroot}/usr/lib/*.la

%files
%{_bindir}/cloog
%{_libdir}/libcloog-isl.so.*

%files devel
%{_includedir}/cloog
%{_libdir}/libcloog-isl.so
%{_libdir}/pkgconfig/cloog-isl.pc
%exclude %{_libdir}/libcloog-isl.a

%changelog
