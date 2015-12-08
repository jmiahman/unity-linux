%define _target_platform %{_arch}-unity-linux-musl

%global develdocdir %{_docdir}/%{name}-devel-%{version}

Name:           libevent
Version:        2.0.22
Release:        1%{?dist}
Summary:        Abstract asynchronous event notification library

Group:          System Environment/Libraries
License:        BSD
URL:            http://sourceforge.net/projects/levent/        
Source0:        http://downloads.sourceforge.net/levent/%{name}-%{version}-stable.tar.gz

BuildRequires: doxygen openssl-devel

Patch00: libevent-2.0.10-stable-configure.patch
# Disable network tests
Patch01: libevent-nonettests.patch
Patch02: libevent-fix-SSL_new.patch

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files and libraries for developing
with %{name}.

%package doc
Summary: Development documentation for %{name}
Group: Documentation
BuildArch: noarch

%description doc
This package contains the development documentation for %{name}.

%prep
%setup -q -n libevent-%{version}-stable

# 477685 -  libevent-devel multilib conflict
#%patch00 -p1
%patch01 -p1 -b .nonettests
%patch02 -p1

%build
#build
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && rm -f $i && cp -fv \
                 /usr/share/automake-1.15/$(basename $i) $i ; \
done

autoconf
aclocal
automake --add-missing
./configure \
	--build=%_target_platform \
	--host=%_target_platform \
	--prefix=/usr \
	--sysconfdir=/etc \
	--disable-static \

make %{?_smp_mflags} all

# Create the docs
make doxygen

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

mkdir -p $RPM_BUILD_ROOT/%{develdocdir}/html
(cd doxygen/html; \
	install -p -m 644 *.* $RPM_BUILD_ROOT/%{develdocdir}/html)

mkdir -p $RPM_BUILD_ROOT/%{develdocdir}/sample
(cd sample; \
	install -p -m 644 *.c Makefile* $RPM_BUILD_ROOT/%{develdocdir}/sample)

%clean
rm -rf $RPM_BUILD_ROOT

#%check
#make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%doc ChangeLog LICENSE README
%{_libdir}/libevent-*.so.*
%{_libdir}/libevent_core-*.so.*
%{_libdir}/libevent_extra-*.so.*
%{_libdir}/libevent_openssl-*.so.*
%{_libdir}/libevent_pthreads-*.so.*

%files devel
%{_includedir}/event.h
%{_includedir}/evdns.h
%{_includedir}/evhttp.h
%{_includedir}/evrpc.h
%{_includedir}/evutil.h
%dir %{_includedir}/event2
%{_includedir}/event2/*.h
%{_libdir}/libevent.so
%{_libdir}/libevent_core.so
%{_libdir}/libevent_extra.so
%{_libdir}/libevent_openssl.so
%{_libdir}/libevent_pthreads.so
%{_libdir}/pkgconfig/libevent.pc
%{_libdir}/pkgconfig/libevent_openssl.pc
%{_libdir}/pkgconfig/libevent_pthreads.pc
%{_bindir}/event_rpcgen.*

#%files doc
#%{develdocdir}/

%changelog
