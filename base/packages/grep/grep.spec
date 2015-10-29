%define _target_platform %{_arch}-unity-linux-musl

%define _sysconfdir /etc

Summary: Pattern matching utilities
Name: grep
Version: 2.21
Release: 1%{?dist}
License: GPLv3+
URL: http://www.gnu.org/software/grep/
Group: Applications/Text

Source: ftp://ftp.gnu.org/pub/gnu/grep/grep-%{version}.tar.xz
Source1: colorgrep.sh
Source2: colorgrep.csh
Source3: GREP_COLORS
Source4: grepconf.sh
# upstream ticket 39444
Patch0: grep-2.21-man-fix-gs.patch
# upstream ticket 39445
Patch1: grep-2.21-help-align.patch
# fix buffer overrun for grep -F, rhbz#1183653
Patch2: grep-2.21-buf-overrun-fix.patch
# backported from upstream
# http://git.savannah.gnu.org/cgit/grep.git/commit/?id=c8b9364d5900a40809827aee6cc53705073278f6
Patch3: grep-2.21-recurse-behaviour-change-doc.patch
# http://www.mail-archive.com/bug-gnulib%40gnu.org/msg31638.html
Patch4: grep-2.21-gnulib.patch
Requires(post): install-info
Requires(preun): install-info

BuildRequires: pcre-devel texinfo gettext
BuildRequires: autoconf automake texinfo
Requires: pcre

%description
The GNU versions of commonly used grep utilities. Grep searches through
textual input for lines which contain a match to a specified pattern and then
prints the matching lines. GNU's grep utilities include grep, egrep and fgrep.

GNU grep is needed by many scripts, so it shall be installed on every system.

%prep
%setup -q
#%patch0 -p1 -b .man-fix-gs
#%patch1 -p1 -b .help-align
#%patch2 -p1 -b .buf-overrun-fix
#%patch3 -p1 -b .recurse-behaviour-change-doc
#%patch4 -p1 -b .gnulib

#chmod 755 tests/kwset-abuse

%build
%global BUILD_FLAGS $RPM_OPT_FLAGS

# Currently gcc on ppc uses double-double arithmetic for long double and it
# does not conform to the IEEE floating-point standard. Thus force
# long double to be double and conformant.
%ifarch ppc ppc64
%global BUILD_FLAGS %{BUILD_FLAGS} -mlong-double-64
%endif

./configure \
	--build=%_target_platform \
	--host=%_target_platform \
	--prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-nls \

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install
gzip $RPM_BUILD_ROOT%{_infodir}/grep*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}
install -Dpm 755 %{SOURCE4} $RPM_BUILD_ROOT%{_libexecdir}/grepconf.sh

#Create symlink to overright any existing symlink ie. busybox
mkdir %{buildroot}/bin
cd %{buildroot}/bin
ln -s ../usr/bin/grep grep

#%check
#make check

%post
/usr/bin/install-info --quiet --info-dir=%{_infodir} %{_infodir}/grep.info.gz || :

%preun
if [ $1 = 0 ]; then
/usr/bin/install-info --quiet --info-dir=%{_infodir} --delete %{_infodir}/grep.info.gz || :
fi

%files 
#%doc AUTHORS THANKS TODO NEWS README
#%{!?_licensedir:%global license %%doc}
#%license COPYING
/bin/*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/profile.d/colorgrep.*sh
%config(noreplace) %{_sysconfdir}/GREP_COLORS
%{_datadir}/info/*.info*.gz
#%{_mandir}/*/*
%{_libexecdir}/grepconf.sh

%changelog
