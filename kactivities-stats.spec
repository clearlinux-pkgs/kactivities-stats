#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kactivities-stats
Version  : 5.48.0
Release  : 1
URL      : https://download.kde.org/stable/frameworks/5.48/kactivities-stats-5.48.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.48/kactivities-stats-5.48.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.0 LGPL-2.1
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
# Commit policy
Every non-trivial patch must go through the review before it goes into the
master branch.

%prep
%setup -q -n kactivities-stats-5.48.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532297772
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1532297772
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
