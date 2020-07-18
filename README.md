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
sysmon_version: "11.11"
sysmon_config: swiftonsecurity-sysmonconfig.xml
```

Dependencies
------------

None

Example Playbook
----------------

```
- name: Install sysmon to winlogbeat group
  hosts:
    - winlogbeat
  vars:
    sysmon_install_path: "C:\tools\Sysmon"
    sysmon_version: "11.11"
    sysmon_config: olafhartong-sysmonconfig.xml
  roles:
    - ansible-role-sysmon
  post_tasks:
    - name: Restart Winlogbeat
      win_shell: Restart-Service winlogbeat
```


License
-------

MIT

Author Information
------------------

- j91321
- [viktor0x53](https://github.com/viktor0x53)
