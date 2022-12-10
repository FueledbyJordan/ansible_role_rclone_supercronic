def test_rclone_conf_dir(host):
    config_dir = host.file("/etc/rclone/config")
    assert config_dir.exists
    assert config_dir.is_directory
    assert config_dir.uid == 1000
    assert config_dir.gid == 1000
    assert config_dir.mode == 0o755


def test_rclone_scripts_dir(host):
    scripts_dir = host.file("/etc/rclone/scripts")
    assert scripts_dir.exists
    assert scripts_dir.is_directory
    assert scripts_dir.uid == 1000
    assert scripts_dir.gid == 1000
    assert scripts_dir.mode == 0o755


def test_rclone_config(host):
    rclone_conf = host.file("/etc/rclone/config/rclone.conf")
    assert rclone_conf.exists
    assert rclone_conf.is_file
    assert rclone_conf.uid == 1000
    assert rclone_conf.gid == 1000
    assert rclone_conf.mode == 0o600
    assert rclone_conf.content_string == '[Something]\ntype = s3\naccount = fdsa\nkey = asdf\nhard_delete = true\n\n' # noqa E501


def test_stub_script(host):
    rclone_conf = host.file("/etc/rclone/scripts/some_stub_sh")
    assert rclone_conf.exists
    assert rclone_conf.is_file
    assert rclone_conf.uid == 1000
    assert rclone_conf.gid == 1000
    assert rclone_conf.mode == 0o700
    assert rclone_conf.content_string == '#!/bin/bash\n\necho "Hello!"\n'


def test_rclone_crontab(host):
    rclone_conf = host.file("/etc/rclone/config/crontab")
    assert rclone_conf.exists
    assert rclone_conf.is_file
    assert rclone_conf.uid == 1000
    assert rclone_conf.gid == 1000
    assert rclone_conf.mode == 0o644
    assert rclone_conf.content_string == '45 8 * * * /etc/rclone/scripts/some_stub_sh\n' # noqa E501
