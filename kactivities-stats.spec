#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kactivities-stats
Version  : 5.56.0
Release  : 14
URL      : https://download.kde.org/stable/frameworks/5.56/kactivities-stats-5.56.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.56/kactivities-stats-5.56.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.56/kactivities-stats-5.56.0.tar.xz.sig
Summary  : A library for accessing the usage data collected by the activities system
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kactivities-stats-lib = %{version}-%{release}
Requires: kactivities-stats-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-dev

%description
# KActivitiesStats
Library to access the usage statistics data collected by the KDE activity manager.

%package dev
Summary: dev components for the kactivities-stats package.
Group: Development
Requires: kactivities-stats-lib = %{version}-%{release}
Provides: kactivities-stats-devel = %{version}-%{release}
Requires: kactivities-stats = %{version}-%{release}

%description dev
dev components for the kactivities-stats package.


%package lib
Summary: lib components for the kactivities-stats package.
Group: Libraries
Requires: kactivities-stats-license = %{version}-%{release}

%description lib
lib components for the kactivities-stats package.


%package license
Summary: license components for the kactivities-stats package.
Group: Default

%description license
license components for the kactivities-stats package.


%prep
%setup -q -n kactivities-stats-5.56.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552159864
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1552159864
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kactivities-stats
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/kactivities-stats/COPYING.LGPL-2
cp COPYING.LGPL-2.1 %{buildroot}/usr/share/package-licenses/kactivities-stats/COPYING.LGPL-2.1
cp COPYING.LGPL-3 %{buildroot}/usr/share/package-licenses/kactivities-stats/COPYING.LGPL-3
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

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
/usr/lib64/libKF5ActivitiesStats.so.5.56.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kactivities-stats/COPYING.LGPL-2
/usr/share/package-licenses/kactivities-stats/COPYING.LGPL-2.1
/usr/share/package-licenses/kactivities-stats/COPYING.LGPL-3
