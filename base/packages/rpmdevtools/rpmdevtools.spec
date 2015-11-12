%define		_sysconfdir	/etc

Summary:	RPM Development Tools
Name:		rpmdevtools
Version:	8.6
Release:	1%{?dist}
Group:		Development/Tools
# rpmdev-setuptree is GPLv2, everything else GPLv2+
License:	GPL v2+ and GPL v2
URL:		https://fedorahosted.org/rpmdevtools/
Source0:	https://fedorahosted.org/released/rpmdevtools/%{name}-%{version}.tar.xz
BuildRequires:	perl
BuildRequires:	help2man
BuildRequires:	python
BuildRequires:	rpm-python
Requires:	%{_bindir}/man
Requires:	diffutils
Requires:	fakeroot
Requires:	file
Requires:	findutils
Requires:	gawk
Requires:	grep
Requires:	python
Requires:	rpm-python
Requires:	rpm-build
Requires:	sed
Requires:	wget
Provides:	spectool = %{spectool_version}
BuildArch:	noarch

%description
This package contains scripts to aid in development of RPM packages.

%prep
%setup -q 

%build
%configure \
	--libdir=%{_prefix}/lib

%{__make} bin_SCRIPTS

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# sane naming
#mv $RPM_BUILD_ROOT/etc/bash_completion.d/%{name} \
#	$RPM_BUILD_ROOT/etc/bash_completion.d/%{name}.bash-completion

#install -p spectool-%{spectool_version}/spectool $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/devscripts.conf
%config(noreplace) %{_sysconfdir}/%{name}/newspec.conf
%config(noreplace) %{_sysconfdir}/%{name}/rmdevelrpms.conf

# templates
%config(noreplace) %{_sysconfdir}/%{name}/spectemplate-*.spec
%config(noreplace) %{_sysconfdir}/%{name}/template.init

%attr(755,root,root) %{_bindir}/annotate-output
%attr(755,root,root) %{_bindir}/checkbashisms
%attr(755,root,root) %{_bindir}/licensecheck
%attr(755,root,root) %{_bindir}/manpage-alert
%attr(755,root,root) %{_bindir}/rpmargs
%attr(755,root,root) %{_bindir}/rpmdev-*
%attr(755,root,root) %{_bindir}/rpmelfsym
%attr(755,root,root) %{_bindir}/rpmfile
%attr(755,root,root) %{_bindir}/rpminfo
%attr(755,root,root) %{_bindir}/rpmls
%attr(755,root,root) %{_bindir}/rpmpeek
%attr(755,root,root) %{_bindir}/rpmsodiff
%attr(755,root,root) %{_bindir}/rpmsoname
%attr(755,root,root) %{_bindir}/spectool
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*
%{_datadir}/%{name}

%changelog
