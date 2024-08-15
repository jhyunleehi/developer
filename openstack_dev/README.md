# openstack-zed

https://github.com/Sangwan70/openstack-zed
[https://github.com/Sangwan70/openstack-zed.git](https://github.com/Sangwan70/openstack-zed.git)

## 1. node
1. controller 
2. compute
3. storge

### user: stack/ok

### configurageion 
#### network 
1. host only network #1 10.10.0.1/24
2. host only network #2 203.0.113.1/24

### NIC
1. hostonly network#1
2. internel network eth1
3. hostonly network#2 
4. NAT network

### controller node
1. cpu :1
2. mem :1G
3. disk: 40G, 4G
4. nw : NIC1,NIC2,NIC3,NIC4

### compute node 
1. cpu: 1
2. mem 1G
3. disk 40G 4G 4G 4G
4. nw : NIC1,NIC2,NIC3,NIC4

### storage node 
1. cpu: 1
2. mem 1G
3. disk 40G 4G
4. nw : NIC1,NIC2,NIC3,NIC4


```
------------+--------------------------+--------------------------+------------
            |                          |                          |
      enp0s3|10.10.0.11          enp0s3|10.10.0.31          enp0s3|10.10.0.41
+-----------+-----------+  +-----------+-----------+  +-----------+-----------+
|     [ controller ]    |  |       [ compute ]     |  |       [ storage ]     |
|     (Control Node)    |  |      Nova-Compute     |  |      Swift-Container  |
|     Cinder Volume     |  |     Cinder Volume     |  |      Swift-Account    |
| MariaDB   RabbitMQ    |  |      Swift-Account    |  |       Swift-Object    |
| Memcached Swift Proxy |  |    Swift-Container    |  |                       |
| Keystone  httpd       |  |      Swift-Object     |  |                       |
+-----------------------+  +-----------------------+  +-----------------------+
    enp0s9|NAT                 enp0s9|NAT                 enp0s9|NAT 
    enp0s8|Unconfigured         enp0s8|Unconfigured         enp0s8|Unconfigured

```
Create three Virtual Machines in Oracle VM Virtual Box as given in the diagrame above and set networking.
Login as user "stack" and generate ssh key pair

```sh
ssh-keygen -P ""
ssh-copy-id controller
ssh-copy-id compute
ssh-copy-id storage
```


```sh
/etc/hosts
10.10.0.11	controller
10.10.0.31	compute
10.10.0.41	storage
```

```sh
git clone https://github.com/Sangwan70/openstack-zed.git
```

#### pre-download 
```sh
cd scripts
stack@controller:~/scripts$ ./pre-download.sh
```


```sh
cd ubuntu
```

#### Execute the scriptes in the given order:
```sh
cd ubuntu
stack@controller:~/scripts/ubuntu$ ./apt_upgrade.sh
stack@controller:~/scripts/ubuntu$ ./install_rabbitmq.sh
stack@controller:~/scripts/ubuntu$ ./install_memcached.sh
stack@controller:~/scripts/ubuntu$ ./install_mysql.sh
stack@controller:~/scripts/ubuntu$ ./setup_keystone_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_keystone_2.sh
stack@controller:~/scripts/ubuntu$ ./setup_glance_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_glance_2.sh
stack@controller:~/scripts/ubuntu$ ./setup_placement_controller_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_placement_controller_2.sh
stack@controller:~/scripts/ubuntu$ ./setup_nova_controller_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_nova_controller_2.sh
stack@controller:~/scripts/ubuntu$ ./setup_nova_controller_3.sh
stack@controller:~/scripts/ubuntu$ ./setup_nova_controller_4.sh
stack@controller:~/scripts/ubuntu$ ./setup_neutron_controller_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_neutron_controller_2.sh
stack@controller:~/scripts/ubuntu$ ./setup_neutron_controller_3.sh
stack@controller:~/scripts/ubuntu$ ./setup_neutron_controller_4.sh
stack@controller:~/scripts/ubuntu$ ./setup_cinder_controller_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_cinder_controller_2.sh
stack@controller:~/scripts/ubuntu$ ./setup_cinder_controller_3.sh
stack@controller:~/scripts/ubuntu$ ./setup_cinder_controller_4.sh 
stack@controller:~/scripts/ubuntu$ ./setup_heat_controller_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_heat_controller_2.sh
stack@controller:~/scripts/ubuntu$ ./setup_barbican_server_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_barbican_server_2.sh
stack@controller:~/scripts/ubuntu$ ./setup_barbican_server_3.sh
stack@controller:~/scripts/ubuntu$ ./setup_swift_controller_1.sh
stack@controller:~/scripts/ubuntu$ ./setup_swift_controller_2.sh
```


#### Don't Execute the script setup_swift_controller_2.sh as of now.
```sh
stack@controller:~/scripts/ubuntu$ ./setup_horizon.sh
```



#### On Compute Node, execute the scripts in  the following order.
```sh
stack@compute:~/scripts/ubuntu$ ./apt_upgrade.sh
stack@compute:~/scripts/ubuntu$ ./setup_nova_compute_1.sh
stack@compute:~/scripts/ubuntu$ ./setup_nova_compute_2.sh
stack@compute:~/scripts/ubuntu$ ./setup_neutron_compute_1.sh
stack@compute:~/scripts/ubuntu$ ./setup_neutron_compute_2.sh
stack@compute:~/scripts/ubuntu$ ./setup_neutron_compute_3.sh
stack@compute:~/scripts/ubuntu$ ./setup_neutron_compute_4.sh
stack@compute:~/scripts/ubuntu$ ./setup_swift_1.sh
stack@compute:~/scripts/ubuntu$ ./setup_swift_2.sh
stack@compute:~/scripts/ubuntu$ ./setup_swift_3.sh
stack@compute:~/scripts/ubuntu$ ./setup_cinder_1.sh
stack@compute:~/scripts/ubuntu$ ./setup_cinder_2.sh
```

#### One Storage Node, execute the scripts in  the following order.
```sh
stack@storage:~/scripts/ubuntu$ ./setup_swift_1.sh
stack@storage:~/scripts/ubuntu$ ./setup_swift_2.sh
stack@storage:~/scripts/ubuntu$ ./setup_swift_3.sh
```

#### Back to controller node, execute the following script
```sh
stack@controller:~/scripts/ubuntu$ ./setup_swift_controller_3.sh
```


#### Create public network, private network and router
```sh
stack@controller:~/scripts/ubuntu$ cd ..
stack@controller:~/scripts$ ./config_public_network.sh
stack@controller:~/scripts$ ./config_private_network.sh
```

