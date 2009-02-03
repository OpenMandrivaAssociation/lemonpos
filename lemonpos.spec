Summary:	Open Source point of sale for Linux
Name:		lemonpos
Version: 	0.6.1
Release: 	%mkrel 1
Source0: 	http://downloads.sourceforge.net/lemonpos/%name-%version.tar.bz2
License: 	GPLv2+
Group: 		Office
Url: 		http://lemonpos.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
Requires:	qt4-database-plugin-mysql

%description
Lemon Pos is an opensource point of sale for linux (or any other unix),
targeted for small and medium sized business. It has been tested with a
parallel port ticket printer, and a barcode scanner.

%if %mdkversion < 200900
%post
%update_menus

%postun
%update_menus
%endif

%files -f lemon.lang
%defattr(-,root,root)
%doc README INSTALL NOTES USING
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/lemon
%_kde_appsdir/squeeze
%_kde_configdir/lemonrc
%_kde_datadir/config.kcfg/*.kcfg
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n trunk

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang lemon lemon squeeze

%clean
rm -rf %{buildroot}
