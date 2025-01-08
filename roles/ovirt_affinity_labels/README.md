# Role `mrcnkwcz.ovirt.ovirt_affinity_labels`
Managing affinity labels

## Vars
```yml
---
ovirt_affinity_labels:
# - name: string    # Name of affinity label [required]
#   cluster: string # Cluster of affinity label [required]
#   hosts:          # List of hosts assigned to affinity label
#     - string      # Name of host
#   vms:            # List of VMs assigned to affinity label
#     - string      # Name of VM
#   state: string   # Label state (present*, absent)

ovirt_affinity_labels_wait: true       # Waiting for a response about labels state
ovirt_affinity_labels_timeout: 3       # Labels state timeout
ovirt_affinity_labels_poll_interval: 1 # Interval for checking labels state
```

## Examples
```yml
---
- name: Create affinity labels for K8S nodes
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - mrcnkwcz.ovirt.ovirt_affinity_labels
  vars:
    ovirt_auth_hostname: engine.ovirt.infra.example
    ovirt_auth_username: api@ovirt@internal
    # It is advisable to use ansible-vault for secrets
    ovirt_auth_password: "*******"

    ovirt_affinity_labels:
      - name: mrcnkwcz-k8s-label01
        cluster: APP
        vms:
          - mrcnkwcz-k8s-worker01-sandbox
          - mrcnkwcz-k8s-master01-sandbox
          - mrcnkwcz-k8s-lb01-sandbox
      - name: mrcnkwcz-k8s-label02
        cluster: APP
        vms:
          - mrcnkwcz-k8s-worker02-sandbox
          - mrcnkwcz-k8s-master02-sandbox
          - mrcnkwcz-k8s-lb02-sandbox

```
