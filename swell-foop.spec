%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		swell-foop
Version:	40.0
Release:	1
Summary:	GNOME colored tiles puzzle game
License:	GPLv2+ and GFDL
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Swell_Foop
Source0:	https://download.gnome.org/sources/swell-foop/%{url_ver}/swell-foop-%{version}.tar.xz
BuildRequires:	pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:  meson
BuildRequires:	vala
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
%{_datadir}/applications/org.gnome.SwellFoop.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/apps/org.gnome.SwellFoop*.*
%{_datadir}/%{name}
#{_datadir}/metainfo/org.gnome.SwellFoop.gresource.xml
