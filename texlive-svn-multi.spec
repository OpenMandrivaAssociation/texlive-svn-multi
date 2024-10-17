Name:		texlive-svn-multi
Version:	64967
Release:	2
Summary:	Subversion keywords in multi-file LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/svn-multi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/svn-multi/svn-multi.pl svn-multi
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
