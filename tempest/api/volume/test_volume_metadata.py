# Copyright 2013 Huawei Technologies Co.,LTD
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

from testtools import matchers

from tempest.api.volume import base
from tempest import test


class VolumesV2MetadataTest(base.BaseVolumeTest):

    @classmethod
    @test.safe_setup
    def setUpClass(cls):
        super(VolumesV2MetadataTest, cls).setUpClass()
        # Create a volume
        cls.volume = cls.create_volume()
        cls.volume_id = cls.volume['id']

    def tearDown(self):
        # Update the metadata to {}
        self.volumes_client.update_volume_metadata(self.volume_id, {})
        super(VolumesV2MetadataTest, self).tearDown()

    @test.attr(type='gate')
    def test_create_get_delete_volume_metadata(self):
        # Create metadata for the volume
        metadata = {"key1": "value1",
                    "key2": "value2",
                    "key3": "value3",
                    "key4": "<value&special_chars>"}

        rsp, body = self.volumes_client.create_volume_metadata(self.volume_id,
                                                               metadata)
        self.assertEqual(200, rsp.status)
        # Get the metadata of the volume
        resp, body = self.volumes_client.get_volume_metadata(self.volume_id)
        self.assertEqual(200, resp.status)
        self.assertThat(body.items(), matchers.ContainsAll(metadata.items()))
        # Delete one item metadata of the volume
        rsp, body = self.volumes_client.delete_volume_metadata_item(
            self.volume_id,
            "key1")
        self.assertEqual(200, rsp.status)
        resp, body = self.volumes_client.get_volume_metadata(self.volume_id)
        self.assertNotIn("key1", body)
        del metadata["key1"]
        self.assertThat(body.items(), matchers.ContainsAll(metadata.items()))

    @test.attr(type='gate')
    def test_update_volume_metadata(self):
        # Update metadata for the volume
        metadata = {"key1": "value1",
                    "key2": "value2",
                    "key3": "value3"}

        update = {"key4": "value4",
                  "key1": "value1_update"}

        # Create metadata for the volume
        resp, body = self.volumes_client.create_volume_metadata(
            self.volume_id,
            metadata)
        self.assertEqual(200, resp.status)
        # Get the metadata of the volume
        resp, body = self.volumes_client.get_volume_metadata(self.volume_id)
        self.assertEqual(200, resp.status)
        self.assertThat(body.items(), matchers.ContainsAll(metadata.items()))
        # Update metadata
        resp, body = self.volumes_client.update_volume_metadata(
            self.volume_id,
            update)
        self.assertEqual(200, resp.status)
        # Get the metadata of the volume
        resp, body = self.volumes_client.get_volume_metadata(self.volume_id)
        self.assertEqual(200, resp.status)
        self.assertThat(body.items(), matchers.ContainsAll(update.items()))

    @test.attr(type='gate')
    def test_update_volume_metadata_item(self):
        # Update metadata item for the volume
        metadata = {"key1": "value1",
                    "key2": "value2",
                    "key3": "value3"}
        update_item = {"key3": "value3_update"}
        expect = {"key1": "value1",
                  "key2": "value2",
                  "key3": "value3_update"}
        # Create metadata for the volume
        resp, body = self.volumes_client.create_volume_metadata(
            self.volume_id,
            metadata)
        self.assertEqual(200, resp.status)
        self.assertThat(body.items(), matchers.ContainsAll(metadata.items()))
        # Update metadata item
        resp, body = self.volumes_client.update_volume_metadata_item(
            self.volume_id,
            "key3",
            update_item)
        self.assertEqual(200, resp.status)
        # Get the metadata of the volume
        resp, body = self.volumes_client.get_volume_metadata(self.volume_id)
        self.assertEqual(200, resp.status)
        self.assertThat(body.items(), matchers.ContainsAll(expect.items()))


class VolumesV2MetadataTestXML(VolumesV2MetadataTest):
    _interface = "xml"


class VolumesV1MetadataTest(VolumesV2MetadataTest):
    _api_version = 1


class VolumesV1MetadataTestXML(VolumesV1MetadataTest):
    _interface = "xml"
