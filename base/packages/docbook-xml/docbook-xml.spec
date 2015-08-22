%global version_list {4.5-xml 4.4-xml 4.3-xml 4.2-xml 4.1.2-xml}

Name:		docbook-xml		
Version:	4.5
Release:	1%{?dist}
Summary:	A widely used XML scheme for writing documentation and help

Group:		Applications/Text
License:	Copyright only
URL:		http://www.oasis-open.org/docbook/

Source0:	http://www.docbook.org/xml/%{version}/%{name}-%{version}.zip
Source1:	http://www.docbook.org/xml/4.4/%{name}-4.4.zip
Source2:	http://www.docbook.org/xml/4.3/%{name}-4.3.zip
Source3:	http://www.docbook.org/xml/4.2/%{name}-4.2.zip
Source4:	http://www.docbook.org/xml/4.1.2/docbkx412.zip

BuildRequires:	libxml2	

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This syntax is XML-compliant and is developed by the OASIS consortium.
This package contains XML versions of the DocBook DTD.


%prep
rm -rf %{buildroot}
%setup -c -T
eval mkdir %{version_list}

# DocBook XML V4.1.2
cd 4.1.2-xml
unzip %{SOURCE4}
mkdir -p %{buildroot}/usr/share/xml/docbook/xml-dtd-4.1.2-xml
cp -af docbook.cat *.dtd ent/ *.mod %{buildroot}/usr/share/xml/docbook/xml-dtd-4.1.2-xml/
cd ..

# DocBook XML V4.2
cd 4.2-xml
unzip %{SOURCE3}
mkdir -p %{buildroot}/usr/share/xml/docbook/xml-dtd-4.2-xml
cp -af docbook.cat *.dtd ent/ *.mod %{buildroot}/usr/share/xml/docbook/xml-dtd-4.2-xml/
cd ..

# DocBook XML V4.3
cd 4.3-xml
unzip %{SOURCE2}
mkdir -p %{buildroot}/usr/share/xml/docbook/xml-dtd-4.3-xml
cp -af docbook.cat *.dtd ent/ *.mod %{buildroot}/usr/share/xml/docbook/xml-dtd-4.3-xml/
cd ..

# DocBook XML V4.4
cd 4.4-xml
unzip %{SOURCE1}
mkdir -p %{buildroot}/usr/share/xml/docbook/xml-dtd-4.4-xml
cp -af docbook.cat *.dtd ent/ *.mod %{buildroot}/usr/share/xml/docbook/xml-dtd-4.4-xml/
cd ..

# DocBook XML v4.5
cd 4.5-xml
unzip %{SOURCE0}
mkdir -p %{buildroot}/usr/share/xml/docbook/xml-dtd-4.5-xml
cp -af docbook.cat *.dtd ent/ *.mod %{buildroot}/usr/share/xml/docbook/xml-dtd-4.5-xml/
cd ..

# fix of \r\n issue from rpmlint
sed -i 's/\r//' */*.txt

if [ `id -u` -eq 0 ]; then
  chown -R root:root .
  chmod -R a+rX,g-w,o-w .
fi

%build
#nothing here

%install

chmod 755 %{buildroot}/usr/share/xml/docbook/xml-dtd-*/ent
mkdir -p %{buildroot}/etc/xml
export XML_CATALOG_FILES=""
xmlcatalog --noout --create %{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add \
	"public" \
	"-//OASIS//DTD DocBook XML V4.1.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook XML CALS Table Model V4.1.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/calstblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook XML CALS Table Model V4.1.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/calstblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/soextblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook XML Information Pool V4.1.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/dbpoolx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.1.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/dbhierx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook XML Additional General Entities V4.1.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/dbgenent.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook XML Notations V4.1.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/dbnotnx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook XML Character Entities V4.1.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.1.2/dbcentx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteSystem" \
	"http://www.oasis-open.org/docbook/xml/4.1.2" \
	"file:///usr/share/xml/docbook/xml-dtd-4.1.2" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteURI" \
	"http://www.oasis-open.org/docbook/xml/4.1.2" \
	"file:///usr/share/xml/docbook/xml-dtd-4.1.2" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook XML V4.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook CALS Table Model V4.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.2/calstblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
	"http://www.oasis-open.org/docbook/xml/4.2/soextblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook Information Pool V4.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.2/dbpoolx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook Document Hierarchy V4.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.2/dbhierx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Additional General Entities V4.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.2/dbgenent.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Notations V4.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.2/dbnotnx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Character Entities V4.2//EN" \
	"http://www.oasis-open.org/docbook/xml/4.2/dbcentx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteSystem" \
	"http://www.oasis-open.org/docbook/xml/4.2" \
	"file:///usr/share/xml/docbook/xml-dtd-4.2" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteURI" \
	"http://www.oasis-open.org/docbook/xml/4.2" \
	"file:///usr/share/xml/docbook/xml-dtd-4.2" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook XML V4.3//EN" \
	"http://www.oasis-open.org/docbook/xml/4.3/docbookx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook CALS Table Model V4.3//EN" \
	"http://www.oasis-open.org/docbook/xml/4.3/calstblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
	"http://www.oasis-open.org/docbook/xml/4.3/soextblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook Information Pool V4.3//EN" \
	"http://www.oasis-open.org/docbook/xml/4.3/dbpoolx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook Document Hierarchy V4.3//EN" \
	"http://www.oasis-open.org/docbook/xml/4.3/dbhierx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Additional General Entities V4.3//EN" \
	"http://www.oasis-open.org/docbook/xml/4.3/dbgenent.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Notations V4.3//EN" \
	"http://www.oasis-open.org/docbook/xml/4.3/dbnotnx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Character Entities V4.3//EN" \
	"http://www.oasis-open.org/docbook/xml/4.3/dbcentx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteSystem" \
	"http://www.oasis-open.org/docbook/xml/4.3" \
	"file:///usr/share/xml/docbook/xml-dtd-4.3" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteURI" \
	"http://www.oasis-open.org/docbook/xml/4.3" \
	"file:///usr/share/xml/docbook/xml-dtd-4.3" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook XML V4.4//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/docbookx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook CALS Table Model V4.4//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/calstblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook XML HTML Tables V4.4//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/htmltblx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/soextblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook Information Pool V4.4//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/dbpoolx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook Document Hierarchy V4.4//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/dbhierx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Additional General Entities V4.4//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/dbgenent.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Notations V4.4//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/dbnotnx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook Character Entities V4.4//EN" \
	"http://www.oasis-open.org/docbook/xml/4.4/dbcentx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteSystem" \
	"http://www.oasis-open.org/docbook/xml/4.4" \
	"file:///usr/share/xml/docbook/xml-dtd-4.4" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteURI" \
	"http://www.oasis-open.org/docbook/xml/4.4" \
	"file:///usr/share/xml/docbook/xml-dtd-4.4" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook XML V4.5//EN" \
	"http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD DocBook XML CALS Table Model V4.5//EN" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5/calstblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5/soextblx.dtd" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook XML Information Pool V4.5//EN" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5/dbpoolx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.5//EN" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5/dbhierx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ELEMENTS DocBook XML HTML Tables V4.5//EN" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5/htmltblx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook XML Notations V4.5//EN" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5/dbnotnx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook XML Character Entities V4.5//EN" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5/dbcentx.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "public" \
	"-//OASIS//ENTITIES DocBook XML Additional General Entities V4.5//EN" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5/dbgenent.mod" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteSystem" \
	"http://www.oasis-open.org/docbook/xml/4.5" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5" \
	%{buildroot}/etc/xml/docbook-xml
xmlcatalog --noout --add "rewriteURI" \
	"http://www.oasis-open.org/docbook/xml/4.5" \
	"file:///usr/share/xml/docbook/xml-dtd-4.5" \
	%{buildroot}/etc/xml/docbook-xml
unset XML_CATALOG_FILES

%files
/etc/xml/docbook-xml
%dir /etc/xml/
%{_datadir}/xml/docbook/*
%dir %{_datadir}/xml/
%dir %{_datadir}/xml/docbook/

%changelog

