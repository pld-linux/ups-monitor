Summary:	A graphical UPS monitor for the GNOME desktop
Summary(pl):	Graficzny monitor UPS-a dla ¶rodowiska GNOME
Name:		ups-monitor
Vendor:		Amauta
Version:	0.1 
Release:	0.1 
License:	GPL
Group:		System/Monitoring
Source:		http://freshmeat.net/redir/ups-monitor/51922/url_tgz/%{name}-%{version}.tar.gz
URL:		http://www.amautacorp.com/
Requires:	python-pygtk >= 2.0.0
Requires:	python-pygtk-glade >= 2.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UPS monitor is a graphical application that lets you monitor your UPS
in real-time.  You can check locally attached UPSs or networked UPS.

UPS monitor requires a working Network UPS Tools (nut) server.

%description -l pl
UPS monitor jest graficzn± aplikacj± pozwalaj±c± monitorowaæ UPS w
czasie rzeczywistym. Obs³uguje zarówno lokalny jak i sieciowy UPS.

UPS monitor wymaga serwer Network UPS Tools (nut).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -D -m 755 ups-monitor $RPM_BUILD_ROOT%{_bindir}/ups-monitor
install -D -m 644 ups-monitor.glade $RPM_BUILD_ROOT%{_datadir}/ups-monitor/ups-monitor.glade
install -D -m 644 ups-monitor.gladep $RPM_BUILD_ROOT%{_datadir}/ups-monitor/ups-monitor.gladep
install -D -m 644 battery-level.png $RPM_BUILD_ROOT%{_datadir}/ups-monitor/battery-level.png
install -D -m 644 load.png $RPM_BUILD_ROOT%{_datadir}/ups-monitor/load.png
install -D -m 644 remaining-time.png $RPM_BUILD_ROOT%{_datadir}/ups-monitor/remaining-time.png
install -D -m 644 ups-monitor.png $RPM_BUILD_ROOT%{_datadir}/ups-monitor/ups-monitor.png
install -D -m 644 ups-monitor.png $RPM_BUILD_ROOT%{_pixmapsdir}/ups-monitor.png
install -D -m 644 ups-monitor.desktop $RPM_BUILD_ROOT%{_desktopdir}/ups-monitor.desktop

%files
%defattr(644,root,root,755)
%doc README TODO version
%attr(755,root,root) %{_bindir}/ups-monitor
%{_datadir}/ups-monitor
%{_pixmapsdir}/ups-monitor.png
%{_desktopdir}/ups-monitor.desktop
