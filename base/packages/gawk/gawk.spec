Name:		gawk	
Version:	4.1.3
Release:	1%{?dist}
Summary:	The GNU version of the awk text processing utility

Group:		Applications/Text
License:	GPLv3+ and GPL and LGPLv3+ and LGPL and BSD
URL:		http://www.gnu.org/software/gawk/gawk.html		
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz	

#BuildRequires:	
#Requires:	
Provides: /bin/awk
Provides: /bin/gawk

%description
The gawk package contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs.

Install the gawk package if you need a text processing utility. Gawk is
considered to be a standard Linux tool for processing text.

%prep
%setup -q


%build

./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-nls

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

%postun
exec /bin/busybox --install -s

%files
%{_bindir}/*awk
%{_infodir}/gawk.info*
%{_infodir}/gawkinet.info*
%{_libexecdir}/awk
%{_datadir}/awk
%{_includedir}/gawkapi.h
%{_libdir}/gawk

%changelog
