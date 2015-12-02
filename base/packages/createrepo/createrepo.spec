%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary:	Creates a common metadata repository
Name:		createrepo
Version:	0.10.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://createrepo.baseurl.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	5fb50b63aaa5932ab16b2196badaf167
Patch1:		createrepo-0.9.8-disable-deltarpm.patch
URL:		http://createrepo.baseurl.org/
BuildRequires:	python-devel
BuildRequires:	rpm-build
BuildRequires:	sed >= 4.0
Requires:	python
#Requires:	python-deltarpm
Requires:	libxml2-python
Requires:	python-pyliblzma
Requires:	rpm-python
Requires:	yum 
Requires:	yum-metadata-parser
BuildArch:	noarch

%description
A set of utilities for generating a common metadata repository from a
directory of RPM packages and maintaining it.

%package -n bash-completion-%{name}
Summary:	bash-completion for createrepo commands
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-%{name}
bash-completion for createrepo commands.

%prep
%setup -q
%patch1 -p1

sed -i -e '1s,#!.*python,#!%{__python},' modifyrepo.py

#Don't build Docs for now
sed -i 's!--verbose!!g' Makefile
sed -i 's!--verbose!!g' createrepo/Makefile

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	sysconfdir=%{_sysconfdir} \
	PKGDIR=%{python_sitearch}/%{name} \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc ChangeLog README
%attr(755,root,root) %{_bindir}/createrepo
%attr(755,root,root) %{_bindir}/mergerepo
%attr(755,root,root) %{_bindir}/modifyrepo
%{_mandir}/man1/mergerepo.1*
%{_mandir}/man1/modifyrepo.1*
%{_mandir}/man8/createrepo.8*
%dir %{_datadir}/%{name}
# note that these DO NEED executable bit set!
%attr(755,root,root) %{_datadir}/%{name}/genpkgmetadata.py
%attr(755,root,root) %{_datadir}/%{name}/mergerepo.py
%attr(755,root,root) %{_datadir}/%{name}/modifyrepo.py
%attr(755,root,root) %{_datadir}/%{name}/worker.py
%{_datadir}/%{name}/*.py*
%dir %{python_sitearch}/%{name}
%{python_sitearch}/%{name}/*.py*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/
