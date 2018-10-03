#!/usr/bin/env bash
set -ex


echo '##########################################################################'
echo '################# About to run install-python.sh script ##################'
echo '##########################################################################'

#pip install --upgrade pip
#pip install virtualenv
#yum -y update    # don't do this because it will cause vagrant restart to fail. 
yum install -y gcc openssl-devel bzip2-devel

yum groupinstall -y "development tools"
yum install -y \
  libffi-devel \
  zlib-devel \
  bzip2-devel \
  openssl-devel \
  ncurses-devel \
  sqlite-devel \
  readline-devel \
  tk-devel \
  gdbm-devel \
  db4-devel \
  libpcap-devel \
  xz-devel \
  expat-devel

cd /usr/src
wget http://python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
tar xf Python-3.6.4.tar.xz
cd Python-3.6.4
./configure --enable-optimizations
make altinstall

/usr/local/bin/pip3.6 install --upgrade pip


/usr/local/bin/pip3.6 install virtualenv


echo "alias py='python3.6'" >> ~/.bashrc

exit