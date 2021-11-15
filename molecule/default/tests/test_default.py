import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_sysmon_package(host):
    package_auditbeat = host.package('sysmonforlinux')
    assert package_auditbeat.is_installed


def test_sysmon_etc_config(host):
    config = host.file("/etc/sysmon/config.xml")
    assert config.exists
    assert config.is_file


def test_sysmon_opt_rules(host):
    config = host.file("/opt/sysmon/config.xml")
    assert config.exists
    assert config.is_file

def test_sysmon_eula_accepted(host):
    eula = host.file("/opt/sysmon/eula_accepted")
    assert eula.exists
    assert eula.is_file
