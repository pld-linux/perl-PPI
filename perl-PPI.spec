#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PPI
Summary:	PPI - parse and manipulate Perl code non-destructively, without using perl itself
Summary(pl):	PPI - parsowanie i manipulacja kodem Perla w sposób niedestruktywny, bez u¿ycia Perla jako takiego
Name:		perl-%{pdir}
Version:	0.991
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AD/ADAMK/%{pdir}-%{version}.tar.gz
# Source0-md5:	750b2bde8aef41abb591b0fb0925b24c
URL:		http://search.cpan.org/dist/PPI/
%if %{with tests}
BuildRequires:	perl-Class-Autouse >= 1.04
BuildRequires:	perl-Clone >= 0.13
BuildRequires:	perl-ExtUtils-AutoInstall >= 0.49
BuildRequires:	perl-File-Slurp >= 9999.04
BuildRequires:	perl-IO-stringy >= 2.105
BuildRequires:	perl-List-MoreUtils >= 0.04
BuildRequires:	perl-Params-Util >= 0.05
BuildRequires:	perl-Test-ClassAPI >= 1.02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Technicznie PPI to skrót od Parse::Perl::Isolated. Ze ¶wiadomo¶ci±, ¿e
pewnego dnia kto¶ mo¿e poprawnie rozwi±zaæ problem gramatyki,
zadecydowano o pozostawieniu wolnej przestrzeni nazw Parse::Perl.

Celem tego parsera nie jest parsowanie kodu Perla, ale parsowanie
dokumentów Perla. W wiêkszo¶ci przypadków jeden plik jest poprawny w
obu zastosowaniach. Traktuj±c problem w ten sposób, mo¿na
przeanalizowaæ jeden plik zawieraj±cy ¼ród³o Perla w od³±czeniu od
wszystkich innych zasobów, takich jak biblioteki, na których polega
kod, i bez potrzeby uruchamiania instancji Perla obok lub wewn±trz
parsera (mo¿liwe rozwi±zanie Parse::Perl badane od czasu do czasu).

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
