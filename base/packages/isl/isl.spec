%global libmajor 13
%global libversion %{libmajor}.1.1

Name:		isl	
Version:	0.14.1
Release:	1%{?dist}
Summary:	Integer point manipulation library

Group:		System Environment/Libraries
License:	MIT
URL:		http://isl.gforge.inria.fr/
Source0:	http://isl.gforge.inria.fr/isl-%{version}.tar.xz

#BuildRequires: gmp-devel, pkgconfig	
#Requires:	

%description
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints.  Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.  It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

%package devel
Summary: Development for building integer point manipulation library
Group: Development/Libraries

%description devel
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints.  Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.  It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \
	--with-sysroot=%{buildroot}

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} INSTALL="install -D" install
rm -f %{buildroot}/usr/lib/*.la

%files
%{_libdir}/libisl.so.%{libmajor}
%{_libdir}/libisl.so.%{libversion}
%{gdbprettydir}/*

%files devel
%{_includedir}/*
%{_libdir}/libisl.so
%{_libdir}/pkgconfig/isl.pc

%changelog
