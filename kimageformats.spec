#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kimageformats
Version  : 6.10.0
Release  : 108
URL      : https://download.kde.org/stable/frameworks/6.10/kimageformats-6.10.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.10/kimageformats-6.10.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.10/kimageformats-6.10.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kimageformats-lib = %{version}-%{release}
Requires: kimageformats-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : libavif-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(OpenEXR)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KImageFormats
Plugins to allow [`QImage`](https://doc.qt.io/qt-6/qimage.html) to support
extra file formats.

%package lib
Summary: lib components for the kimageformats package.
Group: Libraries
Requires: kimageformats-license = %{version}-%{release}

%description lib
lib components for the kimageformats package.


%package license
Summary: license components for the kimageformats package.
Group: Default

%description license
license components for the kimageformats package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kimageformats-6.10.0
cd %{_builddir}/kimageformats-6.10.0
pushd ..
cp -a kimageformats-6.10.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736542273
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
%cmake .. -DKIMAGEFORMATS_HEIF=OFF  -G 'Unix Makefiles'
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
%cmake .. -DKIMAGEFORMATS_HEIF=OFF  -G 'Unix Makefiles'
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
export SOURCE_DATE_EPOCH=1736542273
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kimageformats
cp %{_builddir}/kimageformats-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kimageformats/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kimageformats/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kimageformats/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kimageformats/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kimageformats/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kimageformats/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kimageformats/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kimageformats/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kimageformats-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kimageformats/e458941548e0864907e654fa2e192844ae90fc32 || :
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/imageformats/kimg_ani.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_avif.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_dds.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_eps.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_exr.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_hdr.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_kra.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_ora.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_pcx.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_pfm.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_pic.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_psd.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_pxr.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_qoi.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_ras.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_raw.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_rgb.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_sct.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_tga.so
/V3/usr/lib64/qt6/plugins/imageformats/kimg_xcf.so
/usr/lib64/qt6/plugins/imageformats/kimg_ani.so
/usr/lib64/qt6/plugins/imageformats/kimg_avif.so
/usr/lib64/qt6/plugins/imageformats/kimg_dds.so
/usr/lib64/qt6/plugins/imageformats/kimg_eps.so
/usr/lib64/qt6/plugins/imageformats/kimg_exr.so
/usr/lib64/qt6/plugins/imageformats/kimg_hdr.so
/usr/lib64/qt6/plugins/imageformats/kimg_kra.so
/usr/lib64/qt6/plugins/imageformats/kimg_ora.so
/usr/lib64/qt6/plugins/imageformats/kimg_pcx.so
/usr/lib64/qt6/plugins/imageformats/kimg_pfm.so
/usr/lib64/qt6/plugins/imageformats/kimg_pic.so
/usr/lib64/qt6/plugins/imageformats/kimg_psd.so
/usr/lib64/qt6/plugins/imageformats/kimg_pxr.so
/usr/lib64/qt6/plugins/imageformats/kimg_qoi.so
/usr/lib64/qt6/plugins/imageformats/kimg_ras.so
/usr/lib64/qt6/plugins/imageformats/kimg_raw.so
/usr/lib64/qt6/plugins/imageformats/kimg_rgb.so
/usr/lib64/qt6/plugins/imageformats/kimg_sct.so
/usr/lib64/qt6/plugins/imageformats/kimg_tga.so
/usr/lib64/qt6/plugins/imageformats/kimg_xcf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kimageformats/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kimageformats/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kimageformats/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/kimageformats/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kimageformats/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kimageformats/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kimageformats/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kimageformats/e458941548e0864907e654fa2e192844ae90fc32
