"""VMs generator"""

import argparse
import yaml

PROFILES_VAR = "ovirt_vm_profiles"
VMS_VAR = "ovirt_vms"


class IndentDumper(yaml.Dumper): # pylint: disable=too-many-ancestors
    """Dumper class for fix YAML render"""

    def increase_indent(self, flow=False, indentless=False):
        """Increase indent for nested list"""
        return super().increase_indent(flow, False)

    def ignore_aliases(self, data):
        """Ignore aliases for YAML dump"""
        return True


def generate_vms_from_profiles(profiles_input_file, profiles_output_file):
    """Generate func"""
    with open(profiles_input_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    profiles = data.get(PROFILES_VAR, {})
    vm_list = []
    for profile_name, profile_data in profiles.items():
        count = profile_data.get("count", 1)
        for i in range(1, count + 1):
            vm = {
                "name": f"{profile_name}-{i}",
                **{k: v for k, v in profile_data.items() if k not in ["count"]},
            }
            vm_list.append(vm)
    with open(profiles_output_file, "w", encoding="utf-8") as f:
        yaml.dump(
            {VMS_VAR: vm_list},
            f,
            Dumper=IndentDumper,
            default_flow_style=False,
            sort_keys=False,
            width=120,
            explicit_start=True,
        )

    print(f"VMs list saved to: {profiles_output_file}")


def main():
    """Main func"""
    parser = argparse.ArgumentParser(
        description="CLI for generating of list VM configuration from profiles"
    )
    parser.add_argument(
        "-f", "--profiles", required=True, type=str, help="YAML file with profiles"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="ovirt_vms.yml",
        type=str,
        help="Path to the generated YAML",
    )
    args = parser.parse_args()
    generate_vms_from_profiles(args.profiles, args.output)


if __name__ == "__main__":
    main()
