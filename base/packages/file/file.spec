Name:		file	
Version:	5.24
Release:	1%{?dist}
Summary:	File type identification utility

Group: 		Applications/File
License:	BSD
URL:		http://www.darwinsys.com/file/
Source0:	http://fossies.org/linux/misc/%{name}-%{version}.tar.gz

#BuildRequires:	
#Requires:	

%description
The file command is used to identify a particular file according to the
type of data contained by the file.  File can identify many different
file types, including ELF binaries, system libraries, RPM packages, and
different graphics formats.

%package        devel                                                   
Summary:        Development files for %{name}                           
Group:          Development/Libraries                                   
Requires:       %{name} = %{version}-%{release}                         
Requires:       pkgconfig                                               
                                                                        
%description    devel                                                   
The %{name}-devel package contains libraries and header files for       
developing applications that use %{name}. 

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--datadir=/usr/share \


make %{?_smp_mflags}
make tests

%install
%make_install
rm %{buildroot}/usr/lib/*.la

%files
/usr/bin/file
/usr/lib/libmagic.so.1.0.0
/usr/lib/libmagic.so.1
%dir /usr/share/misc/
/usr/share/misc/magic.mgc

%files devel
%{_includedir}/*.h
%{_libdir}/libmagic.so

%changelog
