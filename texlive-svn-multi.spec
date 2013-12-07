# revision 26313
# category Package
# catalog-ctan /macros/latex/contrib/svn-multi
# catalog-date 2012-05-07 15:25:51 +0200
# catalog-license lppl
# catalog-version 2.4d
Name:		texlive-svn-multi
Version:	2.4d
Release:	6
Summary:	Subversion keywords in multi-file LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svn-multi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-svn-multi.bin = %{EVRD}

%description
This package lets you typeset keywords of the version control
system Subversion inside your LaTeX files anywhere you like.
Unlike the otherwise similar package svn the use of multiple
files for one LaTeX document is well supported. The package
uses the author's filehook and currfile packages. The package
interacts with an external Perl script, to retrieve information
necessary for the required output.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/svn-multi
%{_texmfdistdir}/scripts/svn-multi/svn-multi.pl
%{_texmfdistdir}/tex/latex/svn-multi/svn-multi.sty
%{_texmfdistdir}/tex/latex/svn-multi/svnkw.sty
%doc %{_texmfdistdir}/doc/latex/svn-multi/README
%doc %{_texmfdistdir}/doc/latex/svn-multi/example_chap1.tex
%doc %{_texmfdistdir}/doc/latex/svn-multi/example_main.tex
%doc %{_texmfdistdir}/doc/latex/svn-multi/group_example.tex
%doc %{_texmfdistdir}/doc/latex/svn-multi/svn-multi.pdf
%doc %{_texmfdistdir}/doc/support/svn-multi/svn-multi-pl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/svn-multi/svn-multi-pl.dtx
%doc %{_texmfdistdir}/source/latex/svn-multi/svn-multi.dtx
%doc %{_texmfdistdir}/source/latex/svn-multi/svn-multi.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/svn-multi/svn-multi.pl svn-multi
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4d-4
+ Revision: 812885
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4d-3
+ Revision: 805102
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4d-2
+ Revision: 756361
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4d-1
+ Revision: 719619
- texlive-svn-multi
- texlive-svn-multi
- texlive-svn-multi
- texlive-svn-multi

