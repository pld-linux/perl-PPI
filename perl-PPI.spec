#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PPI
Summary:	PPI - Parse and manipulate Perl code non-destructively, without using perl itself
Summary(pl):	PPI - Parsowanie i manipulacja kodem Perla w sposób niedestruktywny, bez u¿ycia perla jako takiego
Name:		perl-%{pdir}
Version:	0.828
Release:	1
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{pdir}-%{version}.tar.gz
# Source0-md5:	cece851dda209cb98d3aa1f14c8b47c5
URL:		http://search.cpan.org/dist/PPI/
%if %{with tests}
BuildRequires:	perl-Class-Autouse >= 1.04
BuildRequires:	perl-File-Slurp >= 9999.04
BuildRequires:	perl-List-MoreUtils >= 0.04
BuildRequires:	perl-Test-ClassAPI >= 0.9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Technically, PPI is short for Parse::Perl::Isolated. In aknowledgement
that someone may some day come up with a valid solution for the
grammar problem, it was decided to leave the Parse::Perl namespace
free.

The purpose of this parser is not to parse Perl code, but to parse
Perl documents. In most cases, a single file is valid as both. By
treating the problem this way, we can parse a single file containing
Perl source isolated from any other resources, such as the libraries
upon which the code may depend, and without needing to run an instance
of perl alongside or inside the the parser (a possible solution for
Parse::Perl that is investigated from time to time).

#%description -l pl

%prep
%setup -q -n %{pdir}-%{version}

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
%{perl_vendorlib}/PPI.pm
%{perl_vendorlib}/PPI
%{_mandir}/man3/*
