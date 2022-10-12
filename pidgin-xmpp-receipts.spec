%define git_tag release_%{version}

Name:		pidgin-xmpp-receipts
Version:	0.8
Release:	1
Summary:	xmpp message delivery receipts (XEP-0184) plugin for libpurple.

Group:		Applications/Internet
License:	GNU
URL:		https://github.com/noonien-d/pidgin-xmpp-receipts/
Source0:	https://github.com/noonien-d/pidgin-xmpp-receipts/archive/refs/tags/%{git_tag}.tar.gz#/pidgin-xmpp-receipts-%{version}.tar.gz

BuildRequires: pidgin-devel
BuildRequires: gcc
BuildRequires: make
Requires:	libpurple

%description
This pidgin-plugin implements xmpp message delivery receipts (XEP-0184).
When no delivering confirmation is displayed, it is also possible that
the receiver doesn't support the extension.

%prep
%setup -n %{name}-%{git_tag}

%build
make %{?_smp_mflags}

%install
install -D -m 0755 xmpp-receipts.so $RPM_BUILD_ROOT/%{_libdir}/purple-2/xmpp-receipts.so

%files
%doc
%{_libdir}/purple-2/xmpp-receipts.so

%changelog
* Wed Oct 12 2022 BOPOHA <vorona.tolik@gmail.com> - 0.8-1
- rebuild packages
- XEP-0184 v1.2 support

* Sun Nov 15 2015 BOPOHA <vorona.tolik@gmail.com> - 0.6-6
- Added spec for build with OBS.
