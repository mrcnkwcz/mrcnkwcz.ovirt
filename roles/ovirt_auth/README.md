# Role `mrcnkwcz.ovirt.ovirt_auth`
Managing authentication

## Vars
```yml
---
ovirt_auth_url: ""          # URL Engine. Example: "https://engine.infra.example/ovirt-engine/api"
ovirt_auth_username: ""     # Username with domain for authentication. Example: "api@internal" or "api@internalsso"
ovirt_auth_password: ""     # Password for user
ovirt_auth_hostname: ""     # Engine hostname. May be used instead of URL. Example: "engine.ovirt.infra.example"
ovirt_auth_ca_file: ""      # A PEM file containing the trusted CA certificates. Example: ~/ca.crt
ovirt_auth_insecure: false  # A boolean flag if the server TLS certificate should be checked (true, false*)
ovirt_auth_token:           # May be used token instead of username with password
ovirt_auth_headers: {}      # A dictionary of HTTP headers to be added to each API call
ovirt_auth_kerberos: false  # Set using kerberos auth instead of standard auth (true, false*)
ovirt_auth_compress: true   # A boolean flag if the SDK should ask server to send compressed responses (true*, false)
ovirt_auth_timeout: 15      # Time during which the connection to the server must be established
```

## Environment variables
```bash
`OVIRT_URL`      # May be used instead of `ovirt_auth_url`
`OVIRT_HOSTNAME` # May be used instead of `ovirt_auth_hostname`
`OVIRT_USERNAME` # May be used instead of `ovirt_auth_username`
`OVIRT_PASSWORD` # May be used instead of `ovirt_auth_password`
`OVIRT_TOKEN`    # May be used instead of `ovirt_auth_token`
`OVIRT_CAFILE`   # May be used instead of `ovirt_auth_ca_file`

```

## Examples
```yml
---
- name: Use auth tasks and get info about application Cluster
  hosts: localhost
  connection: local
  gather_facts: false
  vars:
    ovirt_auth_hostname: engine.ovirt.infra.example
    ovirt_auth_username: api@ovirt@internal
    # It is advisable to use ansible-vault for secrets
    ovirt_auth_password: "*******"
  pre_tasks:
    - name: Pre Auth | Obtain token
      ansible.builtin.include_role:
        name: mrcnkwcz.ovirt.ovirt_auth
        tasks_from: obtain_token.yml
  post_tasks:
    - name: Post Auth | Revoke token
      ansible.builtin.include_role:
        name: mrcnkwcz.ovirt.ovirt_auth
        tasks_from: revoke_token.yml
  tasks:
    - name: Get info about Cluster `APP`
      ovirt.ovirt.ovirt_cluster_info:
        auth: "{{ ovirt_auth }}"
        pattern: "name=APP"
      register: cluster_app_info
    - name: Show info about Cluster `APP`
      ansible.builtin.debug:
        var: cluster_app_info

```
