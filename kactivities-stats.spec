#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kactivities-stats
Version  : 5.83.0
Release  : 40
URL      : https://download.kde.org/stable/frameworks/5.83/kactivities-stats-5.83.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.83/kactivities-stats-5.83.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.83/kactivities-stats-5.83.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kactivities-stats-data = %{version}-%{release}
Requires: kactivities-stats-lib = %{version}-%{release}
Requires: kactivities-stats-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-dev

%description
# Commit policy
Every non-trivial patch must go through the review before it goes into the
master branch.

%package data
Summary: data components for the kactivities-stats package.
Group: Data

%description data
data components for the kactivities-stats package.


%package dev
Summary: dev components for the kactivities-stats package.
Group: Development
Requires: kactivities-stats-lib = %{version}-%{release}
Requires: kactivities-stats-data = %{version}-%{release}
Provides: kactivities-stats-devel = %{version}-%{release}
Requires: kactivities-stats = %{version}-%{release}

%description dev
dev components for the kactivities-stats package.


%package lib
Summary: lib components for the kactivities-stats package.
Group: Libraries
Requires: kactivities-stats-data = %{version}-%{release}
Requires: kactivities-stats-license = %{version}-%{release}

%description lib
lib components for the kactivities-stats package.


%package license
Summary: license components for the kactivities-stats package.
Group: Default

%description license
license components for the kactivities-stats package.


%prep
%setup -q -n kactivities-stats-5.83.0
cd %{_builddir}/kactivities-stats-5.83.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623649656
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623649656
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kactivities-stats
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kactivities-stats-5.83.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kactivities-stats/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kactivities-stats.categories
/usr/share/qlogging-categories5/kactivities-stats.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KActivitiesStats/KActivities/Stats/Cleaning
/usr/include/KF5/KActivitiesStats/KActivities/Stats/Query
/usr/include/KF5/KActivitiesStats/KActivities/Stats/ResultModel
/usr/include/KF5/KActivitiesStats/KActivities/Stats/ResultSet
/usr/include/KF5/KActivitiesStats/KActivities/Stats/ResultWatcher
/usr/include/KF5/KActivitiesStats/KActivities/Stats/Terms
/usr/include/KF5/KActivitiesStats/kactivitiesstats/cleaning.h
/usr/include/KF5/KActivitiesStats/kactivitiesstats/kactivitiesstats_export.h
/usr/include/KF5/KActivitiesStats/kactivitiesstats/query.h
/usr/include/KF5/KActivitiesStats/kactivitiesstats/resultmodel.h
/usr/include/KF5/KActivitiesStats/kactivitiesstats/resultset.h
/usr/include/KF5/KActivitiesStats/kactivitiesstats/resultwatcher.h
/usr/include/KF5/KActivitiesStats/kactivitiesstats/terms.h
/usr/include/KF5/kactivitiesstats_version.h
/usr/lib64/cmake/KF5ActivitiesStats/KF5ActivitiesStatsConfig.cmake
/usr/lib64/cmake/KF5ActivitiesStats/KF5ActivitiesStatsConfigVersion.cmake
/usr/lib64/cmake/KF5ActivitiesStats/KF5ActivitiesStatsLibraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5ActivitiesStats/KF5ActivitiesStatsLibraryTargets.cmake
/usr/lib64/libKF5ActivitiesStats.so
/usr/lib64/pkgconfig/libKActivitiesStats.pc
/usr/lib64/qt5/mkspecs/modules/qt_KActivitiesStats.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5ActivitiesStats.so.1
/usr/lib64/libKF5ActivitiesStats.so.5.83.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kactivities-stats/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kactivities-stats/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kactivities-stats/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kactivities-stats/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kactivities-stats/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kactivities-stats/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kactivities-stats/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kactivities-stats/e712eadfab0d2357c0f50f599ef35ee0d87534cb
