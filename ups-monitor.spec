# TODO:
# - .desktop
Summary:	A graphical UPS monitor for the GNOME desktop
Summary(pl):	Graficzny monitor UPS-a dla ¶rodowiska GNOME
Name:		ups-monitor
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.amautacorp.com/staff/Rudd-O/ups-monitor/files/%{name}-%{version}.tar.gz
# Source0-md5:	dadb371842fc82b82d88df18417dd2a9
URL:		http://www.amautacorp.com/staff/Rudd-O/ups-monitor/
Requires:	python-pygtk >= 2.0.0
Requires:	python-pygtk-glade >= 2.0.0
Requires:	nut
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UPS monitor is a graphical application that lets you monitor your UPS
in real-time. You can check locally attached UPSs or networked UPS.

UPS monitor requires a working Network UPS Tools (nut) server.

%description -l pl
UPS monitor jest graficzn± aplikacj± pozwalaj±c± monitorowaæ UPS w
czasie rzeczywistym. Obs³uguje zarówno lokalny jak i sieciowy UPS.

UPS monitor wymaga serwer Network UPS Tools (nut).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir}}

install	%{name}			$RPM_BUILD_ROOT%{_bindir}
install	%{name}.glade*		$RPM_BUILD_ROOT%{_datadir}/ups-monitor
install	*.png			$RPM_BUILD_ROOT%{_datadir}/ups-monitor
install	%{name}.png		$RPM_BUILD_ROOT%{_pixmapsdir}
#install	%{name}.desktop		$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/ups-monitor
%{_datadir}/%{name}
%{_pixmapsdir}/*
#%{_desktopdir}/*
