Name: bb
Summary: AA demo
Version: 1.3.0
Release: %mkrel 10
Source: %{name}-%{version}.tar.bz2 
Patch1: %{name}-1.3.0-timer.patch
Group: Games/Other
URL: http://aa-project.sourceforge.net/aalib/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	aalib-devel
BuildRequires:	libmikmod-devel
License: GPLv2+

%description
BB is a portable demo based on AAlib

%prep
%setup -q
%patch1 -p0 -b .timers

%build
%configure 
%make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
%makeinstall 

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*


