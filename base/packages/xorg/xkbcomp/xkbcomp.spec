Summary:    xkbcomp - compile XKB keyboard description
Name:       xkbcomp
Version:    1.1.1
Release:    1%{?dist}
License:    MIT
Group:      User Interface/X
URL:        http://www.x.org

Source0:    http://www.x.org/pub/individual/app/xkbcomp-%{version}.tar.bz2

BuildRequires:  libx11-devel libxkbfile-devel

%description
The xkbcomp keymap compiler converts a description 
of an XKB keymap into one of several output formats.

%package docs
Summary:  Doc files for xkbcomp
Requires: %{name} = %{version}

%description docs
Documentation files for the xkbcomp keymap compiler

%prep
%setup -q 

%build

%configure

make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/xkbcomp

%files docs
%{_mandir}/man1/xkbcomp.1*
