%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		swell-foop
Version:	3.30.0
Release:	1
Summary:	GNOME colored tiles puzzle game
License:	GPLv2+ and GFDL
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Swell_Foop
Source0:	https://download.gnome.org/sources/swell-foop/%{url_ver}/swell-foop-%{version}.tar.xz
BuildRequires:	pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:  meson
# For help
Requires:	yelp

%description
Clear the screen by removing groups of colored and shaped tiles

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/apps/%{name}.*
%{_iconsdir}/*/*/apps/%{name}-symbolic.*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.0-3.mga5
+ Revision: 815346
- require yelp for showing help

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 744083
- Second Mageia 5 Mass Rebuild

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719246
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 689638
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676964
- new version 3.13.92

* Sat Aug 23 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 666662
- new version 3.13.90
- update url

* Thu May 29 2014 ovitters <ovitters> 3.13.1-1.mga5
+ Revision: 627595
- new version 3.13.1

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622338
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614158
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608071
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604569
- new version 3.11.92

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594049
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.3-1.mga5
+ Revision: 582961
- new version 3.11.3

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 541387
- Mageia 4 Mass Rebuild

* Sat Oct 12 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 495803
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484282
- new version 3.10.0

* Tue Sep 17 2013 dams <dams> 3.9.92-1.mga4
+ Revision: 480613
- new version 3.9.92

* Tue Aug 20 2013 ovitters <ovitters> 3.8.2-1.mga4
+ Revision: 468321
- new version 3.8.2

  + fwang <fwang>
    - cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.1-1.mga4
+ Revision: 440905
- add help files
- imported package swell-foop

