%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \


Name:		xproto
Version:	7.0.28
Release:	1%{?dist}
Summary:	X11 core wire protocol and auxiliary headers

Group:		Development/System
License:	MIT	
URL:		http://www.x.org/
Source0:	http://xorg.freedesktop.org/releases/individual/proto/%{name}-%{version}.tar.bz2

%description
Header files and libraries needed to communicate directly with X server and
extensions, including the XML-XCB extension, a full replacement for the original
protocol.

%prep
%setup -q


%build
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

%files
/usr/lib/pkgconfig/xproto.pc
#/usr/share/licenses/xproto/COPYING
#/usr/share/doc/xproto/*.xml
%dir /usr/include/X11/
/usr/include/X11/*.h

%changelog

