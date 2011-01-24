Summary:	SIP connection manager for the Telepathy
Summary(pl.UTF-8):	Zarządca połączeń SIP dla Telepathy
Name:		telepathy-sofiasip
Version:	0.7.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-sofiasip/%{name}-%{version}.tar.gz
# Source0-md5:	3e1ea234edbc3d3763ae0cf84bc120a8
URL:		http://tp-sofiasip.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	sofia-sip-devel >= 1.12.10
BuildRequires:	telepathy-glib-devel >= 0.5.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides SIP functionality for Telepathy.

%description -l pl.UTF-8
Ten pakiet udostępnia funkcjonalność SIP dla Telepathy.

%package devel
Summary:	Header files for telepathy-sofiasip library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-sofiasip
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for telepathy-sofiasip library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-sofiasip.

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
%attr(755,root,root) %{_libexecdir}/telepathy-sofiasip
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.sofiasip.service
%{_datadir}/telepathy/managers/sofiasip.manager
%{_mandir}/man8/telepathy-sofiasip.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-0.6/tpsip
