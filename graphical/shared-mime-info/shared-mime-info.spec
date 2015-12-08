# Conditional build:
%bcond_without	tests		# build without tests
%bcond_with	doc		# build documentation

Summary:	Shared MIME-info specification
Name:		shared-mime-info
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://people.freedesktop.org/~hadess/%{name}-%{version}.tar.xz
URL:		http://www.freedesktop.org/wiki/Software/shared-mime-info
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.9
BuildRequires:	docbook-xml
BuildRequires:	gettext
BuildRequires:	glib-devel >= 2.18.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libxml2-devel >= 2.6.26
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 1.446
BuildRequires:	tar >= 1.22
BuildRequires:	xz
Requires:	glib >= 2.18.0

%description
This is the freedesktop.org shared MIME info database.

Many programs and desktops use the MIME system to represent the types
of files. Frequently, it is necessary to work out the correct MIME
type for a file. This is generally done by examining the file's name
or contents, and looking up the correct MIME type in a database.

For interoperability, it is useful for different programs to use the
same database so that different programs agree on the type of a file,
and new rules for determining the type apply to all programs.

This specification attempts to unify the type-guessing systems
currently in use by GNOME, KDE and ROX. Only the name-to-type and
contents-to-type mappings are covered by this spec; other MIME type
information, such as the default handler for a particular type, or the
icon to use to display it in a file manager, are not covered since
these are a matter of style.

In addition, freedesktop.org provides a shared database in this format
to avoid inconsistencies between desktops. This database has been
created by converting the existing KDE and GNOME databases to the new
format and merging them together.

%package doc
Summary:	Shared MIME-info Database specification
Group:		Documentation

%description doc
Shared MIME-info Database specification

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-default-make-check \
	--disable-update-mimedb
%{__make} -j1

%{?with_tests:%{__make} check}

%{?with_doc:db2html shared-mime-info-spec.xml}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove bogus translation files
# translations are already in the xml file installed
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}

# convience symlink
%{?with_doc:ln -s t1.html shared-mime-info-spec/index.html}

# ghost generated files
# see update-mime-database.c const char *media_types
install -d $RPM_BUILD_ROOT%{_datadir}/mime/application
install -d $RPM_BUILD_ROOT%{_datadir}/mime/audio
install -d $RPM_BUILD_ROOT%{_datadir}/mime/image
install -d $RPM_BUILD_ROOT%{_datadir}/mime/inode
install -d $RPM_BUILD_ROOT%{_datadir}/mime/message
install -d $RPM_BUILD_ROOT%{_datadir}/mime/model
install -d $RPM_BUILD_ROOT%{_datadir}/mime/multipart
install -d $RPM_BUILD_ROOT%{_datadir}/mime/text
install -d $RPM_BUILD_ROOT%{_datadir}/mime/video
install -d $RPM_BUILD_ROOT%{_datadir}/mime/x-content
install -d $RPM_BUILD_ROOT%{_datadir}/mime/x-epoc
# see specification, also grep -F .new update-mime-database.c
touch $RPM_BUILD_ROOT%{_datadir}/mime/globs
touch $RPM_BUILD_ROOT%{_datadir}/mime/globs2
touch $RPM_BUILD_ROOT%{_datadir}/mime/magic
touch $RPM_BUILD_ROOT%{_datadir}/mime/XMLnamespaces
touch $RPM_BUILD_ROOT%{_datadir}/mime/subclasses
touch $RPM_BUILD_ROOT%{_datadir}/mime/aliases
touch $RPM_BUILD_ROOT%{_datadir}/mime/types
touch $RPM_BUILD_ROOT%{_datadir}/mime/generic-icons
touch $RPM_BUILD_ROOT%{_datadir}/mime/icons
touch $RPM_BUILD_ROOT%{_datadir}/mime/treemagic
touch $RPM_BUILD_ROOT%{_datadir}/mime/mime.cache

install -d %{buildroot}%{_libdir}/pkgconfig/
mv %{buildroot}%{_datadir}/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%post
#%update_mime_database

%preun
# remove dirs and files created by update-mime-database
if [ "$1" = "0" ]; then
	%{__rm} -rf %{_datadir}/mime/*
fi

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog
%attr(755,root,root) %{_bindir}/update-mime-database
%dir %{_datadir}/mime
%dir %{_datadir}/mime/packages
%{_datadir}/mime/packages/freedesktop.org.xml
%{_mandir}/man1/update-mime-database.1*
%{_libdir}/pkgconfig/shared-mime-info.pc

# generated content
%dir %{_datadir}/mime/application
%dir %{_datadir}/mime/audio
%dir %{_datadir}/mime/image
%dir %{_datadir}/mime/inode
%dir %{_datadir}/mime/message
%dir %{_datadir}/mime/model
%dir %{_datadir}/mime/multipart
%dir %{_datadir}/mime/text
%dir %{_datadir}/mime/video
%dir %{_datadir}/mime/x-content
%dir %{_datadir}/mime/x-epoc
%{_datadir}/mime/globs
%{_datadir}/mime/globs2
%{_datadir}/mime/magic
%{_datadir}/mime/XMLnamespaces
%{_datadir}/mime/subclasses
%{_datadir}/mime/aliases
%{_datadir}/mime/types
%{_datadir}/mime/generic-icons
%{_datadir}/mime/icons
%{_datadir}/mime/treemagic
%{_datadir}/mime/mime.cache

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc shared-mime-info-spec/*
%endif

%changelog
