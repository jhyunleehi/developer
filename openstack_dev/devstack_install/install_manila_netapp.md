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

HOST_IP=192.168.137.24

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
lvm_share_export_ips = 192.168.137.24
backend_availability_zone = manila-zone-0
driver_handles_share_servers = False
service_instance_user = manila
service_image_name = manila-service-image-master
path_to_private_key = /opt/stack/.ssh/id_ecdsa
path_to_public_key = /opt/stack/.ssh/id_ecdsa.pub
share_backend_name = CHICAGO
share_driver = manila.share.drivers.lvm.LVMShareDriver

[denver]
lvm_share_export_ips = 192.168.137.24
backend_availability_zone = manila-zone-1
driver_handles_share_servers = False
service_instance_user = manila
service_image_name = manila-service-image-master
path_to_private_key = /opt/stack/.ssh/id_ecdsa
path_to_public_key = /opt/stack/.ssh/id_ecdsa.pub
share_backend_name = DENVER
share_driver = manila.share.drivers.lvm.LVMShareDriver
```

### netapp manila 연동
### 1. netapp 환경 구성 

* svm 생성
* LIF 생성
* nfs export policy 생성
* nfs protocol enable
* aggr 할당 
* REST API를 사용하려면 ontap 9.12 이상 적용
* REST API 방식에서는  http, https 두가지 모두 가능 
* WebService 방식 XML은 ontap 9.12 이하 에서 https 방식으로 서비스

```sh 
FlexGroup::> vserver create -vserver manila-vserver -rootvolume vol1 -aggregate N1_aggr1 -ns-switch file -rootvolume-security-style unix
FlexGroup::> network interface create -vserver manila-vserver -lif manila-nfs-data -role data -home-node ontap-select-node -home-port e0b -address 192.168.56.117 -netmask 255.255.255.0
FlexGroup::> vserver export-policy rule create -vserver manila-vserver -policyname default -clientmatch 0.0.0.0/0 -rorule any -rwrule any -superuser any -anon 0
FlexGroup::> nfs modify -vserver manila-vserver -v4.0 enabled -v4.1 enabled -v4.1-pnfs enabled
FlexGroup::> vserver modify -vserver manila-vserver -aggr-list N1_aggr1,N1_aggr2
FlexGroup::> set d
FlexGroup::*> system services  web modify  -http-enabled true
FlexGroup::*> system services  web show

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
+----+------------------+------------------------+------+---------+-------+----------------------------+
| Id | Binary           | Host                   | Zone | Stamanila
(venv) stack@DevStack:~$
(venv) stack@DevStack:~$
(venv) stack@DevStack:~$ manila service-list
manila CLI is deprecated and will be removed in the future. Use openstack CLI instead. The equivalent command is " openstack share service list "
+----+------------------+------------------------+------+---------+-------+----------------------------+
| Id | Binary           | Host                   | Zone | Status  | State | Updated_at                 |
+----+------------------+------------------------+------+---------+-------+----------------------------+
| 3  | manila-scheduler | DevStack               | nova | enabled | up    | 2024-06-04T00:16:32.844902 |
| 4  | manila-data      | DevStack               | nova | enabled | up    | 2024-06-04T00:16:40.628233 |
| 5  | manila-share     | DevStack@cdotSingleSVM | nova | enabled | up    | 2024-06-04T00:16:34.583150 |
+----+------------------+------------------------+------+---------+-------+----------------------------+

(venv) stack@DevStack:~$ manila type-create general False
(venv) stack@DevStack:~$ manila type-create flash False
(venv) stack@DevStack:~$ manila type-create archive False
(venv) stack@DevStack:~$ manila type-create --snapshot_support True shared True
(venv) stack@DevStack:~$ manila type-list
manila CLI is deprecated and will be removed in the future. Use openstack CLI instead. The equivalent command is " openstack share type list "
+--------------------------------------+---------+------------+------------+--------------------------------------+-------------------------+-------------+
| ID                                   | Name    | visibility | is_default | required_extra_specs                 | optional_extra_specs    | Description |
+--------------------------------------+---------+------------+------------+--------------------------------------+-------------------------+-------------+
| 0c1d0278-06c2-4f04-9717-ce5579c26d73 | general | public     | -          | driver_handles_share_servers : False |                         | None        |
| 4c4c010b-05b9-44e0-b5b3-7d63c90fd703 | shared  | public     | -          | driver_handles_share_servers : True  | snapshot_support : True | None        |
| b6821982-8850-4f9d-a1ad-f4b52eacb43f | archive | public     | -          | driver_handles_share_servers : False |                         | None        |
| d938b6d9-72bf-41ab-90a1-d0bbe5125171 | flash   | public     | -          | driver_handles_share_servers : False |                         | None        |
+--------------------------------------+---------+------------+------------+--------------------------------------+-------------------------+-------------+
(venv) stack@DevStack:~$ manila type-key general set share_backend_name=cdotSingleSVM
(venv) stack@DevStack:~$ manila type-key general set snapshot_support=True
(venv) stack@DevStack:~$ manila type-key general set revert_to_snapshot_support=True
(venv) stack@DevStack:~$ manila type-key general set create_share_from_snapshot_support=Tru
(venv) stack@DevStack:~$ manila type-key general set create_share_from_snapshot_support=True

(venv) stack@DevStack:~$ manila list
manila CLI is deprecated and will be removed in the future. Use openstack CLI instead. The equivalent command is " openstack share list "
+--------------------------------------+----------+------+-------------+-----------+-----------+-----------------+---------------------------------+-------------------+
| ID                                   | Name     | Size | Share Proto | Status    | Is Public | Share Type Name | Host                            | Availability Zone |
+--------------------------------------+----------+------+-------------+-----------+-----------+-----------------+---------------------------------+-------------------+
| 9e120af1-aaff-4e9a-a446-a0be49b0b29f | myShare3 | 1    | NFS         | available | False     | general         | DevStack@cdotSingleSVM#N1_aggr1 | nova              |
| c0ec24d5-d96d-41f2-bcae-231511e3b282 | myShare2 | 1    | NFS         | available | False     | general         | DevStack@cdotSingleSVM#N1_aggr1 | nova              |
| 2c6040a3-01be-4eaa-b04e-c60d11725fa9 | myShare1 | 1    | NFS         | available | False     | general         | DevStack@cdotSingleSVM#N1_aggr1 | nova              |
+--------------------------------------+----------+------+-------------+-----------+-----------+-----------------+---------------------------------+-------------------+

```



#### manila.conf 예시 
```conf
[keystone_authtoken]
memcached_servers = localhost:11211
cafile = /opt/stack/data/ca-bundle.pem
project_domain_name = Default
project_name = service
user_domain_name = Default
password = secret
username = manila
auth_url = http://192.168.137.24/identity
interface = public
auth_type = password

[DEFAULT]
data_node_access_ips = 192.168.137.24
logging_exception_prefix = ERROR %(name)s [01;35m%(instance)s[00m
logging_default_format_string = %(color)s%(levelname)s %(name)s [[00;36m-%(color)s] [01;35m%(instance)s%(color)s%(message)s[00m
logging_context_format_string = %(color)s%(levelname)s %(name)s [[01;36m%(global_request_id)s %(request_id)s [00;36m%(project_name)s %(user_name)s%(color)s] [01;35m%(instance)s%(color)s%(message)s[00m
logging_debug_format_suffix = [00;33m{{(pid=%(process)d) %(funcName)s %(pathname)s:%(lineno)d}}[00m
transport_url = rabbit://stackrabbit:secret@192.168.137.24:5672/
manila_service_keypair_name = manila-service
enabled_share_backends = cdotSingleSVM
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

[neutron]
memcached_servers = localhost:11211
cafile = /opt/stack/data/ca-bundle.pem
project_domain_name = Default
project_name = service
user_domain_name = Default
password = secret
username = neutron
auth_url = http://192.168.137.24/identity
interface = public
auth_type = password

[nova]
memcached_servers = localhost:11211
cafile = /opt/stack/data/ca-bundle.pem
project_domain_name = Default
project_name = service
user_domain_name = Default
password = secret
username = nova
auth_url = http://192.168.137.24/identity
interface = public
auth_type = password

[cinder]
memcached_servers = localhost:11211
cafile = /opt/stack/data/ca-bundle.pem
project_domain_name = Default
project_name = service
user_domain_name = Default
password = secret
username = cinder
auth_url = http://192.168.137.24/identity
interface = public
auth_type = password

[glance]
memcached_servers = localhost:11211
cafile = /opt/stack/data/ca-bundle.pem
project_domain_name = Default
project_name = service
user_domain_name = Default
password = secret
username = glance
auth_url = http://192.168.137.24/identity
interface = public
auth_type = password


[cdotSingleSVM]
share_backend_name=cdotSingleSVM
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


### python venv 설정
```sh
stack@DevStack:~$ source data/venv/bin/activate
(venv) stack@DevStack:~$ sudo systemctl daemon-reload
(venv) stack@DevStack:~$ sudo systemctl restart system-devstack.slice  
(venv) stack@DevStack:~$ source ~/devstack/openrc admin admin
```

## manila debug 
```sh
(venv) root@stack:/opt/stack/data/venv# systemctl | grep devstack  
  devstack@m-api.service                                                                    loaded active     running         Devstack devstack@m-api.service
  devstack@m-dat.service                                                                    loaded active     running         Devstack devstack@m-dat.service
  devstack@m-sch.service                                                                    loaded active     running         Devstack devstack@m-sch.service
  devstack@m-shr.service                                                                    loaded active     running         Devstack devstack@m-shr.service


  ● devstack@m-shr.service - Devstack devstack@m-shr.service
     Loaded: loaded (/etc/systemd/system/devstack@m-shr.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2024-05-29 17:35:43 KST; 1 week 6 days ago
   Main PID: 117301 (manila-share)
      Tasks: 7 (limit: 9132)
     Memory: 191.7M
        CPU: 9h 33min 39.482s
     CGroup: /system.slice/system-devstack.slice/devstack@m-shr.service
             ├─117301 /opt/stack/data/venv/bin/python3.10 /opt/stack/data/venv/bin/manila-share --config-file /etc/manila/manila.conf
             ├─117935 /opt/stack/data/venv/bin/python3.10 /opt/stack/data/venv/bin/manila-share --config-file /etc/manila/manila.conf
             ├─117936 /opt/stack/data/venv/bin/python3.10 /opt/stack/data/venv/bin/manila-share --config-file /etc/manila/manila.conf
             ├─118311 /opt/stack/data/venv/bin/python3.10 /usr/local/bin/privsep-helper --config-file /etc/manila/manila.conf --privsep_context manila.privsep.sys_admin_pctxt --privsep_>
             └─118321 /opt/stack/data/venv/bin/python3.10 /usr/local/bin/privsep-helper --config-file /etc/manila/manila.conf --privsep_context manila.privsep.sys_admin_pctxt --privsep_>

```


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

### devstack@m-shr.service를 디버깅 하려면
* 생각을 해보면  `$ /opt/stack/data/venv/bin/manila-share --config-file /etc/manila/manila.conf`  이렇게 실행하면 되는데... vscode에서 디버깅이 안되는 단순한 상황이였기 때문에
* vscode의 setting에서 python program을 기준으로 할지 아니면  `/opt/stack/data/venv/bin/manila-share`를 program으로 지정했으면 이렇게 헛 수고는 없을 것을..

```json
 {
            "name": "Python: DevStack-Share",
            "type": "python",
            "request": "launch",
            //"program": "/usr/local/bin/openstack",              
            "program": "/opt/stack/data/venv/bin/manila-share",
            "args": [               
                "--config-file",
                "/etc/manila/manila.conf"
            ],
            "console": "integratedTerminal",
            "env": {                
                "VIRTUALENV_CMD": "python3 -m venv",
                "USE_PYTHON3": "True",
                "PYTHON3_VERSION": "3.10"
            },
            "justMyCode": false,
            "gevent": true,
            "redirectOutput": true
        }
```        
