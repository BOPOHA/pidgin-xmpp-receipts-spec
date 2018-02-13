Name:		pidgin-xmpp-receipts
Version:	0.6
Release:	9.1
Summary:	xmpp message delivery receipts (XEP-0184) plugin for libpurple.

Group:		Applications/Internet
License:	GNU
URL:		https://www.assembla.com/spaces/pidgin-xmpp-receipts/documents
Source0:	pidgin-xmpp-receipts-0.6.tar.gz

BuildRequires:	libpurple-devel, pidgin-devel
Requires:	libpurple

%description
This pidgin-plugin implements xmpp message delivery receipts (XEP-0184).
When no delivering confirmation is displayed, it is also possible that
the receiver doesn't support the extension.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -D -m 0755 xmpp-receipts.so $RPM_BUILD_ROOT/%{_libdir}/purple-2/xmpp-receipts.so

%files
%doc
%{_libdir}/purple-2/xmpp-receipts.so

%changelog
* Sun Nov 15 2015 BOPOHA <vorona.tolik@gmail.com> - 0.6-6
- Added spec for build with OBS.
