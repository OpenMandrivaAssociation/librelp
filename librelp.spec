%define major 0
%define libname %mklibname relp %{major}
%define devname %mklibname relp -d

Summary:	Reliable Event Logging Protocol (RELP) library
Name:		librelp
Version:	1.12.0
Release:	1
License:	GPLv3+
Group:		System/Libraries
Url:		https://www.librelp.com/
Source0:	http://download.rsyslog.com/librelp/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(openssl)

%description
librelp is an easy to use library for the RELP protocol. RELP in turn provides
reliable event logging over the network (and consequently RELP stands for
Reliable Event Logging Protocol). RELP was initiated by Rainer Gerhards after
he was finally upset by the lossy nature of plain tcp syslog and wanted a cure
for all these dangling issues.

%package -n %{libname}
Summary:	Reliable Event Logging Protocol (RELP) library
Group:		System/Libraries

%description -n %{libname}
librelp is an easy to use library for the RELP protocol. RELP in turn provides
reliable event logging over the network (and consequently RELP stands for
Reliable Event Logging Protocol). RELP was initiated by Rainer Gerhards after
he was finally upset by the lossy nature of plain tcp syslog and wanted a cure
for all these dangling issues.

%package -n %{devname}
Summary:	Development files for the %{libname} library
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	relp-devel = %{version}-%{release}

%description -n %{devname}
Development files for the %{libname} library.

%prep
%autosetup -p1

%build
%configure \
	--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/librelp.so.%{major}*

%files -n %{devname}
%doc ChangeLog doc/*.html
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
