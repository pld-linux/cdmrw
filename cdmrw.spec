Summary:	CDMRW Utility
Name:		cdmrw
Version:	1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp.kernel.org/pub/linux/kernel/people/axboe/tools/%{name}.c
URL:		http://old.lwn.net/2002/0328/a/rainier.php3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	kernel-headers
Requires:	kernel(cdmrw)

%description
Utility to manage mt rainier cd drives + media

%prep
if [ ! -d %{_builddir}/cdmrw]
then 
  mkdir %{_builddir}/cdmrw
fi 
cp %{SOURCE0} %{_builddir}/cdmrw
cd %{_builddir}/cdmrw

%build
cd %{_builddir}/cdmrw
gcc %{name}.c -o %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -f %{_builddir}/cdmrw/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun



%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
