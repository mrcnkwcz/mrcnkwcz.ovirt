# Role `mrcnkwcz.ovirt.ovirt_async`
Managing async check operations for resources. Used for other roles

## Vars
```yml
---
ovirt_async_statuses: [] # List of async statuses for checking
ovirt_async_retries: 3   # Count of retries
ovirt_async_delay: 1     # Retry interval
```

## Examples
```yml
---
# Example task for an abstract resource
- name: Resource | Check statuses
  ansible.builtin.import_role:
    name: mrcnkwcz.ovirt.ovirt_async
    tasks_from: check.yml
  vars:
    ovirt_async_statuses: "{{ ovirt_resource_statuses.results }}"
    ovirt_async_retries: "{{ ovirt_resource_timeout // ovirt_resource_poll_interval }}"
    ovirt_async_delay: "{{ ovirt_resource_poll_interval }}"
  when: ovirt_resource_wait

```
