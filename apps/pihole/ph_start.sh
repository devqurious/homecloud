#!/bin/bash
# Script to turn off systemd-resolv on reboot so pihole can start properly
# See: https://www.aquriousmind.com/posts/pi/14_install-pihole/

service systemd-resolved stop
echo 'nameserver 8.8.8.8' >> /etc/resolv.conf
exit 0