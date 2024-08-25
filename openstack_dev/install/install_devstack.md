# How to Install OpenStack on Ubuntu with DevStack [ Easy method ]

https://opendev.org/openstack/devstack/src/branch/stable/2024.1#


### Step 1: Preparing the system

```sh
$ sudo apt-get update && sudo apt-get upgrade -y
```

### Step 2: Creating stack user with Sudo privileges
```sh
$ sudo useradd -s /bin/bash -d /opt/stack -m stack
$ echo "stack ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/stack
$ sudo su - stack
```


### Step 3: Downloading Devstack
```sh
$ echo "check_certificate = off" >> ~/.wgetrc
$ git clone https://opendev.org/openstack/devstack
```

### Step 4: Creating configuration (.conf) file for Devstack
```sh
$ cd devstack
$ vim local.conf

[[local|localr]]
 
ADMIN_PASSWORD=1234qwer
DATABASE_PASSWORD=$ADMIN_PASSWOCinder
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD
ENABLED_SERVICES=placement-api
```

Note:
1. StrongAdminSecret is the password we used here, you can change it with your choice.
2. You can find a sample configuration file for local.conf in the Samples directory under the Devstack repository.

### Step 5: Installing Openstack with Devstack
```sh
$ ./stack.sh
```

The script will install the listed features for your OpenStack environment –

Horizon – OpenStack Dashboard
Keystone – Identity Service
Nova – Compute Service
Glance – Image Service
Neutron – Network Service
Placement – Placement API
Cinder – Block Storage Service
The setup will take around 10 to 20 minutes, based on your system performance and internet speed, as many git trees and packages are installed during the process.

After your installation successfully finishes, your terminal will look like the image below.


### Step 6: Accessing OpenStack using a web browser
```sh 
https://server-ip/dashboard
https://localhost/dashboard

Openstack Login
Openstack Login
Now, enter the credentials. You can also log in as admin here, by having User Name as admin & for Password using the one we added to local.conf file.
```

## ==> reinstall reset all 
$  ./unstack.sh
$  ./clean.sh
$ ps -ef | grep  "^stack"
$ sudo kill -9 `ps -ef | grep  "^stack" | awk '{print $2}'`
$ sudo  deluser stack
$ sudo  rm  -rf /opt/stack
$ sudo systemctl stop ufw
$ sudo systemctl disable ufw



==> Didn't find service registered by hostname after 60 seconds - Openstack/devstack deployment fails

```sh
stack@gpu-4:~/devstack$ head /etc/hosts
127.0.0.1	localhost gpu-4
```


### install package 
```sh
sudo apt install -y python3-openstackclient openstack-keystone httpd python3-mod_wsgi python3-heatclient openstack-glance openstack-neutron openstack-neutron-ml2 openstack-nova-api openstack-nova-conductor openstack-nova-novncproxy openstack-nova-scheduler openstack-neutron-linuxbridge openstack-cinder openstack-placement-api openstack-dashboard openstack-heat-common openstack-heat-api openstack-heat-api-cfn openstack-heat-engine

sudo apt install -y openstack-swift-proxy python3-swift python3-swiftclient rdo-release  python3-keystoneclient python3-keystonemiddleware

sudo apt install -y openstack-selinux python3-openstacksdk
```

### remove network

```sh
stack@gpu-3:~/devstack$ sudo  ifconfig  virbr0 down
stack@gpu-3:~/devstack$ sudo  ifconfig mybr0  down
stack@gpu-3:~/devstack$ sudo  brctl delbr virbr0
stack@gpu-3:~/devstack$ sudo  brctl delbr mybr0
```
