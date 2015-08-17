Summary: Development Libraries and headers for EFI
Name: gnu-efi
Version: 3.0.2
Release: 1%{?dist}
Group: Development/System
License: BSD 
URL: ftp://ftp.hpl.hp.com/pub/linux-ia64
ExclusiveArch: %{ix86} x86_64 ia64
Source: http://downloads.sourceforge.net/project/gnu-efi/gnu-efi-%{version}.tar.bz2

%ifarch x86_64
%global efiarch x86_64
%endif
%ifarch %{ix86}
%global efiarch ia32
%endif

%description
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%package devel
Summary: Development Libraries and headers for EFI
Group: Development/System
Obsoletes: gnu-efi < 3.0.1-1
Requires: gnu-efi

%description devel
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%package utils
Summary: Utilities for EFI systems
Group: Applications/System

%description utils
This package contains utilties for debugging and developing EFI systems.

%prep
%setup -q -n gnu-efi-%{version}

%build
# Package cannot build with %{?_smp_mflags}.
make -j1

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_libdir}

make PREFIX=%{_prefix} LIBDIR=%{_libdir} INSTALLROOT=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%{_libdir}/*

%files devel
%defattr(-,root,root,-)
#%doc README.* ChangeLog
%{_includedir}/efi

#%files utils
#%dir /boot/efi/EFI/%{efidir}/
#%attr(0644,root,root) /boot/efi/EFI/%{efidir}/*.efi

%changelog
