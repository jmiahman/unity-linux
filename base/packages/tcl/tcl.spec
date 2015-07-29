%define majorver 8.6
%define	vers %{majorver}.4

Name:		tcl	
Version:	%{vers}	
Release:	1%{?dist}
Summary:	Tool Command Language, pronounced tickle

Group:		Development/Languages
License:	TCL
URL:		http://tcl.sourceforge.net/
Source0:	ftp://ftp.tcl.tk/pub/tcl/tcl8_6/tcl-core8.6.4-src.tar.gz	
Patch0:		tcl-stat64.patch

BuildRequires:	autoconf, zlib-devel
#Requires:	

%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

%package devel
Summary: Tcl scripting language development environment
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description devel
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

The package contains the development files and man pages for tcl.

%prep
%setup -q -n %{name}%{version}

%patch0 -p1 -b .tcl-stat64

%build
unix/configure \
	--prefix=/usr \
	--mandir=/usr/share/man \
	%ifarch x86_64
	--enable-64bit
	%else
	--disable-64bit
	%endif

make %{?_smp_mflags}


%install

export LD_LIBRARY_PATH=%{_builddir}
make -j1 INSTALL_ROOT=%{buildroot} install install-private-headers

ln -sf tclsh${_majorver} %{buildroot}/usr/bin/tclsh
install -Dm644 license.terms %{buildroot}/usr/share/licenses/%{name}/LICENSE

# remove buildroot traces
find %{buildroot} -name '*Config.sh' -exec sed -i 's%${srcdir}%/usr/src%g' {} \; 

%files
%{_bindir}/tclsh*
%exclude %{_libdir}/%{name}%{majorver}/tclAppInit.c
%{_libdir}/%{name}8
%{_libdir}/%{name}%{majorver}
%{_libdir}/lib%{name}%{majorver}.so


%files devel
%{_includedir}/*
%{_libdir}/lib%{name}stub%{majorver}.a
%{_libdir}/lib%{name}*.so
%{_libdir}/%{name}Config.sh
%{_libdir}/%{name}ooConfig.sh
%{_libdir}/pkgconfig/tcl.pc
%{_libdir}/%{name}%{majorver}/tclAppInit.c

%changelog
