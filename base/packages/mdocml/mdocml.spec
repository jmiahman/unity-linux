Name:		mdocml
Version:	1.13.3
Release:	1%{?dist}
Summary:	A mdoc/man compiler
Group:		System Environment/Base
License:	BSD
URL:		http://mdocml.bsd.lv/
Source0:	http://download.openpkg.org/components/cache/mdocml/mdocml-1.13.3.tar.gz
Source1:	man.conf

Patch0:		shared-libmandoc.patch
patch1:		default-pager.patch

BuildRequires:	sqlite

%description
%{name} is an ISC licensed utility for formatting man pages, specifically those written 
in the mdoc macro language. Unlike the groff and older troff and nroff tools 
predominantly used for this purpose, mandoc focuses specifically on manuals and 
is not suitable for general-purpose type-setting.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	docs
Summary:	Documentation for mdoc/man compiler
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	docs
The %{name}-docs package contains man pages and examples for
developing applications that use %{name}.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build

cat >configure.local<<EOF
PREFIX=/usr
MANDIR=/usr/share/man
LIBDIR=/usr/lib
CFLAGS="$CFLAGS"
EOF

%configure
make

%install
make -j1 DESTDIR=%{buildroot} base-install db-install

install -Dm644 %{SOURCE1} %{buildroot}/etc/man.conf

mkdir -p %{buildroot}/%{_datadir}/man/man4/

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_sbindir}/*
%{_bindir}/*
%{_libdir}/libmandoc.so
%dir %{_datadir}/examples/
%dir %{_datadir}/examples/mandoc/
%{_datadir}/examples/mandoc/example.style.css
/etc/man.conf

%files docs
%{_datadir}/man/man1/*.1
%{_datadir}/man/man5/mandoc.db.5
%{_datadir}/man/man3/*.3
%{_datadir}/man/man8/makewhatis.8
%{_datadir}/man/man7/*.7

%dir %{_datadir}/man/man1
%dir %{_datadir}/man/man3
%dir %{_datadir}/man/man4
%dir %{_datadir}/man/man5
%dir %{_datadir}/man/man7
%dir %{_datadir}/man/man8

%files devel
%dir /usr/include/mandoc/
/usr/include/mandoc/*.h

%changelog
