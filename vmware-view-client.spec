%define debug_package %{nil}
Name:		vmware-view-client
Version:	2.2.0
Release:	1%{?dist}
Summary:	VMware Horizon View Client

Group:		Remote Access
License:	NA
URL:		vmware.com
Source0:	vmware-view-client_2.2.0.orig.tar.gz

BuildRequires:	gcc
Requires:	firefox

%description
VMware Horizon View client, built by LV for Fedora 20


%prep
%setup -q


%build
#configure
#make %{?_smp_mflags}


%install
#make install DESTDIR=%{buildroot}
rm -rf %{buildroot}
mkdir -p %{buildroot}/
cp -pr . %{buildroot}


%files
%attr(-, root, root)   /usr/bin/vmware-remotemks
%attr(-, root, root)   /usr/bin/vmware-remotemks-container
%attr(-, root, root)   /usr/bin/vmware-view
%attr(-, root, root)   /usr/bin/vmware-view-log-collector
%attr(-, root, root)   /usr/bin/vmware-view-tunnel
%attr(-, root, root)   /usr/lib/libpcoip_client.so
%attr(-, root, root)   /usr/lib/libpcoip_crypto.so
%attr(-, root, root)   /usr/lib/libpcoip_crypto_non_fips.so
%dir /usr/lib/pcoip
%dir /usr/lib/pcoip/vchan_plugins
%attr(-, root, root)   /usr/lib/pcoip/vchan_plugins/libmksvchanclient.so
%attr(-, root, root)   /usr/lib/pcoip/vchan_plugins/libscredirvchanclient.so
%dir /usr/lib/vmware
%dir /usr/lib/vmware/xkeymap
%attr(-, root, root)   /usr/lib/vmware/xkeymap/be101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/be104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/chde101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/chde104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/chfr101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/chfr104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/de101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/de104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/dk101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/dk104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/es101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/es104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/fi101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/fi104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/fr101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/fr104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/gb101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/gb104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/is101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/is104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/it101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/it104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/jp106
%attr(-, root, root)   /usr/lib/vmware/xkeymap/jp109
%attr(-, root, root)   /usr/lib/vmware/xkeymap/no101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/no104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/pt101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/pt104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/se101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/se104
%attr(-, root, root)   /usr/lib/vmware/xkeymap/us101
%attr(-, root, root)   /usr/lib/vmware/xkeymap/us104
%dir /usr/share/doc/vmware-view-client
%doc   /usr/share/doc/vmware-view-client/VMware-Horizon-View-Client-EULA-de.txt
%doc   /usr/share/doc/vmware-view-client/VMware-Horizon-View-Client-EULA-en.txt
%doc   /usr/share/doc/vmware-view-client/VMware-Horizon-View-Client-EULA-fr.txt
%doc   /usr/share/doc/vmware-view-client/VMware-Horizon-View-Client-EULA-ja.txt
%doc   /usr/share/doc/vmware-view-client/VMware-Horizon-View-Client-EULA-ko.txt
%doc   /usr/share/doc/vmware-view-client/VMware-Horizon-View-Client-EULA-zh_CN.txt
%doc   /usr/share/doc/vmware-view-client/VMware-Horizon-View-Client-EULA-zh_TW.txt
%doc   /usr/share/doc/vmware-view-client/open_source_licenses.txt
%attr(-, root, root)   /usr/share/locale/de/LC_MESSAGES/vmware-view.mo
%attr(-, root, root)   /usr/share/locale/fr/LC_MESSAGES/vmware-view.mo
%attr(-, root, root)   /usr/share/locale/ja/LC_MESSAGES/vmware-view.mo
%attr(-, root, root)   /usr/share/locale/ko/LC_MESSAGES/vmware-view.mo
%attr(-, root, root)   /usr/share/locale/zh_CN/LC_MESSAGES/vmware-view.mo
%attr(-, root, root)   /usr/share/locale/zh_TW/LC_MESSAGES/vmware-view.mo


%changelog
* Mon Apr 21 2014 - 2.2.0-1 LV
- First build
