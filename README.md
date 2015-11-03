Role Name
=========

Role to manage LVM Groups/Logical Volumes. Can be used to create, extend or resize LVM.

Requirements
------------

Devices/disks to be part of the LVM setup must be identified prior to using this role. Ensure that you select the correct devices/disks.

##### Creating LVM
###### /dev/sda5

##### Extending LVM
###### Current disk /dev/sda5
###### New Disk /dev/sdb

Role Variables
--------------

````
---
# defaults file for ansible-manage-lvm
create_lvm: false  #defines if lvm should be created when adding additional disks...should be defined in host_vars/host (do not set extend or resize to true)
create_lvname: test-lv  #define lvm name when adding additional disks...should be defined in host_vars/host
create_lvsize: 100%FREE  #defines the lvm lv size --- (10G) - would create new lvm with 10Gigabytes -- (512) - would create new lvm with 512m
create_vgname: test-vg  #defines the lvm vg name to create...
extend_lvm: false  #defines if lvm vg should be extended (do not set create to true)...should be defined in host_vars/host
extend_lvname: test-lv  #defines the lvm lv name to extend...should be defined in host_vars/host
extend_vgname: test-vg  #defines the lvm vg name to extend...should be defined in host_vars/host
lvextend_options: '-L+10G'  #defines the options to pass to lvextend --- ('-L+10G') - would increase by 10GB whereas ('-l +100%FREE') would increase to full capacity
lvm_current_disk: /dev/sda5  #defines the disk currently configured for lvm...should be defined in host_vars/host
lvm_extend_disks: '{{ lvm_current_disk }},{{ lvm_new_disk }}'  #defines the disks to extend in lvm group...should be defined in host_vars/host
lvm_filesystem: ext4  #defines the filesystem type to create when configuring lvm ( ext3, ext4, xfs, etc. )...should be defined in host_vars/host
lvm_new_disk: /dev/sdb  #defines the new disk being added to volume group...should be defined in host_vars/host
lvm_new_mntp: /mnt/test  #defines the desired mount point to be created and new logical volume to be mounted to...should be defined in host_vars/host
resize_lvm: false  #set to true if resizing the logical volume (do not set create to true)...should be defined in host_vars/host
resize_lvname: test-lv  #defines the logical volume name to resize...should be defined in host_vars/host
resize_vgname: test-vg  #defines the volume group name to resize...should be defined in host_vars/host
````

Dependencies
------------

None

Example Playbook
----------------

#### Galaxy
-----------
    - hosts: servers
      roles:
         - { role: mrlesmithjr.manage-lvm }
#### GitHub
-----------
    - hosts: servers
      roles:
        - ansible-manage-lvm

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
