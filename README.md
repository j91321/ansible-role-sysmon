ansible-role-sysmon
=========

[![GitHub license](https://img.shields.io/github/license/j91321/ansible-role-sysmon?style=flat-square)](https://github.com/j91321/ansible-role-sysmon/blob/master/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/j91321/ansible-role-sysmon.svg?style=flat-square)](https://github.com/j91321/ansible-role-sysmon/commit/master)
![Build](https://github.com/j91321/ansible-role-sysmon/workflows/Test%20ansible%20role%20installation%20and%20publish%20to%20galaxy/badge.svg)
[![Twitter](https://img.shields.io/twitter/follow/j91321.svg?style=social&label=Follow)](https://twitter.com/j91321)

An Ansible role that installs Sysmon with selected configuration. Included configurations are [SwiftOnSecurity sysmon config](https://github.com/SwiftOnSecurity/sysmon-config) or [olafhartong sysmon-modular config](https://github.com/olafhartong/sysmon-modular). You can also supply your own config.

Currently there are no configurations included for Linux. You must supply your own if you wish to use this role on Linux hosts.

Supported platforms:

- Windows 10
- Windows Server 2019
- Windows Server 2016
- Debian 10
- Debian 11
- Ubuntu 18.04
- Ubuntu 20.04
- RHEL/CentOS 8

Requirements
------------

None

Role Variables
--------------

Ansible variables from defaults/main.yml

```
sysmon_install_path: "C:\\Program Files\\Sysmon"
sysmon_version: "11.11"
sysmon_config: swiftonsecurity-sysmonconfig.xml
sysmon_linux_config: linux_sysmonconfig.xml
```

Dependencies
------------

None

Example Playbook Windows
----------------

```
- name: Install Sysmon
  hosts:
    - windows_host
    - linux_host
  vars:
    sysmon_install_path: "C:\tools\Sysmon"
    sysmon_version: "13.30"
    sysmon_config: olafhartong-sysmonconfig.xml
    sysmon_linux_config: linux-sysmonconfig.xml
  roles:
    - ansible-role-sysmon
```

License
-------

MIT

Author Information
------------------

- j91321
- [viktor0x53](https://github.com/viktor0x53)
