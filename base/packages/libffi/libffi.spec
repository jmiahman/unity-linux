Name:		libffi	
Version:	3.2.1
Release:	1%{?dist}
Summary:	A portable foreign function interface library

Group:		System Environment/Libraries
License:	BSD
URL:		http://sourceware.org/libffi
Source0:	ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz

Patch0:		gnu-linux-define.patch

BuildRequires: texinfo

%description
Compilers for high level languages generate code that follow certain
conventions.  These conventions are necessary, in part, for separate
compilation to work.  One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function.  A
calling convention also specifies where the return value for a function
is found.  

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function.  `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface.  A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language.  The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface.  A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.  

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:       pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch -p1 -b .gnu-linux-define

%build
./configure \
	--prefix=/usr \
	--enable-pax_emutramp

make %{?_smp_mflags}


%install
%__rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/*.la
install -m755 -d "%{buildroot}/usr/share/licenses/%{name}"
install -m644 LICENSE "%{buildroot}/usr/share/licenses/%{name}/"

mkdir %{buildroot}/usr/include/
mv %{buildroot}/usr/lib/libffi-3.2.1/include/*.h %{buildroot}/usr/include/ 

%files
%{_libdir}/libffi.so.6.0.4
%{_libdir}/libffi.so.6


%files devel
%{_libdir}/pkgconfig/*.pc
/usr/include/ffi*.h
%{_libdir}/*.so

%changelog
