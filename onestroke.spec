Summary:	OneStroke - Freehand gesture based character input system for Tablet PCs
Name:		onestroke
Version:	0.8.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.paperaffinity.com/risujin/%{name}-%{version}.tar.gz
# Source0-md5:	69d3dc65eb043ac3586f367fb6e9aafe
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.paperaffinity.com/risujin/onestroke.php
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OneStroke is a gesture-based character input program. Because
a tablet PC in tablet mode does not have a keyboard, a software
replacement is necessary. OneStroke aims to be a more elegant
replacement to the bulky on-screen keyboard.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}-0.8
%{_datadir}/%{name}-0.8/*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
