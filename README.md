ansible-role-sysmon
=========

An Ansible role that installs Sysmon with selected configuration. Included configurations are [SwiftOnSecurity sysmon config](https://github.com/SwiftOnSecurity/sysmon-config) or [olafhartong sysmon-modular config](https://github.com/olafhartong/sysmon-modular). You can also supply your own config.

Supported platforms:

- Windows 10
- Windows Server 2019
- Windows Server 2016

Requirements
------------

None

Role Variables
--------------

Ansible variables from defaults/main.yml

```
sysmon_install_path: "C:\\Program Files\\Sysmon"
sysmon_version: 1042
sysmon_config: swiftonsecurity-sysmonconfig.xml
```

The `sysmon_version` variable is used to keep track of which Sysmon version is currently installed. Role creates a registry entry in `HKLM:\SYSTEM\CurrentControlSet\Services\Sysmon` or `HKLM:\SYSTEM\CurrentControlSet\Services\Sysmon64` with key `Version` containing the variable value.

Dependencies
------------

None

Example Playbook
----------------

```
- name: Install sysmon to workstations
  hosts:
    - workstations:
  vars:
    sysmon_install_path: "C:\tools\Sysmon"
    sysmon_version: 1042
    sysmon_config: swiftonsecurity-sysmonconfig.xml
  roles:
    - ansible-role-sysmon
```


License
-------

MIT

Author Information
------------------

j91321
[viktor0x53](https://github.com/viktor0x53)
