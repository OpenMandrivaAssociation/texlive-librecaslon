Name:		texlive-librecaslon
Version:	64432
Release:	1
Summary:	Libre Caslon fonts, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/librecaslon
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librecaslon.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librecaslon.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Libre Caslon fonts are designed by Pablo Impallari.
Although they have been designed for use as web fonts, they
work well as conventional text fonts. A bold italic variant is
not currently available. As a stopgap, an artificially slanted
bold variant has been created and treated as italic.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/librecaslon
%{_texmfdistdir}/fonts/map/dvips/librecaslon
%{_texmfdistdir}/fonts/opentype/impallari/librecaslon
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon
%{_texmfdistdir}/fonts/type1/impallari/librecaslon
%{_texmfdistdir}/fonts/vf/impallari/librecaslon
%{_texmfdistdir}/tex/latex/librecaslon
%doc %{_texmfdistdir}/doc/fonts/librecaslon

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
