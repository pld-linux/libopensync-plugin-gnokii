Summary:	OpenSync gnokii plugin
Summary(pl.UTF-8):	Wtyczka gnokii do OpenSync
Name:		libopensync-plugin-gnokii
Version:	0.22
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	6a5b6c1753508801c4b03333f2a33542
#Patch0:		%{name}.patch
U31RL:		http://www.opensync.org/
BuildRequires:	gnokii >= 0.6.14
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel
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
#%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%attr(755,root,root) %{_libdir}/opensync/formats/*.so
%{_libdir}/opensync/formats/*.la
%{_datadir}/opensync/defaults/*
