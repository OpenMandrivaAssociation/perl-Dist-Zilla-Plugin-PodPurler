%define upstream_name    Dist-Zilla-Plugin-PodPurler
%define upstream_version 0.093401

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Like PodWeaver, but more erratic and amateurish
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Pod::Elemental)
BuildRequires:	perl(Pod::Elemental::PerlMunger)
BuildRequires:	perl(Pod::Eventual)

BuildArch:	noarch

%description
PodPurler ress, which rips apart your kinda-POD and reconstructs it as
boring old real POD.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


