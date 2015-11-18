%define _target_platform %{_arch}-unity-linux-musl

Name:		gdb	
Version:	7.9.1
Release:	1%{?dist}
Summary:	A GNU source-level debugger for C, C++, Fortran, Go and other languages

Group:		Development/Debuggers
License:	GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and BSD and Public Domain and GFDL
URL:		http://sources.redhat.com/gdb/	
Source0:	ftp://sourceware.org/pub/gdb/releases/%{name}-%{version}.tar.xz

Patch0:		gdb-linux_nat.patch

BuildRequires:	ncurses-devel expat-devel texinfo readline-devel python-devel
BuildRequires:  autoconf automake libtool linux-headers

%description
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.


%prep
%setup -q
%patch0 -p1

%build
	local _config="
		--build=%{_target_platform}
		--host=%{_target_platform}
		--prefix=/usr
		--target=%{_target_platform}
		--with-build-sysroot=%{buildroot}
		--disable-nls
		--disable-werror
		--mandir=/usr/share/man
		--infodir=/usr/share/info
		--with-system-readline
		--disable-gdbserver"

	./configure $_config
	(cd opcodes && ./configure $_config)

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/usr/share/info/dir
# those are provided by binutils
rm -rf %{buildroot}/usr/include
rm -rf %{buildroot}/usr/lib
install -d %{buildroot}%{_datadir}/gdb/auto-load/usr/lib

%files
#%doc
%{_bindir}/*
%{_datadir}/gdb/system-gdbinit/wrs-linux.py
%{_datadir}/gdb/system-gdbinit/elinos.py
%{_datadir}/gdb/python/gdb/frames.py
%{_datadir}/gdb/python/gdb/__init__.py
%{_datadir}/gdb/python/gdb/types.py
%{_datadir}/gdb/python/gdb/FrameIterator.py
%{_datadir}/gdb/python/gdb/xmethod.py
%{_datadir}/gdb/python/gdb/prompt.py
%{_datadir}/gdb/python/gdb/function/strfns.py
%{_datadir}/gdb/python/gdb/function/__init__.py
%{_datadir}/gdb/python/gdb/function/caller_is.py
%{_datadir}/gdb/python/gdb/printer/__init__.py
%{_datadir}/gdb/python/gdb/printer/bound_registers.py
%{_datadir}/gdb/python/gdb/command/type_printers.py
%{_datadir}/gdb/python/gdb/command/__init__.py
%{_datadir}/gdb/python/gdb/command/xmethods.py
%{_datadir}/gdb/python/gdb/command/explore.py
%{_datadir}/gdb/python/gdb/command/prompt.py
%{_datadir}/gdb/python/gdb/command/pretty_printers.py
%{_datadir}/gdb/python/gdb/command/frame_filters.py
%{_datadir}/gdb/python/gdb/printing.py
%{_datadir}/gdb/python/gdb/FrameDecorator.py
%{_datadir}/gdb/syscalls/sparc64-linux.xml
%{_datadir}/gdb/syscalls/sparc-linux.xml
%{_datadir}/gdb/syscalls/mips-n32-linux.xml
%{_datadir}/gdb/syscalls/mips-n64-linux.xml
%{_datadir}/gdb/syscalls/s390x-linux.xml
%{_datadir}/gdb/syscalls/mips-o32-linux.xml
%{_datadir}/gdb/syscalls/arm-linux.xml
%{_datadir}/gdb/syscalls/ppc-linux.xml
%{_datadir}/gdb/syscalls/gdb-syscalls.dtd
%{_datadir}/gdb/syscalls/s390-linux.xml
%{_datadir}/gdb/syscalls/amd64-linux.xml
%{_datadir}/gdb/syscalls/ppc64-linux.xml
%{_datadir}/gdb/syscalls/i386-linux.xml

%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/python
%dir %{_datadir}/gdb/python/gdb
%dir %{_datadir}/gdb/python/gdb/command
%dir %{_datadir}/gdb/python/gdb/function
%dir %{_datadir}/gdb/python/gdb/printer
%dir %{_datadir}/gdb/syscalls
%dir %{_datadir}/gdb/system-gdbinit
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load/usr
%dir %{_datadir}/gdb/auto-load/usr/lib

%changelog

