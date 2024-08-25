# install manila neapp driver 

## DevStack 설치 

https://docs.openstack.org/manila/ocata/devref/development-environment-devstack.html

https://netapp-openstack-dev.github.io/openstack-docs/draft/manila/ch_manila-configuration.html

```sh
git clone https://github.com/openstack-dev/devstack
cd devstack/
cp samples/local.conf .

enable_plugin manila https://github.com/openstack/manila
enable_plugin manila-ui https://github.com/openstack/manila-ui
```

### local.conf 

#### 1. 변경전 local.conf 
```sh
stack@DevStack:~/devstack$ cat local.conf
[[local|localrc]]
ADMIN_PASSWORD=secret
DATABASE_PASSWORD=$ADMIN_PASSWORD
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD

HOST_IP=192.168.100.100

LOGFILE=$DEST/logs/stack.sh.log
```

#### 2. manila 인스톨 

* reinstall reset all 
```sh
$  ./unstack.sh
$  ./clean.sh
$ ps -ef | grep  "^stack"
$ sudo kill -9 `ps -ef | grep  "^stack" | awk '{print $2}'`
$ sudo  deluser stack
$ sudo  rm  -rf /opt/stack
$ sudo systemctl stop ufw
$ sudo systemctl disable ufw

$ echo "check_certificate = off" >> ~/.wgetrc
$ git clone https://opendev.org/openstack/devstack
```
#### 3. manila local.conf 
```sh
stack@stack:~/devstack$ cat local.conf
 
[[local|localrc]]
ADMIN_PASSWORD=secret
DATABASE_PASSWORD=$ADMIN_PASSWORD
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD
DEST=/opt/stack
DATA_DIR=/opt/stack/data
HOST_IP=192.168.137.24
LOGFILE=$DEST/logs/stack.sh.log
 
# Enabling manila services
LIBS_FROM_GIT=python-manilaclient
enable_plugin manila https://opendev.org/openstack/manila
enable_plugin manila-ui https://opendev.org/openstack/manila-ui
enable_plugin manila-tempest-plugin https://opendev.org/openstack/manila-tempest-plugin
 
 
# LVM Backend config options
MANILA_SERVICE_IMAGE_ENABLED=False
SHARE_DRIVER=manila.share.drivers.lvm.LVMShareDriver
MANILA_ENABLED_BACKENDS=chicago,denver
MANILA_OPTGROUP_chicago_driver_handles_share_servers=False
MANILA_OPTGROUP_denver_driver_handles_share_servers=False
SHARE_BACKING_FILE_SIZE=32000M
MANILA_DEFAULT_SHARE_TYPE_EXTRA_SPECS='snapshot_support=True create_share_from_snapshot_support=True revert_to_snapshot_support=True mount_snapshot_support=True'
MANILA_CONFIGURE_DEFAULT_TYPES=True
 
# Required for mounting shares
MANILA_ALLOW_NAS_SERVER_PORTS_ON_HOST=True
```
* 그런데 이것 설치되도 lvm manila 드라이버는 잘 동작하지 않음 
* 나중에 원인 분석이 좀 필요함 

#### 4. 기본설치 이후 자동생성된 manila.conf 
```sh
[chicago]
lvm_share_export_ips = 192.168.100.100
backend_availability_zone = manila-zone-0
driver_handles_share_servers = False
service_instance_user = manila
service_image_name = manila-service-image-master
path_to_private_key = /opt/stack/.ssh/id_ecdsa
path_to_public_key = /opt/stack/.ssh/id_ecdsa.pub
share_backend_name = CHICAGO
share_driver = manila.share.drivers.lvm.LVMShareDriver

[denver]
lvm_share_export_ips = 192.168.100.100
backend_availability_zone = manila-zone-1
driver_handles_share_servers = False
service_instance_user = manila
service_image_name = manila-service-image-master
path_to_private_key = /opt/stack/.ssh/id_ecdsa
path_to_public_key = /opt/stack/.ssh/id_ecdsa.pub
share_backend_name = DENVER
share_driver = manila.share.drivers.lvm.LVMShareDriver
```

## so manila 연동
### 1. /etc/manila/manila.conf 설정
```conf

[keystone_authtoken]
memcached_servers = localhost:11211
cafile = /opt/stack/data/ca-bundle.pem
project_domain_name = Default
project_name = service
user_domain_name = Default
password = secret
username = manila
auth_url = http://192.168.100.100/identity
interface = public
auth_type = password

[DEFAULT]
data_node_access_ips = 192.168.100.100
logging_exception_prefix = ERROR %(name)s [01;35m%(instance)s[00m
logging_default_format_string = %(color)s%(levelname)s %(name)s [[00;36m-%(color)s] [01;35m%(instance)s%(color)s%(message)s[00m
logging_context_format_string = %(color)s%(levelname)s %(name)s [[01;36m%(global_request_id)s %(request_id)s [00;36m%(project_name)s %(user_name)s%(color)s] [01;35m%(instance)s%(color)s%(message)s[00m
logging_debug_format_suffix = [00;33m{{(pid=%(process)d) %(funcName)s %(pathname)s:%(lineno)d}}[00m
transport_url = rabbit://stackrabbit:secret@192.168.100.100:5672/
manila_service_keypair_name = manila-service
enabled_share_backends = so,netapp   # <<<
use_scheduler_creating_share_from_snapshot = False
replica_state_update_interval = 300
lvm_share_volume_group = lvm-shares
wsgi_keep_alive = False
enabled_share_protocols = NFS,CIFS
check_hash = True
periodic_deferred_delete_interval = 10
default_share_group_type = default
default_share_type = default
state_path = /opt/stack/data/manila
osapi_share_extension = manila.api.contrib.standard_extensions
rootwrap_config = /etc/manila/rootwrap.conf
api_paste_config = /etc/manila/api-paste.ini
share_name_template = share-%s
scheduler_driver = manila.scheduler.drivers.filter.FilterScheduler
debug = True
auth_strategy = keystone

[DATABASE]
max_pool_size = 40
connection = mysql+pymysql://root:secret@127.0.0.1/manila?charset=utf8&plugin=dbcounter

[oslo_concurrency]
lock_path = /opt/stack/manila/manila_locks

[so] 
share_backend_name=so
share_driver = manila.share.drivers.so.driver.SOShareDriver
driver_handles_share_servers = False
SO_login = sds
SO_password = 1234
SO_server = 70.60.31.72
SO_port = 443
#SO_storageId = 231
#SO_volumePoolName = svm2
#SO_volumePoolId = svm2:N1_aggr1 
SO_storageId = 36
SO_volumePoolName = svm1
SO_volumePoolId = svm1:N1_aggr1
SO_backend = v1

[netapp]
share_backend_name=netapp
share_driver = manila.share.drivers.netapp.common.NetAppDriver
driver_handles_share_servers = False
netapp_use_legacy_client =  False
netapp_storage_family = ontap_cluster
netapp_server_hostname=70.60.31.187
netapp_server_port = 80
netapp_login = admin
netapp_password = 1234qwer
netapp_vserver = manila-vserver
netapp_transport_type = http
#netapp_aggregate_name_search_pattern = N1_aggr1
netapp_aggregate_name_search_pattern = ^((?!aggr0).)*$

```

### 2. manila share service 재기동 
```sh  
stack@DevStack:~$ source /opt/stack/data/venv/bin/activate
(venv) stack@DevStack:~$ source ~/devstack/openrc admin admin
(venv) stack@DevStack:~$ env | grep OS
(venv) stack@DevStack:~/devstack$ sudo systemctl  daemon-reload
(venv) stack@DevStack:~/devstack$ sudo systemctl  restart  devstack@m-shr.service
```

### 3. manila share service 상태 확인 
* share service log 모니터링 
```sh
$ sudo  journalctl -f  -u  devstack@m-shr.service
$ sudo  journalctl -n 100  -u  devstack@m-shr.service
```

* service list 확인 
```sh
(venv) stack@DevStack:~$ manila service-list
manila CLI is deprecated and will be removed in the future. Use openstack CLI instead. The equivalent command is " openstack share service list "
(venv) stack@DevStack:~$ manila service-list

(venv) stack@DevStack:~$ manila type-create so-36 False
(venv) stack@DevStack:~$ manila type-list
(venv) stack@DevStack:~$ manila type-key so-36 set share_backend_name=so
(venv) stack@DevStack:~$ manila type-key so-36 set snapshot_support=True
(venv) stack@DevStack:~$ manila type-key so-36 set storage_id=36
(venv) stack@DevStack:~$ manila type-key so-36 set volume_pool_id=svm1:N1_aggr1
(venv) stack@DevStack:~$ manila type-key so-36 set volume_pool=svm1
(venv) stack@DevStack:~$ manila type-show  so-36

source /opt/stack/data/venv/bin/activate
source ~/devstack/openrc admin admin
env | grep OS
sudo systemctl  daemon-reload
sudo systemctl  restart  devstack@m-shr.service

```


### 3. manila 데몬 모니터링 
####  python venv 설정
```sh
stack@DevStack:~$ source data/venv/bin/activate
(venv) stack@DevStack:~$ sudo systemctl daemon-reload
(venv) stack@DevStack:~$ sudo systemctl restart system-devstack.slice  
(venv) stack@DevStack:~$ source ~/devstack/openrc admin admin
```
#### journalctl  -f -u   devstack@m-shr

* 등록된 driver가 `Finished initialization of driver: 'SOShareDriver@DevStack@so'` 성공했는지 확인한다. 



##### devstack@m-shr.service
```sh
(venv) root@stack:/etc/systemd/system# cat devstack@m-shr.service

[Unit]
Description = Devstack devstack@m-shr.service

[Service]
ExecReload = /usr/bin/kill -HUP $MAINPID
TimeoutStopSec = 300
KillMode = process
ExecStart = /opt/stack/data/venv/bin/manila-share --config-file /etc/manila/manila.conf
User = stack
Environment = "PATH=/bin:/opt/stack/data/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin:/sbin"

[Install]
WantedBy = multi-user.target
```


#### 소스코드 copy

```sh
$ cp  /opt/stack/code/so-manila/manila/share/drivers/so/*  /opt/stack/manila/manila/share/drivers/so
```

### extra spec 정의 (진짜 주의 사항)
* 중요한 것은  extra-spec에 등록된 항목이 manila scheduler에 의해서 사용된다는 것이다.
* 그래서 드라이버 종속된 항목으로 정의하지 않으면 문제가 된다. 
* 따라서 드라이버에서 만 사용할 항목은 접두사을 붙여서 사용해야 한다. 
* 이렇게 하면 DB의 share-type-extra-specs 테이블에 해당 내용이 등록된다. 
* manila scheduler가 해당 함목은 드라이버 선택할 때 사용하지 않기 때문에 해당 드라이버가 선택 될 수 있다.
