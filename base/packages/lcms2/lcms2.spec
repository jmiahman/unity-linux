Name:           lcms2
Version:        2.7
Release:        2%{?dist}
Summary:        Color Management Engine
License:        MIT
Group:		Development/Libraries
URL:            http://www.littlecms.com/
Source0:        http://www.littlecms.com/lcms2-2.7.tar.gz

BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libtiff-devel
BuildRequires:  zlib-devel

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form. LCMS2 is the current version of LCMS, and can be
parallel installed with the original (deprecated) lcms.

%package        utils
Summary:        Utility applications for %{name}
Group:          Applications/Productivity
Requires:       %{name} = %{version}-%{release}

%description    utils
The %{name}-utils package contains utility applications for %{name}.

%package        devel
Summary:        Development files for LittleCMS
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Provides:       littlecms-devel = %{version}-%{release}

%description    devel
Development files for LittleCMS.

%prep
%setup -q -n lcms2-2.7
%build
%configure --disable-static --program-suffix=2

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p"
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
install -D -m 644 include/lcms2.h $RPM_BUILD_ROOT/usr/include/lcms2.h
install -D -m 644 include/lcms2_plugin.h $RPM_BUILD_ROOT/usr/include/lcms2_plugin.h

# install docs as this is all we've got
#install -D -m 644 doc/LittleCMS2.?\ tutorial.pdf $RPM_BUILD_ROOT/usr/share/doc/lcms2-devel-2.6/tutorial.pdf
#install -D -m 644 doc/LittleCMS2.?\ API.pdf $RPM_BUILD_ROOT/usr/share/doc/lcms2-devel-2.6/api.pdf
#install -D -m 644 doc/LittleCMS2.?\ Plugin\ API.pdf $RPM_BUILD_ROOT/usr/share/doc/lcms2-devel-2.6/plugin-api.pdf

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
#%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
#%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
#%{_datadir}/doc/lcms2-devel-2.6/*.pdf
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
