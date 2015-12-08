Name:		libbsd	
Version:	0.6.0
Release:	1%{?dist}
Summary:	Commonly-used BSD functions not implemented by all libcs

Group:		Development/C
License:	BSD	
URL:		http://libbsd.freedesktop.org/	
Source0:	http://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz

Patch0:		Revert_Force_setproctitle_into_.init_array_section.patch
Patch1:		musl-fix-headers.patch

BuildRequires:	autoconf automake libtool libc-devel linux-headers

%description
commonly-used BSD functions not implemented by all libcs

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--localstatedir=/var \

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/usr/lib/*.la

%files
/usr/lib/libbsd.so.0.6.0
/usr/lib/libbsd.so.0

%changelog

