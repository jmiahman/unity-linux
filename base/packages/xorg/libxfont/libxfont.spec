Name:       libxfont
Version:    1.5.1
Release:    1%{?dist}
Summary:    X.Org font library used by the X server
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXfont-%{version}.tar.bz2

BuildRequires: xproto resourceproto xtrans
BuildRequires: libx11-devel zlib-devel bzip2-devel
BuildRequires: freetype-devel docbook-xml fontsproto
BuildRequires: xmlto util-macros

%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font
file formats, and rasterizing them. It is used by the X servers, the X
Font Server (xfs), and some font utilities (bdftopcf for instance),
but should not be used by normal X11 clients. X11 clients access fonts
via either the new API's in libXft, or the legacy API's in libX11.

%package devel                                                          
Summary: Development tools for %{name}.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel. 

%prep
%setup -q -n libXres-%{version}

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure \
	--sysconfdir=/etc \
                                     
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

#mv pc file to correct location
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*
%{_libdir}/*.so.*.*.*

%files devel
%{_libdir}/*.so
%{_includedir}/X11/fonts/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
