#
# Conditional build:
#
%define		qtver		5.5.0

Summary:	lxqt - libraries
Name:		liblxqt
Version:	0.10.0
Release:	1%{?dist}
License:	LGPL
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	7159035b93fc585b173f41c96b44a523
URL:		http://www.lxqt.org/
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5core-devel >= %{qtver}
BuildRequires:	qt5dbus-devel >= %{qtver}
BuildRequires:	qt5gui-devel >= %{qtver}
#BuildRequires:	qt5gui-platform-directfb >= %{qtver}
#BuildRequires:	qt5gui-platform-egl >= %{qtver}
#BuildRequires:	qt5gui-platform-kms >= %{qtver}
BuildRequires:	qt5xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	libqtxdg-devel >= 1.0.0
BuildRequires:	xz-devel

%description
lxqt - libraries.

%package devel
Summary:	liblxqt - header files and development documentation
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	qt5core-devel >= %{qtver}
Requires:	qt5dbus-devel >= %{qtver}
Requires:	qt5gui-devel >= %{qtver}
Requires:	qt5xml-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
lxqt.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblxqt-qt5.so.*.*.*
%{_libdir}/liblxqt-qt5.so.0
%dir %{_datadir}/lxqt-qt5
%dir %{_datadir}/lxqt-qt5/translations
%dir %{_datadir}/lxqt-qt5/translations/liblxqt

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqt-qt5
%{_libdir}/liblxqt-qt5.so
%{_libdir}/pkgconfig/lxqt-qt5.pc
%{_datadir}/cmake/lxqt-qt5

%changelog
