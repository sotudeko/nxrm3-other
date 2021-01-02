#!/usr/bin/env bash

tools_dir="/opt/sonatype"
iq_server_dir=${tools_dir}/nexus-iq-server

if [[ ! -d ${iq_server_dir} ]]; then
    mkdir -p ${iq_server_dir}
    tar xvzf /vagrant/packages/archive/nexus-iq-server-1.45.0-01-bundle.tar.gz -C ${iq_server_dir} 
    sudo cp /vagrant/packages/nexus-iq-server /etc/init.d
    cd /etc/init.d
    sudo chkconfig --add nexus-iq-server
    sudo chkconfig --levels 345 nexus-iq-server on
    sudo service nexus-iq-server start
else
    echo "Nexus IQ Server is running"
fi

