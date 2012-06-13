Summary:	A perfect hash function generator
Name:	 	gperf
Version:	3.0.4
Release:	4
License:	GPLv3+
URL:		http://www.gnu.org/software/gperf/
Source:		ftp://ftp.gnu.org/gnu/gperf/%{name}-%{version}.tar.gz
Patch0:		gperf-3.0.1-gcc401.patch.bz2
Group:		Development/Other

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
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_datadir}/doc/gperf.html

%files
%doc README NEWS doc/gperf.html
%{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*
