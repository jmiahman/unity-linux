Summary:	Interface description language used by DirectFB
Name:		directfb-flux
Version:	1.4.4
Release:	1%{?dist}
License:	MIT
Group:		Development/Tools
Source0:	http://www.directfb.org/downloads/Core/flux/flux-%{version}.tar.gz
URL:		http://www.directfb.org/

BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig

%description
flux is an interface description language used by DirectFB.
fluxcomp compiles .flux files to .cpp or .c files.

%prep
%setup -q -n flux-%{version}

%build
%configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/fluxcomp

%changelog
