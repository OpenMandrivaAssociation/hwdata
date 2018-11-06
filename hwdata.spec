Summary:	Hardware identification and configuration data
Name:		hwdata
Version:	0.317
Release:	1
License:	GPLv2+
URL:		https://github.com/vcrhonek/hwdata
Source0:	https://github.com/vcrhonek/hwdata/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch
Obsoletes:	ldetect-lst < 0.1.339
Provides:	ldetect-lst = 0.1.339

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%prep
%autosetup -p1
%configure

%build
# nothing to build

%install
make install DESTDIR=%{buildroot} libdir=%{_prefix}/lib

%files
%doc LICENSE COPYING
%dir %{_datadir}/%{name}
%{_prefix}/lib/modprobe.d/dist-blacklist.conf
%{_datadir}/%{name}/*
