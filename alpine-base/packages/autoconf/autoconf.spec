Name:		autoconf		
Version:	2.69		
Release:	1%{?dist}
Summary:	A GNU tool for automatically configuring source code

Group:		Development/Tools
License:	GPLv2+ and GFDL
URL:		http://www.gnu.org/software/autoconf/
Source0:	http://gnu.mirror.vexxhost.com/%{name}/%{name}-%{version}.tar.xz

#BuildRequires:	
#Requires:	

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to
specify various configuration options.

You should install Autoconf if you are developing software and
would like to create shell scripts that configure your source code
packages. If you are installing Autoconf, you will also need to
install the GNU m4 package.

Note that the Autoconf package is not required for the end-user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not
their use.

%prep
%setup -q


%build
export M4=/usr/bin/m4 
./configure \
	--build=%{_build} \
	--host=%{_host} \
	--prefix=/usr
										%make

%install
%make_install
%__rm -f %{buildroot}/usr/share/info/dir
%__rm -f %{buildroot}/usr/share/info/standards.info

%files
%{_bindir}/*
%{_infodir}/autoconf.info*
%{_datadir}/autoconf/
%{_mandir}/man1/*
%doc AUTHORS COPYING* ChangeLog NEWS README THANKS TODO


%changelog
