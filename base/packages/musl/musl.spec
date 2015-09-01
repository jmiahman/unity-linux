%define _target_platform %{_arch}-unity-linux-musl

Summary: Development files for musl libc
Name:	 musl
Version: 1.1.11
Release: 1
Source0: http://www.musl-libc.org/releases/%{name}-%{version}.tar.gz
Source1: __stack_chk_fail_local.c
Source2: libssp_nonshared.a
Source3: ldconfig
Source4: getconf.c
Source5: getent.c
Source6: iconv.c

Patch0:  musl-1.1.10-add-qsort_r.patch

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
Requires:	%{name}-utils = %{version}

%description devel
Development files and headers for %{name}.

%package utils
Summary:        Utilities files for %{name}
Group:          Development/C
License:        LGPLv2+
Requires:       %{name} = %{version}

%description utils
Utilities for the %{name} c library (libc) implementation.

%prep
%setup -q
%patch0 -p1

%build

make ARCH=%{_arch} prefix=/usr DESTDIR=%{buildroot} install-headers

/usr/bin/%{_target_platform}-gcc $CPPFLAGS $CFLAGS -c %{SOURCE1} -o __stack_chk_fail_local.o
%__ar r libssp_nonshared.a __stack_chk_fail_local.o

LDFLAGS='-Wl,-soname,libc.musl-%{_arch}.so.1' \
ARCH=%{_arch} \
./configure \
        --host=%{_target_platform} \
        --prefix=/usr \
        --sysconfdir=/etc \
        --mandir=/usr/share/man \
        --infodir=/usr/share/info \
        --localstatedir=/var

make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install

%__mkdir -p %{buildroot}/usr/lib/
%__cp %{SOURCE2} %{buildroot}/usr/lib/
local LDSO=$(make -f Makefile --eval "$(echo -e 'print-ldso:\n\t@echo $$(basename $(LDSO_PATHNAME))')" print-ldso)
%__mkdir -p %{buildroot}/usr/bin
%__mkdir -p %{buildroot}/lib/

%__mv -f %{buildroot}/usr/lib/libc.so %{buildroot}/lib/ld-musl-%{_arch}.so.1
%__ln_s -f ld-musl-%{_arch}.so.1 %{buildroot}/lib/libc.musl-%{_arch}.so.1
%__ln_s -f /lib/ld-musl-%{_arch}.so.1 %{buildroot}/usr/lib/libc.so
%__mkdir -p %{buildroot}/usr/bin
%__ln_s -f /lib/ld-musl-%{_arch}.so.1 %{buildroot}/usr/bin/ldd

# remove libintl.h, currently we don't want by default any NLS
# and use GNU gettext where needed. the plan is to migrate to
# musl gettext() later on as fully as possible.
%__rm %{buildroot}/usr/include/libintl.h

#%__sed -i 's!/usr/lib/musl!/usr!' %{buildroot}/usr/bin/musl-gcc

/usr/bin/%{_target_platform}-gcc $CPPFLAGS $CFLAGS %{SOURCE4} -o getconf
/usr/bin/%{_target_platform}-gcc $CPPFLAGS $CFLAGS %{SOURCE5} -o getent
/usr/bin/%{_target_platform}-gcc $CPPFLAGS $CFLAGS %{SOURCE6} -o iconv

#Utils
	mkdir -p %{buildroot}/usr/bin 
	mkdir -p %{buildroot}/sbin
	install -D \
		getent \
		getconf \
		iconv \
		%{buildroot}/usr/bin/

	install -D -m755 %{SOURCE3} %{buildroot}/sbin/ldconfig

#Compat (Different Package Maybe?)

%define _ld ld-linux-x86-64.so.2
	mkdir -p %{buildroot}/lib
	ln -sf /lib/libc.musl-%{_arch}.so.1 %{buildroot}/lib/%{_ld}

	for i in libc.so.6 libm.so.6 libpthread.so.0 librt.so.1 libutil.so.1; do
		ln -sf /lib/libc.musl-%{_arch}.so.1 %{buildroot}/lib/$i
	done



%clean
rm -rf $RPM_BUILD_ROOT

%files
#%doc INSTALL README WHATSNEW 
/%{_lib}/*-%{_arch}.so.*
/lib/*

%files devel
%{_libdir}/
%{_includedir}/*

%files utils
/sbin/*
%{_bindir}/*

%changelog
* Tue Jun 23 2015 JMiahMan <JMiahMan@gmail.com> - 1.1.10-1
- Test Build
