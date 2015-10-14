%define infin_ver 2015-06-09

Name:		freetype	
Version:	2.6
Release:	1%{?dist}
Summary:	A free and portable font rendering engine

Group:		System Environment/Libraries
License:	(FTL or GPLv2+) and BSD and MIT and Public Domain and zlib with acknowledgement
URL:		http://www.freetype.org	
Source0:	http://download.savannah.gnu.org/releases/freetype/freetype-%{version}.tar.bz2
#Source2:	https://github.com/bohoomil/fontconfig-ultimate/archive/%{infin_ver}.tar.gz

Patch0: 01-freetype-2.6-enable-valid.patch
Patch1: 03-infinality-2.6-2015.06.08.patch
Patch2: 20-enable-spr.patch
Patch3: 30-enable-valid.patch
Patch4: 40-memcpy-fix.patch


BuildRequires: libpng-devel zlib-devel 

%description
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.

%package devel
Summary: FreeType development libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The freetype-devel package includes the static libraries and header files
for the FreeType font rendering engine.

Install freetype-devel if you want to develop programs which will use
FreeType.

%package docs
Summary: FreeType documentation
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description docs
Documentation for Freetype

Install freetype-devel if you want to develop programs which will use
FreeType.

%prep
%setup -q


%build

./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-static \

make %{?_smp_mflags}

%install
make -j1 DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la

# for compat. This should be removed once all apps are properly using
# pkg-config
ln -s freetype2 %{buildroot}/usr/include/freetype

%files
%defattr(-,root,root)
%{_libdir}/libfreetype.so.*
%doc docs/LICENSE.TXT docs/FTL.TXT docs/GPLv2.TXT

%files devel
%defattr(-,root,root)
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_libdir}/libfreetype.so
%{_bindir}/freetype-config
%{_libdir}/pkgconfig/freetype2.pc

%files docs
%doc README
%doc docs/CHANGES docs/VERSION.DLL docs/formats.txt docs/ft2faq.html
%doc docs/design
%doc docs/glyphs
%doc docs/reference
%doc docs/tutorial
%{_mandir}/man1/*

%changelog

