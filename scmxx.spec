Summary:	Tool to edit almost all Siemens mobile phones
Summary(pl):	Narzêdzie do edycji praktycznie ka¿dego rodzaju telefonu komórkowego Siemens
Name:		scmxx
Version:	0.6.0
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://www.hendrik-sattler.de/scmxx/download/%{name}-%{version}.tar.bz2
Patch0:		%{name}-destdir.patch
URL:		http://www.hendrik-sattler.de/scmxx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCMXX is a tool that allows editing your Siemens cell phone in many
ways. You can download and upload phone books, bitmaps, midi files.
Also it is possible to check current parameters of your phone,
synchronize its clock, send and get SMS messages.

%description -l pl
SCMXX jest narzêdziem pozwalaj±cym na edycjê telefonu komórkowego
marki Siemens na wiele ró¿nych sposobów. Dziêki niemu mo¿esz ¶ci±gaæ
oraz wgrywaæ ksi±¿ki telefoniczne, obrazki, melodie. Jest tak¿e
mo¿liwe sprawdzenie aktualnych parametrów Twojego telefonu,
synchronizacja zegara oraz wysy³anie i odbior wiadomo¶ci SMS.

%prep
%setup  -q
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

#install docs/scmxx.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README CHANGELOG BUGS AUTHORS TODO docs/gsmcharset.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/gsmcharset.txt.gz examples
%attr(755,root,root) %{_bindir}/scmxx
#%{_mandir}/man1/scmxx.1*
