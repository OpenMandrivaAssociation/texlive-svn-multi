%global tl_name svn-multi
%global tl_revision 79618
%global tl_bin_links svn-multi:%{_texmfdistdir}/scripts/svn-multi/svn-multi.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4d
Release:	%{tl_revision}.1
Summary:	Subversion keywords in multi-file LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/svn-multi
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-multi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(svn-multi.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This package lets you typeset keywords of the version control system
Subversion inside your LaTeX files anywhere you like. Unlike the
otherwise similar package svn the use of multiple files for one LaTeX
document is well supported. The package uses the author's filehook and
currfile packages. The package interacts with an external Perl script,
to retrieve information necessary for the required output.

