Name: hwdata
Summary: Hardware identification and configuration data
Version: 0.282
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Base
Source: https://fedorahosted.org/releases/h/w/%{name}/%{name}-%{version}.tar.bz2
URL:    http://git.fedorahosted.org/git/hwdata.git
BuildArch: noarch

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%prep
%setup -q
%configure

%build
# nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_prefix}/lib/modprobe.d
make install DESTDIR=$RPM_BUILD_ROOT libdir=%{_prefix}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE COPYING
%dir %{_datadir}/%{name}
%dir %{_prefix}/lib/modprobe.d
%{_prefix}/lib/modprobe.d/dist-blacklist.conf
%{_datadir}/%{name}/*

%changelog
