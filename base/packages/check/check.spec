Name:           check
Version:        0.10.0
Release:        1%{?dist}
Summary:        A unit test framework for C
Source0:        http://downloads.sourceforge.net/check/%{name}-%{version}.tar.gz
Group:          Development/Tools
License:        LGPLv2+
URL:            http://check.sourceforge.net/
# Only needed for autotools in Fedora
#Patch0:         %{name}-0.10.0-info-in-builddir.patch
BuildRequires:  pkgconfig, libtool, autoconf, automake
BuildRequires:	texinfo
Requires(post): info
Requires(preun): info

%description
Check is a unit test framework for C. It features a simple interface for 
defining unit tests, putting little in the way of the developer. Tests 
are run in a separate address space, so Check can catch both assertion 
failures and code errors that cause segmentation faults or other signals. 
The output from unit tests can be used within source code editors and IDEs.

%package devel
Summary:        Libraries and headers for developing programs with check
Group:          Development/Libraries
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}

%description devel
Libraries and headers for developing programs with check

%package static
Summary:        Static libraries of check
Group:          Development/Libraries

%description static
Static libraries of check.

%package checkmk
Summary:        Translate concise versions of test suites into C programs
License:        BSD
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description checkmk
The checkmk binary translates concise versions of test suites into C
programs suitable for use with the Check unit test framework.

%prep
%setup -q
#%patch0 -p1 -b .info-in-builddir

autoreconf -ivf

%build
%configure

# Get rid of undesirable hardcoded rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%post
/sbin/ldconfig
if [ -e %{_infodir}/%{name}.info* ]; then
  /sbin/install-info \
    --entry='* Check: (check).               A unit testing framework for C.' \
    %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%postun -p /sbin/ldconfig

%preun
if [ $1 = 0 -a -e %{_infodir}/%{name}.info* ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
#%doc AUTHORS COPYING.LESSER ChangeLog ChangeLogOld NEWS README SVNChangeLog
#%doc THANKS TODO
%{_libdir}/libcheck.so.*
%{_infodir}/check*

%files devel
#%doc doc/example
%{_includedir}/check.h
%{_includedir}/check_stdint.h
%{_libdir}/libcheck.so
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4

#check used to be static only, hence this.
%files static
#%doc COPYING.LESSER
%{_libdir}/libcheck.a

%files checkmk
#%doc checkmk/README checkmk/examples
%{_bindir}/checkmk
%{_mandir}/man1/checkmk.1*

%changelog
