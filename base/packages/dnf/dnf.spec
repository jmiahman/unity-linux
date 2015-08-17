%global hawkey_version 0.6.0
%global librepo_version 1.7.16
%global libcomps_version 0.1.6
%global rpm_version 4.12.0

%global confdir %{_sysconfdir}/dnf

%global pluginconfpath %{confdir}/plugins
%global py2pluginpath %{python_sitelib}/dnf-plugins

Name:		dnf
Version:	1.1.0
Release:	1%{?dist}
Summary:	Package manager forked from Yum, using libsolv as a dependency resolver
# For a breakdown of the licensing, see PACKAGE-LICENSING
License:	GPLv2+ and GPLv2 and GPL
URL:		https://github.com/rpm-software-management/dnf
# The Source0 tarball can be generated using following commands:
# git clone http://github.com/rpm-software-management/dnf.git
# cd dnf/package
# ./archive
# tarball will be generated in $HOME/rpmbuild/sources/
Source0:    http://rpm-software-management.fedorapeople.org/dnf-%{version}.tar.gz
Patch0: dnf-1.1.0-1-to-dnf-1.1.0-2.patch
BuildArch:  noarch
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  python-bugzilla
BuildRequires:  python-sphinx
Requires:   python-dnf = %{version}-%{release}

%description
Package manager forked from Yum, using libsolv as a dependency resolver.

%package conf
Requires:   libreport-filesystem
Summary:    Configuration files for DNF.
%description conf
Configuration files for DNF.

%package -n dnf-yum
Conflicts:      yum < 3.4.3-505
Requires:   dnf = %{version}-%{release}
Summary:    As a Yum CLI compatibility layer, supplies /usr/bin/yum redirecting to DNF.
%description -n dnf-yum
As a Yum CLI compatibility layer, supplies /usr/bin/yum redirecting to DNF.

%package -n python-dnf
Summary:    Python 2 interface to DNF.
BuildRequires:  pygpgme
BuildRequires:  pyliblzma
BuildRequires:  python2
BuildRequires:  python-hawkey >= %{hawkey_version}
BuildRequires:  python-iniparse
BuildRequires:  python-libcomps >= %{libcomps_version}
BuildRequires:  python-librepo >= %{librepo_version}
BuildRequires:  python-nose
BuildRequires:  rpm-python >= %{rpm_version}

Requires:   dnf-conf = %{version}-%{release}
Requires:   deltarpm
Requires:   pygpgme
Requires:   pyliblzma
Requires:   python-hawkey >= %{hawkey_version}
Requires:   python-iniparse
Requires:   python-libcomps >= %{libcomps_version}
Requires:   python-librepo >= %{librepo_version}
Requires:   rpm-python >= %{rpm_version}

%description -n python-dnf
Python 2 interface to DNF.

%prep
%setup -q -n dnf-%{version}
%patch0 -p1

%build
%cmake .
make %{?_smp_mflags}
make doc-man

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{pluginconfpath}
mkdir -p $RPM_BUILD_ROOT%{py2pluginpath}
mkdir -p $RPM_BUILD_ROOT%{py3pluginpath}/__pycache__
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log
mkdir -p $RPM_BUILD_ROOT%{_var}/cache/dnf
touch $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}.log
ln -sr $RPM_BUILD_ROOT%{_bindir}/dnf-2 $RPM_BUILD_ROOT%{_bindir}/dnf
mv $RPM_BUILD_ROOT%{_bindir}/dnf-automatic-2 $RPM_BUILD_ROOT%{_bindir}/dnf-automatic
rm $RPM_BUILD_ROOT%{_bindir}/dnf-automatic-3

%check
make ARGS="-V" test

%files 
%doc AUTHORS README.rst COPYING PACKAGE-LICENSING
%{_bindir}/dnf
%{_mandir}/man8/dnf.8.gz
%{_mandir}/man8/yum2dnf.8.gz
%{_unitdir}/dnf-makecache.service
%{_unitdir}/dnf-makecache.timer
%{_var}/cache/dnf

%files conf
%doc AUTHORS README.rst COPYING PACKAGE-LICENSING
%dir %{confdir}
%dir %{pluginconfpath}
%dir %{confdir}/protected.d
%config(noreplace) %{confdir}/dnf.conf
%config(noreplace) %{confdir}/protected.d/dnf.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %{_localstatedir}/%{_lib}/dnf
%ghost %{_localstatedir}/log/hawkey.log
%ghost %{_localstatedir}/log/%{name}.log
%ghost %{_localstatedir}/log/%{name}.librepo.log
%ghost %{_localstatedir}/log/%{name}.rpm.log
%ghost %{_localstatedir}/log/%{name}.plugin.log
%config %{_sysconfdir}/bash_completion.d/dnf-completion.bash
%{_mandir}/man5/dnf.conf.5.gz
%{_tmpfilesdir}/dnf.conf
%{_sysconfdir}/libreport/events.d/collect_dnf.conf

%files -n dnf-yum
%doc AUTHORS README.rst COPYING PACKAGE-LICENSING
%{_bindir}/yum
%{_mandir}/man8/yum.8.gz

%files -n python-dnf
%{_bindir}/dnf-2
%doc AUTHORS README.rst COPYING PACKAGE-LICENSING
%exclude %{python_sitelib}/dnf/automatic
%{python_sitelib}/dnf/
%dir %{py2pluginpath}

%changelog
