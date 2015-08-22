
Name:		libsm
Version:	1.2.2
Release:	1%{?dist}
Summary:	X11 Session Management library

Group:		System Environment/Libraries
License:	MIT
URL:		http://www.x.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.bz2	

BuildRequires:	xproto libice-devel e2fsprogs-devel xtrans

%description
X11 Session Management library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n libSM-%{version}


%build

./configure \
	--prefix=/usr \
	--sysconfdir=/etc \

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/usr/lib/*.la

%files
%{_libdir}/libSM.so.*
#/usr/share/doc/libSM/*

%files devel
%{_libdir}/libSM.a
%{_libdir}/pkgconfig/sm.pc
%{_libdir}/libSM.so
%dir %{_includedir}/X11/SM/
%{_includedir}/X11/SM/*.h

%changelog
