Summary:        unity package repositories
Name:           unity-repos
Version:        0.4
Release:        1
License:        MIT
Group:          System Environment/Base
URL:            http://www.unity-linux.org/
# tarball is created by running make archive in the git checkout
Source0:        unity.repo
Provides:       unity-repos(%{version})
BuildArch:      noarch

%description
unity package repository files for yum 

%prep
#%setup -q
mkdir -p %{name}-%{version}
cp %{SOURCE0} %{name}-%{version}

%build

%install
# Install the keys
# I need Keys
#install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
#install -m 644 RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

#pushd $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
#for keyfile in RPM-GPG-KEY*; do
#    key=${keyfile#RPM-GPG-KEY-} # e.g. 'unity-primary'
#    arches=$(sed -ne "s/^${key}://p" $RPM_BUILD_DIR/%{name}-%{version}/archmap) \
#        || echo "WARNING: no archmap entry for $key"
#    for arch in $arches; do
#        # replace last part with $arch (unity-primary -> unity-$arch)
#        ln -s $keyfile ${keyfile%%-*}-$arch # NOTE: RPM replaces %% with %
#    done
#done
# and add symlink for compat generic location
#ln -s RPM-GPG-KEY-unity-%{version}-primary RPM-GPG-KEY-%{version}-unity
#popd

install -d -m 755 $RPM_BUILD_ROOT/etc/yum/repos.d/
#for file in *.repo ; do
#  install -m 644 $file $RPM_BUILD_ROOT/etc/yum/repos.d/
#done

install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum/repos.d/

%files
%defattr(-,root,root,-)
%dir /etc/yum/repos.d/
%config(noreplace) /etc/yum/repos.d/unity.repo
#%config(noreplace) /etc/yum.repos.d/unity-updates*.repo
#%dir /etc/pki/rpm-gpg
#/etc/pki/rpm-gpg/*

%changelog
