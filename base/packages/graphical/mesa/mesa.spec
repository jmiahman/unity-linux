%define _pkgconfigdir %{_libdir}/pkgconfig

#
# todo:
# - check if gallium_intel note is still valid, switch the bcond if not
# - consider:
# - arm drivers (ilo,freedreno,vc4)?
# - subpackage with non-dri libGL for use with x-servers with missing glx extension?
# - resurrect static if it's useful (using plain xorg target? dri doesn't support static)
#
# conditional build:
%bcond_with	gallium		# gallium drivers
%bcond_with	gallium_intel	# gallium i915 driver (instead of plain dri; doesn't work with aiglx)
%bcond_without	gallium_nouveau	# gallium nouveau driver
%bcond_without	gallium_radeon	# gallium radeon drivers
%bcond_without	egl		# egl libraries
%bcond_with	openvg		# openvg library [not builind since 10.4, dropped in 10.6]
%bcond_without	gbm		# graphics buffer manager
%bcond_without	nine		# nine direct3d 9+ state tracker (for wine)
%bcond_without	opencl		# opencl support
%bcond_without	ocl_icd		# opencl as icd (installable client driver)
%bcond_without	omx		# openmax (bellagio omxil) support
%bcond_with	va		# va library
%bcond_without	wayland		# wayland egl
%bcond_without	xa		# xa state tracker (for vmwgfx xorg driver)
%bcond_with	texture_float	# floating-point textures and renderbuffers (sgi patent in us)
%bcond_with	static_libs	# static libraries [not supported for dri, thus broken currently]
%bcond_with	tests		# tests
#
# glapi version (glapi tables in dri drivers and libGLx must be in sync);
# set to current mesa version on abi break, when xserver tables get regenerated
# (until they start to be somehow versioned themselves)
%define		glapi_ver		7.1.0
# minimal supported xserver version
%define		xserver_ver		1.5.0
# other packages
%define		libdrm_ver		2.4.65
%define		dri2proto_ver		2.8
%define		dri3proto_ver		1.0
%define		glproto_ver		1.4.14
%define		presentproto_ver	1.0
%define		_sysconfdir		/etc

%if %{without gallium}
%undefine	with_gallium_intel
%undefine	with_gallium_nouveau
%undefine	with_gallium_radeon
%undefine	with_nine
%undefine	with_ocl_icd
%undefine	with_omx
%undefine	with_opencl
%undefine	with_xa
%endif

%if %{without egl}
%undefine	with_gbm
%undefine	with_wayland
%endif

Summary:	free opengl implementation
Name:		mesa
version:	11.0.3
Release:	1
License:	mit (core) and others - see license.html file
Group:		x11/libraries
Source0:	ftp://ftp.freedesktop.org/pub/mesa/%{version}/mesa-%{version}.tar.xz
# source0-md5:	bf9118bf0fbf360715cfe60baf7a1db5
#patch0:		missing-type.patch
#patch1:		x32.patch
Url:		http://www.mesa3d.org/
buildrequires:	autoconf >= 2.60
buildrequires:	automake
%{?with_opencl:buildrequires:	clang-devel}
buildrequires:	expat-devel
buildrequires:	gcc 
%{?with_opencl:buildrequires:	gcc-c++}
buildrequires:	libdrm-devel
buildrequires:	libstdc++-devel
buildrequires:	talloc
buildrequires:	libtool
%{?with_va:buildrequires:	libva-devel}
buildrequires:	libvdpau-devel
buildrequires:	libxcb-devel 
%{?with_gallium_radeon:buildrequires:	llvm-devel}
%{?with_opencl:buildrequires:	llvm-libclc}
# for sha1 (could use also libmd/libsha1/libgcrypt/openssl instead)
#buildrequires:	nettle-devel
#%{?with_ocl_icd:buildrequires:	ocl-icd-devel}
#%{?with_omx:buildrequires:	libomxil-bellagio-devel}
buildrequires:	perl
buildrequires:	pixman-devel
buildrequires:	pkgconfig
buildrequires:	python 
#buildrequires:	python-mako
#buildrequires:	python-modules 
buildrequires:	rpm-build
buildrequires:	sed
%{?with_egl:buildrequires:	eudev-devel}
# wayland-{client,server}
%{?with_wayland:buildrequires:	wayland-devel}
buildrequires:	libxdamage-devel
buildrequires:	libxext-devel
buildrequires:	libxfixes-devel
buildrequires:	libxt-devel
buildrequires:	libxvmc-devel
buildrequires:	libxxf86vm-devel
buildrequires:	libxshmfence-devel
buildrequires:	dri2proto
buildrequires:	dri3proto
buildrequires:	glproto 
buildrequires:	presentproto
buildrequires:	makedepend
%if %{with gallium}
buildrequires:	xextproto-devel 
buildrequires:	xserver-server-devel
%endif

# libGLESv1_cm, libGLESv2, libGL, libOSMesa:
#  _glapi_tls_dispatch is defined in libGLapi, but it's some kind of symbol ldd -r doesn't notice(?)
# libgbm: circular dependency with libEGL (wayland_buffer_is_drm symbol)
%define		skip_post_check_so      libGLESv1_CM.so.1.* libGLESv2.so.2.* libGL.so.1.* libOSMesa.so.* libgbm.*.so.*

# llvm build broken
%define		filterout_ld    -wl,--as-needed

%description
mesa is a 3-d graphics library with an api which is very similar to
that of opengl(r). to the extent that mesa utilizes the opengl command
syntax or state machine, it is being used with authorization from
silicon graphics, inc. however, the author does not possess an opengl
license from sgi, and makes no claim that mesa is in any way a
compatible replacement for opengl or associated with sgi.

%package libegl
summary:	mesa implementation of egl native platform graphics interface library
license:	mit
group:		libraries
requires:	%{name}-libglapi = %{version}-%{release}
# glx driver in libEGL dlopens libGL.so
requires:	opengl >= 1.2
requires:	libdrm >= %{libdrm_ver}
requires:	libxcb >= 1.9
%{?with_wayland:requires:	libwayland-server}
%if %{with gallium}
requires:	eudev 
%endif
%if %{with gbm}
requires:	%{name}-libgbm = %{version}-%{release}
%endif
provides:	egl = 1.4

%description libegl
this package contains shared libEGL - mesa implementation of egl
native platform graphics interface as specified by khronos group:
<http://www.khronos.org/egl/>.

%package libegl-devel
summary:	header files for mesa implementation of egl library
license:	mit
group:		development/libraries
requires:	%{name}-khrplatform-devel = %{version}-%{release}
requires:	%{name}-libegl = %{version}-%{release}
requires:	libdrm-devel >= %{libdrm_ver}
requires:	libx11-devel
requires:	libxdamage-devel
requires:	libxext-devel >= 1.0.5
requires:	libxfixes-devel
requires:	libxxf86vm-devel
requires:	dri2proto >= %{dri2proto_ver}
requires:	glproto >= %{glproto_ver}
provides:	egl-devel = 1.4

%description libegl-devel
header files for mesa implementation of egl library.

%package libegl-static
summary:	static mesa egl library
license:	mit
group:		development/libraries
requires:	%{name}-libegl-devel = %{version}-%{release}
provides:	egl-static = 1.4

%description libegl-static
static mesa egl library.

%package libgl
summary:	free mesa3d implementation of libGL opengl library
license:	mit
group:		x11/libraries
requires:	%{name}-libglapi = %{version}-%{release}
requires:	libdrm >= %{libdrm_ver}
provides:	opengl = 3.3
provides:	opengl-glx = 1.4

%description libgl
mesa is a 3-d graphics library with an api which is very similar to
that of opengl(r). to the extent that mesa utilizes the opengl command
syntax or state machine, it is being used with authorization from
silicon graphics, inc. however, the author does not possess an opengl
license from sgi, and makes no claim that mesa is in any way a
compatible replacement for opengl or associated with sgi.

this package contains libGL which implements opengl 1.5 and glx 1.4
specifications. it uses dri for rendering.

%package libgl-devel
summary:	header files for mesa3d libGL library
license:	mit
group:		x11/development/libraries
# loose dependency on libGL to use with other libGL binaries
requires:	opengl >= 1.5
requires:	libdrm-devel >= %{libdrm_ver}
requires:	libx11-devel
requires:	libxdamage-devel
requires:	libxext-devel >= 1.0.5
requires:	libxxf86vm-devel
requires:	dri2proto >= %{dri2proto_ver}
requires:	glproto >= %{glproto_ver}
provides:	opengl-glx-devel = 1.4
provides:	opengl-devel = 3.3
obsoletes:	mesa-devel
obsoletes:	x11-opengl-devel < 1:7.0.0
obsoletes:	x11-opengl-devel-base < 1:7.0.0
obsoletes:	xfree86-opengl-devel < 1:7.0.0
obsoletes:	xfree86-opengl-devel-base < 1:7.0.0

%description libgl-devel
header files for mesa3d libGL library.

%package libgl-static
summary:	static mesa3d libGL library
license:	mit
group:		x11/development/libraries
requires:	%{name}-libgl-devel = %{version}-%{release}
provides:	opengl-static = 3.3
obsoletes:	mesa-static
obsoletes:	x11-opengl-static < 1:7.0.0
obsoletes:	xfree86-opengl-static < 1:7.0.0

%description libgl-static
static mesa3d libGL library. it uses software renderer.

%package libgles
summary:	mesa implementation of gles (opengl es) libraries
group:		libraries
requires:	%{name}-libglapi = %{version}-%{release}
provides:	opengles
provides:	openglesv1 = 1.1
provides:	openglesv2 = 2.0

%description libgles
this package contains shared libraries of mesa implementation of gles
(opengl es) - cross-platform api for full-function 2d and 3d graphics
on embedded systems. opengl es specification can be found on khronos
group site: <http://www.khronos.org/opengles/>. mesa implements opengl
es 1.1 and 2.0.

%package libgles-devel
summary:	header files for mesa gles libraries
group:		development/libraries
requires:	%{name}-khrplatform-devel = %{version}-%{release}
# <egl/egl.h> for <gles/egl.h>
requires:	%{name}-libegl-devel = %{version}-%{release}
requires:	%{name}-libgles = %{version}-%{release}
provides:	opengles-devel
provides:	openglesv1-devel = 1.1
provides:	openglesv2-devel = 2.0

%description libgles-devel
header files for mesa gles libraries.

%package libosmesa
summary:	osmesa (off-screen renderer) library
license:	mit
group:		libraries

%description libosmesa
osmesa (off-screen renderer) library.

%package libosmesa-devel
summary:	header file for osmesa (off-screen renderer) library
license:	mit
group:		development/libraries
requires:	%{name}-libosmesa = %{version}-%{release}
# for <gl/gl.h> only
requires:	opengl-devel

%description libosmesa-devel
header file for osmesa (off-screen renderer) library.

%package libosmesa-static
summary:	static osmesa (off-screen renderer) library
license:	mit
group:		development/libraries
requires:	%{name}-libosmesa-devel = %{version}-%{release}
# this static build of osmesa needs static non-dri mesa implementation
requires:	%{name}-libgl-static = %{version}-%{release}

%description libosmesa-static
static osmesa (off-screen renderer) library.

%package opencl-icd
summary:	mesa implementation of opencl (compuing language) api icd
license:	mit
group:		libraries
requires:	filesystem >= 4.0-29
requires:	libdrm >= %{libdrm_ver}
requires:	llvm-libclc
requires:	eudev
provides:	opencl = 1.1
provides:	ocl-icd-driver

%description opencl-icd
this package contains mesa implementation of opencl - standard for
cross-platform, parallel programming of modern processors found in
personal computers, servers and handheld/embedded devices. opencl
specification can be found on khronos group site:
<http://www.khronos.org/opencl/>. mesa implements opencl 1.1.

the implementation is provided as an installable client driver (icd)
for use with the ocl-icd loader.

%package libopencl
summary:	mesa implementation of opencl (compuing language) api
license:	mit
group:		libraries
requires:	libdrm >= %{libdrm_ver}
requires:	llvm-libclc
requires:	eudev
provides:	opencl = 1.1

%description libopencl
this package contains mesa implementation of opencl - standard for
cross-platform, parallel programming of modern processors found in
personal computers, servers and handheld/embedded devices. opencl
specification can be found on khronos group site:
<http://www.khronos.org/opencl/>. mesa implements opencl 1.1.

%package libopencl-devel
summary:	header files for mesa opencl library
license:	mit
group:		development/libraries
requires:	%{name}-libopencl = %{version}-%{release}
provides:	opencl-devel = 1.1

%description libopencl-devel
header files for mesa opencl library.

%package libopenvg
summary:	mesa implementation of openvg (vector graphics accelleration) api
license:	mit
group:		libraries
provides:	openvg = 1.1

%description libopenvg
this package contains mesa implementation of openvg - cross-platform
api that provides a low-level hardware acceleration interface for
vector graphics libraries such as flash and svg. openvg specification
can be found on khronos group site: <http://www.khronos.org/openvg/>.
mesa implements openvg 1.1.

%package libopenvg-devel
summary:	header file for mesa openvg library
license:	mit
group:		development/libraries
requires:	%{name}-khrplatform-devel = %{version}-%{release}
requires:	%{name}-libopenvg = %{version}-%{release}
provides:	openvg-devel = 1.1

%description libopenvg-devel
header file for mesa openvg library.

%package libxvmc-nouveau
summary:	mesa implementation of xvmc api for nvidia adapters
license:	mit
group:		libraries
requires:	libdrm >= %{libdrm_ver}
requires:	xorg-lib-libxvmc >= 1.0.6
conflicts:	mesa-libxvmc

%description libxvmc-nouveau
mesa implementation of xvmc api for nvidia adapters (nv40-nv96, nva0).

%package libxvmc-r600
summary:	mesa implementation of xvmc api for ati radeon r600 series adapters
license:	mit
group:		libraries
requires:	libdrm >= %{libdrm_ver}
requires:	xorg-lib-libxvmc >= 1.0.6
conflicts:	mesa-libxvmc

%description libxvmc-r600
mesa implementation of xvmc api for ati radeon adapters based on
r600/r700 chips.

%package -n libva-driver-gallium
summary:	va driver for gallium state tracker
group:		libraries
requires:	libva >= 1.3.0

%description -n libva-driver-gallium
va driver for gallium state tracker.

%package libgbm
summary:	mesa graphics buffer manager library
group:		libraries
requires:	%{name}-libglapi = %{version}-%{release}
requires:	eudev

%description libgbm
mesa graphics buffer manager library.

%package libgbm-devel
summary:	header file for mesa graphics buffer manager library
group:		development/libraries
requires:	%{name}-libgbm = %{version}-%{release}
requires:	eudev-devel

%description libgbm-devel
header file for mesa graphics buffer manager library.

%package gbm-driver-i915
summary:	i915 driver for mesa gbm framework
group:		libraries
requires:	%{name}-libgbm = %{version}-%{release}
obsoletes:	mesa-opencl-driver-i915

%description gbm-driver-i915
i915 driver for mesa graphics buffer manager. it supports intel
915/945/g33/q33/q35/pineview chips.

%package gbm-driver-nouveau
summary:	nouveau driver for mesa gbm framework
group:		libraries
requires:	%{name}-libgbm = %{version}-%{release}
obsoletes:	mesa-opencl-driver-nouveau

%description gbm-driver-nouveau
nouveau driver for mesa graphics buffer manager. it supports nvidia
adapters.

%package gbm-driver-r300
summary:	r300 driver for mesa gbm framework
group:		libraries
requires:	%{name}-libgbm = %{version}-%{release}
obsoletes:	mesa-opencl-driver-r300

%description gbm-driver-r300
r300 driver for mesa graphics buffer manager. it supports ati radeon
adapters based on r300/r400/rs690/r500 chips.

%package gbm-driver-r600
summary:	r600 driver for mesa gbm framework
group:		libraries
requires:	%{name}-libgbm = %{version}-%{release}
obsoletes:	mesa-libllvmradeon
obsoletes:	mesa-opencl-driver-r600

%description gbm-driver-r600
r600 driver for mesa graphics buffer manager. it supports ati radeon
adapters based on r600/r700 chips.

%package gbm-driver-radeonsi
summary:	radeonsi driver for mesa gbm framework
group:		libraries
requires:	%{name}-libgbm = %{version}-%{release}
obsoletes:	mesa-libllvmradeon
obsoletes:	mesa-opencl-driver-radeonsi

%description gbm-driver-radeonsi
radeonsi driver for mesa graphics buffer manager. it supports ati
radeon adapters based on southern islands chips.

%package gbm-driver-swrast
summary:	software (swrast) driver for mesa gbm framework
group:		libraries
requires:	%{name}-libgbm = %{version}-%{release}
obsoletes:	mesa-opencl-driver-swrast

%description gbm-driver-swrast
software (swrast) driver for mesa graphics buffer manager.

%package gbm-driver-vmwgfx
summary:	vmwgfx driver for mesa gbm framework
group:		libraries
requires:	%{name}-libgbm = %{version}-%{release}
obsoletes:	mesa-opencl-driver-vmwgfx

%description gbm-driver-vmwgfx
vmwgfx driver for mesa graphics buffer manager. it supports vmware
virtual video adapter.

%package libglapi
summary:	mesa gl api shared library
group:		libraries

%description libglapi
mesa gl api shared library, common for various apis (egl, gl, gles).

%package libwayland-egl
summary:	wayland egl library
group:		libraries
requires:	libdrm >= %{libdrm_ver}

%description libwayland-egl
wayland egl platform library.

%package libwayland-egl-devel
summary:	development files for wayland egl library
group:		development/libraries
requires:	%{name}-libwayland-egl = %{version}-%{release}
requires:	libdrm-devel >= %{libdrm_ver}

%description libwayland-egl-devel
development files for wayland egl platform library.

%package libxatracker
summary:	xorg gallium3d accelleration library
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}

%description libxatracker
xorg gallium3d accelleration library (used by new vmwgfx driver).

%package libxatracker-devel
summary:	header files for xorg gallium3d accelleration library
group:		x11/development/libraries
requires:	%{name}-libxatracker = %{version}-%{release}
requires:	libdrm-devel >= %{libdrm_ver}

%description libxatracker-devel
header files for xorg gallium3d accelleration library.

%package khrplatform-devel
summary:	khronos platform header file
group:		development/libraries

%description khrplatform-devel
khronos platform header file.

%package dri-driver-ati-radeon-r100
summary:	x.org dri driver for ati r100 card family
license:	mit
group:		x11/libraries
requires:	xorg-driver-video-ati
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-ati-radeon-r100
x.org dri driver for ati r100 card family (radeon 7000-7500).

%package dri-driver-ati-radeon-r200
summary:	x.org dri driver for ati r200 card family
license:	mit
group:		x11/libraries
requires:	xorg-driver-video-ati
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-ati-radeon-r200
x.org dri driver for ati r200 card family (radeon 8500-92xx)

%package dri-driver-ati-radeon-r300
summary:	x.org dri driver for ati r300 card family
license:	mit
group:		x11/libraries
requires:	xorg-driver-video-ati
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-ati-radeon-r300
x.org dri driver for ati r300/r400/rs690/r500 card family.

%package dri-driver-ati-radeon-r600
summary:	x.org dri driver for ati r600 card family
license:	mit
group:		x11/libraries
requires:	radeon-ucode
requires:	xorg-driver-video-ati
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-ati-radeon-r600
x.org dri driver for ati r600/r700 card family.

%package dri-driver-ati-radeon-si
summary:	x.org dri driver for ati southern islands card family
license:	mit
group:		x11/libraries
requires:	radeon-ucode
requires:	xorg-driver-video-ati
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-ati-radeon-si
x.org dri driver for ati southern islands card family.

%package dri-driver-intel-i915
summary:	x.org dri driver for intel i915 card family
license:	mit
group:		x11/libraries
requires:	xorg-driver-video-intel
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}
obsoletes:	mesa-dri-driver-intel-i830

%description dri-driver-intel-i915
x.org dri driver for intel i915 card family (915, 945, g33, q33, q35,
pineview).

%package dri-driver-intel-i965
summary:	x.org dri driver for intel i965 card family
license:	mit
group:		x11/libraries
requires:	xorg-driver-video-intel
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-intel-i965
x.org dri driver for intel i965 card family (946gz, 965g, 965q, 965gm,
965gme, gm45, g41, b43, q45, g45);

%package dri-driver-nouveau
summary:	x.org dri driver for nvidia card family
license:	mit
group:		x11/libraries
requires:	xorg-driver-video-nouveau
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-nouveau
x.org dri drivers for nvidia card family.

%package dri-driver-swrast
summary:	x.org dri software rasterizer driver
license:	mit
group:		x11/libraries
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-swrast
x.org dri software rasterizer driver.

%package dri-driver-vmwgfx
summary:	x.org dri driver for vmware
license:	mit
group:		x11/libraries
requires:	xorg-driver-video-vmware
requires:	xorg-xserver-libGLx(glapi) = %{glapi_ver}
requires:	xorg-xserver-server >= %{xserver_ver}

%description dri-driver-vmwgfx
x.org dri driver for vmware.

%package d3d
summary:	nine direct3d9 driver (for wine)
group:		libraries
requires:	libdrm >= %{libdrm_ver}

%description d3d
nine direct3d9 driver (for wine).

%package d3d-devel
summary:	nine direct3d9 driver api
group:		development/libraries
requires:	libdrm-devel >= %{libdrm_ver}

%description d3d-devel
nine direct3d9 driver api.

%package -n libvdpau-driver-mesa-nouveau
summary:	mesa nouveau driver for the vdpau api
license:	mit
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}
requires:	libvdpau >= 0.4.1
conflicts:	libvdpau-driver-mesa

%description -n libvdpau-driver-mesa-nouveau
mesa nouveau driver for the vdpau api. it supports nvidia adapters
(nv40-nv96, nva0).

%package -n libvdpau-driver-mesa-r300
summary:	mesa r300 driver for the vdpau api
license:	mit
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}
requires:	libvdpau >= 0.4.1
conflicts:	libvdpau-driver-mesa

%description -n libvdpau-driver-mesa-r300
mesa r300 driver for the vdpau api. it supports ati radeon adapters
based on r300 chips.

%package -n libvdpau-driver-mesa-r600
summary:	mesa r600 driver for the vdpau api
license:	mit
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}
requires:	libvdpau >= 0.4.1
conflicts:	libvdpau-driver-mesa

%description -n libvdpau-driver-mesa-r600
mesa r600 driver for the vdpau api. it supports ati radeon adapters
based on r600/r700 chips.

%package -n libvdpau-driver-mesa-radeonsi
summary:	mesa radeonsi driver for the vdpau api
license:	mit
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}
requires:	libvdpau >= 0.4.1
conflicts:	libvdpau-driver-mesa
obsoletes:	mesa-libllvmradeon

%description -n libvdpau-driver-mesa-radeonsi
mesa radeonsi driver for the vdpau api. it supports ati radeon
adapters based on southern islands chips.

%package -n omxil-mesa
summary:	mesa driver for bellagio openmax il api
license:	mit
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}
requires:	libxcb >= 1.8
requires:	libomxil-bellagio
obsoletes:	omxil-mesa-nouveau
obsoletes:	omxil-mesa-r600
obsoletes:	omxil-mesa-radeonsi

%description -n omxil-mesa
mesa driver for bellagio openmax il api.

%package -n omxil-mesa-nouveau
summary:	mesa nouveau driver for bellagio openmax il api
license:	mit
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}
requires:	libxcb >= 1.8
requires:	libomxil-bellagio

%description -n omxil-mesa-nouveau
mesa nouveau driver for bellagio openmax il api. it supports nvidia
adapters (nv40-nv96, nva0).

%package -n omxil-mesa-r600
summary:	mesa r600 driver for bellagio openmax il api
license:	mit
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}
requires:	libxcb >= 1.8
requires:	libomxil-bellagio

%description -n omxil-mesa-r600
mesa r600 driver for bellagio openmax il api. it supports ati radeon
adapters based on r600/r700 chips.

%package -n omxil-mesa-radeonsi
summary:	mesa radeonsi driver for bellagio openmax il api
license:	mit
group:		x11/libraries
requires:	libdrm >= %{libdrm_ver}
requires:	libxcb >= 1.8
requires:	libomxil-bellagio

%description -n omxil-mesa-radeonsi
mesa radeonsi driver for bellagio openmax il api. it supports ati
radeon adapters based on southern islands chips.

%prep
%setup -q -n mesa-%{version}
#%patch0 -p1
#%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

dri_drivers="r200 radeon \
%if %{without gallium_intel}
i915 \
%endif
i965 \
nouveau \
%ifarch sparc sparcv9 sparc64
ffb \
%endif
swrast"

dri_drivers=$(echo $dri_drivers | xargs | tr ' ' ',')

gallium_drivers="svga swrast \
%if %{with gallium_intel}
i915 \
%endif
%if %{with gallium_radeon}
r300 \
r600 \
radeonsi \
%endif
%if %{with gallium_nouveau}
nouveau
%endif
"

gallium_drivers=$(echo $gallium_drivers | xargs | tr ' ' ',')

%configure \
	--sysconfdir=/etc \
	--disable-silent-rules \
	--enable-glx-tls \
	--enable-osmesa \
	--disable-selinux \
	--enable-shared \
	--enable-shared-glapi \
	%{?with_static_libs:--enable-static} \
	%{?with_texture_float:--enable-texture-float} \
%if %{with egl}
	--enable-egl \
	--enable-gles1 \
	--enable-gles2 \
	--with-egl-platforms=x11%{?with_gbm:,drm}%{?with_wayland:,wayland} \
%endif
%if %{with gallium}
	--enable-gallium-llvm \
	--enable-llvm-shared-libs \
	%{__enable egl gallium-egl} \
	%{__enable gbm gallium-gbm} \
	%{__enable ocl_icd opencl-icd} \
	%{?with_nine:--enable-nine} \
	%{__enable opencl} \
	--enable-vdpau \
	%{?with_omx:--enable-omx} \
	%{?with_xa:--enable-xa} \
	--enable-xvmc \
	--with-gallium-drivers=${gallium_drivers} \
%else
	--without-gallium-drivers \
%endif
	--with-dri-drivers=${dri_drivers} \
	--with-dri-driverdir=%{_libdir}/xorg/modules/dri \
	--with-sha1=libnettle \
	--with-va-libdir=%{_libdir}/libva/dri

%{__make}

%{?with_tests:%{__make} check}

%install
make install DESTDIR=%{buildroot}

# strip out undesirable headers
%{__rm} %{buildroot}%{_includedir}/GL/wglext.h
# dlopened by soname
%{?with_gallium:%{__rm} %{buildroot}%{_libdir}/libxvmc*.so}
%{?with_gallium:%{__rm} %{buildroot}%{_libdir}/libxvmc*.so.1.0}
# dlopened by soname or .so link
%{?with_gallium:%{__rm} %{buildroot}%{_libdir}/vdpau/libvdpau_*.so.1.0}
# not used externally
%{__rm} %{buildroot}%{_libdir}/libglapi.so
# dlopened
%{?with_omx:%{__rm} %{buildroot}%{_libdir}/bellagio/libomx_*.la}
%{?with_nine:%{__rm} %{buildroot}%{_libdir}/d3d/d3dadapter9.la}
%{?with_gallium:%{__rm} %{buildroot}%{_libdir}/gallium-pipe/pipe_*.la}
# not defined by standards; and not needed, there is pkg-config support
%{__rm} %{buildroot}%{_libdir}/lib*.la
%{?with_gallium:%{__rm} %{buildroot}%{_libdir}/libva/dri/gallium_drv_video.la}

# remove "os abi: linux 2.4.20" tag, so private copies (nvidia or fglrx),
# set up via /etc/ld.so.conf.d/*.conf will be preferred over this
# strip -R .note.abi-tag %{buildroot}%{_libdir}/libGL.so.*.*

%clean
rm -rf %{buildroot}

%post	libegl -p /sbin/ldconfig
%postun	libegl -p /sbin/ldconfig

%post	libgl -p /sbin/ldconfig
%postun	libgl -p /sbin/ldconfig

%post	libgles -p /sbin/ldconfig
%postun	libgles -p /sbin/ldconfig

%post	libosmesa -p /sbin/ldconfig
%postun	libosmesa -p /sbin/ldconfig

%post	libopencl -p /sbin/ldconfig
%postun	libopencl -p /sbin/ldconfig

%post	libopenvg -p /sbin/ldconfig
%postun	libopenvg -p /sbin/ldconfig

%post	libxvmc-nouveau -p /sbin/ldconfig
%postun	libxvmc-nouveau -p /sbin/ldconfig
%post	libxvmc-r600 -p /sbin/ldconfig
%postun	libxvmc-r600 -p /sbin/ldconfig

%post	libgbm -p /sbin/ldconfig
%postun	libgbm -p /sbin/ldconfig

%post	libglapi -p /sbin/ldconfig
%postun	libglapi -p /sbin/ldconfig

%post	libwayland-egl -p /sbin/ldconfig
%postun	libwayland-egl -p /sbin/ldconfig

%post	libxatracker -p /sbin/ldconfig
%postun	libxatracker -p /sbin/ldconfig

%if %{with egl}
%files libegl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libEGL.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libEGL.so.1

%files libegl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libEGL.so
%dir %{_includedir}/EGL
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/eglextchromium.h
%{_includedir}/EGL/eglmesaext.h
%{_includedir}/EGL/eglplatform.h
%{_pkgconfigdir}/egl.pc

%if %{with static_libs}
%files libegl-static
%defattr(644,root,root,755)
%{_libdir}/libEGL.a
%endif
%endif

%files libgl
%defattr(644,root,root,755)
%doc docs/{*.html,readme.uvd,patents.txt,relnotes/*.html}
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libGL.so.1
# symlink for binary apps which fail to conform linux opengl abi
# (and dlopen libGL.so instead of libGL.so.1; the same does mesa libEGL)
%attr(755,root,root) %{_libdir}/libGL.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drirc

%files libgl-devel
%defattr(644,root,root,755)
%doc docs/specs/*
%dir %{_includedir}/GL
%{_includedir}/GL/gl.h
%{_includedir}/GL/glcorearb.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glxext.h
%{_includedir}/GL/glx_mangle.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%{_pkgconfigdir}/dri.pc
%{_pkgconfigdir}/gl.pc

%if %{with static_libs}
%files libgl-static
%defattr(644,root,root,755)
%{_libdir}/libGL.a
%endif

%files libgles
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLESv1_CM.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGLESv1_CM.so.1
%attr(755,root,root) %{_libdir}/libGLESv2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libGLESv2.so.2

%files libgles-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLESv1_CM.so
%attr(755,root,root) %{_libdir}/libGLESv2.so
%{_includedir}/GLES
%{_includedir}/GLES2
%{_includedir}/GLES3
%{_pkgconfigdir}/glesv1_cm.pc
%{_pkgconfigdir}/glesv2.pc

%files libosmesa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOSMesa.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libOSMesa.so.8

%files libosmesa-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOSMesa.so
%{_includedir}/GL/osmesa.h
%{_pkgconfigdir}/osmesa.pc

%if %{with static_libs}
%files libosmesa-static
%defattr(644,root,root,755)
%{_libdir}/libOSMesa.a
%endif

%if %{with opencl}
%if %{with ocl_icd}
%files opencl-icd
%defattr(644,root,root,755)
/etc/opencl/vendors/mesa.icd
%attr(755,root,root) %{_libdir}/libmesaopencl.so
%attr(755,root,root) %{_libdir}/libmesaopencl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmesaopencl.so.1
%else
%files libopencl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopencl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopencl.so.1

%files libopencl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopencl.so
%{_includedir}/CL
%endif
%endif

%if %{with egl} && %{with openvg} && %{with gallium}
%files libopenvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenvg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenvg.so.1

%files libopenvg-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenvg.so
%{_includedir}/VG
%{_pkgconfigdir}/vg.pc
%endif

%if %{with gallium}
%if %{with gallium_nouveau}
%files libxvmc-nouveau
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxvmcnouveau.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libxvmcnouveau.so.1
%endif

%if %{with gallium_radeon}
%files libxvmc-r600
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxvmcr600.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libxvmcr600.so.1
%endif

%if %{with va}
%files -n libva-driver-gallium
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva/dri/gallium_drv_video.so
%endif
%endif

%if %{with gbm}
%files libgbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgbm.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgbm.so.1
%if %{with gallium}
%dir %{_libdir}/gallium-pipe
%endif

%files libgbm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgbm.so
%{_includedir}/gbm.h
%{_pkgconfigdir}/gbm.pc
%endif

%if %{with gallium}
%if %{with gallium_intel}
%files gbm-driver-i915
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_i915.so
%endif

%if %{with gallium_nouveau}
%files gbm-driver-nouveau
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_nouveau.so
%endif

%if %{with gallium_radeon}
%files gbm-driver-r300
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_r300.so

%files gbm-driver-r600
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_r600.so

%files gbm-driver-radeonsi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_radeonsi.so
%endif

%files gbm-driver-swrast
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_swrast.so

%files gbm-driver-vmwgfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_vmwgfx.so
%endif

%files libglapi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglapi.so.*.*
%{_libdir}/libglapi.so.0
# libGLapi-devel? nothing seems to need it atm.
#%attr(755,root,root) %{_libdir}/libGLapi.so

%if %{with wayland}
%files libwayland-egl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwayland-egl.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libwayland-egl.so.1

%files libwayland-egl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwayland-egl.so
%{_pkgconfigdir}/wayland-egl.pc
%endif

%if %{with xa}
%files libxatracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxatracker.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxatracker.so.2

%files libxatracker-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxatracker.so
%{_includedir}/xa_composite.h
%{_includedir}/xa_context.h
%{_includedir}/xa_tracker.h
%{_pkgconfigdir}/xatracker.pc
%endif

%if %{with egl}
%files khrplatform-devel
%defattr(644,root,root,755)
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%endif

%files dri-driver-ati-radeon-r100
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/radeon_dri.so

%files dri-driver-ati-radeon-r200
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/r200_dri.so

%if %{with gallium}
%if %{with gallium_radeon}
%files dri-driver-ati-radeon-r300
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/r300_dri.so

%files dri-driver-ati-radeon-r600
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/r600_dri.so

%files dri-driver-ati-radeon-si
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/radeonsi_dri.so
%endif
%endif

%files dri-driver-intel-i915
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/i915_dri.so

%files dri-driver-intel-i965
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/i965_dri.so

%files dri-driver-nouveau
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/nouveau_vieux_dri.so
%if %{with gallium_nouveau}
%attr(755,root,root) %{_libdir}/xorg/modules/dri/nouveau_dri.so
%endif

%files dri-driver-swrast
%defattr(644,root,root,755)
%if %{with gallium}
%attr(755,root,root) %{_libdir}/xorg/modules/dri/kms_swrast_dri.so
%endif
%attr(755,root,root) %{_libdir}/xorg/modules/dri/swrast_dri.so

%if %{with gallium}
%files dri-driver-vmwgfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/vmwgfx_dri.so
%endif

%if %{with nine}
%files d3d
%defattr(644,root,root,755)
%dir %{_libdir}/d3d
%attr(755,root,root) %{_libdir}/d3d/d3dadapter9.so*

%files d3d-devel
%defattr(644,root,root,755)
%{_includedir}/d3dadapter
%{_pkgconfigdir}/d3d.pc
%endif

%if %{with gallium}
# ldconfig is not used in vdpau tree, so package all symlinks
%if %{with gallium_nouveau}
%files -n libvdpau-driver-mesa-nouveau
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_nouveau.so.1.0.0
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_nouveau.so.1
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_nouveau.so
%endif

%if %{with gallium_radeon}
%files -n libvdpau-driver-mesa-r300
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_r300.so.1.0.0
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_r300.so.1
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_r300.so

%files -n libvdpau-driver-mesa-r600
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_r600.so.1.0.0
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_r600.so.1
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_r600.so

%files -n libvdpau-driver-mesa-radeonsi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_radeonsi.so.1.0.0
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_radeonsi.so.1
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_radeonsi.so
%endif
%endif

%if %{with gallium} && %{with omx}
%files -n omxil-mesa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bellagio/libomx_mesa.so
%endif
