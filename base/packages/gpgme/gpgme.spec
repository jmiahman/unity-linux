
# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    gpgme
Summary: GnuPG Made Easy - high level crypto API
Version: 1.4.3
Release: 6%{?dist}

License: LGPLv2+
URL:     http://www.gnupg.org/related_software/gpgme/
Source0: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig
Source2: gpgme-multilib.h

Patch1: gpgme-1.3.2-config_extras.patch

# gpgsm t-verify check/test hangs if using gnupg2 < 2.0.22
# see http://bugs.g10code.com/gnupg/issue1493
Patch2: gpgme-1.4.3-no_gpgsm_t-verify.patch

# add -D_FILE_OFFSET_BITS... to gpgme-config, upstreamable
Patch3:  gpgme-1.3.2-largefile.patch

Patch4: gpgme-1.3.2-bufferoverflow.patch

BuildRequires: gawk
# see patch2 above, else we only need 2.0.4
BuildRequires: gnupg2 >= 2.0.22
BuildRequires: gnupg2-smime
BuildRequires: libgpg-error-devel >= 1.8
BuildRequires: pth-devel
BuildRequires: libassuan-devel >= 2.0.2

%define _with_gpg --with-gpg=%{_bindir}/gpg2
Requires: gnupg2

# On the following architectures workaround multiarch conflict of -devel packages:
%define multilib_arches %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:  Development headers and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libgpg-error-devel%{?_isa}
# http://bugzilla.redhat.com/676954
# TODO: see if -lassuan can be added to config_extras patch too -- Rex
#Requires: libassuan2-devel
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%description devel
%{summary}


%prep
%setup -q

%patch1 -p1 -b .config_extras
#patch2 -p1 -b .no_gpgsm_t-verify
%patch3 -p1 -b .largefile
%patch4 -p1 -b .overflow

## HACK ALERT
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpgme-config.in


%build
%configure \
  --disable-static \
  --without-g13 \
  %{?_with_gpg}

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# unpackaged files
rm -fv $RPM_BUILD_ROOT%{_infodir}/dir
rm -fv $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -rfv $RPM_BUILD_ROOT%{_datadir}/common-lisp/source/gpgme/

# Hack to resolve multiarch conflict (#341351)
%ifarch %{multilib_arches}
mv $RPM_BUILD_ROOT%{_bindir}/gpgme-config{,.%{_target_cpu}}
cat > gpgme-config-multilib.sh <<__END__
#!/bin/sh
exec %{_bindir}/gpgme-config.\$(arch) \$@
__END__
install -D -p gpgme-config-multilib.sh $RPM_BUILD_ROOT%{_bindir}/gpgme-config
mv $RPM_BUILD_ROOT%{_includedir}/gpgme.h \
   $RPM_BUILD_ROOT%{_includedir}/gpgme-%{__isa_bits}.h
install -m644 -p -D %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/gpgme.h
%endif


%check 
make check


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING*
%doc AUTHORS ChangeLog NEWS README* THANKS TODO VERSION
%{_libdir}/libgpgme.so.11*
%{_libdir}/libgpgme-pthread.so.11*

%post devel
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%preun devel
if [ $1 -eq 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
fi

%files devel
%{_bindir}/gpgme-config
%ifarch %{multilib_arches}
%{_bindir}/gpgme-config.%{_target_cpu}
%{_includedir}/gpgme-%{__isa_bits}.h
%endif
%{_includedir}/gpgme.h
%{_libdir}/libgpgme*.so
%{_datadir}/aclocal/gpgme.m4
%{_infodir}/gpgme.info*


%changelog
