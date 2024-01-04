#!/bin/bash
sed -i.bak 's|http://repo.openeuler.org/|https://archives.openeuler.openatom.cn/|g' /etc/yum.repos.d/openEuler.repo
yum update
yum install gcc make git -y