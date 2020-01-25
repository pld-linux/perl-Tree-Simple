#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Tree
%define		pnam	Simple
Summary:	Tree::Simple - A simple tree object
Summary(pl.UTF-8):	Tree::Simple - obiekt prostego drzewa
Name:		perl-Tree-Simple
Version:	1.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70462938108a8b8658b1b1d2f12dbeab
URL:		http://search.cpan.org/dist/Tree-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception >= 0.15
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module in an fully object-oriented implementation of a simple
n-ary tree. It is built upon the concept of parent-child
relationships, so therefore every Tree::Simple object has both a
parent and a set of children (who themselves may have children, and so
on). Every Tree::Simple object also has siblings, as they are just the
children of their immediate parent.

It is can be used to model hierarchal information such as a
file-system, the organizational structure of a company, an object
inheritance hierarchy, versioned files from a version control system
or even an abstract syntax tree for use in a parser. It makes no
assumptions as to your intended usage, but instead simply provides the
structure and means of accessing and traversing said structure.

%description -l pl.UTF-8
Ten moduł to w pełni obiektowo zorientowana implementacja prostego
drzewa n-arnego. Jest zbudowany w oparciu i ideę relacji
rodzic-dziecko, tak że każdy obiekt Tree::Simple ma rodzica oraz zbiór
dzieci (które też mogą mieć dzieci, i tak dalej). Każdy obiekt
Tree::Simple ma także rodzeństwo - czyli dzieci bezpośredniego
rodzica.

Moduł może być używany do informacji o modelu hierarchicznym, takich
jak system plików, struktura organizacyjna firmy, hierarchia
dziedziczenia obiektów, wersjonowane pliki z systemu kontroli wersji
czy nawet abstrakcyjne drzewo składniowe do używania w parserze. Moduł
nie czyni żadnych założeń co do wykorzystania, ale po prostu dostarcza
strukturę oraz metody dostępu i przechodzenia po strukturze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tree/*.pm
%{perl_vendorlib}/Tree/Simple
%{_mandir}/man3/*
