Summary:	Exchange data SCMxx and Siemens mobile phones
Summary(pl):	Wymiana danych z urz�dzeniami SCMxx i telefonami Siemens
Name:		scmxx
Version:	0.6.0
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://www.hendrik-sattler.de/scmxx/download/%{name}-%{version}.tar.bz2
URL:		http://www.hendrik-sattler.de/scmxx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCMxx is a console program that allows you to exchange certain types
of data with mobile phones made by Siemens. Some of the data types
that can be exchanged are logos, ring tones, vCalendars, phonebook
entries, and SMS messages. It works with the following models: S25,
S35i, M35i and C35i, SL45, S45 and ME45 and probably others.

%description -l pl
SCMxx jest programem kt�ry umo�liwia wymian� niekt�rych typ�w
informacji z telefonami kom�rkowymi produkcji Siemensa, w
szczeg�lno�ci logo, dzwonki, wpisy kalendarza i ksi��ki telefoncznej,
SMSy. Dzia�a z nast�puj�cymi modelami: S25, S35i, M35i, C35i, SL45,
S45, ME45 i prawdopodobnie innymi.

%prep
%setup  -q

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv docs/README docs/README.info

gzip -9nf README CHANGELOG BUGS AUTHORS TODO docs/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.gz examples contrib
%attr(755,root,root) %{_bindir}/scmxx
