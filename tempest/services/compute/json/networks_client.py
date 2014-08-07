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

import json

from tempest.api_schema.compute.v2 import networks as schema
from tempest.common import rest_client
from tempest import config

CONF = config.CONF


class NetworksClientJSON(rest_client.RestClient):

    def __init__(self, auth_provider):
        super(NetworksClientJSON, self).__init__(auth_provider)
        self.service = CONF.compute.catalog_type

    def create_network(self, label, **kwargs):
        """
        label(Required): Network label.
        bridge: VIFs on this network are connected to this bridge.
        bridge_interface: The bridge is connected to this interface.
        cidr: IPv4 subnet.
        multi_host: Multi host.
        vlan: Vlan id.
        cidr_v6: IPv6 subnet.
        dns1: First dns.
        dns2: Second dns.
        gateway: IPv4 gateway.
        gateway_v6: IPv6 gateway.
        project_id: Project id.
        """
        post_body = {'label': label}

        for option in ['bridge', 'bridge_interface', 'cidr',
                       'multi_host', 'vlan', 'cidr_v6',
                       'dns1', 'dns2', 'gateway', 'gateway_v6',
                       'project_id']:
            post_param = option
            key = option
            value = kwargs.get(key)
            if value is not None:
                post_body[post_param] = value

        post_body = {'network': post_body}

        post_body = json.dumps(post_body)
        resp, body = self.post("", body=post_body)
        body = json.loads(body)
        self.validate_response(schema.create_get_network, resp, body)
        return resp, body['network']

    def delete_network(self, network_id):
        resp, body = self.delete("os-networks/%s" % str(network_id))
        self.validate_response(schema.delete_network, resp, body)
        return resp, body

    def list_networks(self):
        resp, body = self.get("os-networks")
        body = json.loads(body)
        self.validate_response(schema.list_networks, resp, body)
        return resp, body['networks']

    def get_network(self, network_id):
        resp, body = self.get("os-networks/%s" % str(network_id))
        body = json.loads(body)
        self.validate_response(schema.create_get_network, resp, body)
        return resp, body['network']

    def add_network_to_project(self, network_id=None):
        # The UUID of the network to add to the project.
        # Specify None to choose a random available network.
        post_body = {'id': network_id}

        post_body = json.dumps(post_body)
        resp, body = self.post("os-networks/add", post_body)
        body = json.loads(body)
        self.validate_response(schema.add_network_to_project, resp, body)
        return resp, body['network']

    def associate_host(self, network_id, host):
        return self.action(network_id, 'associate_host', kwarg=host)

    def disassociate_host(self, network_id):
        return self.action(network_id, 'disassociate_host')

    def disassociate_network(self, network_id):
        return self.action(network_id, 'disassociate')

    def disassociate_project(self, network_id):
        return self.action(network_id, 'disassociate_project')

    def action(self, network_id, action_name,
               schema=schema.network_actions_common_schema, kwarg=None):
        post_body = json.dumps({action_name: kwarg})
        resp, body = self.post('os-networks/%s/action' % str(network_id),
                               post_body)
        self.validate_response(schema, resp, body)
        return resp, body
