Name:		pciutils
Version:	3.4.0
Release:	1%{?dist}
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
#Source1:        multilibconfigh

#change pci.ids directory to hwdata, fedora/rhel specific
Patch1:		pciutils-2.2.1-idpath.patch

#add support for directory with another pci.ids, rejected by upstream, rhbz#195327
Patch2:		pciutils-dir-d.patch
Patch3:		pciutils-fix-linking-pci-malloc-Makefile.patch
Patch4:		pciutils-pread.patch

License:	GPLv2+
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.shtml
ExclusiveOS:	Linux
Requires:	hwdata
Requires:	wget
Requires:	%{name}-libs = %{version}-%{release}
BuildRequires:	sed kmod-devel
Summary: PCI bus related utilities
Group: Applications/System

%description
The pciutils package contains various utilities for inspecting and
setting devices connected to the PCI bus. The utilities provided
require kernel version 2.1.82 or newer (which support the
/proc/bus/pci interface).

%package devel
Summary: Linux PCI development library
Group: Development/Libraries
Requires: zlib-devel pkgconfig %{name} = %{version}-%{release}

%description devel
This package contains a library for inspecting and setting
devices connected to the PCI bus.

%package libs
Summary: Linux PCI library
Group: System Environment/Libraries

%description libs
This package contains a library for inspecting and setting
devices connected to the PCI bus.

%package docs
Summary: Documentation for the Linux PCI library
Group: System Environment/Libraries

%description docs
This package contains Documentation for the
Linux PCI library

#%package devel-static
#Summary: Linux PCI static library
#Group: System Environment/Libraries
#Requires: %{name}-devel = %{version}-%{release}

#%description devel-static
#This package contains a static library for inspecting and setting
#devices connected to the PCI bus.

%prep
%setup -q -n pciutils-%{version}
%patch1 -p1 -b .idpath
%patch2 -p1 -b .dird
%patch3 -p1 -b .link
%patch4 -p1 -b .pread

sed -i -e 's|^SRC=.*|SRC="http://pciids.sourceforge.net/pci.ids"|' update-pciids.sh
sed -i -e "106s/^/\#/" Makefile

%build
	make ZLIB=no \
		SHARED=yes \
		PREFIX=/usr \
		SHAREDIR=%{_datadir} \
		MANDIR=/usr/share/man \
		all
make clean

	make PREFIX=/usr \
		SHARED=yes \
		SHAREDIR=%{_datadir} \
		MANDIR=/usr/share/man \
		install

#fix lib vs. lib64 in libpci.pc (static Makefile is used)
#sed -i "s|^libdir=.*$|libdir=/%{_lib}|" lib/libpci.pc


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/sbin 
install -d $RPM_BUILD_ROOT/%{_sbindir}
install -d $RPM_BUILD_ROOT/%{_lib}
install -d $RPM_BUILD_ROOT/%{_mandir}/man8
install -d $RPM_BUILD_ROOT/%{_libdir}
install -d $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
install -d $RPM_BUILD_ROOT/%{_includedir}/pci

install -p lspci setpci $RPM_BUILD_ROOT/sbin
install -p update-pciids $RPM_BUILD_ROOT/%{_sbindir}
install -p -m 644 lspci.8 setpci.8 update-pciids.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p lib/libpci.so.* $RPM_BUILD_ROOT/%{_lib}/
ln -s ../../%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/*.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpci.so

#mv lib/libpci.a.toinstall lib/libpci.a
#install -p -m 644 lib/libpci.a $RPM_BUILD_ROOT%{_libdir}
/sbin/ldconfig -N $RPM_BUILD_ROOT/%{_lib}
install -p lib/pci.h $RPM_BUILD_ROOT%{_includedir}/pci
install -p lib/header.h $RPM_BUILD_ROOT%{_includedir}/pci
#install -p %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/pci/config.h
install -p lib/config.h $RPM_BUILD_ROOT%{_includedir}/pci/config.%{_lib}.h
install -p lib/types.h $RPM_BUILD_ROOT%{_includedir}/pci
install -p lib/libpci.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/sbin/lspci
/sbin/setpci
%{_sbindir}/update-pciids

%files libs
%doc COPYING
%defattr(-,root,root,-)
/%{_lib}/libpci.so.*

#%files devel-static
#%defattr(-,root,root,-)
#%{_libdir}/libpci.a

%files devel
%defattr(0644, root, root, 0755)
%{_libdir}/pkgconfig/libpci.pc
%{_libdir}/libpci.so
%{_includedir}/pci

%files docs
%defattr(0644, root, root, 0755)
%doc README ChangeLog pciutils.lsm COPYING
%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
