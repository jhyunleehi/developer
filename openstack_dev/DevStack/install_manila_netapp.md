[](https://docs.openstack.org/manila/latest/contributor/development-environment-devstack.html)


```sh
################################################################
# This local.conf sets up Devstack with manila enabling the LVM
# driver which operates in driver_handles_share_services=False
# mode
################################################################

[[local|localrc]]
ADMIN_PASSWORD=secret
DATABASE_PASSWORD=$ADMIN_PASSWORD
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD
DEST=/opt/stack
DATA_DIR=/opt/stack/data
LOGFILE=/opt/stack/devstacklog.txt


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

### install 

```sh
./stack.sh

$ systemctl status devstack@m-sch
$ systemctl status devstack@m-shr
$ systemctl status devstack@m-dat

$ source DEVSTACK_DIR/openrc admin demo
$ manila service-list

$ journalctl -a -o short-precise --unit devstack@m-sch
$ journalctl -a -o short-precise --unit devstack@m-shr
$ journalctl -a -o short-precise --unit devstack@m-dat


