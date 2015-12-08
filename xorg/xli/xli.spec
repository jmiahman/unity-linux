Summary:	XLI - X11 Image Loading Utility
Name:		xli
Version:	1.16
Release:	1
License:	MIT
Group:		X11/Window Managers
Source0:	ftp://ftp.x.org/contrib/applications/xli.1.16.tar.gz
URL:		http://xorg.freedesktop.org/

BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel

%description
This utility will view several types of images under X11, or load
images onto the X11 root window.  Can view the following image types
under X11: 

FBM Image, Sun Rasterfile, CMU WM Raster, Portable Bit Map (PBM, PGM,
PPM), Faces Project, GIF Image, JFIF style jpeg Image, Utah RLE Image,
Windows, OS/2 RLE Image, Photograph on CD Image, X Window Dump, Targa 
Image, McIDAS areafile, G3 FAX Image, PC Paintbrush Image, GEM Bit Image,
MacPaint Image, X Pixmap (.xpm), XBitmap

%prep
%setup -q -c -n %{name}-%{version}

%build
make -f Makefile.std

for i in xli xlito; do cp -f $i.man $i.1; done
cp -f xliguide.man xliguide.5

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/X11/app-defaults/
make install SYSPATHFILE=%{buildroot}%{_sysconfdir}/X11/app-defaults/Xli BINDIR=%{buildroot}%{_bindir}

for i in *.1;do install -m644 $i -D %{buildroot}%{_mandir}/man1/$i;done
install -m644 xliguide.5 -D %{buildroot}%{_mandir}/man5/xliguide.5

ln -sf xli %{buildroot}%{_bindir}/xsetbg
ln -sf xli %{buildroot}%{_bindir}/xview 
ln -sf xli %{buildroot}%{_bindir}/xloadimage

# quick fix for doc permissions
chmod 644 README*

%files
%doc chkgamma.jpg README* ABOUTGAMMA
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/X11/app-defaults/*
%{_mandir}/man[15]/*
