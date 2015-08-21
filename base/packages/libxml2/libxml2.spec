%define _target_platform %{_arch}-unity-linux-musl
#       --build=%{_target_platform} \
#       --host=%{_target_platform} \


Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.9.2
Release: 1%{?dist}
License: MIT
Group: Development/Libraries
Source: ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig
BuildRequires: xz-devel
URL: http://xmlsoft.org/
#Patch0: libxml2-multilib.patch
Patch1: libxml2-pthread.patch
Patch2: CVE-2014-0191.patch

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary: Libraries, includes, etc. to develop XML and HTML applications
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Requires: zlib-devel
Requires: xz-devel
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package static
Summary: Static library for libxml2
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}

%description static
Static library for libxml2 provided for specific uses or shaving a few
microseconds when parsing, do not link to them for generic purpose packages.

%package python
Summary: Python bindings for the libxml2 library
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}

%description python
The libxml2-python package contains a Python 2 module that permits applications
written in the Python programming language, version 2, to use the interface
supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1  
%patch2 -p1 

%build
#Remove OLD config.sub
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
	[ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done 

./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \

make

%install
rm -fr %{buildroot}

make install DESTDIR=%{buildroot}

# multiarch crazyness on timestamp differences or Makefile/binaries for examples
#touch -m --reference=$RPM_BUILD_ROOT/%{_includedir}/libxml2/libxml/parser.h $RPM_BUILD_ROOT/%{_bindir}/xml2-config

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-%{version}/*
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-python-%{version}/*
(cd doc/examples ; make clean ; rm -rf .deps Makefile)
gzip -9 -c doc/libxml2-api.xml > doc/libxml2-api.xml.gz

%clean
rm -fr %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
#%license Copyright
#%doc AUTHORS NEWS README TODO
#%doc %{_mandir}/man1/xmllint.1*
#%doc %{_mandir}/man1/xmlcatalog.1*
#%doc %{_mandir}/man3/libxml.3*

%{_libdir}/lib*.so.*
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%defattr(-, root, root)

#%doc %{_mandir}/man1/xml2-config.1*
#%doc AUTHORS NEWS README Copyright
#%doc doc/*.html doc/html doc/*.gif doc/*.png
#%doc doc/tutorial doc/libxml2-api.xml.gz
#%doc doc/examples
#%doc %dir %{_datadir}/gtk-doc/html/libxml2
#%doc %{_datadir}/gtk-doc/html/libxml2/*.devhelp
#%doc %{_datadir}/gtk-doc/html/libxml2/*.html
#%doc %{_datadir}/gtk-doc/html/libxml2/*.png
#%doc %{_datadir}/gtk-doc/html/libxml2/*.css

%{_libdir}/lib*.so
%{_libdir}/*.sh
%{_includedir}/*
%{_bindir}/xml2-config
%{_datadir}/aclocal/libxml.m4
%{_libdir}/pkgconfig/libxml-2.0.pc
%dir /usr/lib/cmake/libxml2
%{_libdir}/cmake/libxml2/libxml2-config.cmake

%files static
%defattr(-, root, root)

%{_libdir}/*a

%files python
%defattr(-, root, root)

%{_libdir}/python2*/site-packages/libxml2.py*
%{_libdir}/python2*/site-packages/drv_libxml2.py*
%{_libdir}/python2*/site-packages/libxml2mod*
#%doc python/TODO
#%doc python/libxml2class.txt
#%doc python/tests/*.py
#%doc doc/*.py
#%doc doc/python.html

%changelog
