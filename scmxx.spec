Summary:	Exchange data SCMxx and Siemens mobile phones
Summary(pl):	Wymiana danych z urz±dzeniami SCMxx i telefonami Siemens
Name:		scmxx
Version:	0.7.4
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/sourceforge/scmxx/%{name}-%{version}.tar.bz2
# Source0-md5:	3139f8ce4da47b684851fed208e6d41e
URL:		http://www.hendrik-sattler.de/scmxx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCMxx is a console program that allows you to exchange certain types
of data with mobile phones made by Siemens. Some of the data types
that can be exchanged are logos, ring tones, vCalendars, phonebook
entries, and SMS messages. It works with the following models: S25,
S35i, M35i and C35i, SL45, S45 and ME45 and probably others.

%description -l pl
SCMxx jest programem który umo¿liwia wymianê niektórych typów
informacji z telefonami komórkowymi produkcji Siemensa, w
szczególno¶ci logo, dzwonki, wpisy kalendarza i ksi±¿ki telefonicznej,
SMSy. Dzia³a z nastêpuj±cymi modelami: S25, S35i, M35i, C35i, SL45,
S45, ME45 i prawdopodobnie innymi.

%prep
%setup  -q

%build
%configure
%{__make} CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG BUGS AUTHORS TODO docs examples contrib
%attr(755,root,root) %{_bindir}/scmxx
%{_mandir}/man1/%{name}.1*
