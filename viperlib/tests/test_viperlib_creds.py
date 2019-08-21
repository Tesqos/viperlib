import pytest

import keyring

import viperlib
from viperlib.tests import dir_data
from viperlib import creds

test_alias = 'viper_test_user'
test_uid = 'user_viper'
test_pwd = 'password_viper'


class keyring_record:

    service = 'VIPER_TEST'

    def create(self):
        keyring.set_password(self.service, test_alias, test_uid)
        keyring.set_password(test_uid, 'pwd', test_pwd)

    def delete(self):
        keyring.delete_password(self.service, test_alias)
        keyring.delete_password(test_uid, 'pwd')

def test_json_credentials_valid():
    x = creds(creds.CREDS_TYPE_PLAIN)
    x.alias = test_alias
    x.location = dir_data
    x.get()
    assert x.user == test_uid
    assert x.password == test_pwd

def test_keyring_credentials_valid():
    kr = keyring_record()
    kr.create()
    x = creds()
    x.alias = test_alias
    x.get()
    assert x.user == test_uid
    assert x.password == test_pwd
    kr.delete()
