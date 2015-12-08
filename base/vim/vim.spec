%define _target_platform %{_arch}-unity-linux-musl
%define _sysconfdir /etc

Summary: An advanced text editor
Name: vim
Version: 7.4
Release: 1%{?dist}
License: BSD
Group: Applications/Editors
BuildRequires: gcc-c++ ncurses-devel
Requires: ncurses
URL: http://www.vim.org
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2
Source1: vimrc 
Source2: rpmspec-template

%description
Vim is an advanced text editor that seeks to provide the power of the de-facto Unix editor 'Vi', with a more complete feature set.

%prep
%setup -q -n vim74

%build
echo '#define SYS_VIMRC_FILE "/etc/vim/vimrc"' >> src/feature.h
./configure \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--target=%{_target_platform} \
	--prefix=/usr \
	--with-features=huge \
	--disable-selinux \
	--disable-darwin \
	--enable-multibyte \
	--without-x \
	--enable-gui=no \

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install  DESTDIR=%{buildroot} 
mkdir -p %{buildroot}/%{_sysconfdir}/vim/
install -p -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/vim/vimrc
cp -f %{SOURCE2} %{buildroot}/%{_datadir}/%{name}/vim74/template.spec

%clean
%{__rm} -rf %{buildroot}

%post
echo 'alias vi=/usr/bin/vim
alias vim=/usr/bin/vim' > /etc/profile.d/vim.sh
chmod +x /etc/profile.d/vim.sh
source /etc/profile.d/vim.sh

%files
%dir %{_sysconfdir}/vim 
%config(noreplace) %{_sysconfdir}/vim/vimrc
%{_datadir}/vim/*
%{_bindir}/*

%changelog
