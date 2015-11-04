%define _pkgconfigdir %{_libdir}/pkgconfig
#
# Conditional build:
%bcond_with	apidocs		# do not build and package API docs
#
Summary:	OpenCL C programming language library implementation
Name:		llvm-libclc
Version:	0.1.0
%define	snap	20150710
Release:	0.%{snap}.1
License:	BSD-like or MIT
Group:		Libraries
# git clone http://llvm.org/git/libclc.git
Source0:	libclc.tar.xz
# Source0-md5:	223fb33e939258ff69462d37cd7c8897
Patch0:		build.patch
URL:		http://libclc.llvm.org/
BuildRequires:	clang
BuildRequires:	llvm-devel
BuildRequires:	python
BuildRequires:	rpm-build
Requires:	llvm-libs

%description
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification. The following sections of the specification
impose library requirements:

 * 6.1: Supported Data Types
 * 6.2.3: Explicit Conversions
 * 6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
 * 6.9: Preprocessor Directives and Macros
 * 6.11: Built-in Functions
 * 9.3: Double Precision Floating-Point
 * 9.4: 64-bit Atomics
 * 9.5: Writing to 3D image memory objects
 * 9.6: Half Precision Floating-Point

libclc is intended to be used with the Clang compiler's OpenCL
frontend.

%prep
%setup -q -n libclc
%patch0 -p1

%build
./configure.py \
	--prefix=%{_prefix} \
	--libexecdir=%{_datadir}/clc \
	--pkgconfigdir=%{_pkgconfigdir} \
	--with-llvm-config=/usr/bin/llvm-config

%{__make} \
	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.TXT LICENSE.TXT README.TXT www/index.html
%{_includedir}/clc
%{_datadir}/clc
%{_pkgconfigdir}/libclc.pc
