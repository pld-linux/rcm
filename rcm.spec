Summary:	rc file (dotfile) management
Name:		rcm
Version:	1.2.3
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://thoughtbot.github.io/rcm/dist/%{name}-%{version}.tar.gz
# Source0-md5:	7ac43eef04cacb91a00f902852369aaf
URL:		https://github.com/thoughtbot/rcm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rc file (dotfile) management.

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE *.md
%attr(755,root,root) %{_bindir}/lsrc
%attr(755,root,root) %{_bindir}/mkrc
%attr(755,root,root) %{_bindir}/rcdn
%attr(755,root,root) %{_bindir}/rcup
%{_mandir}/man1/lsrc.1*
%{_mandir}/man1/mkrc.1*
%{_mandir}/man1/rcdn.1*
%{_mandir}/man1/rcup.1*
%{_mandir}/man5/rcrc.5*
%{_mandir}/man7/rcm.7*
%{_datadir}/rcm
