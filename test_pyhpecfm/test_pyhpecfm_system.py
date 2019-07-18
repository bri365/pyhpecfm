# -*- coding: utf-8 -*-
""" Module for testing functions in pyhpecfm.system. """

import os

from unittest import TestCase

from pyhpecfm import client
from pyhpecfm import system

CFM_IP = os.environ['CFM_IP']
CFM_USERNAME = os.environ['CFM_USERNAME']
CFM_PASSWORD = os.environ['CFM_PASSWORD']

CFM = client.CFMClient(CFM_IP, CFM_USERNAME, CFM_PASSWORD)
CFM.connect()


class TestGetVersions(TestCase):
    """ Test pyhpecfm.system.get_versions. """

    def test_get_versions(self):
        """ Try to get versions. """
        test_version = system.get_versions(CFM)
        my_attributes = ['current', 'supported', 'software']
        self.assertIs(type(test_version), dict)
        for i in test_version.keys():
            self.assertIn(i, my_attributes)


class TestGetAuditLogs(TestCase):
    """ Test pyhpecfm.system.get_audit_logs. """

    def test_get_audit_logs(self):
        """ Try to get audit logs. """
        my_logs = system.get_audit_logs(CFM)
        my_attributes = ['description', 'record_type', 'log_date', 'uuid',
                         'stream_id', 'data', 'severity']
        self.assertIs(type(my_logs), list)
        for i in my_logs[0].keys():
            self.assertIn(i, my_attributes)


class TestGetBackups(TestCase):
    """ Test pyhpecfm.system.get_backups. """

    def test_get_backups(self):
        """ Try to get a list of backups. """
        my_backups = system.get_backups(CFM)
        my_attributes = ['url', 'checksum', 'uuid', 'name', 'date_created']
        self.assertIs(type(my_backups), list)
        for i in my_backups[0].keys():
            self.assertIn(i, my_attributes)

    def test_get_specific_backup(self):
        """ Try to get a specific backup. """
        my_backups = system.get_backups(CFM)
        my_uuid = my_backups[0]['uuid']
        single_backup = system.get_backups(CFM, my_uuid)
        my_attributes = ['url', 'checksum', 'uuid', 'name', 'date_created']
        self.assertIs(type(single_backup), dict)
        for i in single_backup.keys():
            self.assertIn(i, my_attributes)


class TestCreateBackup(TestCase):
    """ Test pyhpecfm.system.create_backup. """

    def test_get_backups(self):
        """ Try to create a backup. """
        backup_result = system.create_backup(CFM)
        self.assertEqual(200, backup_result.status_code)
        my_attributes = ['url', 'checksum', 'uuid', 'name', 'date_created']
        self.assertIs(type(backup_result), list)
        for i in backup_result[0].keys():
            self.assertIn(i, my_attributes)
