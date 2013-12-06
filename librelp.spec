%define	major	0
%define libname	%mklibname relp %{major}
%define devname	%mklibname relp -d

Summary:	Reliable Event Logging Protocol (RELP) library
Name:		librelp
Version:	1.2.0
Release:	3
License:	GPLv3+
Group:		System/Libraries
Url:		http://www.librelp.com/
Source0:	http://download.rsyslog.com/librelp/%{name}-%{version}.tar.gz

%description
librelp is an easy to use library for the RELP protocol. RELP in turn provides
reliable event logging over the network (and consequently RELP stands for
Reliable Event Logging Protocol). RELP was initiated by Rainer Gerhards after
he was finally upset by the lossy nature of plain tcp syslog and wanted a cure
for all these dangling issues.

%package -n	%{libname}
Summary:	Reliable Event Logging Protocol (RELP) library
Group:		System/Libraries

%description -n	%{libname}
librelp is an easy to use library for the RELP protocol. RELP in turn provides
reliable event logging over the network (and consequently RELP stands for
Reliable Event Logging Protocol). RELP was initiated by Rainer Gerhards after
he was finally upset by the lossy nature of plain tcp syslog and wanted a cure
for all these dangling issues.

%package -n	%{devname}
Summary:	Development files for the %{libname} library
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	relp-devel = %{version}-%{release}

%description -n	%{devname}
Development files for the %{libname} library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%check
make check

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/librelp.so.%{major}*

%files -n %{devname}
%doc ChangeLog doc/*.html
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

