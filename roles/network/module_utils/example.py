#
# (c) 2018 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import (absolute_import, division, print_function)
from ansible.errors import AnsibleError
__metaclass__ = type

### Imports
try:
    from ansible.module_utils.basic import env_fallback, return_values
    from ansible.module_utils.connection import Connection
    """
        Examples:
            https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/network/iosxr/iosxr.py
            https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/network/junos//junos.py
    """
except ImportError:
    raise AnsibleError("Netconf Plugin [ network ]: Dependency not satisfied")

### Implementation
"""
    Examples:
        https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/network/iosxr/iosxr.py
        https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/network/junos//junos.py
"""