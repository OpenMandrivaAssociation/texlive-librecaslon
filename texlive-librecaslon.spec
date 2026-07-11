%global tl_name librecaslon
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Libre Caslon fonts, with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/librecaslon
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/librecaslon.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/librecaslon.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Libre Caslon fonts are designed by Pablo Impallari. Although they
have been designed for use as web fonts, they work well as conventional
text fonts. An artificially generated BoldItalic variant has been added.

