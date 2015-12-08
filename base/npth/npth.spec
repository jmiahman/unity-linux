%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \



Name:		npth	
Version:	1.2
Release:	1%{?dist}
Summary:	The New GNU Portable Threads library

Group:		Development/Libraries		
License:	LGPL-2.1
URL:		ftp://ftp.gnupg.org/gcrypt/npth/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	npth-config.1

#BuildRequires:	
#Requires:	

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--infodir=/usr/share/info \
	--mandir=/usr/share/man \

make %{?_smp_mflags}


%install
make -j1 DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la

mkdir -p %{buildroot}%{_mandir}/man1/
install -pm0644 %{S:1} %{buildroot}%{_mandir}/man1/

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%license COPYING COPYING.LESSER
%{_libdir}/*.so.*

%files devel
#%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_libdir}/*.so
%{_includedir}/*.h
#%{_mandir}/*/*
%{_datadir}/aclocal/*

%changelog
