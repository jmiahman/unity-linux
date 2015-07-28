Name:		sed	
Version:	4.2.2
Release:	1%{?dist}
Summary:	A GNU stream text editor

Group:		Applications/Text
License:	GPLv3+
URL:		http://sed.sourceforge.net/
Source0:	ftp://ftp.gnu.org/pub/gnu/sed/sed-%{version}.tar.bz2

#BuildRequires:	
#Requires:	

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.


%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--bindir=/bin \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--disable-i18n \
	--disable-nls

make

%install
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}/usr/lib/charset.alias

%postun
exec /bin/busybox --install -s

%files
/bin/sed

%changelog
