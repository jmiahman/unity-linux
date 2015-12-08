%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}


Name:		xcb-proto
Version:	1.11
Release:	1%{?dist}
Summary:	XML-XCB protocol descriptions

Group:		Development/Libraries
License:	MIT	
URL:		http://xcb.freedesktop.org/	
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2

%description
The xcb-proto package provides the XML-XCB protocol descriptions that libxcb uses 
to generate the majority of its code and API. 

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -m755 -d %{buildroot}/usr/share/licenses/%{name}
install -m644 COPYING %{buildroot}/usr/share/licenses/%{name}/

%files
%{_libdir}/pkgconfig/xcb-proto.pc
%dir %{python_sitearch}/xcbgen/
%{python_sitearch}/xcbgen/*.py*
#/usr/share/licenses/xcb-proto/COPYING
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xml

%changelog

