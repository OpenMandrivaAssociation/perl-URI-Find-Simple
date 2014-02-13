%define upstream_name    URI-Find-Simple
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A simple interface to URI::Find 
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/URI/URI-Find-Simple-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI::Find)

BuildArch:	noarch

%description
URI::Find is all very well, but sometimes you just want a list of the links 
in a given piece of text, or you want to change all the urls in some text 
somehow, and don't want to mess with callback interfaces.

This module uses URI::Find, but hides the callback interface, providing two 
functions - one to list all the uris, and one to change all the uris.
%prep
%setup -q -n URI-Find-Simple-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/URI/
%{_mandir}/man3/*


%changelog
* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 596696
- update to 1.03
- update to 1.03

* Tue Nov 10 2009 Michael Scherer <misc@mandriva.org> 1.01-3mdv2011.0
+ Revision: 463854
- fix License
- add a note on the patch i have added, as upstream is not such about it
- fix test, with a patch from rt.cpan.org written by David Golden

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.1
+ Revision: 292357
- update to new version 1.01

* Fri Jun 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1-1mdv2009.0
+ Revision: 227427
- update to new version 1

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.7-1mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Dec 07 2006 Michael Scherer <misc@mandriva.org> 0.7-1mdv2007.0
+ Revision: 91986
- Import perl-URI-Find-Simple

* Thu Dec 07 2006 Michael Scherer <misc@mandriva.org> 0.7-1mdv2007.1
- First Mandriva package



