%define module 	SCMxx
%define version 0.4.1
%define release 8

Summary:	Perl module to access siemens cell phonebooks
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
Url:		https://sourceforge.net/projects/gscmxx/
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  scmxx
Requires:  scmxx
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch
Provides: perl(SCMxx::Config)

%description
Perl module to access siemens cell phonebooks.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
# (tv) fix build:
perl -pi -e 's!/usr/local/share/man/!/usr/share/man/!; s!INSTALLDIRS = site!INSTALLDIRS = vendor!' Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/%{module}.pm
%{perl_vendorlib}/%{module}
%{_mandir}/*/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.1-6mdv2010.0
+ Revision: 433637
- fix build
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.1-5mdv2009.0
+ Revision: 241854
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- simplify buildrequires

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.4.1-3mdv2008.0
+ Revision: 23912
- rebuild


* Tue Jun 14 2005 Götz Waschk <waschk@mandriva.org> 0.4.1-2mdk
- fix deps
- fix provides
- fix buildrequires

* Mon Nov 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.4.1-1mdk
- new

