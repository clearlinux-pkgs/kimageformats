#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kimageformats
Version  : 5.69.0
Release  : 29
URL      : https://download.kde.org/stable/frameworks/5.69/kimageformats-5.69.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.69/kimageformats-5.69.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.69/kimageformats-5.69.0.tar.xz.sig
Summary  : Image format plugins for Qt5
Group    : Development/Tools
License  : LGPL-2.1
Requires: kimageformats-data = %{version}-%{release}
Requires: kimageformats-lib = %{version}-%{release}
Requires: kimageformats-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)

%description
# KImageFormats
Plugins to allow QImage to support extra file formats.
## Introduction

%package data
Summary: data components for the kimageformats package.
Group: Data

%description data
data components for the kimageformats package.


%package lib
Summary: lib components for the kimageformats package.
Group: Libraries
Requires: kimageformats-data = %{version}-%{release}
Requires: kimageformats-license = %{version}-%{release}

%description lib
lib components for the kimageformats package.


%package license
Summary: license components for the kimageformats package.
Group: Default

%description license
license components for the kimageformats package.


%prep
%setup -q -n kimageformats-5.69.0
cd %{_builddir}/kimageformats-5.69.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586876873
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
export SOURCE_DATE_EPOCH=1586876873
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kimageformats
cp %{_builddir}/kimageformats-5.69.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kimageformats/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/qimageioplugins/dds.desktop
/usr/share/kservices5/qimageioplugins/eps.desktop
/usr/share/kservices5/qimageioplugins/exr.desktop
/usr/share/kservices5/qimageioplugins/hdr.desktop
/usr/share/kservices5/qimageioplugins/jp2.desktop
/usr/share/kservices5/qimageioplugins/kra.desktop
/usr/share/kservices5/qimageioplugins/ora.desktop
/usr/share/kservices5/qimageioplugins/pcx.desktop
/usr/share/kservices5/qimageioplugins/pic.desktop
/usr/share/kservices5/qimageioplugins/psd.desktop
/usr/share/kservices5/qimageioplugins/ras.desktop
/usr/share/kservices5/qimageioplugins/rgb.desktop
/usr/share/kservices5/qimageioplugins/tga.desktop
/usr/share/kservices5/qimageioplugins/xcf.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/imageformats/kimg_eps.so
/usr/lib64/qt5/plugins/imageformats/kimg_exr.so
/usr/lib64/qt5/plugins/imageformats/kimg_hdr.so
/usr/lib64/qt5/plugins/imageformats/kimg_kra.so
/usr/lib64/qt5/plugins/imageformats/kimg_ora.so
/usr/lib64/qt5/plugins/imageformats/kimg_pcx.so
/usr/lib64/qt5/plugins/imageformats/kimg_pic.so
/usr/lib64/qt5/plugins/imageformats/kimg_psd.so
/usr/lib64/qt5/plugins/imageformats/kimg_ras.so
/usr/lib64/qt5/plugins/imageformats/kimg_rgb.so
/usr/lib64/qt5/plugins/imageformats/kimg_tga.so
/usr/lib64/qt5/plugins/imageformats/kimg_xcf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kimageformats/9a1929f4700d2407c70b507b3b2aaf6226a9543c
