#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kimageformats
Version  : 5.113.0
Release  : 86
URL      : https://download.kde.org/stable/frameworks/5.113/kimageformats-5.113.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.113/kimageformats-5.113.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.113/kimageformats-5.113.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kimageformats-data = %{version}-%{release}
Requires: kimageformats-lib = %{version}-%{release}
Requires: kimageformats-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : extra-cmake-modules-data
BuildRequires : karchive-dev
BuildRequires : libavif-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kimageformats-5.113.0
cd %{_builddir}/kimageformats-5.113.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702969342
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
%cmake .. -DKIMAGEFORMATS_HEIF=OFF
make  %{?_smp_mflags}
popd
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DKIMAGEFORMATS_HEIF=OFF
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1702969342
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kimageformats
cp %{_builddir}/kimageformats-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kimageformats/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kimageformats/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kimageformats/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kimageformats/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kimageformats/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kimageformats/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kimageformats/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/qimageioplugins/ani.desktop
/usr/share/kservices5/qimageioplugins/avif.desktop
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
/usr/share/kservices5/qimageioplugins/qoi.desktop
/usr/share/kservices5/qimageioplugins/ras.desktop
/usr/share/kservices5/qimageioplugins/raw.desktop
/usr/share/kservices5/qimageioplugins/rgb.desktop
/usr/share/kservices5/qimageioplugins/tga.desktop
/usr/share/kservices5/qimageioplugins/xcf.desktop

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/imageformats/kimg_ani.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_avif.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_eps.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_exr.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_hdr.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_kra.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_ora.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_pcx.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_pic.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_psd.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_qoi.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_ras.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_raw.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_rgb.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_tga.so
/V3/usr/lib64/qt5/plugins/imageformats/kimg_xcf.so
/usr/lib64/qt5/plugins/imageformats/kimg_ani.so
/usr/lib64/qt5/plugins/imageformats/kimg_avif.so
/usr/lib64/qt5/plugins/imageformats/kimg_eps.so
/usr/lib64/qt5/plugins/imageformats/kimg_exr.so
/usr/lib64/qt5/plugins/imageformats/kimg_hdr.so
/usr/lib64/qt5/plugins/imageformats/kimg_kra.so
/usr/lib64/qt5/plugins/imageformats/kimg_ora.so
/usr/lib64/qt5/plugins/imageformats/kimg_pcx.so
/usr/lib64/qt5/plugins/imageformats/kimg_pic.so
/usr/lib64/qt5/plugins/imageformats/kimg_psd.so
/usr/lib64/qt5/plugins/imageformats/kimg_qoi.so
/usr/lib64/qt5/plugins/imageformats/kimg_ras.so
/usr/lib64/qt5/plugins/imageformats/kimg_raw.so
/usr/lib64/qt5/plugins/imageformats/kimg_rgb.so
/usr/lib64/qt5/plugins/imageformats/kimg_tga.so
/usr/lib64/qt5/plugins/imageformats/kimg_xcf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kimageformats/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kimageformats/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kimageformats/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kimageformats/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kimageformats/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kimageformats/e458941548e0864907e654fa2e192844ae90fc32
