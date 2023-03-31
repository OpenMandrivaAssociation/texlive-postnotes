Name:		texlive-postnotes
Version:	65007
Release:	2
Summary:	Endnotes for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/postnotes
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postnotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postnotes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postnotes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an endnotes package for LaTeX. Its user interface
provides means to print multiple sections of notes along the
document, and to subdivide them either automatically -- by
chapter, by section -- or at manually specified places, thus
being able to easily handle both numbered and unnumbered
headings. The package also provides infrastructure for setting
up contextual running headers for printed notes. The default is
a simple but useful one, in the form "Notes to pages N-M", but
more elaborate ones can be built. When hyperref is loaded,
postnotes provides hyperlinked notes, including back links.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/postnotes
%{_texmfdistdir}/tex/latex/postnotes
%doc %{_texmfdistdir}/doc/latex/postnotes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
