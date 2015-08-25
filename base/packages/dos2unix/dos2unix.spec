Summary: Text file format converters
Name: dos2unix
Version: 7.3
Release: 1%{?dist}
Group: Applications/Text
License: BSD
URL: http://waterlan.home.xs4all.nl/dos2unix.html
Source: http://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz
BuildRequires: gettext
BuildRequires: perl-Pod-Checker
Provides: unix2dos = %{version}-%{release}
Obsoletes: unix2dos < 5.1-1

%description
Convert text files with DOS or Mac line endings to Unix line endings and 
vice versa.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# We add doc files manually to %%doc
rm -rf $RPM_BUILD_ROOT%{_docdir}

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc man/man1/dos2unix.htm  ChangeLog.txt COPYING.txt
%doc NEWS.txt README.txt TODO.txt
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%{_bindir}/unix2dos
%{_bindir}/unix2mac
%{_mandir}/man1/*.1*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
