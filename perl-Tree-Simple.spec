#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	Simple
Summary:	Tree::Simple - A simple tree object
#Summary(pl):	
Name:		perl-Tree-Simple
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d42225daa3740b10ef37a6bfa945a07
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception >= 0.15
BuildRequires:	perl-Test-Simple >= 0.47,
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module in an fully object-oriented implementation of a simple
n-ary tree. It is built upon the concept of parent-child relationships,
so therefore every B<Tree::Simple> object has both a parent and a
set of children (who themselves may have children, and so on). Every
B<Tree::Simple> object also has siblings, as they are just the children
of their immediate parent.

It is can be used to model hierarchal information such as a file-system,
the organizational structure of a company, an object inheritance
hierarchy, versioned files from a version control system or even an
abstract syntax tree for use in a parser. It makes no assumptions as
to your intended usage, but instead simply provides the structure and
means of accessing and traversing said structure.

# %description -l pl
# TODO

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
