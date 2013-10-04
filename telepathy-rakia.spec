Summary:	SIP connection manager for the Telepathy
Summary(pl.UTF-8):	Zarządca połączeń SIP dla Telepathy
Name:		telepathy-rakia
Version:	0.8.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-rakia/%{name}-%{version}.tar.gz
# Source0-md5:	09038d4625fcf81e9d3228ebf18bc378
URL:		http://tp-sofiasip.sourceforge.net/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	glib2-devel >= 1:2.30
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.3
BuildRequires:	sofia-sip-devel >= 1.12.11
BuildRequires:	telepathy-glib-devel >= 0.17.7
Requires:	dbus-glib >= 0.60
Requires:	glib2 >= 1:2.30
Obsoletes:	telepathy-sofiasip < 0.7.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides SIP functionality for Telepathy.

%description -l pl.UTF-8
Ten pakiet udostępnia funkcjonalność SIP dla Telepathy.

%package devel
Summary:	Header files for telepathy-rakia library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-rakia
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.30
Requires:	sofia-sip-devel >= 1.12.11
Requires:	telepathy-glib-devel >= 0.17.7
Obsoletes:	telepathy-sofiasip-devel < 0.7.2

%description devel
Header files for telepathy-rakia library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-rakia.

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libexecdir}/telepathy-rakia
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.sofiasip.service
%{_datadir}/telepathy/managers/rakia.manager
%{_mandir}/man8/telepathy-rakia.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-0.7
