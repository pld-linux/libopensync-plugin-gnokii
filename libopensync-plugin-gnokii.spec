Summary:	OpenSync gnokii plugin
Summary(pl.UTF-8):	Wtyczka gnokii do OpenSync
Name:		libopensync-plugin-gnokii
Version:	0.36
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.opensync.org/download/releases/0.36/%{name}-%{version}
# Source0-md5:	72a9d96cccdc49b23ad371f0c566031d
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libgnokii-devel >= 0.6.14
BuildRequires:	libopensync-devel >= 1:%{version}
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
mkdir build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync-1.0/plugins/gnokii-sync.so
%attr(755,root,root) %{_libdir}/opensync-1.0/formats/gnokii-*.so
%{_datadir}/opensync-1.0/defaults/gnokii-sync

# devel
#%{_includedir}/opensync-1.0/opensync/gnokii_*.h
