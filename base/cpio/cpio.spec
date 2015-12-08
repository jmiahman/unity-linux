Summary:	GNU cpio archiving program
Name:		cpio
Version:	2.11
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	http://ftp.gnu.org/gnu/cpio/%{name}-%{version}.tar.bz2
# Source0-md5:	20fc912915c629e809f80b96b2e75d7d
#Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	027552f4053477462a09fadc162a5e65
Patch0:		%{name}-info.patch
Patch1:		%{name}-ifdef.patch
Patch2:		%{name}-crc-is-32-bit.patch
Patch3:		%{name}-stdio.in.patch
URL:		http://www.gnu.org/software/cpio/
BuildRequires:	autoconf
BuildRequires:	automake 
#BuildRequires:	gettext-tools
#BuildRequires:	texinfo

%define		_bindir		/bin

%description
GNU cpio copies files into or out of a cpio or tar archive. Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions. The archive can be another file on the disk, a magnetic
tape, or a pipe. GNU cpio supports the following archive formats:
binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old
tar and POSIX.1 tar. By default, cpio creates binary format archives,
so that they are compatible with older cpio programs. When it is
extracting files from archives, cpio automatically recognizes which
kind of archive it is reading and can read archives created on
machines with a different byte-order.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
aclocal -I m4 -I am
autoconf
autoheader
automake --add-missing
%configure \
	--disable-silent-rules

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

#%post	-p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

#%postun	-p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

%files  
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/cpio
#%lang(es) %{_mandir}/es/man1/cpio.1*
#%lang(hu) %{_mandir}/hu/man1/cpio.1*
#%lang(ja) %{_mandir}/ja/man1/cpio.1*
#%lang(pt_BR) %{_mandir}/pt_BR/man1/cpio.1*
#%{_infodir}/cpio.info*
