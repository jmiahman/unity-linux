Name:       xinit
Version:    1.3.3
Release:    1%{?dist}
Summary:    X.Org initialisation program.
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:    xinitrc
Source2:    xsession.skel
Source3:    Xsession
Source4:    xserverrc


Requires:   xauth mcookie xmodmap xrdb
BuildRequires: libx11-devel

%description
%{name} is a program used for initialisation of the X server.

%prep
%setup -q -n %{name}-%{version}

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure \
	--with-xinitdir=/etc/X11/xinit \

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

chmod +x %{buildroot}/usr/bin/startx
install -m755 -d %{buildroot}/etc/skel
install -m755 -D %{SOURCE1} %{buildroot}/etc/X11/xinit/xinitrc
install -m755 -D %{SOURCE3} %{buildroot}/etc/X11/xinit/Xsession 
install -m755 %{SOURCE2} %{buildroot}/etc/skel/.xsession
install -m755 %{SOURCE4} %{buildroot}/etc/X11/xinit/xserverrc 
mkdir -p %{buildroot}/etc/X11/xinit/xinitrc.d

#mv pc file to correct location
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
/etc/skel/.xsession
%dir /etc/X11/xinit
%dir /etc/X11
/etc/X11/xinit/*

%changelog
