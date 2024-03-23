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
Group:          Productivity/Networking/Security
License:        ISC 
URL:            https://github.com/openiked/openiked-portable

Source:         %{name}-portable-%{version}.tar.xz
Source1:        openiked.service
Source2:        openiked-keygen.service
Source3:        openiked-keygen.target
Source4:        openiked-keygen

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
mkdir -p %{buildroot}/var/empty
mkdir -p %{buildroot}%{_sysconfdir}/iked/private/
mkdir -p %{buildroot}/usr/libexec/openiked

mv %{buildroot}/usr/local/sbin/iked   %{buildroot}%{_sbindir}/iked
mv %{buildroot}/usr/local/sbin/ikectl %{buildroot}%{_sbindir}/ikectl

install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/openiked.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/openiked-keygen.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/openiked-keygen.target
install -D -m 0644 %{SOURCE4} %{buildroot}/usr/libexec/openiked/openiked-keygen

#groupadd _iked
#useradd -M -d /var/empty -s $(which nologin) -c "IKEv2 Daemon" -g _iked _iked

%pre
%service_add_pre openiked.service
%service_add_pre openiked-keygen.service
%service_add_pre openiked-keygen.target

%preun
%service_del_preun openiked.service
%service_del_preun openiked-keygen.service
%service_del_preun openiked-keygen.target

%postun
%service_del_postun openiked.service
%service_del_postun openiked-keygen.service
%service_del_postun openiked-keygen.target

%post
%service_add_post openiked.service
%service_add_post openiked-keygen.service
%service_add_post openiked-keygen.target


%files
%defattr(-,root,root)
%config  /etc/iked.conf
%config  /etc/ssl/ikeca.cnf
%config  /etc/ssl/ikex509v3.cnf
%attr(555,root,root) %{_sbindir}/ikectl
%attr(555,root,root) %{_sbindir}/iked
%attr(0755,root,root) %{_sysconfdir}/iked/
%attr(0644,root,root) %{_unitdir}/openiked.service
%attr(0644,root,root) %{_unitdir}/openiked-keygen.service
%attr(0644,root,root) %{_unitdir}/openiked-keygen.target
%attr(0700,root,root) /var/empty
%attr(0700,root,root) /usr/libexec/
%attr(0700,root,root) /usr/libexec/openiked/
%attr(0744,root,root) /usr/libexec/openiked/openiked-keygen
%{_mandir}/man5/iked.conf.5.gz
%{_mandir}/man8/ikectl.8.gz
%{_mandir}/man8/iked.8.gz

%license LICENSE
%changelog

