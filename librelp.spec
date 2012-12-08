%define	major 0
%define libname	%mklibname relp %{major}
%define develname %mklibname relp -d

Summary:	Reliable Event Logging Protocol (RELP) library
Name:		librelp
Version:	0.1.3
Release:	%mkrel 6
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



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-4mdv2011.0
+ Revision: 661522
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-3mdv2011.0
+ Revision: 602602
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-2mdv2010.1
+ Revision: 520900
- rebuilt for 2010.1

* Wed Sep 23 2009 Emmanuel Andry <eandry@mandriva.org> 0.1.3-1mdv2010.0
+ Revision: 447886
- New version 0.1.3
- check major

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.1-3mdv2010.0
+ Revision: 429829
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.1.1-2mdv2009.0
+ Revision: 267990
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat May 03 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-1mdv2009.0
+ Revision: 200681
- import librelp


* Sat May 03 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-1mdv2009.0
- initial Mandriva package
