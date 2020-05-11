"""Role testing files using testinfra."""


def test_lvm_package_shall_be_installed(host):
    assert host.package("lvm2").is_installed


def test_non_persistent_volume_group_is_created(host):
    command = """sudo vgdisplay | grep -c 'my_vg'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_mylv_logical_volume_is_created(host):
    command = """sudo lvs -o lv_name  my_vg --separator='|' --noheadings \
    | grep -c 'my_lv'"""
    cmd = host.run(command)
    assert int(cmd.stdout.rstrip()) >= 1


def test_volume_is_mounted(host):
    host.file("/var/lib/mountpoint").mode == 0o731
