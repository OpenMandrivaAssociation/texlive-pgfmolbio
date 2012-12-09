# revision 24040
# category Package
# catalog-ctan /macros/luatex/latex/pgfmolbio
# catalog-date 2011-09-20 19:53:04 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-pgfmolbio
Version:	0.1
Release:	2
Summary:	Draw graphs typically found in molevular biology texts
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
texts. Currently, the package contains one module, which
creates DNA sequencing chromatograms from files in standard
chromatogram format (scf).

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
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.sty
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/README
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleScf.scf
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 754817
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719242
- texlive-pgfmolbio
- texlive-pgfmolbio
- texlive-pgfmolbio

