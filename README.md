# ansible-manage-lvm

An [Ansible](https://www.ansible.com) role to create, extend, and resize [LVM](https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)) volume groups and logical volumes.

> Used by [OpenStack Kayobe](https://docs.openstack.org/kayobe/latest/) for LVM management.

## Ansible Galaxy

```bash
ansible-galaxy install mrlesmithjr.manage_lvm
```

> **Note:** As of December 2025, the canonical Galaxy name is `mrlesmithjr.manage_lvm` (underscore).
> Update any `requirements.yml` using the older hyphen-style name `mrlesmithjr.manage-lvm`.

<details>
<summary>Historical download statistics</summary>

| Role Name | Downloads (as of Dec 2025) |
|-----------|---------------------------|
| `mrlesmithjr.manage_lvm` | 697,492 |
| `mrlesmithjr.manage-lvm` | 494,517 |
| **Combined** | **1,192,009** |

Download counts reset when roles are re-imported to Galaxy. These figures represent actual historical usage.
</details>

## Supported Platforms

Any Linux distribution with LVM support, including:

| Platform | Versions |
|----------|----------|
| Ubuntu | 20.04, 22.04, 24.04 |
| Debian | 11, 12 |
| Rocky Linux / RHEL | 8, 9 |
| Fedora | 39+ |

## Requirements

- Unpartitioned disk devices to assign to volume groups
- `lvm2` package (installed automatically by the role)

## Important: Safety Default

`manage_lvm` defaults to `false`. **The role will not make any disk changes** unless you explicitly set:

```yaml
manage_lvm: true
```

This prevents accidental modifications on misconfigured runs.

## Quick Start

```yaml
---
- hosts: all
  become: true
  vars:
    manage_lvm: true
    lvm_groups:
      - vgname: data-vg
        disks:
          - /dev/sdb
        create: true
        lvnames:
          - lvname: data
            size: 100%FREE
            create: true
            filesystem: ext4
            mount: true
            mntp: /data
  roles:
    - role: mrlesmithjr.manage_lvm
```

## Key Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `manage_lvm` | `false` | Master switch — must be `true` to make any changes |
| `lvm_groups` | `[]` | List of volume group definitions |
| `pvresize_to_max` | `false` | Resize all PVs to maximum available size |

### `lvm_groups` Structure

```yaml
lvm_groups:
  - vgname: my-vg           # Volume group name
    disks:                   # Physical volumes to assign
      - /dev/sdb
      - /dev/sdc
    create: true             # true = create, false = remove
    pvresize: false          # Resize PV to max size
    lvnames:
      - lvname: data         # Logical volume name
        size: 50g            # Size: 10g | 1024 (MB) | 100%FREE
        create: true         # true = create, false = remove
        filesystem: ext4     # ext4 | xfs | swap | etc.
        mount: true          # Mount after creation
        mntp: /data          # Mountpoint
        mopts: noatime       # Mount options (optional)
        fsopts:              # Filesystem creation options (optional)
```

See [defaults/main.yml](defaults/main.yml) for full examples including XFS, swap, and OpenStack Cinder volumes.

## License

MIT

## Support This Project

This role has been downloaded over **1.1 million times** from Ansible Galaxy.
If your organization depends on it in production, consider
[sponsoring its maintenance](https://github.com/sponsors/mrlesmithjr).
Enterprise support tiers are available.

## Author

Larry Smith Jr. — [everythingshouldbevirtual.com](http://everythingshouldbevirtual.com) · [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
