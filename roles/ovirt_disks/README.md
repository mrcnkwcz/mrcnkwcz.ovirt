# Role `mrcnkwcz.ovirt.ovirt_disks`
Managing disks

## Vars
```yml
---
ovirt_disks_vms:
  - name: string                           # Name of VM [required]
    storage_domain: string                 # Name of storage domain, where disks should be created
    disk_format: string                    # Set disk format of VM (cow, raw)
    disks:                                 # List of virtual disks
      - activate: boolean                  # Activate disk after creation (true, false)
        backup: string                     # Enable incremental backup option
        bootable: boolean                  # Set disk as bootable (true, false)
        description: string                # Add description to disk
        format: string                     # Set disk format (cow*, raw). May inherit from "disk_format" [required]
        interface: string                  # Set disk interface (virtio_scsi*, virtio, sata, ide)
        name: string                       # Name of disk [required]
        pass_discard: boolean              # Set pass discard (true, false)
        profile: string                    # Set disk profile
        read_only: boolean                 # Set disk as read only
        shareable: boolean                 # Set disk as shareable (true, false)
        size: string                       # Set disk size [required]
        storage_domain: string             # Set storage domain. May inherit from "storage_domain" value [required]
        wipe_after_delete: boolean         # Set wipe after delete (true, false)
        state: string                      # State of disk

ovirt_disks_vms_prefix_name: true # Use VM name as prefix for disks (true*, false)
ovirt_disks_vms_separator: "-"    # Set separator symbol for prefix
ovirt_disks_wait: true            # Waiting for a response about disks state
ovirt_disks_timeout: 300          # Disks state timeout
ovirt_disks_poll_interval: 5      # Interval for checking disks state

```

## Examples
```yml
---
- name: Create additional data and log disks for worker nodes
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - mrcnkwcz.ovirt.ovirt_disks
  vars:
    ovirt_auth_hostname: engine.ovirt.infra.example
    ovirt_auth_username: api@ovirt@internal
    # It is advisable to use ansible-vault for secrets
    ovirt_auth_password: "*******"
    ovirt_disk_vms:
      - name: mrcnkwcz-worker-1
        storage_domain: "iscsi-ssd-storage-1"
        disk_format: raw
        disks: # By default, disk names will be prefixed with the VM name
          - name: data
            size: 64 GiB
          - name: logs
            size: 16 GiB
      - name: mrcnkwcz-worker-2
        storage_domain: "iscsi-ssd-storage-1"
        disk_format: raw
        disks: # By default, disk names will be prefixed with the VM name
          - name: data
            size: 64 GiB
          - name: logs
            size: 16 GiB

```
