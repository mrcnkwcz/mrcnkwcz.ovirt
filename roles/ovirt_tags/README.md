# Role `mrcnkwcz.ovirt.ovirt_tags`
Managing tags for virtualization resources

## Vars
```yml
---
ovirt_tags:
# - name: string         # Name of tag [required]
#   description: string  # Description of tag
#   hosts:               # List of hosts assigned to tag
#     - string           # Name of host
#   parent: string       # Parent tag
#   vms:                 # List of VMs assigned to tag
#     - string           # Name of VM
#   state: string        # State of tag (present*, absent, attached, detached)

ovirt_tags_wait: true       # Waiting for a response about tags state
ovirt_tags_timeout: 3       # Tags state timeout
ovirt_tags_poll_interval: 1 # Interval for checking tags state

```

## Examples
```yml
---
- name: Create tags for K8S resources
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - mrcnkwcz.ovirt.ovirt_tags
  vars:
    ovirt_auth_hostname: engine.ovirt.infra.example
    ovirt_auth_username: api@ovirt@internal
    # It is advisable to use ansible-vault for secrets
    ovirt_auth_password: "*******"

    # Creating hierarchy of tags
    #
    # `mrcnkwcz`
    # └── `mrcnkwcz-k8s`
    #     ├── `mrcnkwcz-k8s-master`
    #     ├── `mrcnkwcz-k8s-worker`
    #     └── `mrcnkwcz-k8s-lb`

    ovirt_tags:
      - name: mrcnkwcz
        description: Martsinkevich resources
      - name: mrcnwkcz-k8s
        description: Martsinkevich K8S resources
        parent: mrcnkwcz
      - name: mrcnwkcz-k8s-master
        description: Martsinkevich K8S Master nodes
        parent: mrcnwkcz-k8s
      - name: mrcnwkcz-k8s-worker
        description: Martsinkevich K8S Worker nodes
        parent: mrcnwkcz-k8s
      - name: mrcnwkcz-lb
        description: Martsinkevich K8S Load Balancer nodes
        parent: mrcnwkcz-k8s

```
