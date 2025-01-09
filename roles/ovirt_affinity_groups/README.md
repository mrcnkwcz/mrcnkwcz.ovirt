# Role `mrcnkwcz.ovirt.ovirt_affinity_groups`
ManAffinity Grouping affinity groups

## Vars
```yml
---
ovirt_affinity_groups:
  - name: string          # Name of affinity group [required]
    cluster: string       # Name of cluster for group [required]
    description: string   # Description of group
    host_enforcing: bool  # Enforce host rule (true, false)
    host_rule: string     # Host rule (positive, negative, disabled)
    hosts:                # List of hosts assigned to affinity groups
      - string            # Name of host
    hosts_labels:         # List of host affinity labels assigned to affinity groups
      - string            # Name of host affinity label
    vm_enforcing: bool    # Enforce VM rule (true, false)
    vm_rule: string       # VM rule (positive, negative, disabled)
    vms:                  # List of virtuAffinity Label machines assigned to affinity groups
      - string            # Name of virtuAffinity Label machine
    vms_labels:           # List of VM affinity labels assigned to affinity groups
      - string            # Name of VM affinity label
    state: string         # State of group (present*, absent)

ovirt_affinity_groups_wait: true       # Waiting for a response about groups state
ovirt_affinity_groups_timeout: 3       # Groups state timeout
ovirt_affinity_groups_poll_interval: 1 # Interval for checking groups state

```

## Examples
```yml
---
- name: Create affinity groups for K8S nodes
  hosts: localhosth
  connection: local
  gather_facts: false
  roles:
    - mrcnkwcz.ovirt.ovirt_affinity_groups
  vars:
    ovirt_auth_hostname: engine.ovirt.infra.example
    ovirt_auth_username: api@ovirt@internal
    # It is advisable to use ansible-vault for secrets
    ovirt_auth_password: "*******"

    # Example of running a VM after creating a affinity group
    # The cluster is logically divided into two parts and VMs do not compete for resources
    # And with the help of labels and the negative rule, VMs are running on different hosts
    #
    # `APP`
    # ├── `mrcnkwcz-k8s-group01`
    # │   ├── `app-host01`
    # │   │   └── `mrcnkwcz-k8s-worker01-sandbox` (`mrcnkwcz-k8s-label01`)
    # │   ├── `app-host02`
    # │   │   └── `mrcnkwcz-k8s-master01-sandbox` (`mrcnkwcz-k8s-label01`)
    # │   └── `app-host03`
    # │       └── `mrcnkwcz-k8s-lb01-sandbox`     (`mrcnkwcz-k8s-label01`)
    # └── `mrcnkwcz-k8s-group02`
    #     ├── `app-host04`
    #     │   └── `mrcnkwcz-k8s-worker02-sandbox` (`mrcnkwcz-k8s-label02`)
    #     ├── `app-host05`
    #     │   └── `mrcnkwcz-k8s-master02-sandbox` (`mrcnkwcz-k8s-label02`)
    #     └── `app-host06`
    #         └── `mrcnkwcz-k8s-lb02-sandbox`     (`mrcnkwcz-k8s-label02`)

    ovirt_affinity_groups:
      - name: mrcnkwcz-k8s-group01
        cluster: APP
        host_enforcing: true
        host_rule: positive
        hosts:
          - app-host01
          - app-host02
          - app-host03
        vm_enforcing: true
        vm_rule: negative
        vms_labels:
          - mrcnkwcz-k8s-label01

      - name: mrcnkwcz-k8s-group02
        cluster: APP
        host_enforcing: true
        host_rule: positive
        hosts:
          - app-host04
          - app-host05
          - app-host06
        vm_enforcing: true
        vm_rule: negative
        vms_labels:
          - mrcnkwcz-k8s-label02

```
