%define module 	SCMxx
%define version 0.4.1
%define release %mkrel 3

Summary:	Perl module to access siemens cell phonebooks
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
Url:		http://sourceforge.net/projects/gscmxx/
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

