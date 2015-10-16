%define _sysconfdir /etc/

Summary: A document formatting system
Name: groff
Version: 1.22.3
Release: 1%{?dist}
License: GPLv3+ and GFDL and BSD and MIT
Group: Applications/Publishing
URL: http://www.gnu.org/software/groff/
Source: ftp://ftp.gnu.org/gnu/groff/groff-%{version}.tar.gz

Requires: coreutils, texinfo 

%description
Groff is a document formatting system. Groff takes standard text and
formatting commands as input and produces formatted output. The
created documents can be shown on a display or printed on a printer.
Groff's formatting commands allow you to specify font type and size,
bold type, italic type, the number and size of columns on a page, and
more.

%package docs
Summary: Documentation for groff document formatting system
Group: Documentation
BuildArch: noarch
Requires: groff = %{version}-%{release}

%description docs
The groff-doc package includes additional documentation for groff
text processor package. It contains examples, documentation for PIC
language and documentation for creating PDF files.

%prep
%setup -q

%build
%configure \
	--without-x \

make arch/misc && make

%install
make install DESTDIR=%{buildroot}


%files
# data
%{_datadir}/%{name}/%{version}/font/devdvi/
%{_datadir}/%{name}/%{version}/font/devlbp/
%{_datadir}/%{name}/%{version}/font/devlj4/
%{_datadir}/%{name}/%{version}/oldfont/
%{_datadir}/%{name}/%{version}/pic/
%{_datadir}/%{name}/%{version}/tmac/62bit.tmac
%{_datadir}/%{name}/%{version}/tmac/a4.tmac
%{_datadir}/%{name}/%{version}/tmac/dvi.tmac
%{_datadir}/%{name}/%{version}/tmac/e.tmac
%{_datadir}/%{name}/%{version}/tmac/ec.tmac
%{_datadir}/%{name}/%{version}/tmac/hdmisc.tmac
%{_datadir}/%{name}/%{version}/tmac/hdtbl.tmac
%{_datadir}/%{name}/%{version}/tmac/lbp.tmac
%{_datadir}/%{name}/%{version}/tmac/lj4.tmac
%{_datadir}/%{name}/%{version}/tmac/m.tmac
%{_datadir}/%{name}/%{version}/tmac/me.tmac
%{_datadir}/%{name}/%{version}/tmac/mm.tmac
%{_datadir}/%{name}/%{version}/tmac/mm/
%{_datadir}/%{name}/%{version}/tmac/mmse.tmac
%{_datadir}/%{name}/%{version}/tmac/mom.tmac
%{_datadir}/%{name}/%{version}/tmac/ms.tmac
%{_datadir}/%{name}/%{version}/tmac/mse.tmac
%{_datadir}/%{name}/%{version}/tmac/om.tmac
%{_datadir}/%{name}/%{version}/tmac/pdfmark.tmac
%{_datadir}/%{name}/%{version}/tmac/refer-me.tmac
%{_datadir}/%{name}/%{version}/tmac/refer-mm.tmac
%{_datadir}/%{name}/%{version}/tmac/refer-ms.tmac
%{_datadir}/%{name}/%{version}/tmac/refer.tmac
%{_datadir}/%{name}/%{version}/tmac/s.tmac
%{_datadir}/%{name}/%{version}/tmac/spdf.tmac
%{_datadir}/%{name}/%{version}/tmac/trace.tmac
# programs
%{_bindir}/addftinfo
%{_bindir}/eqn2graph
%{_bindir}/gdiffmk
%{_bindir}/grap2graph
%{_bindir}/grn
%{_bindir}/grodvi
%{_bindir}/grolbp
%{_bindir}/grolj4
%{_bindir}/hpftodit
%{_bindir}/indxbib
%{_bindir}/lkbib
%{_bindir}/lookbib
%{_bindir}/pdfroff
%{_bindir}/pfbtops
%{_bindir}/pic2graph
%{_bindir}/refer
%{_bindir}/tfmtodit
%{_libdir}/groff/groff_opts_no_arg.txt
%{_libdir}/groff/groff_opts_with_arg.txt
%dir %{_libdir}/groff/grog/
%{_libdir}/groff/grog/subs.pl

%{!?_licensedir:%global license %%doc}
%license COPYING FDL LICENSES
%doc BUG-REPORT MORE.STUFF NEWS PROBLEMS
# data
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/%{version}/
%dir %{_datadir}/%{name}/%{version}/font/
%dir %{_datadir}/%{name}/%{version}/tmac/
%{_datadir}/%{name}/current
%{_datadir}/%{name}/%{version}/eign
%{_datadir}/%{name}/%{version}/font/devascii/
%{_datadir}/%{name}/%{version}/font/devlatin1/
%{_datadir}/%{name}/%{version}/font/devps/
%{_datadir}/%{name}/%{version}/font/devutf8/
%{_datadir}/%{name}/%{version}/font/devhtml/
%{_datadir}/%{name}/%{version}/tmac/an-ext.tmac
%{_datadir}/%{name}/%{version}/tmac/an-old.tmac
%{_datadir}/%{name}/%{version}/tmac/an.tmac
%{_datadir}/%{name}/%{version}/tmac/andoc.tmac
%{_datadir}/%{name}/%{version}/tmac/composite.tmac
%{_datadir}/%{name}/%{version}/tmac/cp1047.tmac
%{_datadir}/%{name}/%{version}/tmac/cs.tmac
%{_datadir}/%{name}/%{version}/tmac/de.tmac
%{_datadir}/%{name}/%{version}/tmac/den.tmac
%{_datadir}/%{name}/%{version}/tmac/devtag.tmac
%{_datadir}/%{name}/%{version}/tmac/doc-old.tmac
%{_datadir}/%{name}/%{version}/tmac/doc.tmac
%{_datadir}/%{name}/%{version}/tmac/eqnrc
%{_datadir}/%{name}/%{version}/tmac/europs.tmac
%{_datadir}/%{name}/%{version}/tmac/fallbacks.tmac
%{_datadir}/%{name}/%{version}/tmac/fr.tmac
%{_datadir}/%{name}/%{version}/tmac/html-end.tmac
%{_datadir}/%{name}/%{version}/tmac/html.tmac
%{_datadir}/%{name}/%{version}/tmac/hyphen.cs
%{_datadir}/%{name}/%{version}/tmac/hyphen.den
%{_datadir}/%{name}/%{version}/tmac/hyphen.det
%{_datadir}/%{name}/%{version}/tmac/hyphen.fr
%{_datadir}/%{name}/%{version}/tmac/hyphen.sv
%{_datadir}/%{name}/%{version}/tmac/hyphen.us
%{_datadir}/%{name}/%{version}/tmac/hyphenex.cs
%{_datadir}/%{name}/%{version}/tmac/hyphenex.det
%{_datadir}/%{name}/%{version}/tmac/hyphenex.us
%{_datadir}/%{name}/%{version}/tmac/ja.tmac
%{_datadir}/%{name}/%{version}/tmac/latin1.tmac
%{_datadir}/%{name}/%{version}/tmac/latin2.tmac
%{_datadir}/%{name}/%{version}/tmac/latin5.tmac
%{_datadir}/%{name}/%{version}/tmac/latin9.tmac
%{_datadir}/%{name}/%{version}/tmac/man.tmac
%{_datadir}/%{name}/%{version}/tmac/mandoc.tmac
%{_datadir}/%{name}/%{version}/tmac/mdoc.tmac
%{_datadir}/%{name}/%{version}/tmac/mdoc/
%{_datadir}/%{name}/%{version}/tmac/papersize.tmac
%{_datadir}/%{name}/%{version}/tmac/pic.tmac
%{_datadir}/%{name}/%{version}/tmac/ps.tmac
%{_datadir}/%{name}/%{version}/tmac/psatk.tmac
%{_datadir}/%{name}/%{version}/tmac/psold.tmac
%{_datadir}/%{name}/%{version}/tmac/pspic.tmac
%{_datadir}/%{name}/%{version}/tmac/safer.tmac
%{_datadir}/%{name}/%{version}/tmac/sv.tmac
%{_datadir}/%{name}/%{version}/tmac/trans.tmac
%{_datadir}/%{name}/%{version}/tmac/troffrc
%{_datadir}/%{name}/%{version}/tmac/troffrc-end
%{_datadir}/%{name}/%{version}/tmac/tty-char.tmac
%{_datadir}/%{name}/%{version}/tmac/tty.tmac
%{_datadir}/%{name}/%{version}/tmac/unicode.tmac
%{_datadir}/%{name}/%{version}/tmac/www.tmac
# programs
%{_bindir}/eqn
%{_bindir}/groff
%{_bindir}/grops
%{_bindir}/grotty
%{_bindir}/neqn
%{_bindir}/nroff
%{_bindir}/pic
%{_bindir}/post-grohtml
%{_bindir}/pre-grohtml
%{_bindir}/preconv
%{_bindir}/soelim
%{_bindir}/tbl
%{_bindir}/troff

# data
%{_datadir}/%{name}/%{version}/font/devpdf/
%{_datadir}/%{name}/%{version}/tmac/pdf.tmac
# programs
%{_bindir}/afmtodit
%{_bindir}/chem
%{_bindir}/gperl
%{_bindir}/gpinyin
%{_bindir}/glilypond
%{_bindir}/groffer
%{_bindir}/grog
%{_bindir}/gropdf
%{_bindir}/mmroff
%{_bindir}/pdfmom
%{_bindir}/roff2dvi
%{_bindir}/roff2html
%{_bindir}/roff2pdf
%{_bindir}/roff2ps
%{_bindir}/roff2text
%{_bindir}/roff2x
%dir %{_libdir}/groff/
%dir %{_libdir}/groff/glilypond/
%{_libdir}/groff/glilypond/args.pl
%{_libdir}/groff/glilypond/oop_fh.pl
%{_libdir}/groff/glilypond/subs.pl
%dir %{_libdir}/groff/gpinyin/
%{_libdir}/groff/gpinyin/subs.pl

%files doc
%doc %{_pkgdocdir}/*.me
%doc %{_pkgdocdir}/*.ps
%doc %{_pkgdocdir}/*.ms
%doc %{_pkgdocdir}/examples/
%doc %{_pkgdocdir}/html/
%doc %{_pkgdocdir}/pdf/
%{_mandir}/man1/afmtodit.*                                                                     
%{_mandir}/man1/chem.*                                                                         
%{_mandir}/man1/gperl.*                                                                        
%{_mandir}/man1/gpinyin.*                                                                  
%{_mandir}/man1/glilypond.*                                                                
%{_mandir}/man1/groffer.*                                                                  
%{_mandir}/man1/grog.*                                                                
%{_mandir}/man1/gropdf.*                                                                       
%{_mandir}/man1/mmroff.*                                                                       
%{_mandir}/man1/pdfmom.*                                                                   
%{_mandir}/man1/roff2dvi.*                                                                 
%{_mandir}/man1/roff2html.*                                                                    
%{_mandir}/man1/roff2pdf.*                                                                 
%{_mandir}/man1/roff2ps.*                                                                  
%{_mandir}/man1/roff2text.*                                                                
%{_mandir}/man1/roff2x.*  
%{_mandir}/man1/gnroff.*                                                                       
%{_mandir}/man1/gtroff.*                                                                   
%{_mandir}/man1/gtbl.*                                                                     
%{_mandir}/man1/gpic.*                                                                         
%{_mandir}/man1/geqn.*                                                                         
%{_mandir}/man1/gneqn.*                                                                        
%{_mandir}/man1/gsoelim.*                                                                      
%{_mandir}/man1/zsoelim.* 
%{_mandir}/man1/eqn.*                                                                      
%{_mandir}/man1/groff.*                                                                    
%{_mandir}/man1/grops.*                                                                    
%{_mandir}/man1/grotty.*                                                                       
%{_mandir}/man1/neqn.*                                                                         
%{_mandir}/man1/nroff.*                                                                    
%{_mandir}/man1/pic.*                                                                      
%{_mandir}/man1/preconv.*                                                                      
%{_mandir}/man1/soelim.*                                                                       
%{_mandir}/man1/tbl.*                                                                          
%{_mandir}/man1/troff.*       
%{_mandir}/man1/addftinfo.*                                                                    
%{_mandir}/man1/eqn2graph.*                                                                    
%{_mandir}/man1/gdiffmk.*                                                                      
%{_mandir}/man1/grap2graph.*                                                                   
%{_mandir}/man1/grn.*                                                                      
%{_mandir}/man1/grodvi.*                                                                   
%{_mandir}/man1/grohtml.*                                                                  
%{_mandir}/man1/grolbp.*                                                              
%{_mandir}/man1/grolj4.*                                                                       
%{_mandir}/man1/hpftodit.*                                                                     
%{_mandir}/man1/indxbib.*                                                                  
%{_mandir}/man1/lkbib.*                                                                    
%{_mandir}/man1/lookbib.*                                                                      
%{_mandir}/man1/pdfroff.*                                                                  
%{_mandir}/man1/pfbtops.*                                                                  
%{_mandir}/man1/pic2graph.*                                                                
%{_mandir}/man1/refer.*                                                                    
%{_mandir}/man1/tfmtodit.*                                                                     
%{_mandir}/man1/grefer.*                                                                       
%{_mandir}/man1/glookbib.*                                                                     
%{_mandir}/man1/gindxbib.*                                                                     
# groff processor documentation                                                                
%{_mandir}/man5/*                                                                              
%{_mandir}/man7/*                                                                              
%{_infodir}/groff.info* 

%changelog
