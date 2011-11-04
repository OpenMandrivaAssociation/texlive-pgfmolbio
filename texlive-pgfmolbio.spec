# revision 24040
# category Package
# catalog-ctan /macros/luatex/latex/pgfmolbio
# catalog-date 2011-09-20 19:53:04 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-pgfmolbio
Version:	0.1
Release:	1
Summary:	Draw graphs typically found in molevular biology texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/pgfmolbio
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package draws graphs typically found in molecular biology
texts. Currently, the package contains one module, which
creates DNA sequencing chromatograms from files in standard
chromatogram format (scf).

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
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.chromatogram.lua
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.chromatogram.tex
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.sty
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/README
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleScf.scf
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/pgfmolbio.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/pgfmolbio/pgfmolbio.dtx
%doc %{_texmfdistdir}/source/lualatex/pgfmolbio/pgfmolbio.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
