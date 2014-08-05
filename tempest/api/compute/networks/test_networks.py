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

from tempest.api.compute import base
from tempest.common.utils import data_utils
from tempest import config
from tempest import exceptions
from tempest import test

CONF = config.CONF


class NetworksTestJSON(base.BaseV2ComputeTest):

    def __init__(self, *args, **kwargs):
        super(NetworksTestJSON, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        # Floating IP actions might need a full network configuration
        super(NetworksTestJSON, cls).setUpClass()
        cls.client = cls.networks_client

    @test.attr(type='gate')
    def test_create_delete_network(self):
        label = data_utils.rand_name('test-network')
        cidr = "192.168.244.0/24"
        resp, network = self.client.create_network(label=label,
                                                   cidr=cidr)
        self.addCleanup(self.client.delete_network, network['id'])
        self.assertEqual(200, resp.status)

        resp, network_list = self.client.list_networks()
        network_id_list = map(lambda x: x['id'], network_list)
        self.assertIn(network['id'], network_id_list)

        resp, body = self.client.delete_network(network['id'])
        self.assertEqual(202, resp.status)
        (network['id'])
        self.assertRaises(exceptions.NotFound,
                          self.client.get_network,
                          network['id'])

    @test.attr(type='gate')
    def test_list_networks(self):
        resp, network_list = self.client.list_networks()
        network_id_list = map(lambda x: x['id'], network_list)
        self.assertNotEmpty(network_id_list)

    @test.attr(type='gate')
    def test_get_network(self):
        resp, network_list = self.client.list_networks()

        network_id = network_list[0]['id']
        resp, network = self.client.get_network(network_id)
        self.assertEqual(network_id, network['id'])
