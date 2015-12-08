
Name:		libatomic_ops
Version:	7.4.2
Release:	1%{?dist}
Summary:	Provides semi-portable access to hardware provided atomic memory operations

Group:		Development/Libraries		
License:	GPL
URL:		https://github.com/ivmai/libatomic_ops
Source0:	https://github.com/ivmai/libatomic_ops/archive/libatomic_ops-7_4_2.tar.gz

BuildRequires:	automake libtool autoconf
#Requires:	

%description
This package provides semi-portable access to hardware-provided 
atomic memory update operations on a number architectures. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n libatomic_ops-libatomic_ops-7_4_2

%build
./autogen.sh
./configure \
	--prefix=/usr \
	--disable-static \

make %{?_smp_mflags}


%install
make -j1 DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la
install -Dm644 doc/LICENSING.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%license COPYING COPYING.LESSER
%dir %{_datadir}/libatomic_ops/
%{_datadir}/libatomic_ops/*

%files devel
#%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/atomic_ops/
%{_includedir}/*.h
%dir %{_includedir}/atomic_ops/
#%{_mandir}/*/*

%changelog
