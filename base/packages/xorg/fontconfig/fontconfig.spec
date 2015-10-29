%define _sysconfdir /etc
%define _fontbasedir %{_datadir}/fonts
%define _fontconfig_masterdir   %{_sysconfdir}/fonts
%define _fontconfig_confdir     %{_sysconfdir}/fonts/conf.d
%define _fontconfig_templatedir %{_datadir}/fontconfig/conf.avail

Summary:	Font configuration and customization library
Name:		fontconfig
Version:	2.11.94
Release:	1%{?dist}
License:	MIT and Public Domain and UCD
Group:		System Environment/Libraries
Source:		http://fontconfig.org/release/%{name}-%{version}.tar.bz2
URL:		http://fontconfig.org

BuildRequires:	expat-devel
BuildRequires:	freetype-devel zlib-devel

Requires(pre):	freetype
Requires(post):	grep coreutils
#Requires:	font(:lang=en)

%description
Fontconfig is designed to locate fonts within the
system and select them according to requirements specified by 
applications.

%package	devel
Summary:	Font configuration and customization library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	freetype-devel >= %{freetype_version}
Requires:	pkgconfig

%description	devel
The fontconfig-devel package includes the header files,
and developer docs for the fontconfig package.

Install fontconfig-devel if you want to develop programs which 
will use fontconfig.

%package	docs
Summary:	Documentation files for fontconfig library
Group:		Documentation
BuildArch:	noarch
Requires:	%{name}-devel = %{version}-%{release}

%description	docs
The fontconfig docs package contains the documentation files
which is useful for developing applications that uses fontconfig.

%prep
%setup -q

%build
# We don't want to rebuild the docs, but we want to install the included ones.
export HASDOCBOOK=no

%configure	--with-add-fonts=/usr/share/X11/fonts/Type1,/usr/share/X11/fonts/TTF,/usr/local/share/fonts \
		--disable-static --disable-docs --localstatedir=/var

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post
/sbin/ldconfig

umask 0022

mkdir -p /var/cache/fontconfig

# Force regeneration of all fontconfig cache files
# The check for existance is needed on dual-arch installs (the second
#  copy of fontconfig might install the binary instead of the first)
# The HOME setting is to avoid problems if HOME hasn't been reset
if [ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache --version 2>&1 | grep -q %{version} ; then
  HOME=/root /usr/bin/fc-cache -f
fi

%postun -p /sbin/ldconfig

#%transfiletriggerin -- /usr/share/fonts /usr/share/X11/fonts/Type1 /usr/share/X11/fonts/TTF /usr/local/share/fonts
#HOME=/root /usr/bin/fc-cache -s

#%transfiletriggerpostun -- /usr/share/fonts /usr/share/X11/fonts/Type1 /usr/share/X11/fonts/TTF /usr/local/share/fonts
#HOME=/root /usr/bin/fc-cache -s

%files
%{_libdir}/libfontconfig.so.*
%{_bindir}/fc-cache
%{_bindir}/fc-cat
%{_bindir}/fc-list
%{_bindir}/fc-match
%{_bindir}/fc-pattern
%{_bindir}/fc-query
%{_bindir}/fc-scan
%{_bindir}/fc-validate
%dir %{_datadir}/fontconfig
%dir %{_fontconfig_templatedir}
%{_fontconfig_templatedir}/*.conf
%{_datadir}/xml/fontconfig
%dir /etc/fonts
%dir /etc/fonts/conf.d

# fonts.conf is not supposed to be modified.
# If you want to do so, you should use local.conf instead.
%{_fontconfig_masterdir}/fonts.conf
%{_fontconfig_confdir}/*.conf
%dir /var/cache/fontconfig

%files devel
%{_libdir}/libfontconfig.so
%{_libdir}/pkgconfig/*
%{_includedir}/fontconfig

%files docs
%doc fontconfig-devel.txt fontconfig-devel
%doc README AUTHORS COPYING
%doc fontconfig-user.txt fontconfig-user.html
%doc %{_fontconfig_confdir}/README

#With Docs
#%{_mandir}/man1/*
#%{_mandir}/man5/*
#%{_mandir}/man3/*

%changelog
