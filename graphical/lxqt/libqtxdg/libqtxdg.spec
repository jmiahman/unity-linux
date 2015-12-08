%define		qtver		5.5.0

Summary:	libqtxdg
Name:		libqtxdg
Version:	1.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/libqtxdg/%{version}/%{name}-%{version}.tar.xz
URL:		http://www.lxqt.org/
BuildRequires:	qt5core-devel >= %{qtver}
BuildRequires:	qt5gui-devel >= %{qtver}
BuildRequires:	qt5xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	file-devel
#BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	xz-devel

%description
libqtxdg.

%package devel
Summary:	libqtxdg - header files and development documentation
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	qt5core-devel >= %{qtver}
Requires:	qt5gui-devel >= %{qtver}
Requires:	qt5xml-devel >= %{qtver}
Obsoletes:	razor-qt-devel

%description devel
This package contains header files and development documentation for
libqtxdg.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
    -DUSE_QT5=ON \
    ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
    DESTDIR=$RPM_BUILD_ROOT

install -d %{buildroot}%{_libdir}
mv %{buildroot}/usr/lib64/libQt5Xdg.* %{buildroot}%{_libdir}

install -d %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}/usr/lib64/pkgconfig/* %{buildroot}%{_libdir}/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Xdg.so.*.*.*
%{_libdir}/libQt5Xdg.so.1

%files devel
%defattr(644,root,root,755)
%{_includedir}/qt5xdg
%attr(755,root,root) %{_libdir}/libQt5Xdg.so
%{_datadir}/cmake/qt5xdg
%{_libdir}/pkgconfig/Qt5Xdg.pc

%changelog
