Summary:	A perfect hash function generator
Name:	 	gperf
Version:	3.0.3
Release:	%mkrel 1
License:	GPL
URL:		http://www.gnu.org/software/gperf/
Source:		ftp://ftp.gnu.org/gnu/gperf/%{name}-%{version}.tar.gz
Patch0:		gperf-3.0.1-gcc401.patch.bz2
Group:		Development/Other
Prereq:		/sbin/install-info
BuildRoot:	%{_tmppath}/%{name}-root

%description
Gperf is a perfect hash function generator written in C++.  Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

Install gperf if you need a program that generates perfect hash
functions.

%prep
%setup -q
%patch0 -p1 -b .gcc401

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/gperf/gperf.html

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc README NEWS doc/gperf.html
%{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*
