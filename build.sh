#!/bin/bash
yum -y install rpm-build sqlite-devel jansson-devel wget mariadb-devel zlib-devel libpcap-devel libtool
mkdir -p ~/rpmbuild/SOURCES
wget https://github.com/pmacct/pmacct/archive/v1.7.2.tar.gz -O ~/rpmbuild/SOURCES/pmacct-1.7.2.tar.gz
rpmbuild -bb pmacct.spec
