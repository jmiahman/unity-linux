Summary: Development files for musl libc
Name:	 musl
Version: 1.1.10
Release: 1
Source0: http://www.musl-libc.org/releases/%{name}-%{version}.tar.gz
Source1: __stack_chk_fail_local.c
Source2: libssp_nonshared.a
Source3: ldconfig
Source4: getconf.c
Source5: getent.c
Source6: iconv.c

License: LGPLv2+
Group:	 Development/C
URL:	 http://www.musl-libc.org/
#BuildRequires: zlib-devel

%description
musl is a new standard library to power Linux-based devices.  It is
lightweight, fast, simple, free, and strives to be correct in the sense of
standards-conformance and safety.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
License:	LGPLv2+
Requires:	%{name} = %{version}

%description devel
Development files and headers for %{name}.

%prep
%setup -q

%build

make ARCH=%{_arch} prefix=/usr DESTDIR=%{buildroot} install-headers

%__cc -c %{SOURCE1} -o __stack_chk_fail_local.o
%__ar r libssp_nonshared.a __stack_chk_fail_local.o


%__cc %{SOURCE4} -o %{buildroot}/getconf
%__cc %{SOURCE5} -o %{buildroot}/getent
%__cc %{SOURCE6} -o %{buildroot}/iconv

LDFLAGS="$LDFLAGS -Wl,-soname,libc.musl-%{_arch}.so.1" \
./configure \
        --host=%{_arch}-alpine-linux-musl \
        --prefix=/ \
        --sysconfdir=/etc \
        --mandir=/usr/share/man \
        --infodir=/usr/share/info \
        --localstatedir=/var
make


%__sed 's!/usr/local!/usr/lib!' dist/config.mak > config.mak
make ARCH="%{_arch}"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%__rm -f %{buildroot}/usr/lib/*.la
%__cp libssp_nonshared.a %{buildroot}/usr/lib/
#local LDSO=$(make -f Makefile --eval "$(echo -e 'print-ldso:\n\t@echo $$(basename $(LDSO_PATHNAME))')" print-ldso)
%__mkdir -p %{buildroot}/usr/bin
%__mkdir -p %{buildroot}/lib/

#%__mv -f %{buildroot}/usr/lib/libc.so %{buildroot}/lib/"$LDSO"
%__mv -f %{buildroot}/usr/lib/libc.so %{buildroot}/lib/ld-musl-%{_arch}.so.1

#%__ln_s -f "$LDSO"  %{buildroot}/lib/libc.musl-%{_arch}.so.1
#%__ln_s -f /lib/"$LDSO" %{buildroot}/usr/lib/libc.so
#%__mkdir -p %{buildroot}/usr/bin
#%__ln_s -f /lib/"$LDSO" %{buildroot}/usr/bin/ldd


%__ln_s -f ld-musl-%{_arch}.so.1 %{buildroot}/lib/libc.musl-%{_arch}.so.1
%__ln_s -f /lib/ld-musl-%{_arch}.so.1 %{buildroot}/lib/libc.so
%__mkdir -p %{buildroot}/usr/bin
%__ln_s -f /lib/ld-musl-%{_arch}.so.1 %{buildroot}/usr/bin/ldd


# remove libintl.h, currently we don't want by default any NLS
# and use GNU gettext where needed. the plan is to migrate to
# musl gettext() later on as fully as possible.
%__rm %{buildroot}/usr/include/libintl.h

%__sed -i 's!/usr/lib/musl!/usr!' %{buildroot}/usr/bin/musl-gcc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc INSTALL README WHATSNEW 
/lib/libc.musl-%{_arch}.so.1
/lib/ld-musl-%{_arch}.so.1

%files devel
%{_libdir}/*.o
%{_libdir}/lib*.a
%{_libdir}/musl-gcc.specs
%{_includedir}/*
%{_bindir}/*

%changelog
* Tue Jun 23 2015 JMiahMan <JMiahMan@gmail.com> - 1.1.10-1
- Test Build
