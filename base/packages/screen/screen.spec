%bcond_with multiuser
%global _hardened_build 1

Summary:        A screen manager that supports multiple logins on one terminal
Name:           screen
Version:        4.3.1
Release:        1%{?dist}
License:        GPLv2+
Group:          Applications/System
URL:            http://www.gnu.org/software/screen

BuildRequires:  ncurses-devel autoconf texinfo automake
#BuildRequires:  pam-devel libutempter-devel

Source0:        ftp://ftp.gnu.org/gnu/screen/screen-%{version}.tar.gz
#Source1:        screen.pam

#Patch1:         screen-4.3.1-screenrc.patch

%description
The screen utility allows you to have multiple logins on just one
terminal. Screen is useful for users who telnet into a machine or are
connected via a dumb terminal, but want to use more than just one
login.

Install the screen package if you need a screen manager that can
support multiple logins on one terminal.


%prep
%setup -q -n %{name}-%{version}
#%patch1 -p1 -b .screenrc


%build
./autogen.sh

./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--enable-colors256 \
	--enable-rxvt_osc \
	--enable-use-locale \
	--enable-telnet \
	--with-pty-mode=0620 \
	--with-pty-group=$(getent group tty | cut -d : -f 3) \
	--with-sys-screenrc="/etc/screenrc" \
	--with-socket-dir="/var/run/screen"

# fails with %{?_smp_mflags}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc
install -m 0644 etc/etcscreenrc $RPM_BUILD_ROOT/etc/screenrc
cat etc/screenrc >> $RPM_BUILD_ROOT/etc/screenrc

# Better not forget to copy the pam file around
#mkdir -p $RPM_BUILD_ROOT/etc/pam.d
#install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/screen

# Create the socket dir
mkdir -p $RPM_BUILD_ROOT/var/run/screen

# Remove files from the buildroot which we don't want packaged
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc README doc/FAQ doc/README.DOTSCREEN ChangeLog
#%license COPYING
#%{_mandir}/man1/screen.*
#%{_infodir}/screen.info*
#%{_datadir}/screen
%config(noreplace) /etc/screenrc
#%config(noreplace) /etc/pam.d/screen
#%{_tmpfilesdir}/screen.conf
%{_bindir}/*
%dir /var/run/screen

%changelog
