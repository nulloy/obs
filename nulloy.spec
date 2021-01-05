Name:          nulloy
URL:           http://nulloy.com
License:       GPLv3
Summary:       Music player with a waveform progress bar
Version:       _DUMMY_
Release:       0
Source:        %{name}-%{version}.tar.gz
BuildRequires: gcc-c++ qt5-qtbase-devel qt5-qttools-devel qt5-qttools-static qt5-qtscript-devel qt5-qtbase-private-devel qt5-linguist gstreamer1-devel gstreamer1-plugins-base-devel zip libX11-devel taglib-devel
BuildRoot:     %{_topdir}/%{name}-%{version}-root

%description
Music player with a waveform progress bar.

%global debug_package %{nil}

%prep
%setup -q

%build
# provided by _service:download_url:ChangeLog:
cp ../../SOURCES/ChangeLog .
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
QMAKE=qmake-qt5 \
LRELEASE=lrelease-qt5 \
./configure --no-update-check --prefix %{buildroot}%{_prefix}
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
