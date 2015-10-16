Summary: Hardware graphics acceleration for the framebuffer device
Name: directfb
Version: 1.7.7
Release: 1%{?dist}
License: GPL
Group: System/Libraries
URL: http://www.directfb.org/
Source0: http://www.directfb.org/downloads/Core/DirectFB-1.4/DirectFB-%{version}.tar.gz

Patch0:		DirectFB-1.7.5-flags.patch
Patch1:		DirectFB-1.6.3-pkgconfig.patch 
Patch2:		DirectFB-1.7.1-build.patch 
Patch3:		DirectFB-1.6.3-setregion.patch 
Patch4:		DirectFB-1.6.3-atomic-fix-compiler-error-when-building-for-thumb2.patch
Patch5:		DirectFB-1.7.6-cle266.patch
Patch6:		DirectFB-1.7.6-uint32_t.patch
Patch7:		DirectFB-1.7.6-union-sigval.patch
Patch8:		DirectFB-1.7.6-use-PTHREAD_MUTEX_RECURSIVE.patch


BuildRequires: gcc-c++
BuildRequires: freetype-devel
BuildRequires: libjpeg-turbo-devel libpng-devel zlib-devel
BuildRequires: libx11-devel libxcomposite-devel
BuildRequires: directfb-flux

%description
DirectFB is a thin library that provides hardware graphics
acceleration, input device handling and abstraction, integrated
windowing system with support for translucent windows and multiple
display layers on top of the Linux Framebuffer Device.

It is a complete hardware abstraction layer with software fallbacks
for every graphics operation that is not supported by the underlying
hardware.

%prep
%setup -q -n DirectFB-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%ifarch ppc
grep -rl '#include <linux/config.h>' . | xargs perl -pi -e's,#include <linux/config.h>,/* #include <linux/config.h> */,'
%endif
perl -pi -e's,/usr/X11R6/lib ,/usr/X11R6/%{_lib} ,' configure directfb-config.in

sed -i -e '/^CXXFLAGS=.*-Werror-implicit-function-declaration/d' configure.in

%build
autoreconf -vif
%configure \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
        --enable-static \
        --enable-shared \
	--enable-x11 \
	--disable-multi \
%ifarch %{ix86}
	--enable-mmx \
%endif
	--enable-sse \
	--enable-fbdev \
	--enable-jpeg \
	--enable-zlib \
	--enable-png \
  	--enable-gif \
  	--enable-freetype \
	--with-gfxdrivers=all \
	--with-inputdrivers=keyboard,linuxinput \
	--with-tests \

echo '#undef HAVE_ASM_PAGE_H' >> config.h

make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

cat > develfiles.list << EOF
%defattr(-,root,root,-)
%{_bindir}/directfb-config
%{_bindir}/directfb-csource
%{_bindir}/coretest_task
%{_bindir}/coretest_task_fillrect
%{_mandir}/man1/directfb-csource.1*
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS INSTALL README NEWS TODO
%{_libdir}/%{name}-*
%{_datadir}/%{name}-*
%{_bindir}/dfb*
%{_bindir}/mkdfiff
%{_bindir}/mkdgiff
%{_bindir}/coretest_blit2
%{_bindir}/direct_*
%{_bindir}/fusion_*
%{_bindir}/mkdgifft
%{_bindir}/pxa3xx_dump
%{_mandir}/man1/dfbg.1*
%{_mandir}/man5/directfbrc.5*

%changelog
