Name:           make
Version:        4.1 
Release:        1%{?dist}
Summary:        A GNU tool which simplifies the build process for users

Group:          Development/Tools
License:        GPLv3+
URL:            http://www.gnu.org/software/make/
Source0:        ftp://ftp.gnu.org/gnu/make/make-%{version}.tar.bz2
Patch0:		fix-atexit-exit.patch

#BuildRequires:  
#Requires:       

%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files. Make
allows users to build and install packages without any significant
knowledge about the details of the build process. The details about
how the program should be built are provided for make in the program's
makefile.

%package devel
Summary: Header file for externally visible definitions
Group: Development/Libraries

%description devel
The make-devel package contains gnumake.h.



%prep
%setup -q
%patch -p1 -b .fix-atexit-exit

%build
./configure \
	--build=x86_64-alpine-linux-musl \
	--host=x86_64-alpine-linux-musl \
	--prefix=/usr \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-nls \
make
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%doc NEWS README COPYING AUTHORS
%{_bindir}/*
#%{_mandir}/man*/*
#%{_infodir}/*.info*
%{_includedir}/gnumake.h

%files devel
%defattr(-,root,root)
%{_includedir}/gnumake.h

%changelog
