# Role `mrcnkwcz.ovirt.ovirt_nics`
Managing network interface controllers

## Vars
```yml
---
ovirt_nics_vms:
  - name: string                   # Name of VM [required]
    nics:                          # List of nics
      - interface: string          # Set nic type
                                   # (e1000, pci_passthrough, rtl8139, rtl8139_virtio, spapr_vlan, virtio*)
        mac_address: string        # Set custom MAC
        network: string            # Set network [required]
        network_filter_parameters: # Set network filters
          - name: string           # Filter name
            value: string          # Filter value
        name: string               # Nic name [required]
        linked: boolean            # Link nic to VM
        profile: string            # Nic profile
        state: string              # Nic state (present*, absent, plugged, unplugged)

ovirt_nics_wait: true       # Waiting for a response about nics state
ovirt_nics_timeout: 3       # Nics state timeout
ovirt_nics_poll_interval: 1 # Interval for checking nic state

```

## Examples
```yml
---
- name: Add networks to virtual routers
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - mrcnkwcz.ovirt.ovirt_nics
  vars:
    ovirt_auth_hostname: engine.ovirt.infra.example
    ovirt_auth_username: api@ovirt@internal
    # It is advisable to use ansible-vault for secrets
    ovirt_auth_password: "*******"
    ovirt_nics_vms:
      - name: mrcnwkcz-router01
        nics:
          - name: vnic1
            network: mrcnwkcz-net-ovn01
          - name: vnic2
            network: mrcnwkcz-net-ovn02
      - name: mrcnwkcz-router02
        nics:
          - name: vnic1
            network: mrcnwkcz-net-ovn01
          - name: vnic2
            network: mrcnwkcz-net-ovn02


```
