Summary: Library for error values used by GnuPG components
Name: libgpg-error
Version: 1.19
Release: 1%{?dist}
URL: ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source0: ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2.sig
Group: System Environment/Libraries
License: LGPLv2+

BuildRequires: gawk, gettext, autoconf, automake, gettext-devel, libtool
BuildRequires: texinfo
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package devel
Summary: Development files for the %{name} package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
#Requires(pre): /sbin/install-info
#Requires(post): /sbin/install-info

%description devel
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future. This package
contains files necessary to develop applications using libgpg-error.

%prep
%setup -q

%build
%configure --disable-static --disable-rpath --disable-languages
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%check
make check

%clean
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
#[ -f %{_infodir}/gpgrt.info.gz ] && \
#    /sbin/install-info %{_infodir}/gpgrt.info.gz %{_infodir}/dir
#exit 0

%preun devel
#if [ $1 = 0 -a -f %{_infodir}/gpgrt.info.gz ]; then
#    /sbin/install-info --delete %{_infodir}/gpgrt.info.gz %{_infodir}/dir
#fi
#exit 0

%files
%defattr(-,root,root)
#%license COPYING COPYING.LIB
#%doc AUTHORS README NEWS ChangeLog
%{_bindir}/gpg-error
%{_libdir}/libgpg-error.so.0*

%files devel
%defattr(-,root,root)
%{_bindir}/gpg-error-config
%{_libdir}/libgpg-error.so
%{_includedir}/gpg-error.h
%{_datadir}/aclocal/gpg-error.m4
#%{_infodir}/gpgrt.info*
#%{_mandir}/man1/gpg-error-config.*

%changelog
