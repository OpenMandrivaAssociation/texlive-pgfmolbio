Name:		texlive-pgfmolbio
Version:	35152
Release:	2
Summary:	Draw graphs typically found in molecular biology texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/pgfmolbio
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmolbio.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/lualatex/pgfmolbio
%doc %{_texmfdistdir}/doc/lualatex/pgfmolbio
#- source
%doc %{_texmfdistdir}/source/lualatex/pgfmolbio

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
rm %{buildroot}%{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleGff.gff
