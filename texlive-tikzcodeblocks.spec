Name:		texlive-tikzcodeblocks
Version:	54758
Release:	1
Summary:	Helps to draw codeblocks like scratch, NEPO and PXT in TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikzcodeblocks
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzcodeblocks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzcodeblocks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
tikzcodeblocks is a LaTeX package for typesetting blockwise
graphic programming languages like scratch, nepo or pxt.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikzcodeblocks
%doc %{_texmfdistdir}/doc/latex/tikzcodeblocks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
