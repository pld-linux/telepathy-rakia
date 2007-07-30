Summary:	SIP connection manager for the Telepathy
Summary(pl.UTF-8):	Zarządca połączeń SIP dla Telepathy
Name:		telepathy-sofiasip
Version:	0.3.26
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/tp-sofiasip/%{name}-%{version}.tar.gz
# Source0-md5:	a72318c069a807a6efb42126d96ecbe7
URL:		http://sourceforge.net/projects/tp-sofiasip/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	sofia-sip-devel
BuildRequires:	telepathy-glib-devel >= 0.5.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides SIP functionality for Telepathy.

%description -l pl.UTF-8
Ten pakiet udostępnia funkcjonalność SIP dla Telepathy.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/telepathy-sofiasip
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.sofiasip.service
%{_datadir}/telepathy/managers/sofiasip.manager
