# revision 31334
# category Package
# catalog-ctan /macros/luatex/latex/pgfmolbio
# catalog-date 2013-07-31 09:13:05 +0200
# catalog-license lppl1.3
# catalog-version 0.21
Name:		texlive-pgfmolbio
Version:	0.21
Release:	8
Summary:	Draw graphs typically found in molecular biology texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/pgfmolbio
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package draws graphs typically found in molecular biology
texts. Currently, the package contains modules for drawing DNA
sequencing chromatograms and protein domain diagrams.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.chromatogram.lua
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.chromatogram.tex
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.convert.tex
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.domains.lua
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.domains.tex
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.sty
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/README
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleScf.scf
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleUniprot.txt
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/pgfmolbio.lua
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/pgfmolbio.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/pgfmolbio/pgfmolbio.dtx
%doc %{_texmfdistdir}/source/lualatex/pgfmolbio/pgfmolbio.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
rm %{buildroot}%{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleGff.gff
