%define move_yum_conf_back 1
%define yum_updatesd 0
%define disable_check 0

%define _sysconfdir /etc

%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

# We always used /usr/lib here, even on 64bit ... so it's a bit meh.
%define yum_pluginslib   /usr/lib/yum-plugins
%define yum_pluginsshare /usr/share/yum-plugins

# disable broken /usr/lib/rpm/brp-python-bytecompile
%define __os_install_post %{nil}
%define compdir %(pkg-config --variable=completionsdir bash-completion)
%if "%{compdir}" == ""
%define compdir "/etc/bash_completion.d"
%endif

Summary: RPM package installer/updater/manager
Name: yum
Version: 3.4.3
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Base
Source0: http://yum.baseurl.org/download/3.4/%{name}-%{version}.tar.gz
Source1: yum.conf
#Source2: yum-updatesd.conf.fedora
Patch0:	rpm5.patch
Patch1: %{name}-pld.patch
Patch3: rpm5-yum.patch
#Patch1: yum-distro-configs.patch
#Patch5: geode-arch.patch
#Patch6: yum-HEAD.patch
#Patch7: yum-ppc64-preferred.patch
#Patch20: yum-manpage-files.patch
#Patch21: yum-completion-helper.patch
#Patch22: yum-deprecated.patch

URL: http://yum.baseurl.org/
BuildArchitectures: noarch
BuildRequires: python
BuildRequires: gettext
#BuildRequires: intltool
# This is really CheckRequires ...
BuildRequires: python-nose
BuildRequires: python >= 2.4
BuildRequires: rpm-python, rpm >= 0:4.4.2
BuildRequires: python-iniparse
BuildRequires: python-sqlite
BuildRequires: python-urlgrabber >= 3.9.0-8
BuildRequires: yum-metadata-parser >= 1.1.0
BuildRequires: pygpgme
# End of CheckRequires
Requires: python >= 2.4
Requires: rpm-python, rpm 
Requires: python-iniparse
Requires: python-sqlite
Requires: python-urlgrabber
Requires: yum-metadata-parser >= 1.1.0
Requires: pygpgme
Requires: python-pyliblzma
Requires: pyxattr
# Suggests, needed for yum fs diff
Requires: diffutils
Requires: cpio

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded 
automatically, prompting the user for permission as necessary.

%package updatesd
Summary: Update notification daemon
Group: Applications/System
Requires: yum = %{version}-%{release}
Requires: dbus-python
Requires: pygobject2
Requires(preun): /sbin/chkconfig
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(post): /sbin/service
Requires(postun): /sbin/chkconfig
Requires(postun): /sbin/service


%description updatesd
yum-updatesd provides a daemon which checks for available updates and 
can notify you when they are available via email, syslog or dbus. 

%package cron
Summary: RPM package installer/updater/manager cron service
Group: System Environment/Base
Requires: yum >= 3.4.3-84 cronie crontabs findutils
Requires: yum-cron-BE = %{version}-%{release}
Requires(post): /sbin/chkconfig
Requires(post): /sbin/service
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service

%description cron
These are the files needed to run any of the yum-cron update services.

%package cron-daily
Summary: Files needed to run yum updates as a daily cron job
Group: System Environment/Base
Provides: yum-cron-BE = %{version}-%{release}
Requires: yum-cron > 3.4.3-131

%description cron-daily
This is the configuration file for the daily yum-cron update service, which
lives %{_sysconfdir}/yum/yum-cron.conf.
Install this package if you want auto yum updates nightly via cron (or something
else, via. changing the configuration).
By default this just downloads updates and does not apply them.

%package cron-hourly
Summary: Files needed to run yum updates as an hourly cron job
Group: System Environment/Base
Provides: yum-cron-BE = %{version}-%{release}
Requires: yum-cron > 3.4.3-131

%description cron-hourly
This is the configuration file for the daily yum-cron update service, which
lives %{_sysconfdir}/yum/yum-cron-hourly.conf.
Install this package if you want automatic yum metadata updates hourly via
cron (or something else, via. changing the configuration).

%package cron-security
Summary: Files needed to run security yum updates as once a day
Group: System Environment/Base
Provides: yum-cron-BE = %{version}-%{release}
Requires: yum-cron > 3.4.3-131

%description cron-security
This is the configuration file for the security yum-cron update service, which
lives here: %{_sysconfdir}/yum/yum-cron-security.conf
Install this package if you want automatic yum security updates once a day
via. cron (or something else, via. changing the configuration -- this will be
confusing if it's not security updates anymore though).
By default this will download and _apply_ the security updates, unlike
yum-cron-daily which will just download all updates by default.
This runs after yum-cron-daily, if that is installed.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
#%patch20 -p1
#%patch21 -p1
#%patch22 -p1
#%patch1 -p1

%build
sed -i 's!rpmUtils yum etc docs po!rpmUtils yum etc docs!g' Makefile

make

#%if !%{disable_check}
#%check
#make check
#%endif


%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

INIT=sysv

make DESTDIR=$RPM_BUILD_ROOT INIT=$INIT install

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/yum.conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d $RPM_BUILD_ROOT/%{yum_pluginslib}
mkdir -p $RPM_BUILD_ROOT/%{yum_pluginsshare}

# for now, move repodir/yum.conf back
#mv $RPM_BUILD_ROOT/%{_sysconfdir}/yum/repos.d $RPM_BUILD_ROOT/%{_sysconfdir}/yum.repos.d
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/yum/yum.conf

echo Keeping local yum-updatesd

# Ghost files:
mkdir -p $RPM_BUILD_ROOT/var/lib/yum/history
mkdir -p $RPM_BUILD_ROOT/var/lib/yum/plugins
mkdir -p $RPM_BUILD_ROOT/var/lib/yum/yumdb
touch $RPM_BUILD_ROOT/var/lib/yum/uuid

# rpmlint bogus stuff...
chmod +x $RPM_BUILD_ROOT/%{_datadir}/yum-cli/*.py
chmod +x $RPM_BUILD_ROOT/%{python_sitelib}/yum/*.py
chmod +x $RPM_BUILD_ROOT/%{python_sitelib}/rpmUtils/*.py

# Remove the yum-cron systemd stuff to make rpmbuild happy..
rm -f $RPM_BUILD_ROOT/%{_unitdir}/yum-cron.service

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT


%post updatesd
/sbin/chkconfig --add yum-updatesd
/sbin/service yum-updatesd condrestart >/dev/null 2>&1
exit 0

%preun updatesd
if [ $1 = 0 ]; then
 /sbin/chkconfig --del yum-updatesd
 /sbin/service yum-updatesd stop >/dev/null 2>&1
fi
exit 0

%post cron

# SYSV init post cron
# Make sure chkconfig knows about the service
/sbin/chkconfig --add yum-cron
# if an upgrade:
if [ "$1" -ge "1" ]; then
# if there's a /etc/rc.d/init.d/yum file left, assume that there was an
# older instance of yum-cron which used this naming convention.  Clean 
# it up, do a conditional restart
 if [ -f /etc/init.d/yum ]; then 
# was it on?
  /sbin/chkconfig yum
  RETVAL=$?
  if [ $RETVAL = 0 ]; then
# if it was, stop it, then turn on new yum-cron
   /sbin/service yum stop 1> /dev/null 2>&1
   /sbin/service yum-cron start 1> /dev/null 2>&1
   /sbin/chkconfig yum-cron on
  fi
# remove it from the service list
  /sbin/chkconfig --del yum
 fi
fi 
exit 0

%preun cron
# SYSV init preun cron
# if this will be a complete removeal of yum-cron rather than an upgrade,
# remove the service from chkconfig control
if [ $1 = 0 ]; then
 /sbin/chkconfig --del yum-cron
 /sbin/service yum-cron stop 1> /dev/null 2>&1
fi
exit 0

%postun cron
# SYSV init postun cron

# If there's a yum-cron package left after uninstalling one, do a
# conditional restart of the service
if [ "$1" -ge "1" ]; then
 /sbin/service yum-cron condrestart 1> /dev/null 2>&1
fi
exit 0

%files 
%defattr(-, root, root, -)
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%doc README AUTHORS TODO ChangeLog PLUGINS
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/yum.conf
#%dir %{_sysconfdir}/yum.repos.d
#%config(noreplace) %{_sysconfdir}/yum/version-groups.conf
%dir %{_sysconfdir}/yum
#%dir %{_sysconfdir}/yum/protected.d
#%dir %{_sysconfdir}/yum/fssnap.d
#%dir %{_sysconfdir}/yum/vars
#%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%(dirname %{compdir})
%dir %{_datadir}/yum-cli
%{_datadir}/yum-cli/*
#%exclude %{_datadir}/yum-cli/completion-helper.py?
%exclude %{_datadir}/yum-cli/yumupd.py*
#%{_bindir}/yum-deprecated
%{python_sitelib}/yum
%{python_sitelib}/rpmUtils
%dir /var/cache/yum
%dir /var/lib/yum
%ghost /var/lib/yum/uuid
%ghost /var/lib/yum/history
%ghost /var/lib/yum/plugins
%ghost /var/lib/yum/yumdb
#%{_mandir}/man*/yum.conf.5
#%{_mandir}/man*/yum-deprecated.8
#%{_mandir}/man*/yum-shell*
# plugin stuff
%dir %{_sysconfdir}/yum/pluginconf.d 
%dir %{yum_pluginslib}
%dir %{yum_pluginsshare}

#%files cron
#%defattr(-,root,root)
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%{_sysconfdir}/cron.daily/0yum-daily.cron
#%{_sysconfdir}/cron.hourly/0yum-hourly.cron
#%config(noreplace) %{_sysconfdir}/yum/yum-cron.conf
#%config(noreplace) %{_sysconfdir}/yum/yum-cron-hourly.conf
#%{_sysconfdir}/rc.d/init.d/yum-cron
#%{_sbindir}/yum-cron
#%{_mandir}/man*/yum-cron.*

#%files cron-daily
#%defattr(-,root,root)
#%{_sysconfdir}/cron.daily/0yum-daily.cron
#%config(noreplace) %{_sysconfdir}/yum/yum-cron.conf

#%files cron-hourly
#%defattr(-,root,root)
#%{_sysconfdir}/cron.hourly/0yum-hourly.cron
#%config(noreplace) %{_sysconfdir}/yum/yum-cron-hourly.conf

#%files cron-security
#%defattr(-,root,root)
#%{_sysconfdir}/cron.daily/0yum-security.cron
#%config(noreplace) %{_sysconfdir}/yum/yum-cron-security.conf

#%files updatesd
#%defattr(-, root, root)
#%config(noreplace) %{_sysconfdir}/yum/yum-updatesd.conf
#%config %{_sysconfdir}/rc.d/init.d/yum-updatesd
#%config %{_sysconfdir}/dbus-1/system.d/yum-updatesd.conf
%{_datadir}/yum-cli/yumupd.py*
#%{_sbindir}/yum-updatesd
#%{_mandir}/man*/yum-updatesd*

%changelog
