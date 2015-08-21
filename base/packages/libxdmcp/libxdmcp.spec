%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \


Name:		libxdmcp
Version:	1.1.2
Release:	1%{?dist}
Summary:	X Display Manager Control Protocol library

Group:		System Environment/Libraries
License:	MIT
URL:		http://www.x.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2	

BuildRequires:	xproto

%description
The libXdmcp package contains a library implementing the X Display Manager Control Protocol. This is useful for allowing clients to interact with the X Display Manager. 


%prep
%setup -q -n libXdmcp-%{version}


%build

./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc \

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/usr/lib/*.la

%configure
%files
/usr/lib/libXdmcp.so.6
/usr/lib/libXdmcp.so.6.0.0
#/usr/share/doc/libXdmcp
#/usr/share/doc/libXdmcp/AUTHORS
#/usr/share/doc/libXdmcp/COPYING
#/usr/share/doc/libXdmcp/ChangeLog
#/usr/share/doc/libXdmcp/Wraphelp.README.crypto

%changelog
