%global multilib_arches %{ix86} ppc ppc64 ppc64p7 s390 s390x x86_64

Name:		libffi	
Version:	3.2.1
Release:	1%{?dist}
Summary:	A portable foreign function interface library

Group:		System Environment/Libraries
License:	BSD
URL:		http://sourceware.org/libffi
Source0:	ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz
Source1:	ffi-multilib.h
Source2:	ffitarget-multilib.h

Patch0:		gnu-linux-define.patch
Patch1:         libffi-3.1-fix-include-path.patch

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
%patch0 -p1 -b .gnu-linux-define
%patch1 -p1 -b .fix-include-path

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

mkdir -p $RPM_BUILD_ROOT%{_includedir}
%ifarch %{multilib_arches}
# Do header file switcheroo to avoid file conflicts on systems where you
# can have both a 32- and 64-bit version of the library, and they each need
# their own correct-but-different versions of the headers to be usable.
for i in ffi ffitarget; do
  mv $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}/include/$i.h $RPM_BUILD_ROOT%{_includedir}/$i-%{_arch}.h
done

install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/ffi.h
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/ffitarget.h
%else
mv $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}/include/{ffi,ffitarget}.h $RPM_BUILD_ROOT%{_includedir}
%endif
rm -rf $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}

%files
%{_libdir}/libffi.so.6.0.4
%{_libdir}/libffi.so.6


%files devel
%{_libdir}/pkgconfig/*.pc
/usr/include/ffi*.h
%{_libdir}/*.so

%changelog
