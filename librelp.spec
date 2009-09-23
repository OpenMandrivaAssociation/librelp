%define	major 0
%define libname	%mklibname relp %{major}
%define develname %mklibname relp -d

Summary:	Reliable Event Logging Protocol (RELP) library
Name:		librelp
Version:	0.1.3
Release:	%mkrel 1
License:	GPLv3+
Group:		System/Libraries
URL:		http://www.librelp.com/
Source0:	http://download.rsyslog.com/librelp/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Development files for the %{libname} library
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	relp-devel = %{version}-%{release}

%description -n	%{develname}
Development files for the %{libname} library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
 
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog doc/*.html
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/*.pc

