Name: rkdeveloptool
Version: 1.3.20180731
Release: 3
Source0: https://github.com/rockchip-linux/rkdeveloptool/archive/%{name}-master.tar.gz
Group: Development/Tools
License: GPLv2
Summary: Tool for flashing Rockchip devices
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: pkgconfig(libusb-1.0)

%description
Tool for flashing Rockchip devices

%prep
%autosetup -p1 -n %{name}-master
aclocal
autoheader
automake -a
autoconf
%configure

%build
%make

%install
%make_install
mkdir -p %{buildroot}/lib/udev/rules.d
cp *.rules %{buildroot}/lib/udev/rules.d

%files
%license license.txt
%{_bindir}/rkdeveloptool
/lib/udev/rules.d/*
