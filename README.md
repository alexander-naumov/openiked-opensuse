# OpenIKED for openSUSE

[![License](https://img.shields.io/github/license/alexander-naumov/openiked-opensuse)](https://github.com/alexander-naumov/openiked-opensuse/LICENSE)
[![#openiked on matrix.org](https://img.shields.io/badge/matrix-%23openiked-blue)](https://app.element.io/#/room/#openiked:matrix.org)
[![#openiked on libera.chat](https://img.shields.io/badge/IRC-%23openiked-blue)](https://kiwiirc.com/nextclient/irc.libera.chat/#openiked)
[![build result](https://build.opensuse.org/projects/network:vpn/packages/openiked/badge.svg?type=percent)](https://build.opensuse.org/package/show/network:vpn/openiked)

<img align="right" src="openiked.png" height="250">

[OpenIKED](https://www.openiked.org) is a FREE implementation of the
Internet Key Exchange (IKEv2) protocol which performs mutual authentication
and which establishes and maintains IPsec VPN security policies
and associations (SAs) between peers.

OpenIKED supports only the [IKEv2 protocol](https://en.wikipedia.org/wiki/Internet_Key_Exchange).
It is defined in [RFC 5996](https://datatracker.ietf.org/doc/html/rfc5996),
which combines and updates the previous standards:
ISAKMP/Oakley (RFC 2408), IKE (RFC 2409), and the Internet DOI (RFC 2407).

### openSUSE

To install OpenIKED on openSUSE you will need to add the VPN repository:
```
$ sudo zypper addrepo https://download.opensuse.org/repositories/network:vpn/openSUSE_Tumbleweed/network:vpn.repo
$ sudo zypper refresh
$ sudo zypper install openiked

$ rpm -qi openiked
Name        : openiked
Version     : 7.3
Release     : 4.1
Architecture: x86_64
Install Date: Mi 27 Mär 2024 15:39:58 CET
Group       : Productivity/Networking/Security
Size        : 575710
License     : ISC
Signature   : RSA/SHA256, Mi 27 Mär 2024 15:36:41 CET, Key ID 62eb1a0917280ddf
Source RPM  : openiked-7.3-4.1.src.rpm
Build Date  : Mi 20 Mär 2024 16:09:22 CET
Build Host  : reproducible
Vendor      : obs://build.opensuse.org/network
URL         : https://github.com/openiked/openiked-portable
Summary     : Internet Key Exchange version 2 (IKEv2) daemon
Description :
OpenIKED is a FREE implementation of the Internet Key Exchange (IKEv2)
protocol which performs mutual authentication and which establishes and
maintains IPsec VPN security policies and associations (SAs) between peers.
Distribution: network:vpn / openSUSE_Tumbleweed

$ rpm -ql openiked
/etc/iked
/etc/iked.conf
/etc/iked/ca
/etc/iked/certs
/etc/iked/crls
/etc/iked/private
/etc/iked/pubkeys
/etc/iked/pubkeys/fqdn
/etc/iked/pubkeys/ipv4
/etc/iked/pubkeys/ipv6
/etc/iked/pubkeys/ufqdn
/etc/ssl/ikeca.cnf
/etc/ssl/ikex509v3.cnf
/usr/lib/systemd/system/openiked-keygen.service
/usr/lib/systemd/system/openiked-keygen.target
/usr/lib/systemd/system/openiked.service
/usr/libexec
/usr/libexec/openiked
/usr/libexec/openiked/openiked-keygen
/usr/sbin/ikectl
/usr/sbin/iked
/usr/share/licenses/openiked
/usr/share/licenses/openiked/LICENSE
/usr/share/man/man5/iked.conf.5.gz
/usr/share/man/man8/ikectl.8.gz
/usr/share/man/man8/iked.8.gz
/var/empty
```

Configuration process on openSUSE is similar with OpenBSD.
The offical manual can be found [here](https://www.openbsd.org/faq/faq17.html) and [here](https://man.openbsd.org/iked).

The [RSA public key](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
is generated by the ```openiked-keygen``` service:
```
# ls -la /etc/iked/local.pub
ls: cannot access '/etc/iked/local.pub': No such file or directory

# systemctl start openiked-keygen
○ openiked-keygen.service - OpenIKED Key Generation
     Loaded: loaded (/usr/lib/systemd/system/openiked-keygen.service; disabled; preset: disabled)
     Active: inactive (dead)

Mär 20 23:22:07 suse systemd[1]: Starting OpenIKED Key Generation...
Mär 20 23:22:07 suse openiked-keygen[1596]: read EC key
Mär 20 23:22:07 suse openiked-keygen[1596]: writing EC key
Mär 20 23:22:07 suse systemd[1]: openiked-keygen.service: Deactivated successfully.
Mär 20 23:22:07 suse systemd[1]: Finished OpenIKED Key Generation.

# ls -la /etc/iked/local.pub
-rw-r--r-- 1 root root 178 Mär 20 23:22 /etc/iked/local.pub

# cat /etc/iked/local.pub
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEmy+IwTy+W8WbrTrLqdzEh+PqQlAW
0m+Nj1gfBCgj0kfaNGJym2awfsl4MNf7pwfFtPsZ73znW9W4lZ3REm/kLg==
-----END PUBLIC KEY-----
```

