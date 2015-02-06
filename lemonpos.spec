Summary:	Open Source point of sale for Linux
Name:		lemonpos
Version:	0.9.3
Release:	2
Source0:	http://downloads.sourceforge.net/lemonpos/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Office
Url:		http://lemonpos.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires: 	automoc4
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
%{_kde_bindir}/*
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/lemon
%{_kde_appsdir}/squeeze
%{_kde_configdir}/lemonrc
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%if %{mdvver} <= 201100
    %find_lang lemon lemon squeeze
%else
    %find_lang lemon squeeze lemon.lang
%endif

%clean
rm -rf %{buildroot}


%changelog
* Sat Nov 19 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.3-1mdv2012.0
+ Revision: 731733
- New version 0.9.3

* Fri Aug 13 2010 Funda Wang <fwang@mandriva.org> 0.9.2-1mdv2011.0
+ Revision: 569376
- update to new version 0.9.2

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2010.1
+ Revision: 503524
- new version 0.9.1

* Fri May 22 2009 Funda Wang <fwang@mandriva.org> 0.8-1mdv2010.0
+ Revision: 378603
- New version 0.8

* Tue Mar 10 2009 Funda Wang <fwang@mandriva.org> 0.7-1mdv2009.1
+ Revision: 353361
- New version 0.7

* Tue Feb 03 2009 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2009.1
+ Revision: 337014
- new version 0.6.1

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 0.6-1mdv2009.1
+ Revision: 336335
- import lemonpos


