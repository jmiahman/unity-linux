%define _sysconfdir /etc

Name:           libvdpau
Version:        1.1.1
Release:        1%{?dist}
Summary:        Wrapper library for the Video Decode and Presentation API
License:        MIT
Group:		System Environment/Libraries
URL:            http://freedesktop.org/wiki/Software/VDPAU
Source0:        http://cgit.freedesktop.org/vdpau/libvdpau/snapshot/%{name}-%{version}.tar.bz2
Patch0:         0001-mesa_dri2-Add-missing-include-of-config.h-to-define-.patch
Patch1:         0002-util.h-Make-getenv_wrapper-static-inline.patch
Patch2:         0003-Fix-doc-error-on-displayable-surface-types.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  libx11-devel
BuildRequires:  libxext-devel
BuildRequires:  xproto

%description
VDPAU is the Video Decode and Presentation API for UNIX. It provides an
interface to video decode acceleration and presentation hardware present in
modern GPUs.

%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    docs
The %{name}-docs package contains documentation for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libx11-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -delete
# Let %%doc macro create the correct location in the rpm file, creates a
# versioned docdir in <= f19 and an unversioned docdir in >= f20.
rm -fr %{buildroot}%{_docdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING
%config(noreplace) %{_sysconfdir}/vdpau_wrapper.cfg
%{_libdir}/*.so.*
%dir %{_libdir}/vdpau
%{_libdir}/vdpau/%{name}_trace.so*

%files docs
%doc html

%files devel
%{_includedir}/vdpau/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/vdpau.pc

%changelog
