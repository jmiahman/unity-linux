Summary:	X.org cf files
Name:		xorg-cf-files
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/

BuildRequires:	font-util
BuildRequires:	util-macros

%description
The xorg-cf-files package contains the data files for the imake
utility, defining the known settings for a wide variety of platforms
(many of which have not been verified or tested in over a decade), and
for many of the libraries formerly delivered in the X.Org monolithic
releases.

%prep
%setup -q -n %{name}-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_libdir}/X11/config

%changelog
