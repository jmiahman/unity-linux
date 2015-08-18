Name: libcap
Version: 2.24
Release: 1%{?dist}
Summary: Library for getting and setting POSIX.1e capabilities
#Source: http://mirror.linux.org.au/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.bz2
Source: https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.gz
# http://manned.org/getpcaps/299a4949/src:

URL: https://sites.google.com/site/fullycapable/
License: GPLv2
Group: System Environment/Libraries
BuildRequires: libattr-devel 
#BuildRequires: pam-devel

%description
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

%package devel
Summary: Development files for libcap
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files (Headers, libraries for static linking, etc) for libcap.

libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

Install libcap-devel if you want to develop or compile applications using
libcap.

%prep
%setup -q

%build
# libcap can not be build with _smp_mflags:
make prefix=%{_prefix} lib=%{_lib} LIBDIR=%{_libdir} SBINDIR=%{_sbindir} \
     INCDIR=%{_includedir} MANDIR=%{_mandir}

%install
make install RAISE_SETFCAP=no \
             DESTDIR=%{buildroot} \
             LIBDIR=%{buildroot}/%{_libdir} \
             SBINDIR=%{buildroot}/%{_sbindir} \
             INCDIR=%{buildroot}/%{_includedir} \
             MANDIR=%{buildroot}/%{_mandir}/ \
             PKGCONFIGDIR=%{buildroot}/%{_libdir}/pkgconfig/
mkdir -p %{buildroot}/%{_mandir}/man{2,3,8}
mv -f doc/*.3 %{buildroot}/%{_mandir}/man3/
#cp -f %{SOURCE1} %{buildroot}/%{_mandir}/man8/

# remove static lib
rm -f %{buildroot}/%{_libdir}/libcap.a

chmod +x %{buildroot}/%{_libdir}/*.so.*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/%{_libdir}/*.so.*
%{_sbindir}/*
#%{_mandir}/man1/*
#%{_mandir}/man8/*
#/%{_libdir}/security/pam_cap.so
#%doc doc/capability.notes
#%{!?_licensedir:%global license %%doc}
#%license License

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
/%{_libdir}/*.so
#%{_mandir}/man3/*
%{_libdir}/pkgconfig/libcap.pc

%clean
rm -rf %{buildroot}

%changelog
