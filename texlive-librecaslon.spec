# revision 31929
# category Package
# catalog-ctan /fonts/librecaslon
# catalog-date 2013-10-17 14:29:03 +0200
# catalog-license ofl
# catalog-version undef
Name:		texlive-librecaslon
Version:	1.0
Release:	10
Summary:	Libre Caslon fonts, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/librecaslon
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librecaslon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librecaslon.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_3cl4ql.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_4g75lz.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_5rmxhc.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_aprite.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_bpmadw.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_cw7ruh.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_hb5o6t.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_klp7zn.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_l5dh3w.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_q5us2t.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_rpuqof.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_wesofd.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_yeotsr.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_ytsyqt.enc
%{_texmfdistdir}/fonts/enc/dvips/librecaslon/lcsl_z4mu2b.enc
%{_texmfdistdir}/fonts/map/dvips/librecaslon/LibreCaslon.map
%{_texmfdistdir}/fonts/opentype/impallari/librecaslon/LibreCaslonText-Bold.otf
%{_texmfdistdir}/fonts/opentype/impallari/librecaslon/LibreCaslonText-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/librecaslon/LibreCaslonText-Italic.otf
%{_texmfdistdir}/fonts/opentype/impallari/librecaslon/LibreCaslonText-Regular.otf
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/librecaslon/LibreCaslonText-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/type1/impallari/librecaslon/LibreCaslonText-Bold.pfb
%{_texmfdistdir}/fonts/type1/impallari/librecaslon/LibreCaslonText-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/librecaslon/LibreCaslonText-Italic.pfb
%{_texmfdistdir}/fonts/type1/impallari/librecaslon/LibreCaslonText-Regular.pfb
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/librecaslon/LibreCaslonText-Regular-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/librecaslon/LY1LibreCaslonText-OsF.fd
%{_texmfdistdir}/tex/latex/librecaslon/LY1LibreCaslonText-Sup.fd
%{_texmfdistdir}/tex/latex/librecaslon/LY1LibreCaslonText-TLF.fd
%{_texmfdistdir}/tex/latex/librecaslon/OT1LibreCaslonText-OsF.fd
%{_texmfdistdir}/tex/latex/librecaslon/OT1LibreCaslonText-Sup.fd
%{_texmfdistdir}/tex/latex/librecaslon/OT1LibreCaslonText-TLF.fd
%{_texmfdistdir}/tex/latex/librecaslon/T1LibreCaslonText-OsF.fd
%{_texmfdistdir}/tex/latex/librecaslon/T1LibreCaslonText-Sup.fd
%{_texmfdistdir}/tex/latex/librecaslon/T1LibreCaslonText-TLF.fd
%{_texmfdistdir}/tex/latex/librecaslon/TS1LibreCaslonText-OsF.fd
%{_texmfdistdir}/tex/latex/librecaslon/TS1LibreCaslonText-TLF.fd
%{_texmfdistdir}/tex/latex/librecaslon/librecaslon.sty
%doc %{_texmfdistdir}/doc/fonts/librecaslon/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/librecaslon/README
%doc %{_texmfdistdir}/doc/fonts/librecaslon/samples.pdf
%doc %{_texmfdistdir}/doc/fonts/librecaslon/samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
