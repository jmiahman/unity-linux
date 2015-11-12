Summary:	List of country and language names
Name:		iso-codes
Version:	3.61
Release:	1
License:	LGPL v2+
Group:		Applications/Text
Source0:	http://pkg-isocodes.alioth.debian.org/downloads/%{name}-%{version}.tar.xz
URL:		http://pkg-isocodes.alioth.debian.org/
BuildRequires:	gettext
BuildRequires:	rpm-build >= 1.446
BuildRequires:	tar >= 1.22
BuildRequires:	xz
BuildArch:	noarch

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not supported yet by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/haw

install -d $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
mv $RPM_BUILD_ROOT%{_datadir}/pkgconfig/iso-codes.pc \
	$RPM_BUILD_ROOT%{_libdir}/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_datadir}/xml/iso-codes
%{_libdir}/pkgconfig/iso-codes.pc

%changelog
