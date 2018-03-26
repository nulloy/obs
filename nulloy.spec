Name:          nulloy
URL:           http://nulloy.com
License:       GPLv3
Summary:       Music player with a waveform progress bar
Version:       _DUMMY_
Release:       0
Source:        %{name}-%{version}.tar.gz
%if 0%{?fedora_version} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: qt-devel gcc-c++
%else
BuildRequires: libqt-devel
%endif
BuildRequires: gstreamer1-devel gstreamer1-plugins-base-devel zip libX11-devel taglib-devel
BuildRoot:     %{_topdir}/%{name}-%{version}-root

%description
Music player with a waveform progress bar.

%global debug_package %{nil}

%prep
%setup -q

%build
%if 0%{?fedora_version} || 0%{?fedora}
%define QMAKE qmake-qt4
%define LRELEASE lrelease-qt4
%else
%define QMAKE qmake
%define LRELEASE lrelease
%endif
# provided by _service:download_url:ChangeLog:
cp ../../SOURCES/ChangeLog .
QMAKE=%{QMAKE} LRELEASE=%{LRELEASE} ./configure --no-update-check --prefix %{buildroot}%{_prefix}
make

%install
make install

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}/skins/*
%{_datadir}/%{name}/i18n/*
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%{_prefix}/lib/%{name}/plugins/

%changelog
