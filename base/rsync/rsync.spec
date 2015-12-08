Summary: A program for synchronizing files over a network
Name: rsync
Version: 3.1.1
Release: 1%{?prerelease}%{?dist}
Group: Applications/Internet
URL: http://rsync.samba.org/

Source0: https://download.samba.org/pub/rsync/src/rsync-%{version}.tar.gz
Source1: rsyncd.conf  
Source2: rsyncd.confd  
Source3: rsyncd.initd  
Source4: rsyncd.logrotate

BuildRequires: libacl-devel, autoconf, popt-devel, perl
License: GPLv3+

%description
Rsync uses a reliable algorithm to bring remote and host files into
sync very quickly. Rsync is fast because it just sends the differences
in the files over the network instead of sending the complete
files. Rsync is often used as a very powerful mirroring process or
just as a more capable replacement for the rcp command. A technical
report which describes the rsync algorithm is included in this
package.

%prep
%setup -q -n rsync-%{version}
chmod -x support/*

%build
CFLAGS="$CFLAGS -DINET6" \
%configure

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall INSTALLCMD='install -p' INSTALLMAN='install -p'
install -D -m 644 %{SOURCE1} %{buildroot}/etc/rsyncd.conf 
install -D -m 644 %{SOURCE2} %{buildroot}/etc/conf.d/rsyncd
install -D -m 755 %{SOURCE3} %{buildroot}/etc/init.d/rsyncd
install -D -m 644 %{SOURCE4} %{buildroot}/etc/logrotate.d/rsyncd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%doc NEWS OLDNEWS README support/ tech_report.tex
%{_bindir}/%{name}
#%{_mandir}/man1/%{name}.1*

%changelog
