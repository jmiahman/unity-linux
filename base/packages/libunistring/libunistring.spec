
Name:		libunistring	
Version:	0.9.6
Release:	1%{?dist}
Summary:	Library for manipulating Unicode strings and C strings

Group:		Development/Libraries		
License:	GPL
URL:		http://www.gnu.org/software/libunistring/
Source0:	http://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz

#BuildRequires:	
#Requires:	

%description
libunistring is for you if your application involves non-trivial
text processing, such as upper/lower case conversi:ons, line breaking, 
operations on words, or more advanced analysis of text.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

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
	--localstatedir=/var \
	--disable-static \

make %{?_smp_mflags}


%install
make -j1 DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la
rm -f %{buildroot}/usr/lib/charset.alias

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%license COPYING COPYING.LESSER
%{_libdir}/*.so.*

%files devel
#%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so
%{_includedir}/unistring/*.h
%{_includedir}/*.h
%dir %{_includedir}/unistring/
#%{_mandir}/*/*

%changelog
