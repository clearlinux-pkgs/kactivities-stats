#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kactivities-stats
Version  : 5.69.0
Release  : 30
URL      : https://download.kde.org/stable/frameworks/5.69/kactivities-stats-5.69.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.69/kactivities-stats-5.69.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.69/kactivities-stats-5.69.0.tar.xz.sig
Summary  : A library for accessing the usage data collected by the activities system
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kactivities-stats-data = %{version}-%{release}
Requires: kactivities-stats-lib = %{version}-%{release}
Requires: kactivities-stats-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-dev

%description
# KActivitiesStats
Library to access the usage statistics data collected by the KDE activity manager.

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
%setup -q -n kactivities-stats-5.69.0
cd %{_builddir}/kactivities-stats-5.69.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586873398
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1586873398
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kactivities-stats
cp %{_builddir}/kactivities-stats-5.69.0/COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/kactivities-stats/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/kactivities-stats-5.69.0/COPYING.LGPL-2.1 %{buildroot}/usr/share/package-licenses/kactivities-stats/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/kactivities-stats-5.69.0/COPYING.LGPL-3 %{buildroot}/usr/share/package-licenses/kactivities-stats/f45ee1c765646813b442ca58de72e20a64a7ddba
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kactivities-stats.categories

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
/usr/lib64/libKF5ActivitiesStats.so.5.69.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kactivities-stats/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/kactivities-stats/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/kactivities-stats/f45ee1c765646813b442ca58de72e20a64a7ddba
