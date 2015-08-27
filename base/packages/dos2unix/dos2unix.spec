Summary: Hany's Dos2Unix Text file format converters
Name: hd2u
Version: 1.0.3
Release: 1%{?dist}
Group: Applications/Text
License: GPL
URL: http://hany.sk/~hany/software/hd2u/
Source: http://terminus.sk/~hany/_data/hd2u/hd2u-1.0.3.tgz
Provides: unix2dos = %{version}-%{release}

BuildRequires: popt-devel

%description
Hany's Dos2Unix Converts text files with DOS or Mac line endings to Unix line endings and 
vice versa.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
install -c -d -m 755 %{buildroot}/usr/bin
install -c -m 755 -s dos2unix %{buildroot}/usr/bin


%files
%defattr(-,root,root,0755)
#%doc man/man1/dos2unix.htm  ChangeLog.txt COPYING.txt
#%doc NEWS.txt README.txt TODO.txt
%{_bindir}/dos2unix
#%{_mandir}/man1/*.1*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
