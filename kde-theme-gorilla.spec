%define		_theme 	gorilla

Summary:	KDE theme - %{_theme}
Summary(pl):	Motyw KDE - %{_theme}
Name:		kde-theme-%{_theme}
Version:	1.0
Release:	0.030726
License:	GPL
Group:		Themes
Source0:	http://www.starsurvivor.net/linux/gorilla/%{_theme}-current-07.26.03.tar.bz2
# Source0-md5:	b377e195e24fb81732c48bc7feede8a2
Source1:	http://www.kde-look.org/content/files/7124-%{_theme}_kside.tar.gz
# Source1-md5:	c1a3f17ab510cc7c4202fdf2a4892f16
Source2:	http://developer.ximian.com/themes/backgrounds/simple.png
# Source2-md5:	e3d187c1b6cbe7fb90ed4220eaeba1af
URL:		http://www.kde-look.org/content/show.php?content=6927
# Also: http://www.kde-look.org/content/show.php?content=7075
# Also: http://www.kde-look.org/content/show.php?content=7003
# Also: http://www.kde-look.org/content/show.php?content=7081
# Also: http://www.kde-look.org/content/show.php?content=7124
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

%description
%{_theme} is a slicker theme that was designed to look nice with
slicker. To developer's surprise, this style looks good even without
slicker.

%description -l pl
%{_theme} to motyw stworzony by wsp�gra� z aplikacj� slicker. Ku
zaskoczeniu tw�rc�w, styl ten jednak okaza� si� pi�knie wygl�da� nawet
bez slickera.

####
# At the moment there is no gorilla style, I expect tthta there will be one in the near future.
####

##%package -n kde-style-%{_theme}
#Summary:	KDE style - %{_theme}
#Summary(pl):	Styl do KDE - %{_theme}
#Group:		Themes
#Requires:	kdelibs
#
#%%description -n kde-style-%{_theme}
#%%{_theme} is a slicker style that was designed to look nice with
#slicker. To developer's surprise, this style looks good even without
##slicker.

#%%description -n kde-style-%{_theme} -l pl
#%%{_theme} to styl stworzony by wsp�gra� z aplikacj� slicker. Ku
#zaskoczeniu tw�rc�w, styl ten jednak okaza� si� pi�knie wygl�da� nawet
#bez slickera.

%package -n kde-icons-%{_theme}
Summary:        KDE icons - %{_theme}
Summary(pl):    Motyw ikon do KDE - %{_theme}
Group:          Themes
Requires:       kdelibs

%description -n kde-icons-%{_theme}
%{_name} is a KDE port of a famous GNOME SVG icon theme.

%description -n kde-icons-%{_theme} -l pl
%{_name} to port do KDE s�ynnego tematu ikon z GNOME.

%package -n kde-wallpaper-%{_theme}
Summary:	KDE wallpaper - %{_theme}
Summary(pl):	Tapeta do KDE - %{_theme}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdebase

%description -n kde-wallpaper-%{_theme}
A wallpaper to go with %{_theme} theme.

%description -n kde-wallpaper-%{_theme} -l pl
Tapeta pasuj�ca do motywu %{_theme}.

%package -n kde-decoration-%{_theme}
Summary:        Icewm window decoration for kwin - %{_theme}
Summary(pl):    Dekoracja icewm dla kwin - %{_theme}
Group:          Themes
Requires:       kde-decoration-icewm

%description -n kde-decoration-%{_theme}
Icewm window decoration for kwin - %{_theme}.

%description -n kde-decoration-%{_theme} -l pl
Dekoracja icewm dla kwin - %{_theme}.

%package -n kde-colorscheme-%{_theme}
Summary:        Color scheme for %{_theme} theme
Summary(pl):    Schemat kolor�w dla motywu %{_theme}
Group:          Themes
Requires:       kdebase

%description -n kde-colorscheme-%{_theme}
Color scheme for %{_theme} theme.

%description -n kde-colorscheme-%{_theme} -l pl
Schemat kolor�w dla motywu %{_theme}.

%package -n kde-splash-%{_theme}
Summary:        Splash screen %{_theme} theme
Summary(pl):    Obrazek startowy dla motywu %{_theme}
Group:          Themes
Requires:       kdebase

%description -n kde-splash-%{_theme}
Splash screen %{_theme} theme.

%description -n kde-splash-%{_theme} -l pl
Obrazek startowy dla motywu %{_theme}.

%package -n kde-kside-%{_theme}
Summary:	Kicker sidebar from %{_theme} 
Summary(pl): 	Boczny pasek do menu kde z tematu %{_theme}
Group:          Themes
Obsoletes:	kde-kside
Provides:	kde-kside
Requires:       kdebase-kicker >= 9:3.1.90.030726-2

%description -n kde-kside-%{_theme}
Kicker sidebar from %{_theme}.

%description -n kde-kside-%{_theme} -l pl
Boczny pasek do menu kde z tematu %{_theme}.

%prep
%setup -q -n Gorilla -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_iconsdir}/gorilla,%{_datadir}/apps/kwin/icewm-themes/gorilla,%{_datadir}/apps/ksplash/gorilla}
install -d $RPM_BUILD_ROOT%{_datadir}/apps/{kicker/pics,kdisplay/color-schemes/}

mv kde/color-scheme/*  $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/
mv kde/gorilla_iceWM/* $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes/gorilla/
mv kde/splash/*	$RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/gorilla/
echo > $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/gorilla/Theme.rc << _EOF_
[KSplash Theme: gorilla]
Name = Gorilla Splash Theme
Description = Gorilla Splash Theme.
Engine = Default
Icons Flashing = true
_EOF_
rm -rf kde
mv gorilla\ kside/* $RPM_BUILD_ROOT%{_datadir}/apps/kicker/pics/
mv [!R]* $RPM_BUILD_ROOT%{_iconsdir}/gorilla 

install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/wallpapers/

%clean
rm -rf $RPM_BUILD_ROOT

#files -n kde-style-%{_theme}
#defattr(644,root,root,755)
#{_libdir}/kde3/plugins/styles/*.la
#attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
#{_datadir}/apps/kstyle/themes/slicker.themerc

%files -n kde-wallpaper-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n kde-icons-%{_theme}
%defattr(644,root,root,755)
%{_iconsdir}/gorilla/

%files -n kde-kside-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/kicker/pics/*.png

%files -n kde-splash-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/gorilla/


%files -n kde-colorscheme-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*

%files -n kde-decoration-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/kwin/icewm-themes/gorilla/
