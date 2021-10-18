#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kontact
Version  : 21.08.2
Release  : 25
URL      : https://download.kde.org/stable/release-service/21.08.2/src/kontact-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/kontact-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/kontact-21.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kontact-bin = %{version}-%{release}
Requires: kontact-data = %{version}-%{release}
Requires: kontact-lib = %{version}-%{release}
Requires: kontact-license = %{version}-%{release}
Requires: kontact-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : grantleetheme-dev
BuildRequires : kcmutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kmime-dev
BuildRequires : kontactinterface-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kwindowsystem-dev
BuildRequires : libkdepim-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtwebengine-dev

%description
No detailed description available

%package bin
Summary: bin components for the kontact package.
Group: Binaries
Requires: kontact-data = %{version}-%{release}
Requires: kontact-license = %{version}-%{release}

%description bin
bin components for the kontact package.


%package data
Summary: data components for the kontact package.
Group: Data

%description data
data components for the kontact package.


%package doc
Summary: doc components for the kontact package.
Group: Documentation

%description doc
doc components for the kontact package.


%package lib
Summary: lib components for the kontact package.
Group: Libraries
Requires: kontact-data = %{version}-%{release}
Requires: kontact-license = %{version}-%{release}

%description lib
lib components for the kontact package.


%package license
Summary: license components for the kontact package.
Group: Default

%description license
license components for the kontact package.


%package locales
Summary: locales components for the kontact package.
Group: Default

%description locales
locales components for the kontact package.


%prep
%setup -q -n kontact-21.08.2
cd %{_builddir}/kontact-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634427494
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634427494
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kontact
cp %{_builddir}/kontact-21.08.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kontact/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kontact-21.08.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kontact/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kontact-21.08.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kontact/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/kontact-21.08.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kontact/e712eadfab0d2357c0f50f599ef35ee0d87534cb
pushd clr-build
%make_install
popd
%find_lang kontact

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kontact

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kontact.desktop
/usr/share/config.kcfg/kontact.kcfg
/usr/share/dbus-1/services/org.kde.kontact.service
/usr/share/icons/hicolor/128x128/apps/kontact.png
/usr/share/icons/hicolor/16x16/apps/kontact.png
/usr/share/icons/hicolor/22x22/apps/kontact.png
/usr/share/icons/hicolor/32x32/apps/kontact.png
/usr/share/icons/hicolor/48x48/apps/kontact.png
/usr/share/icons/hicolor/64x64/apps/kontact.png
/usr/share/icons/hicolor/scalable/apps/kontact.svg
/usr/share/kconf_update/kontact-15.08-kickoff.sh
/usr/share/kconf_update/kontact.upd
/usr/share/kservices5/kontactconfig.desktop
/usr/share/messageviewer/about/default/introduction_kontact.html
/usr/share/messageviewer/about/default/loading_kontact.html
/usr/share/metainfo/org.kde.kontact.appdata.xml
/usr/share/qlogging-categories5/kontact.categories
/usr/share/qlogging-categories5/kontact.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kontact/index.cache.bz2
/usr/share/doc/HTML/ca/kontact/index.docbook
/usr/share/doc/HTML/de/kontact/index.cache.bz2
/usr/share/doc/HTML/de/kontact/index.docbook
/usr/share/doc/HTML/en/kontact/calendar-sidebar-icon.png
/usr/share/doc/HTML/en/kontact/configuration-main.png
/usr/share/doc/HTML/en/kontact/configuration-starting-component.png
/usr/share/doc/HTML/en/kontact/index.cache.bz2
/usr/share/doc/HTML/en/kontact/index.docbook
/usr/share/doc/HTML/en/kontact/kaddressbook-sidebar-icon.png
/usr/share/doc/HTML/en/kontact/main-view.png
/usr/share/doc/HTML/en/kontact/menu-bar-kmail.png
/usr/share/doc/HTML/en/kontact/menu-bar-korganizer.png
/usr/share/doc/HTML/en/kontact/menu-bar-summary.png
/usr/share/doc/HTML/en/kontact/navigator-bar-kontact.png
/usr/share/doc/HTML/en/kontact/new-menu.png
/usr/share/doc/HTML/en/kontact/settings-menu-kmail.png
/usr/share/doc/HTML/en/kontact/side-pane.png
/usr/share/doc/HTML/en/kontact/summary-selection.png
/usr/share/doc/HTML/en/kontact/summary-view-calendar.png
/usr/share/doc/HTML/en/kontact/summary-view-mail.png
/usr/share/doc/HTML/en/kontact/summary-view-notes.png
/usr/share/doc/HTML/en/kontact/summary-view-repositioning.png
/usr/share/doc/HTML/en/kontact/summary-view-special-dates.png
/usr/share/doc/HTML/en/kontact/summary-view-todos.png
/usr/share/doc/HTML/en/kontact/summary-view.png
/usr/share/doc/HTML/en/kontact/todo-list-sidebar-icon.png
/usr/share/doc/HTML/es/kontact/index.cache.bz2
/usr/share/doc/HTML/es/kontact/index.docbook
/usr/share/doc/HTML/it/kontact/index.cache.bz2
/usr/share/doc/HTML/it/kontact/index.docbook
/usr/share/doc/HTML/nl/kontact/index.cache.bz2
/usr/share/doc/HTML/nl/kontact/index.docbook
/usr/share/doc/HTML/pt/kontact/index.cache.bz2
/usr/share/doc/HTML/pt/kontact/index.docbook
/usr/share/doc/HTML/pt_BR/kontact/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kontact/index.docbook
/usr/share/doc/HTML/sv/kontact/index.cache.bz2
/usr/share/doc/HTML/sv/kontact/index.docbook
/usr/share/doc/HTML/uk/kontact/index.cache.bz2
/usr/share/doc/HTML/uk/kontact/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkontactprivate.so.5
/usr/lib64/libkontactprivate.so.5.18.2
/usr/lib64/qt5/plugins/kcm_kontact.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kontact/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kontact/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kontact/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kontact/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kontact.lang
%defattr(-,root,root,-)

