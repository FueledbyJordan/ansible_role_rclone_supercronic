ansible-role-rclone-supercronic
===============================

This role configures rclone supercronic for my homelab.

Requirements
------------

N/A

Role Variables
--------------
* rclone\_conf\_dir
* rclone\_user
* rclone\_group
* rclone\_backends
```
- { backend_name: 'B2-hass', type: 'b2', key_id: 'adsf', key: 'asdf' }
```
* rclone\_scripts
```
- { path: 'yodel.sh.j2', cron: '*/1 * * * *' }
```

Dependencies
------------

N/A

Example Playbook
----------------

```
- hosts: servers
  roles:
    - ansible-role-rclone-supercronic
```

License
-------

MIT

Author Information
------------------

I can be reached at [djm@murrayfoundry.com](mailto:djm@murrayfoundry.com).

