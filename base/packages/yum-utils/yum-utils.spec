%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define		_mandir %{_datadir}/man
%define         _libexecdir     %{_prefix}/libexec/%{name}
%define         _sysconfdir     /etc


#
# Conditional build:
%bcond_with	puppet		# puppet plugin

Summary:	A collection of utilities related to yum
Name:		yum-utils
Version:	1.1.31
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://yum.baseurl.org/download/yum-utils/%{name}-%{version}.tar.gz
# Source0-md5:	b2859b89321b98f2581243536e1b4993
Source1:	yum-plugin-unity-kernel.py
Source2:	yum-plugin-unity-kernel.conf
Patch0:		rpm5.patch
URL:		http://yum.baseurl.org/download/yum-utils/
BuildRequires:	gettext
#BuildRequires:	rpm-pythonprov
BuildRequires:	rpm-build
Requires:	python
Requires:	yum
BuildArch:	noarch

%description
Yum-utils is a collection of utilities, plugins and examples related
to the yum package manager.

%package -n yum-updateonboot
Summary:	Run yum update on system boot
Group:		Base
Requires(post):	/sbin/chkconfig
Requires(pre):	/sbin/chkconfig
Requires:	python
Requires:	yum

%description -n yum-updateonboot
Runs yum update on system boot. This allows machines that have been
turned off for an extended amount of time to become secure
immediately, instead of waiting until the next early morning cron job.

#%package -n yum-plugin-changelog
#Summary:	Yum plugin for viewing package changelogs before/after updating
#Group:		Base
# changelog requires new update_md.UpdateMetadata() API in 3.2.23
#Requires:	python-dateutil
#Requires:	yum 

#%description -n yum-plugin-changelog
#This plugin adds a command line option to allow viewing package
#changelog deltas before or after updating packages.

%package -n yum-plugin-fastestmirror
Summary:	Yum plugin which chooses fastest repository from a mirrorlist
Group:		Base
Requires:	yum 

%description -n yum-plugin-fastestmirror
This plugin sorts each repository's mirrorlist by connection speed
prior to downloading packages.

%package -n yum-plugin-protectbase
Summary:	Yum plugin to protect packages from certain repositories
Group:		Base
Requires:	yum

%description -n yum-plugin-protectbase
This plugin allows certain repositories to be protected. Packages in
the protected repositories can't be overridden by packages in
non-protected repositories even if the non-protected repo has a later
version.

%package -n yum-plugin-versionlock
Summary:	Yum plugin to lock specified packages from being updated
Group:		Base
Requires:	yum

%description -n yum-plugin-versionlock
This plugin allows certain packages specified in a file to be
protected from being updated by newer versions.

%package -n yum-plugin-tsflags
Summary:	Yum plugin to add tsflags by a commandline option
Group:		Base
Requires:	yum

%description -n yum-plugin-tsflags
This plugin allows you to specify optional transaction flags on the
yum command line.

%package -n yum-kernel-module
Summary:	Yum plugin to handle kernel-module-foo type of kernel module
Group:		Base
Requires:	yum 

%description -n yum-kernel-module
This plugin handle installation of kernel-module-foo type of kernel
modules when new version of kernels are installed.

%package -n yum-plugin-downloadonly
Summary:	Yum plugin to add downloadonly command option
Group:		Base
Requires:	yum 

%description -n yum-plugin-downloadonly
This plugin adds a --downloadonly flag to yum so that yum will only
download the packages and not install/update them.

%package -n yum-allowdowngrade
Summary:	Yum plugin to enable manual downgrading of packages
Group:		Base
Requires:	yum 

%description -n yum-allowdowngrade
This plugin adds a --allow-downgrade flag to yum to make it possible
to manually downgrade packages to specific versions.

%package -n yum-plugin-unity-kernel
Summary:	Yum plugin to handle Unity kernel installs
Group:		Base

%description -n yum-plugin-unity-kernel
This plugin handle installation of Unity kernels.

%package -n yum-plugin-priorities
Summary:	Plugin to give priorities to packages from different repos
Group:		Base
Requires:	yum >= 3.0

%description -n yum-plugin-priorities
This plugin allows repositories to have different priorities. Packages
in a repository with a lower priority can't be overridden by packages
from a repository with a higher priority even if repo has a later
version.

#%package -n yum-plugin-refresh-updatesd
#Summary:	Tell yum-updatesd to check for updates when yum exits
#Group:		Base
#Requires:	yum 
#Requires:	yum-updatesd

#%description -n yum-plugin-refresh-updatesd
#yum-plugin-refresh-updatesd tells yum-updatesd to check for updates
#when yum exits. This way, if you run 'yum update' and install all
#available updates, puplet will almost instantly update itself to
#reflect this.

%package -n yum-plugin-merge-conf
Summary:	Yum plugin to merge configuration changes when installing packages
Group:		Base
Requires:	yum

%description -n yum-plugin-merge-conf
This yum plugin adds the "--merge-conf" command line option. With this
option, Yum will ask you what to do with config files which have
changed on updating a package.

%package -n yum-plugin-security
Summary:	Yum plugin to enable security filters
Group:		Base
Requires:	yum

%description -n yum-plugin-security
This plugin adds the options --security, --cve, --bz and --advisory
flags to yum and the list-security and info-security commands. The
options make it possible to limit list/upgrade of packages to specific
security relevant ones. The commands give you the security
information.

%package -n yum-protect-packages
Summary:	Yum plugin to prevents Yum from removing itself and other protected packages
Group:		Base
Requires:	yum 

%description -n yum-protect-packages
This plugin prevents Yum from removing itself and other protected
packages. By default, yum is the only package protected, but by
extension this automatically protects everything on which yum depends
(rpm, python, glibc, and so on).Therefore, the plugin functions well
even without compiling careful lists of all important packages.

%package -n yum-basearchonly
Summary:	Yum plugin to let Yum install only basearch packages
Group:		Base
Requires:	yum

%description -n yum-basearchonly
This plugin makes Yum only install basearch packages on multiarch
systems. If you type 'yum install foo' on a x68_64 system, only
'foo-x.y.x86_64.rpm' is installed. If you want to install the
foo-x.y.i386.rpm, you have to type 'yum install foo.i386'. The plugin
only works with 'yum install'.

%package -n yum-plugin-upgrade-helper
Summary:	Yum plugin to help upgrades to the next distribution version
Group:		Base
Requires:	yum 

%description -n yum-plugin-upgrade-helper
This plugin allows yum to erase specific packages on install/update
based on an additional metadata file in repositories. It is used to
simplify distribution upgrade hangups.

%package -n yum-plugin-aliases
Summary:	Yum plugin to enable aliases filters
Group:		Base
# Requires args_hook
Requires:	yum

%description -n yum-plugin-aliases
This plugin adds the command alias, and parses the aliases config.
file to enable aliases.

%package -n yum-plugin-list-data
Summary:	Yum plugin to list aggregate package data
Group:		Base
Requires:	yum 

%description -n yum-plugin-list-data
This plugin adds the commands list- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes and installed-sizes.

%package -n yum-plugin-filter-data
Summary:	Yum plugin to list filter based on package data
Group:		Base
Requires:	yum 

%description -n yum-plugin-filter-data
This plugin adds the options --filter- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes and installed-sizes. Note that each package must match
at least one pattern/range in each category, if any were specified.

%package -n yum-plugin-tmprepo
Summary:	Yum plugin to add temporary repositories
Group:		Base
Requires:	createrepo
Requires:	yum 

%description -n yum-plugin-tmprepo
This plugin adds the option --tmprepo which takes a URL to a .repo
file downloads it and enables it for a single run. This plugin tries
to ensure that temporary repositories are safe to use, by default, by
not allowing gpg checking to be disabled.

%package -n yum-plugin-verify
Summary:	Yum plugin to add verify command, and options
Group:		Base
Requires:	yum

%description -n yum-plugin-verify
This plugin adds the commands verify, verify-all and verify-rpm. There
are also a couple of options. This command works like rpm -V, to
verify your installation.

%package -n yum-plugin-keys
Summary:	Yum plugin to deal with signing keys
Group:		Base

%description -n yum-plugin-keys
This plugin adds the commands keys, keys-info, keys-data and
keys-remove. They allow you to query and remove signing keys.

%package -n yum-plugin-remove-with-leaves
Summary:	Yum plugin to remove dependencies which are no longer used because of a removal
Group:		Base
Requires:	yum 

%description -n yum-plugin-remove-with-leaves
This plugin removes any unused dependencies that were brought in by an
install but would not normally be removed. It helps to keep a system
clean of unused libraries and packages.

%package -n yum-plugin-post-transaction-actions
Summary:	Yum plugin to run arbitrary commands when certain pkgs are acted on
Group:		Base
Requires:	yum 

%description -n yum-plugin-post-transaction-actions
This plugin allows the user to run arbitrary actions immediately
following a transaction when specified packages are changed.

%package -n yum-NetworkManager-dispatcher
Summary:	NetworkManager script which tells yum to check it's cache on network change
Group:		Base
Requires:	yum 

%description -n yum-NetworkManager-dispatcher
This NetworkManager "dispatch script" forces yum to check its cache
if/when a new network connection happens in NetworkManager. Note that
currently there is no checking of previous data, so if your WiFi keeps
going up and down (or you suspend/resume a lot) yum will recheck its
cached data a lot.

%package -n yum-plugin-rpm-warm-cache
Summary:	Yum plugin to access the rpmdb files early to warm up access to the db
Group:		Base
Requires:	yum 

%description -n yum-plugin-rpm-warm-cache
This plugin reads the rpmdb files into the system cache before
accessing the rpmdb directly. In some cases this should speed up
access to rpmdb information

# Works by searching for *-debuginfo ... so it shouldn't trigger on
itself.

%package -n yum-plugin-auto-update-debug-info
Summary:	Yum plugin to enable automatic updates to installed debuginfo packages
Group:		Base
Requires:	yum 

%description -n yum-plugin-auto-update-debug-info
This plugin looks to see if any debuginfo packages are installed, and
if there are it enables all debuginfo repositories that are "children"
of enabled repositories.

%package -n yum-plugin-show-leaves
Summary:	Yum plugin which shows newly installed leaf packages
Group:		Base
Requires:	yum

%description -n yum-plugin-show-leaves
Yum plugin which shows newly installed leaf packages and packages that
became leaves after a transaction

%package -n yum-plugin-local
Summary:	Yum plugin to automatically manage a local repo. of downloaded packages
Group:		Base
Requires:	createrepo
Requires:	yum 

%description -n yum-plugin-local
When this plugin is installed it will automatically copy all
downloaded packages to a repository on the local filesystem, and
(re)build that repository. This means that anything you've downloaded
will always exist, even if the original repo. removes it (and can
thus. be reinstalled/downgraded/etc.).

%package -n yum-plugin-fs-snapshot
Summary:	Yum plugin to automatically snapshot your filesystems during updates
Group:		Base
Requires:	yum

%description -n yum-plugin-fs-snapshot
When this plugin is installed it will automatically snapshot any
filesystem that is touched by the packages in a yum update or yum
remove.

%package -n yum-plugin-ps
Summary:	Yum plugin to look at processes, with respect to packages
Group:		Base
Requires:	yum

%description -n yum-plugin-ps
When this plugin is installed it adds the yum command "ps", which
allows you to see which running processes are accociated with which
packages (and if they need rebooting, or have updates, etc.)

#%package -n yum-plugin-puppetverify
#Summary:	Yum plugin to add puppet checksums to verify data
#Group:		Base
#Requires:	puppet
#Requires:	python-PyYAML
#Requires:	yum 

#%description -n yum-plugin-puppetverify
#Supplies checksums for files in packages from puppet's state file.

#%package -n bash-completion-%{name}
#Summary:	bash-completion for Yum Utils
#Group:		Applications/Shells
#Requires:	%{name}
#Requires:	bash-completion

#%description -n bash-completion-%{name}
#bash-completion for Yum Utils.

%prep
%setup -q
%patch0 -p1

mv plugins/README README.plugins

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PYLIBDIR=/usr/lib/python2.7 \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C updateonboot install \
	DESTDIR=$RPM_BUILD_ROOT

# Plugins to install
plugins="
%{?with_changelog:changelog}
fastestmirror
protectbase
versionlock
tsflags
kernel-module
downloadonly
allowdowngrade
priorities
%{?with_updatesd:refresh-updatesd}
merge-conf
security
basearchonly
upgrade-helper
aliases
list-data
filter-data
tmprepo
verify

keys
remove-with-leaves
post-transaction-actions
rpm-warm-cache
auto-update-debuginfo
show-leaves
local
fs-snapshot
ps
%{?with_puppet:puppetverify}
"

install -d $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d
install -d $RPM_BUILD_ROOT%{_sysconfdir}/yum/post-actions
install -d $RPM_BUILD_ROOT%{_sysconfdir}/yum
install -d $RPM_BUILD_ROOT%{_libexecdir}

cd plugins
for plug in $plugins; do
	cp -p $plug/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d
	cp -p $plug/*.py $RPM_BUILD_ROOT%{_libexecdir}
done

cp -p aliases/aliases $RPM_BUILD_ROOT%{_sysconfdir}/yum/aliases.conf
cp -p versionlock/versionlock.list $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d

# need for for the ghost in files section of yum-plugin-local
install -d $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/_local.repo

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_libexecdir}/unity-kernel.py
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d/unity-kernel.conf

gzip $RPM_BUILD_ROOT/usr/share/man/man1/*.1 
gzip $RPM_BUILD_ROOT/usr/share/man/man8/*.8
gzip $RPM_BUILD_ROOT/usr/share/man/man5/*.5

%clean
rm -rf $RPM_BUILD_ROOT

%post -n yum-updateonboot
/sbin/chkconfig --add yum-updateonboot

%preun -n yum-updateonboot
if [ "$1" = 0 ]; then
	/sbin/service yum-updateonboot stop
	/sbin/chkconfig --del yum-updateonboot
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.plugins TODO
%doc yum-util-cli-template
%attr(755,root,root) %{_bindir}/debuginfo-install
%attr(755,root,root) %{_bindir}/find-repos-of-install
%attr(755,root,root) %{_bindir}/needs-restarting
%attr(755,root,root) %{_bindir}/package-cleanup
%attr(755,root,root) %{_bindir}/repo-graph
%attr(755,root,root) %{_bindir}/repo-rss
%attr(755,root,root) %{_bindir}/repoclosure
%attr(755,root,root) %{_bindir}/repodiff
%attr(755,root,root) %{_bindir}/repomanage
%attr(755,root,root) %{_bindir}/repoquery
%attr(755,root,root) %{_bindir}/reposync
%attr(755,root,root) %{_bindir}/repotrack
%attr(755,root,root) %{_bindir}/show-changed-rco
%attr(755,root,root) %{_bindir}/show-installed
%attr(755,root,root) %{_bindir}/verifytree
%attr(755,root,root) %{_bindir}/yum-builddep
%attr(755,root,root) %{_bindir}/yum-config-manager
%attr(755,root,root) %{_bindir}/yum-debug-dump
%attr(755,root,root) %{_bindir}/yum-debug-restore
%attr(755,root,root) %{_bindir}/yum-groups-manager
%attr(755,root,root) %{_bindir}/yumdownloader
%attr(755,root,root) %{_sbindir}/yum-complete-transaction
%attr(755,root,root) %{_sbindir}/yumdb
%dir %{_libexecdir}
%dir %{python_sitearch}/yumutils
%{python_sitearch}/yumutils/*.py
%{python_sitearch}/yumutils/*.pyc
%{_mandir}/man1/debuginfo-install.1*
%{_mandir}/man1/package-cleanup.1.*
%{_mandir}/man1/repo-rss.1.*
%{_mandir}/man1/repodiff.1*
%{_mandir}/man1/repoquery.1.*
%{_mandir}/man1/reposync.1.*
%{_mandir}/man1/show-changed-rco.1*
%{_mandir}/man1/show-installed.1*
%{_mandir}/man1/yum-aliases.1*
%{_mandir}/man1/yum-builddep.1.*
%{_mandir}/man1/yum-debug-dump.1*
%{_mandir}/man1/yum-groups-manager.1*
%{_mandir}/man1/yum-utils.1.*
%{_mandir}/man1/yum-versionlock.1*
%{_mandir}/man1/yumdownloader.1.*
%{_mandir}/man5/yum-versionlock.conf.5*
%{_mandir}/man8/yum-complete-transaction.8.*
%{_mandir}/man8/yumdb.8*

%files -n yum-updateonboot
%defattr(644,root,root,755)
%doc updateonboot/README
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/yum-updateonboot
%attr(754,root,root) /etc/rc.d/init.d/yum-updateonboot

#%files -n yum-plugin-changelog
#%defattr(644,root,root,755)
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/changelog.conf
#%{_libexecdir}/changelog.*
#%{_mandir}/man1/yum-changelog.1.*
#%{_mandir}/man5/yum-changelog.conf.5.*

%files -n yum-plugin-fastestmirror
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/fastestmirror.conf
%{_libexecdir}/fastestmirror.*

%files -n yum-plugin-protectbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/protectbase.conf
%{_libexecdir}/protectbase.*

%files -n yum-plugin-versionlock
%defattr(644,root,root,755)
%doc plugins/versionlock/README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/versionlock.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/versionlock.list
%{_libexecdir}/versionlock.*

%files -n yum-plugin-tsflags
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/tsflags.conf
%{_libexecdir}/tsflags.*

# TODO: remove in unity? removed in fedora
%files -n yum-kernel-module
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/kernel-module.conf
%{_libexecdir}/kernel-module.*

%files -n yum-plugin-downloadonly
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/downloadonly.conf
%{_libexecdir}/downloadonly.*

# TODO: remove like fedora?
%files -n yum-allowdowngrade
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/allowdowngrade.conf
%{_libexecdir}/allowdowngrade.*

%files -n yum-plugin-unity-kernel
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/unity-kernel.conf
%{_libexecdir}/unity-kernel.*

%files -n yum-plugin-priorities
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/priorities.conf
%{_libexecdir}/priorities.*

#%files -n yum-plugin-refresh-updatesd
#%defattr(644,root,root,755)
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/refresh-updatesd.conf
#%{_libexecdir}/refresh-updatesd.*

%files -n yum-plugin-merge-conf
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/merge-conf.conf
%{_libexecdir}/merge-conf.*

%files -n yum-plugin-security
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/security.conf
%{_libexecdir}/security.*
%{_mandir}/man8/yum-security.8.*

%if 0
# TODO: renamed to protectbase?
%files -n yum-protect-packages
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/protect-packages.conf
%{_libexecdir}/protect-packages.*
%endif

# TODO: rename to basearchonly like fedora?
%files -n yum-basearchonly
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/basearchonly.conf
%{_libexecdir}/basearchonly.*

%files -n yum-plugin-upgrade-helper
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/upgrade-helper.conf
%{_libexecdir}/upgrade-helper.*

%files -n yum-plugin-aliases
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/aliases.conf
%config(noreplace) %{_sysconfdir}/yum/aliases.conf
%{_libexecdir}/aliases.*

%files -n yum-plugin-list-data
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/list-data.conf
%{_libexecdir}/list-data.*
%{_mandir}/man1/yum-list-data.1.*

%files -n yum-plugin-filter-data
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/filter-data.conf
%{_libexecdir}/filter-data.*
%{_mandir}/man1/yum-filter-data.1.*

%files -n yum-plugin-tmprepo
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/tmprepo.conf
%{_libexecdir}/tmprepo.*

%files -n yum-plugin-verify
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/verify.conf
%{_libexecdir}/verify.*
%{_mandir}/man1/yum-verify.1.*

%files -n yum-plugin-keys
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/keys.conf
%{_libexecdir}/keys.*

%files -n yum-NetworkManager-dispatcher
%defattr(644,root,root,755)
%{_sysconfdir}/NetworkManager/dispatcher.d/yum-NetworkManager-dispatcher

%files -n yum-plugin-remove-with-leaves
%defattr(644,root,root,755)
%{_libexecdir}/remove-with-leaves.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/remove-with-leaves.conf

%files -n yum-plugin-post-transaction-actions
%defattr(644,root,root,755)
%{_libexecdir}/post-transaction-actions.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/post-transaction-actions.conf
%doc plugins/post-transaction-actions/sample.action
# Default *.action file dropping dir.
%dir %{_sysconfdir}/yum/post-actions

%files -n yum-plugin-rpm-warm-cache
%defattr(644,root,root,755)
%{_libexecdir}/rpm-warm-cache.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/rpm-warm-cache.conf

%files -n yum-plugin-auto-update-debug-info
%defattr(644,root,root,755)
%{_libexecdir}/auto-update-debuginfo.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/auto-update-debuginfo.conf

%files -n yum-plugin-show-leaves
%defattr(644,root,root,755)
%{_libexecdir}/show-leaves.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/show-leaves.conf

%files -n yum-plugin-local
%defattr(644,root,root,755)
%ghost %{_sysconfdir}/yum.repos.d/_local.repo
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/local.conf
%{_libexecdir}/local.*

%files -n yum-plugin-fs-snapshot
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/fs-snapshot.conf
%{_libexecdir}/fs-snapshot.*
%{_mandir}/man1/yum-fs-snapshot.1.*
%{_mandir}/man5/yum-fs-snapshot.conf.5.*

%files -n yum-plugin-ps
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/ps.conf
%{_libexecdir}/ps.*

#%if %{with puppet}
#%files -n yum-plugin-puppetverify
#%defattr(644,root,root,755)
#%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/puppetverify.conf
#%{_libexecdir}/puppetverify.*
#%endif

#%files -n bash-completion-%{name}
#%defattr(644,root,root,755)
#/etc/bash_completion.d/*
