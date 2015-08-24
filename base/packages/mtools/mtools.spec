Summary: Programs for accessing MS-DOS disks without mounting the disks
Name: mtools
Version: 4.0.18
Release: 1%{?dist}
License: GPLv3+
Group: Applications/System
Source0: ftp://ftp.gnu.org/gnu/mtools/mtools-%{version}.tar.bz2
Url: http://mtools.linux.lu/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0: mtools-3.9.6-config.patch
#Requires: info

BuildRequires: texinfo, autoconf

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 XDF disks, and 2m disks

Mtools should be installed if you need to use MS-DOS disks

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .conf

%build
autoreconf -fiv
%configure --disable-floppyd --sysconfdir=/etc
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/%{_infodir}
%makeinstall
install -m644 mtools.conf $RPM_BUILD_ROOT/etc
gzip -9f $RPM_BUILD_ROOT/%{_infodir}/*

# We aren't shipping this.
find $RPM_BUILD_ROOT -name "floppyd*" -exec rm {} \;

# dir.gz is handled in %%post and %%preun sections
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir.gz

#ln -s mtools.5.gz %{buildroot}%{_mandir}/man5/mtools.conf.5.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_infodir}/mtools.info ]; then
    /sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :;
fi

%preun
if [ "$1" -eq 0 ]; then
    if [ -f %{_infodir}/mtools.info ]; then
        /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :;
    fi
fi

%files
%defattr(-,root,root)
%config(noreplace) /etc/mtools.conf
#%{!?_licensedir:%global license %%doc}
#%license COPYING
#%doc README Release.notes
%{_bindir}/*
#%{_mandir}/*/*
#%{_infodir}/mtools.info*

%changelog
