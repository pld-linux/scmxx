Summary:	Exchange data SCMxx and Siemens mobile phones
Summary(pl.UTF-8):	Wymiana danych z urządzeniami SCMxx i telefonami Siemens
Name:		scmxx
Version:	0.9.0
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/scmxx/%{name}-%{version}.tar.bz2
# Source0-md5:	9ed8fe297b39ed1c4d3606e40620835e
URL:		http://www.hendrik-sattler.de/scmxx/
BuildRequires:	docbook2X
BuildRequires:	gettext-devel
BuildRequires:	libxslt-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCMxx is a console program that allows you to exchange certain types
of data with mobile phones made by Siemens. Some of the data types
that can be exchanged are logos, ring tones, vCalendars, phonebook
entries, and SMS messages. It works with the following models: S25,
S35i, M35i and C35i, SL45, S45 and ME45 and probably others.

%description -l pl.UTF-8
SCMxx jest programem który umożliwia wymianę niektórych typów
informacji z telefonami komórkowymi produkcji Siemensa, w
szczególności logo, dzwonki, wpisy kalendarza i książki telefonicznej,
SMSy. Działa z następującymi modelami: S25, S35i, M35i, C35i, SL45,
S45, ME45 i prawdopodobnie innymi.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README CHANGELOG BUGS AUTHORS TODO docs examples contrib
%attr(755,root,root) %{_bindir}/scmxx
%attr(755,root,root) %{_bindir}/adr2vcf
%attr(755,root,root) %{_bindir}/apoconv
%attr(755,root,root) %{_bindir}/smi
%{_mandir}/man1/%{name}.1*
%lang(de) %{_mandir}/de/man1/%{name}.1*
%lang(it) %{_mandir}/it/man1/%{name}.1*
%lang(ru) %{_mandir}/ru/man1/%{name}.1*
