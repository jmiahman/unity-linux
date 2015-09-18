Summary: A perfect hash function generator
Name: gperf
Version: 3.0.4
Release: 1%{?dist}
License: GPLv3+
Source: ftp://ftp.gnu.org/pub/gnu/gperf/gperf-%{version}.tar.gz
Group: Development/Tools
URL: http://www.gnu.org/software/gperf/
Requires(post): texinfo
Requires(preun): texinfo

%description
Gperf is a perfect hash function generator written in C++. Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

%prep
%setup -q

%build
./configure \
	--prefix=/usr

make

%install
rm -rf $RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT/usr/share/{man,info}

make DESTDIR=$RPM_BUILD_ROOT install

# remove the stuff from the buildroot
rm -rf $RPM_BUILD_ROOT{%{_mandir}/{dvi,html},%{_datadir}/doc}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/gperf.info.gz %{_infodir}/dir >/dev/null 2>&1 || :
exit 0

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/gperf.info.gz %{_infodir}/dir >/dev/null 2>&1|| :
fi
exit 0

%files
%defattr(-,root,root)
%doc README NEWS doc/*.{html,pdf} COPYING
%{_bindir}/%{name}
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*

%changelog
