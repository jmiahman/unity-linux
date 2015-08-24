
Name:		libice
Version:	1.0.9
Release:	1%{?dist}
Summary:	X11 Inter-Client Exchange library

Group:		System Environment/Libraries
License:	MIT
URL:		http://www.x.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libICE-%{version}.tar.bz2	

BuildRequires:	xproto xtrans

%description
X11 Inter-Client Exchange library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n libICE-%{version}


%build

./configure \
	--prefix=/usr \
	--sysconfdir=/etc \

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/usr/lib/*.la

%files
%{_libdir}/libICE.so.*
#/usr/share/doc/libICE/*

%files devel
%{_libdir}/libICE.a
%{_libdir}/pkgconfig/ice.pc
%{_libdir}/libICE.so
%dir %{_includedir}/X11/ICE/
%{_includedir}/X11/ICE/*.h

%changelog
