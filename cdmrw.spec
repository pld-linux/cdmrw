Summary:	CDMRW Utility
Name:		cdmrw
Version:	1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/axboe/tools/%{name}.c
URL:		http://old.lwn.net/2002/0328/a/rainier.php3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	kernel-headers
Requires:	kernel(cdmrw)

%description
Utility to manage mt rainier cd drives + media

%prep
%setup -q -T -c
cp -f %{SOURCE0} .

%build
%{__cc} %{rpmcflags} %{rpmldflags} %{name}.c -o %{name}

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
