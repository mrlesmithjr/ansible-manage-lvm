"""Role testing files using testinfra."""


def test_lvm_package_shall_be_installed(host):
    assert host.package("lvm2").is_installed


def test_non_persistent_volume_group_is_created(host):
    command = """sudo vgdisplay | grep -c 'my_vg'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
