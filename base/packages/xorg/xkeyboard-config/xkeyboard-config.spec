Summary:    X Keyboard Extension configuration data
Name:       xkeyboard-config
Version:    2.16
Release:    1%{?dist}
License:    MIT
Group:      User Interface/X
URL:        http://www.freedesktop.org/wiki/Software/XKeyboardConfig

Source0:    http://xorg.freedesktop.org/archive/individual/data/%{name}/%{name}-%{version}.tar.bz2

BuildArch:  noarch
BuildRequires: xkbcomp libx11-devel
BuildRequires: intltool

%description
This package contains configuration data used by the X Keyboard Extension (XKB),
which allows selection of keyboard layouts when using a graphical interface.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q 

%build
./configure \
	--prefix=/usr \
	--with-xkb-base=/usr/share/X11/xkb \
	--with-xkb-rules-symlink=xorg \
	--enable-compat-rules=yes \

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove unnecessary symlink
rm -f $RPM_BUILD_ROOT%{_datadir}/X11/xkb/compiled

# Create filelist
{
   FILESLIST=${PWD}/files.list
   cd $RPM_BUILD_ROOT
   find .%{_datadir}/X11/xkb -type d | sed -e "s/^\./%dir /g" > $FILESLIST
   find .%{_datadir}/X11/xkb -type f | sed -e "s/^\.//g" >> $FILESLIST
   cd ..
}

mkdir -p $RPM_BUILD_ROOT%{_libdir}/
mv $RPM_BUILD_ROOT%{_datadir}/pkgconfig $RPM_BUILD_ROOT%{_libdir}/

%files -f files.list 
%doc AUTHORS README NEWS TODO COPYING docs/README.* docs/HOWTO.*
%{_datadir}/X11/xkb/rules/xorg
%{_datadir}/X11/xkb/rules/xorg.lst
%{_datadir}/X11/xkb/rules/xorg.xml
#%{_mandir}/man7/xkeyboard-config.*

%files devel
%{_libdir}/pkgconfig/xkeyboard-config.pc

%changelog
