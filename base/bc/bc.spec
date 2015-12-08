Summary: GNU's bc (a numeric processing language) and dc (a calculator)
Name: bc
Version: 1.06.95
Release: 1%{?dist}
License: GPLv2+
URL: http://www.gnu.org/software/bc/
Group: Applications/Engineering
Source: ftp://alpha.gnu.org/pub/gnu/bc/bc-%{version}.tar.bz2

Patch0: bc-1.06.95-memory_leak-1.patch

#BuildRequires: readline-devel
#BuildRequires: flex, bison, texinfo

%description
The bc package includes bc and dc. Bc is an arbitrary precision
numeric processing arithmetic language. Dc is an interactive
arbitrary precision stack based calculator, which can be used as a
text mode calculator.

Install the bc package if you need its number handling capabilities or
if you would like to use its text mode calculator.

%prep
%setup -q
%patch0 -p1 -b .memleak

%build
#%configure --with-readline
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%defattr(-,root,root,-)
#%doc COPYING COPYING.LIB FAQ AUTHORS NEWS README Examples/
%{_bindir}/dc
%{_bindir}/bc
#%{_mandir}/*/*
#%{_infodir}/*

%changelog
