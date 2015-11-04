Summary:	LZMA file compressor
Name:		lzip
Version:	1.15
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	http://download.savannah.gnu.org/releases/lzip/%{name}-%{version}.tar.gz
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo

%description
Lzip is a lossless file compressor based on the LZMA
(Lempel-Ziv-Markov chain-Algorithm) algorithm designed by Igor Pavlov.
The high compression of LZMA comes from combining two basic,
well-proven compression ideas: sliding dictionaries (i.e. LZ77/78),
and Markov models (i.e. the thing used by every compression algorithm
that uses a range encoder or similar order-0 entropy coder as its last
stage) with segregation of contexts according to what the bits are
used for.

%prep
%setup -q

%build
%configure
%{__make} all info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%post	-p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

#%postun	-p /sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lzip
%{_mandir}/man1/lzip.1*
%{_infodir}/lzip.info*

%changelog
