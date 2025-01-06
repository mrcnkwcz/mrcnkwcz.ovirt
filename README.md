# mrcnwkcz.ovirt
Collection for oVirt environments 

## Roles
| Name | Description | Dependencies | Tags |
| ---- | ----------- | ------------ | ---- |
| [ovirt_affinity_groups](roles/ovirt_affinity_groups/) | Managing affinity groups | ovirt_async, ovirt_auth | - |
| [ovirt_affinity_labels](roles/ovirt_affinity_labels/) | Managing affinity labels | ovirt_async, ovirt_auth | - |
| [ovirt_async](roles/ovirt_async/) | Managing async check operations | - | - |
| [ovirt_auth](roles/ovirt_auth/) | Managing authentication | - | - |
| [ovirt_disks](roles/ovirt_disks/) | Managing disks | ovirt_async, ovirt_auth | - |
| [ovirt_nics](roles/ovirt_nics/) | Managing network interface controllers | ovirt_async, ovirt_auth | - |
| [ovirt_tags](roles/ovirt_tags/) | Managing tags | ovirt_async, ovirt_auth | - |
| [ovirt_vms](roles/ovirt_vms/) | Managing virtual machines | ovirt_async, ovirt_auth, ovirt_affinity_groups, ovirt_affinity_labels, ovirt_disks, ovirt_nics, ovirt_tags | `auth`, `state`, `nics`, `disks`, `tags`, `affinity_labels`, `affinity_groups`, `init_state` |

## Plugins
### Filters
* [ovirt_group_by_affinity_groups](plugins/filter/ovirt_group_by_affinity_groups.yml)
* [ovirt_group_by_affinity_labels](plugins/filter/ovirt_group_by_affinity_labels.yml)
* [ovirt_group_by_tags](plugins/filter/ovirt_group_by_tags.yml)

## Licenses
* Apache 2.0
* GPL 3.0

## Authors
* Martsinkevich Artur (@mrcnkwcz)