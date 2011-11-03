# revision 23782
# category Package
# catalog-ctan /macros/latex/contrib/svn-multi
# catalog-date 2011-09-04 01:09:18 +0200
# catalog-license lppl
# catalog-version 2.4d
Name:		texlive-svn-multi
Version:	2.4d
Release:	1
Summary:	Subversion keywords in multi-file LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svn-multi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-svn-multi.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package lets you typeset keywords of the version control
system Subversion inside your LaTeX files anywhere you like.
Unlike the otherwise similar package svn the use of multiple
files for one LaTeX document is well supported. The package
uses the author's filehook and currfile packages. The package
interacts with an external Perl script, to retrieve information
necessary for the required output.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/svn-multi
%{_texmfdistdir}/scripts/svn-multi/svn-multi.pl
%{_texmfdistdir}/tex/latex/svn-multi/svn-multi.sty
%{_texmfdistdir}/tex/latex/svn-multi/svnkw.sty
%doc %{_texmfdistdir}/doc/latex/svn-multi/README
%doc %{_texmfdistdir}/doc/latex/svn-multi/svn-multi.pdf
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
