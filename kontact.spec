#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kontact
Version  : 25.04.2
Release  : 110
URL      : https://download.kde.org/stable/release-service/25.04.2/src/kontact-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/kontact-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/kontact-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kontact-bin = %{version}-%{release}
Requires: kontact-data = %{version}-%{release}
Requires: kontact-lib = %{version}-%{release}
Requires: kontact-license = %{version}-%{release}
Requires: kontact-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : grantleetheme-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : kontactinterface-dev
BuildRequires : ktextaddons-dev
BuildRequires : libkdepim-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
BuildRequires : qt6webengine-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kontact-25.04.2
cd %{_builddir}/kontact-25.04.2
pushd ..
cp -a kontact-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749574255
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749574255
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kontact
cp %{_builddir}/kontact-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kontact/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kontact-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kontact/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kontact-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kontact/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kontact-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kontact/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kontact-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kontact/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kontact-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kontact/20079e8f79713dce80ab09774505773c926afa2a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kontact
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kontact
/usr/bin/kontact

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kontact.desktop
/usr/share/config.kcfg/kontact.kcfg
/usr/share/dbus-1/services/org.kde.kontact.service
/usr/share/icons/hicolor/128x128/apps/kontact.png
/usr/share/icons/hicolor/144x144/apps/kontact.png
/usr/share/icons/hicolor/16x16/apps/kontact.png
/usr/share/icons/hicolor/22x22/apps/kontact.png
/usr/share/icons/hicolor/32x32/apps/kontact.png
/usr/share/icons/hicolor/44x44/apps/kontact.png
/usr/share/icons/hicolor/48x48/apps/kontact.png
/usr/share/icons/hicolor/64x64/apps/kontact.png
/usr/share/icons/hicolor/scalable/apps/kontact.svg
/usr/share/messageviewer/about/default/introduction_kontact.html
/usr/share/messageviewer/about/default/loading_kontact.html
/usr/share/metainfo/org.kde.kontact.appdata.xml
/usr/share/qlogging-categories6/kontact.categories
/usr/share/qlogging-categories6/kontact.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kontact/index.cache.bz2
/usr/share/doc/HTML/ca/kontact/index.docbook
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
/usr/share/doc/HTML/pt_BR/kontact/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kontact/index.docbook
/usr/share/doc/HTML/ru/kontact/index.cache.bz2
/usr/share/doc/HTML/ru/kontact/index.docbook
/usr/share/doc/HTML/sl/kontact/index.cache.bz2
/usr/share/doc/HTML/sl/kontact/index.docbook
/usr/share/doc/HTML/sv/kontact/index.cache.bz2
/usr/share/doc/HTML/sv/kontact/index.docbook
/usr/share/doc/HTML/uk/kontact/index.cache.bz2
/usr/share/doc/HTML/uk/kontact/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkontactprivate.so.6.4.2
/V3/usr/lib64/qt6/plugins/pim6/kcms/kontact/kcm_kontact.so
/usr/lib64/libkontactprivate.so.6
/usr/lib64/libkontactprivate.so.6.4.2
/usr/lib64/qt6/plugins/pim6/kcms/kontact/kcm_kontact.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kontact/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kontact/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kontact/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kontact/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kontact/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kontact.lang
%defattr(-,root,root,-)

