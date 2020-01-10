Summary:	A perfect hash function generator
Name:	 	gperf
Version:	3.1
Release:	2
License:	GPLv3+
Group:		Development/Other
Url:		http://www.gnu.org/software/gperf/
Source0:	ftp://ftp.gnu.org/gnu/gperf/%{name}-%{version}.tar.gz

%description
Gperf is a perfect hash function generator written in C++.  Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

Install gperf if you need a program that generates perfect hash
functions.

%prep
%setup -q
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/doc/gperf.html

%files
%doc README NEWS doc/gperf.html
%{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*

