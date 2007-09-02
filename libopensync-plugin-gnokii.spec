Summary:	OpenSync gnokii plugin
Summary(pl.UTF-8):	Wtyczka gnokii do OpenSync
Name:		libopensync-plugin-gnokii
Version:	0.22
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	6a5b6c1753508801c4b03333f2a33542
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libgnokii-devel >= 0.6.14
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains gnokii plugin for OpenSync framework (to
synchronize with mobile phones).

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę gnokii (do synchronizacji z telefonami
komórkowymi) dla szkieletu OpenSync.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/{plugins,formats}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/opensync/plugins/gnokii_sync.so
%attr(755,root,root) %{_libdir}/opensync/formats/gnokii.so
%{_datadir}/opensync/defaults/gnokii-sync

# devel
#%{_includedir}/opensync-1.0/opensync/gnokii_*.h
