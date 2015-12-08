Name: intltool
Summary: Utility for internationalizing various kinds of data files
Version: 0.51.0
Release: 1%{?dist}
License: GPLv2 with exceptions
Group: Development/Tools
#VCS: bzr:https://code.edge.launchpad.net/~intltool/intltool/trunk
Source: http://edge.launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz
URL: https://launchpad.net/intltool
BuildArch: noarch
Requires: patch
# for /usr/share/aclocal
Requires: automake
Requires: gettext-devel
Requires: perl-xml-parser
BuildRequires: perl-xml-parser
BuildRequires: gettext
# http://bugzilla.gnome.org/show_bug.cgi?id=568845
# Dropping this patch per the last comment on that thread:
# Martin Pitt: As the reporter of the bug I close this, as the new API du jour is gsettings,
# which has a sensible gettext integration.
#Patch0: schemas-merge.patch
Patch1:  intltool-0.51.0-perl-5.22.patch

%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.

%prep
%setup -q
%patch1 -p1

%build
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%check
make check

%files
#%doc AUTHORS README
#%license COPYING
%{_bindir}/intltool*
%{_datadir}/intltool
%{_datadir}/aclocal/intltool.m4
#%{_mandir}/man8/intltool*.8*

%changelog
