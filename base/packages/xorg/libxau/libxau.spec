%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \

Name:		libxau	
Version:	1.0.8
Release:	1%{?dist}
Summary:	Sample Authorization Protocol for X

Group:		System Environment/Libraries
License:	MIT
URL:		http://www.x.org
Source0:	ftp://ftp.x.org/pub/individual/lib/libXau-%{version}.tar.bz2

BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig
BuildRequires: xproto

%description
This is a very simple mechanism for providing individual access to an X Window
System display.It uses existing core protocol and library hooks for specifying
authorization data in the connection setup block to restrict use of the display
to only those clients that show that they know a server-specific key 
called a "magic cookie".

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: xproto
Requires: pkgconfig
BuildRequires: xproto

%description devel
X.Org X11 libXau development package

%prep
%setup -q -n libXau-%{version}


%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc \

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
#%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXau.so.6
%{_libdir}/libXau.so.6.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_libdir}/pkgconfig/xau.pc
#%{_mandir}/man3/*.3*

%changelog
