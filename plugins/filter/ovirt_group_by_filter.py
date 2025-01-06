from collections import defaultdict

class FilterModule(object):
    'Filter for grouping oVirt objects'
    def filters(self):
        'Define filters'
        return {
            'ovirt_group_by_tags': self.ovirt_group_by_tags,
            'ovirt_group_by_affinity_labels': self.ovirt_group_by_affinity_labels,
            'ovirt_group_by_affinity_groups': self.ovirt_group_by_affinity_groups,
        }
    def ovirt_group_by_tags(self, vms):
        'Filter for grouping by tags'
        vms_tags = defaultdict(lambda: {'vms': []})
        for vm in vms:
            for tag in vm.get('tags', []):
                vms_tags[tag]['vms'].append(vm.get('name', ''))
        return [
            {
                'name': name,
                **data
            }
            for name, data in vms_tags.items()
        ]
    def ovirt_group_by_affinity_labels(self, vms):
        'Filter for grouping by affinity labels'
        vms_affinity_labels = defaultdict(lambda: {'vms': []})
        for vm in vms:
            for label in vm.get('affinity_labels', []):
                vms_affinity_labels[label]['vms'].append(vm['name'])
                vms_affinity_labels[label]['cluster'] = vm['cluster']
        return [
            {
                'name': name,
                **data
            }
            for name, data in vms_affinity_labels.items()
        ]
    def ovirt_group_by_affinity_groups(self, vms):
        'Filter for grouping by affinity groups'
        vms_affinity_groups = defaultdict(lambda: {'vms': []})
        for vm in vms:
            for group in vm.get('affinity_groups', []):
                vms_affinity_groups[group]['vms'].append(vm['name'])
                vms_affinity_groups[group]['cluster'] = vm['cluster']
        return [
            {
                'name': name,
                **data
            }
            for name, data in vms_affinity_groups.items()
        ]