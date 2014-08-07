# Copyright 2014 FUJITSU LIMITED
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

create_get_network = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'network': {
                'type': 'object',
                'properties': {
                    'bridge': {'type': ['string', 'null']},
                    'bridge_interface': {'type': ['string', 'null']},
                    'broadcast': {'type': ['string', 'null']},
                    'cidr': {'type': ['string', 'null']},
                    'cidr_v6': {'type': ['string', 'null']},
                    'created_at': {'type': ['string', 'null']},
                    'deleted': {'type': ['boolean', 'null']},
                    'deleted_at': {'type': ['string', 'null']},
                    'dhcp_start': {'type': ['string', 'null']},
                    'dns1': {'type': ['string', 'null']},
                    'dns2': {'type': ['string', 'null']},
                    'gateway': {'type': ['string', 'null']},
                    'gateway_v6': {'type': ['string', 'null']},
                    'host': {'type': ['string', 'null']},
                    'id': {'type': 'string'},
                    'injected': {'type': ['boolean', 'null']},
                    'label': {'type': 'string'},
                    'multi_host': {'type': ['boolean', 'null']},
                    'netmask': {'type': ['string', 'null']},
                    'netmask_v6': {'type': ['string', 'null']},
                    'priority': {'type': ['integer', 'null']},
                    'project_id': {'type': ['string', 'null']},
                    'rxtx_base': {'type': ['integer', 'null']},
                    'updated_at': {'type': ['string', 'null']},
                    'vlan': {'type': ['integer', 'null']},
                    'vpn_private_address': {'type': ['string', 'null']},
                    'vpn_public_address': {'type': ['string', 'null']},
                    'vpn_public_port': {'type': ['integer', 'null']}
                },
                'required': ['id', 'label']
            }
        },
        'required': ['network']
    }
}

list_networks = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'networks': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'bridge': {'type': ['string', 'null']},
                        'bridge_interface': {'type': ['string', 'null']},
                        'broadcast': {'type': ['string', 'null']},
                        'cidr': {'type': ['string', 'null']},
                        'cidr_v6': {'type': ['string', 'null']},
                        'created_at': {'type': ['string', 'null']},
                        'deleted': {'type': ['boolean', 'null']},
                        'deleted_at': {'type': ['string', 'null']},
                        'dhcp_start': {'type': ['string', 'null']},
                        'dns1': {'type': ['string', 'null']},
                        'dns2': {'type': ['string', 'null']},
                        'gateway': {'type': ['string', 'null']},
                        'gateway_v6': {'type': ['string', 'null']},
                        'host': {'type': ['string', 'null']},
                        'id': {'type': 'string'},
                        'injected': {'type': ['boolean', 'null']},
                        'label': {'type': 'string'},
                        'multi_host': {'type': ['boolean', 'null']},
                        'netmask': {'type': ['string', 'null']},
                        'netmask_v6': {'type': ['string', 'null']},
                        'priority': {'type': ['integer', 'null']},
                        'project_id': {'type': ['string', 'null']},
                        'rxtx_base': {'type': ['integer', 'null']},
                        'updated_at': {'type': ['string', 'null']},
                        'vlan': {'type': ['integer', 'null']},
                        'vpn_private_address': {'type': ['string', 'null']},
                        'vpn_public_address': {'type': ['string', 'null']},
                        'vpn_public_port': {'type': ['integer', 'null']}
                    },
                    'required': ['id', 'label']
                }
            }
        },
        'required': ['networks']
    }
}

delete_network = {
    'status_code': [202]

}

network_actions_common_schema = {
    'status_code': [202]
}
