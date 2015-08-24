Summary: Connects C/C++/Objective C to some high-level programming languages
Name:    swig
Version: 3.0.7
Release: 1%{?dist}
License: GPLv3+ and BSD
Group: Development/Tools
URL:     http://swig.sourceforge.net/
Source0: http://downloads.sourceforge.net/project/swig/swig/swig-%{version}/swig-%{version}.tar.gz

BuildRequires: zlib-devel, pcre-devel
Requires: guile

%description
Simplified Wrapper and Interface Generator (SWIG) is a software
development tool for connecting C, C++ and Objective C programs with a
variety of high-level programming languages.  SWIG is primarily used
with Perl, Python and Tcl/TK, but it has also been extended to Java,
Eiffel and Guile. SWIG is normally used to create high-level
interpreted programming environments, systems integration, and as a
tool for building user interfaces

%package doc
Summary:   Documentation files for SWIG
License:   BSD
Group:     Development/Tools
BuildArch: noarch

%description doc
This package contains documentation for SWIG and useful examples

%prep
%setup -q -n swig-%{version}


%build
%configure

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
install -D -m644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
install -D -m644 LICENSE-UNIVERSITIES %{buildroot}/usr/share/licenses/%{name}/LICENSE-UNIVERSITIES


%files
%{_bindir}/*
%{_datadir}/swig
#%{_mandir}/man1/ccache-swig.1*
#%{_mandir}/man1/swig.1*
#%doc ANNOUNCE CHANGES CHANGES.current LICENSE LICENSE-GPL
#%doc LICENSE-UNIVERSITIES COPYRIGHT README TODO

%files doc
%doc Doc Examples LICENSE LICENSE-GPL LICENSE-UNIVERSITIES COPYRIGHT

%changelog
