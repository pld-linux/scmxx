Summary:	Tool to edit almost all Siemens mobile phones
Summary(pl):	Narz�dzie do edycji praktycznie ka�dego rodzaju telefonu kom�rkowego Siemens
Name:		scmxx
Version:	0.5.7
Release:	0
License:	GPL
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
Source0:	http://www.hendrik-sattler.de/scmxx/download/%{name}-%{version}.tar.bz2
URL:		http://www.hendrik-sattler.de/scmxx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCMXX is a tool that allows editing your Siemens cell phone in many
ways. You can download and upload phone books, bitmaps, midi files.
Also it is possible to check current parameters of your phone,
synchronize its clock, send and get SMS messages.

%description -l tr
SCMXX jest narz�dziem pozwalaj�cym na edycj� telefonu kom�rkowego
marki Siemens na wiele r�nych sposob�w. Dzi�ki niemu mo�esz �ci�ga�
oraz wgrywa� ksi��ki telefoniczne, obrazki, melodie. Jest tak�e
mo�liwe sprawdzenie aktualnych parametr�w Twojego telefonu,
synchronizacja zegara oraz wysy�anie i odbior wiadomo�ci SMS.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGELOG BUGS AUTHORS TODO docs/gsmcharset.txt docs/scmxx.1

install docs/scmxx.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.gz docs/gsmcharset.txt.gz examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/scmxx
%{_mandir}/man1/scmxx.1.gz