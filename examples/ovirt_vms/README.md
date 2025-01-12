## Bootstrap with profiles
### Concept
Auto-generation of virtual machine configurations based on **profiles**

**Profiles** is skeletons your VMs configuration. Using auto-generation, you receive a ready-to-fill or ready-to-use YAML file for configuring your virtual machines in oVirt

### Before start
1. Generate `ovirt_vms.yml` with virtual machines configuration from profile with script. Don't forget to change the values ​​before and after generating. You can use your own profiles for the generator
2. Copy `ovirt_*.yml` to `files/` dir and `prepare.yml`, `absent.yml` to playbooks dir in your Ansible project
3. Manage your infrastructure with state playbook
    - 🏗️ `prepare.yml` - create tags, affinity rules and virtual machines
    - 💥 `absent.yml` - destroy tags, affinity rules and virtual machines