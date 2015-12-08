Name:		libpthread-stubs	
Version:	0.3
Release:	1%{?dist}
Summary:	Pthread functions stubs for platforms missing them

Group:		Development/Libraries
License:	MIT
URL:		http://cgit.freedesktop.org/xcb/pthread-stubs	
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2

%description
The libpthread-stubs package provides weak aliases for pthread functions not provided in libc or otherwise available by default. This is useful for libraries that rely on pthread stubs to use pthreads optionally. 

%prep
%setup -q


%build
%configure
make CFLAGS="$CFLAGS -DHAVE_PTHREAD_EXIT=1"

%install
make -j1 DESTDIR=%{buildroot} install


%files
%{_libdir}/pkgconfig/pthread-stubs.pc

%changelog

