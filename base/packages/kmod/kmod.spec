%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# - alias from /etc/modprobe.d/3.4.32.longterm-1/geninitrd.conf does not work for geninitrd
# - kmod no longer links with library dynamically since kmod-15:
#   kmod binary statically links to libkmod - if distro is only interested in
#   the kmod tool (for example in an initrd) it can refrain from installing the library
#

Summary:	Linux kernel module handling
Name:		kmod
Version:	21
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://www.kernel.org/pub/linux/utils/kernel/kmod/%{name}-%{version}.tar.xz
# Source0-md5:	ee246fab2e1cba9fbdcad6a86ec31531
#Blacklist in baselayout
#Source1:	%{name}-blacklist
Source2:	%{name}-usb
Patch0:		%{name}-modprobe.d-kver.patch
Patch1:		sed-ere.patch
Patch2: 	strndupa.patch

URL:		http://git.kernel.org/?p=utils/kernel/kmod/kmod.git;a=summary
BuildRequires:	autoconf 
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-build
BuildRequires:	tar 
BuildRequires:	xz
BuildRequires:	xz-devel 
BuildRequires:	zlib-devel
# won't work on older kernels as these do not provide require information in /sys

%define		_bindir		/sbin

%description
kmod is a set of tools to handle common tasks with Linux kernel
modules like insert, remove, list, check properties, resolve
dependencies and aliases.

These tools are designed on top of libkmod, a library that is shipped
with kmod. See libkmod/README for more details on this library and how
to use it. The aim is to be compatible with tools, configurations and
indexes from module-init-tools project.

%package libs
Summary:	Linux kernel module handling library
License:	LGPL v2.1+
Group:		Libraries

%description libs
libkmod was created to allow programs to easily insert, remove and
list modules, also checking its properties, dependencies and aliases.

%package devel
Summary:	Header files for %{name} library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for %{name} library.

#%package -n bash-completion-kmod
#Summary:	bash-completion for kmod utilities
#Group:		Applications/Shells
#Requires:	bash-completion >= 2.0
#BuildArch:	noarch

#%description -n bash-completion-kmod
#bash-completion for kmod utilities.

%package -n python-kmod
Summary:	Python binding for kmod API
License:	LGPL v2.1+
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-kmod
Python binding for kmod API.

%package docs                                                     
Summary:        Docs for kmod API              
License:        LGPL v2.1+                                                       
Group:          Applications/System                          
Requires:       %{name} = %{version}-%{release}                             
                                                                                 
%description docs                                                
Documentation files for the kmod API


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
libtoolize
aclocal -I m4
autoconf
autoheader
automake
%configure \
	--disable-silent-rules \
	--disable-test-modules \
	--enable-python \
	--with-rootlibdir=/%{_lib} \
	--with-xz \
	--with-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/modprobe.d
%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	DESTDIR=$RPM_BUILD_ROOT

# install symlinks
for prog in lsmod rmmod insmod modinfo modprobe depmod; do
	ln -s kmod $RPM_BUILD_ROOT%{_bindir}/$prog
done

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libkmod.la

# not needed in python module
%{__rm} $RPM_BUILD_ROOT%{python_sitearch}/kmod/*.la

:> $RPM_BUILD_ROOT/etc/modprobe.d/modprobe.conf

#cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/modprobe.d/blacklist.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/modprobe.d/usb.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir /etc/modprobe.d
#%config(noreplace) %verify(not md5 mtime size) /etc/modprobe.d/blacklist.conf
%config(noreplace) %verify(not md5 mtime size) /etc/modprobe.d/modprobe.conf
%config(noreplace) %verify(not md5 mtime size) /etc/modprobe.d/usb.conf

%attr(755,root,root) %{_bindir}/kmod
%attr(755,root,root) %{_bindir}/lsmod
%attr(755,root,root) %{_bindir}/rmmod
%attr(755,root,root) %{_bindir}/insmod
%attr(755,root,root) %{_bindir}/modinfo
%attr(755,root,root) %{_bindir}/modprobe
%attr(755,root,root) %{_bindir}/depmod

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libkmod.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libkmod.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmod.so
%{_includedir}/libkmod.h
%{_pkgconfigdir}/libkmod.pc

#%files -n bash-completion-kmod
#%defattr(644,root,root,755)
#%{_datadir}/bash-completion/completions/kmod

%files -n python-kmod
%defattr(644,root,root,755)
%dir %{python_sitearch}/kmod
%attr(755,root,root) %{python_sitearch}/kmod/*.so
%{python_sitearch}/kmod/*.py*

%files docs
%doc libkmod/README NEWS README TODO
%{_mandir}/man5/depmod.d.5*                                                      
%{_mandir}/man5/modprobe.d.5*                                                    
%{_mandir}/man5/modules.dep.5*                                                   
%{_mandir}/man5/modules.dep.bin.5*                                               
%{_mandir}/man8/depmod.8*                                                        
%{_mandir}/man8/insmod.8*                                                        
%{_mandir}/man8/kmod.8*                                                          
%{_mandir}/man8/lsmod.8*                                                         
%{_mandir}/man8/modinfo.8*                                                       
%{_mandir}/man8/modprobe.8*                                                      
%{_mandir}/man8/rmmod.8*

