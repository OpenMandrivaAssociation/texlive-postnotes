%global tl_name postnotes
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.1
Release:	%{tl_revision}.1
Summary:	Endnotes for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/postnotes
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/postnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/postnotes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/postnotes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an endnotes package for LaTeX. Its user interface provides means
to print multiple sections of notes along the document, and to subdivide
them either automatically -- by chapter, by section -- or at manually
specified places, thus being able to easily handle both numbered and
unnumbered headings. The package also provides infrastructure for
setting up contextual running headers for printed notes. The default is
a simple but useful one, in the form "Notes to pages N-M", but more
elaborate ones can be built. When hyperref is loaded, postnotes provides
hyperlinked notes, including back links.

