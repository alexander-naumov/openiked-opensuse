#
# spec file for package openiked
#
# Copyright (c) 2022-2024 Alexander Naumov <alexander_naumov@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           openiked
Version:        7.3
Release:        0
Summary:        Internet Key Exchange version 2 (IKEv2) daemon
License:        ISC 
URL:            https://github.com/openiked/openiked-portable
Source:         %{name}-portable-%{version}.tar.xz
Source1:        openiked.service
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  bison
BuildRequires:  libevent-devel
BuildRequires:  systemd-devel

%description
OpenIKED is a FREE implementation of the Internet Key Exchange (IKEv2)
protocol which performs mutual authentication and which establishes and
maintains IPsec VPN security policies and associations (SAs) between peers.

%prep
%setup -n %{name}-portable-%{version}

%build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make

%install
cd build

make install DESTDIR=%buildroot
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/etc/ssl/
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/iked/private/

mv %{buildroot}/usr/local/sbin/iked %{buildroot}%{_sbindir}/iked
mv %{buildroot}/usr/local/sbin/ikectl %{buildroot}%{_sbindir}/ikectl
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/openiked.service
#groupadd _iked
#useradd -M -d /var/empty -s $(which nologin) -c "IKEv2 Daemon" -g _iked _iked

%pre
%service_add_pre openiked.service

%preun
%service_del_preun openiked.service

%postun
%service_del_postun openiked.service

%post
%service_add_post openiked.service


%files
%defattr(-,root,root)
%config  /etc/iked.conf
%config  /etc/ssl/ikeca.cnf
%config  /etc/ssl/ikex509v3.cnf
%attr(555,root,root) %{_sbindir}/ikectl
%attr(555,root,root) %{_sbindir}/iked
%attr(0644,root,root) %{_unitdir}/openiked.service
%attr(0700,root,root) %{_sysconfdir}/iked/
%{_mandir}/man5/iked.conf.5.gz
%{_mandir}/man8/ikectl.8.gz
%{_mandir}/man8/iked.8.gz

%license LICENSE
%changelog

