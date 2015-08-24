
Name:		docbook-xsl
Version:	1.78.1
Release:	1%{?dist}
Summary:	Norman Walsh's XSL stylesheets for DocBook XML	

Group:		Applications/Text
License:	Copyright only
URL:		http://www.oasis-open.org/docbook/

Source0:	http://downloads.sourceforge.net/sourceforge/docbook/%{name}-%{version}.tar.bz2	

BuildRequires:	libxml2 docbook-xml libxslt

%description
These XSL stylesheets allow you to transform any DocBook XML document to
other formats, such as HTML, FO, and XHMTL.  They are highly customizable.

%prep
rm -rf %{buildroot}
%setup -q

%build
#nothing here

%install

local _dest dir f
_dest=%{buildroot}/usr/share/xml/docbook/xsl-stylesheets-%{version}

install -dm755 "$_dest"
install -m644 VERSION VERSION.xsl "$_dest"/

for dir in assembly common eclipse epub epub3 fo highlighting html \
	htmlhelp javahelp lib manpages params profiling roundtrip \
	template website xhtml xhtml-1_1 xhtml5; do

	install -dm755 $_dest/$dir
	for f in $dir/*.xml $dir/*.xsl $dir/*.dtd $dir/*.ent; do
		[ -e "$f" ] || continue
		install -m644 $f $_dest/$dir
	done
done

install -dm755 %{buildroot}/etc/xml

install -m644 -D COPYING \
	%{buildroot}/usr/share/licenses/%{name}/COPYING

%files
/etc/xml/
%{_datadir}/xml/docbook/*

%changelog

