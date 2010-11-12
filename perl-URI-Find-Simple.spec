%define upstream_name    URI-Find-Simple
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A simple interface to URI::Find 
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Find)

BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
URI::Find is all very well, but sometimes you just want a list of the links 
in a given piece of text, or you want to change all the urls in some text 
somehow, and don't want to mess with callback interfaces.

This module uses URI::Find, but hides the callback interface, providing two 
functions - one to list all the uris, and one to change all the uris.
%prep
%setup -q -n URI-Find-Simple-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/URI/
%{_mandir}/man3/*
