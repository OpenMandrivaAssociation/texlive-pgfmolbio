%global tl_name pgfmolbio
%global tl_revision 71551

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.21a
Release:	%{tl_revision}.1
Summary:	Draw graphs typically found in molecular biology texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/pgfmolbio
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package draws graphs typically found in molecular biology texts.
Currently, the package contains modules for drawing DNA sequencing
chromatograms and protein domain diagrams.

