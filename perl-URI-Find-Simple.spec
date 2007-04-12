%define realname   URI-Find-Simple

Name:		perl-%{realname}
Version:    0.7
Release:    %mkrel 1
License:	GPL
Group:		Development/Perl
Summary:    A simple interface to URI::Find 
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/URI-Find-Simple-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Find)
BuildArch: noarch

%description
URI::Find is all very well, but sometimes you just want a list of the links 
in a given piece of text, or you want to change all the urls in some text 
somehow, and don't want to mess with callback interfaces.

This module uses URI::Find, but hides the callback interface, providing two 
functions - one to list all the uris, and one to change all the uris.
%prep
%setup -q -n URI-Find-Simple-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/URI/
%{_mandir}/man3/*


