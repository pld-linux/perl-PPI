#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PPI
Summary:	PPI - parse and manipulate Perl code non-destructively, without using perl itself
Summary(pl.UTF-8):	PPI - analiza i manipulacja kodem Perla w sposób niedestruktywny, bez użycia Perla jako takiego
Name:		perl-PPI
Version:	1.215
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AD/ADAMK/%{pdir}-%{version}.tar.gz
# Source0-md5:	7b58542e39e8a162d2f6866d7c059bae
URL:		http://search.cpan.org/dist/PPI/
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.84
BuildRequires:	perl-Class-Inspector >= 1.22
BuildRequires:	perl-Clone >= 0.30
BuildRequires:	perl-Digest-MD5 >= 2.35
BuildRequires:	perl-File-Remove >= 1.42
BuildRequires:	perl-IO-String >= 1.07
BuildRequires:	perl-List-MoreUtils >= 0.16
BuildRequires:	perl-Params-Util >= 1.00
BuildRequires:	perl-Storable >= 2.17
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-ClassAPI >= 1.02
BuildRequires:	perl-Test-NoWarnings >= 0.084
BuildRequires:	perl-Test-Object >= 0.07
BuildRequires:	perl-Test-Simple >= 0.86
BuildRequires:	perl-Test-SubCalls >= 1.07
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Clone >= 0.30
Requires:	perl-Digest-MD5 >= 2.35
Requires:	perl-IO-String >= 1.07
Requires:	perl-List-MoreUtils >= 0.16
Requires:	perl-Params-Util >= 1.00
Requires:	perl-Storable >= 2.17
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

Celem tego analizatora nie jest analiza kodu Perla, ale analiza
dokumentów Perla. W większości przypadków jeden plik jest poprawny w
obu zastosowaniach. Traktując problem w ten sposób, można
przeanalizować jeden plik zawierający źródło Perla w odłączeniu od
wszystkich innych zasobów, takich jak biblioteki, na których polega
kod, i bez potrzeby uruchamiania instancji Perla obok lub wewnątrz
analizatora (możliwe rozwiązanie Parse::Perl badane od czasu do
czasu).

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
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/PPIx

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/PPI.pm
%{perl_vendorlib}/PPI
%dir %{perl_vendorlib}/PPIx
%{_mandir}/man3/PPI*.3pm*
