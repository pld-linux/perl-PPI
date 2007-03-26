#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PPI
Summary:	PPI - parse and manipulate Perl code non-destructively, without using perl itself
Summary(pl.UTF-8):	PPI - parsowanie i manipulacja kodem Perla w sposób niedestruktywny, bez użycia Perla jako takiego
Name:		perl-PPI
Version:	1.118
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AD/ADAMK/%{pdir}-%{version}.tar.gz
# Source0-md5:	189ca5c1fa39c403f65e28967985f4cb
URL:		http://search.cpan.org/dist/PPI/
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.84
BuildRequires:	perl-Clone >= 0.17
BuildRequires:	perl-Digest-MD5 >= 2.27
BuildRequires:	perl-IO-String >= 1.07
BuildRequires:	perl-List-MoreUtils >= 0.13
BuildRequires:	perl-Params-Util >= 0.10
BuildRequires:	perl-Scalar-List-Utils >= 1.18
BuildRequires:	perl-Storable >= 2.14
BuildRequires:	perl-Test-ClassAPI >= 1.02
BuildRequires:	perl-Test-Object >= 0.06
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Clone >= 0.17
Requires:	perl-Digest-MD5 >= 2.27
Requires:	perl-IO-String >= 1.07
Requires:	perl-List-MoreUtils >= 0.13
Requires:	perl-Params-Util >= 0.10
Requires:	perl-Scalar-List-Utils >= 1.18
Requires:	perl-Storable >= 2.14
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautreq	'perl(PPI::.*)'

%description
Technically, PPI is short for Parse::Perl::Isolated. In
acknowledgement that someone may some day come up with a valid
solution for the grammar problem, it was decided to leave the
Parse::Perl namespace free.

The purpose of this parser is not to parse Perl code, but to parse
Perl documents. In most cases, a single file is valid as both. By
treating the problem this way, we can parse a single file containing
Perl source isolated from any other resources, such as the libraries
upon which the code may depend, and without needing to run an instance
of Perl alongside or inside the parser (a possible solution for
Parse::Perl that is investigated from time to time).

%description -l pl.UTF-8
Technicznie PPI to skrót od Parse::Perl::Isolated. Ze świadomością, że
pewnego dnia ktoś może poprawnie rozwiązać problem gramatyki,
zadecydowano o pozostawieniu wolnej przestrzeni nazw Parse::Perl.

Celem tego parsera nie jest parsowanie kodu Perla, ale parsowanie
dokumentów Perla. W większości przypadków jeden plik jest poprawny w
obu zastosowaniach. Traktując problem w ten sposób, można
przeanalizować jeden plik zawierający źródło Perla w odłączeniu od
wszystkich innych zasobów, takich jak biblioteki, na których polega
kod, i bez potrzeby uruchamiania instancji Perla obok lub wewnątrz
parsera (możliwe rozwiązanie Parse::Perl badane od czasu do czasu).

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--skipdeps

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
