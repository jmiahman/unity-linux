Summary: Modify rpath of compiled programs
Name:    chrpath
Version: 0.16
Release: 1%{?dist}
License: GPL+
Group:   Development/Tools
URL:     https://chrpath.alioth.debian.org/
Source0: https://alioth.debian.org/frs/download.php/file/3979/%{name}-%{version}.tar.gz


%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -fr %{buildroot}/usr/doc


%files
#%doc AUTHORS README NEWS ChangeLog*
#%license COPYING
%{_bindir}/chrpath
#%{_mandir}/man1/chrpath.1*



%changelog
