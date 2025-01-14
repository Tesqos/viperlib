import logging

import keyring

from viperlib import jsondata

logger = logging.getLogger(__name__)

class creds():

    _srctype = None
    _alias = None
    _user = None
    _pwd = None
    _unsecure = jsondata()

    CREDS_TYPE_PLAIN = 'json' # used for storing credentials as plain text in JSON format
    CREDS_TYPE_SECURE = 'keyring' # used for storing credentials securely using keyring package
    KWD_UID = 'uid'
    KWD_PWD = 'pwd'
    DEFAULT_FNAME_PLAIN = 'credentials'

    def __init__(self, type=None):
        self._unsecure.filename = self.DEFAULT_FNAME_PLAIN
        self.type = type
        if type == None:
            self.type = self.CREDS_TYPE_SECURE
        assert self.type == self.CREDS_TYPE_PLAIN or self.type == self.CREDS_TYPE_SECURE, 'Invalid credentials type value.'

    @property
    def type(self):
        return self._srctype

    @type.setter
    def type(self, val):
        self._srctype = val

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, val):
        self._alias = val

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, val):
        self._user = val

    @property
    def password(self):
        return self._pwd

    @password.setter
    def password(self, val):
        self._pwd = val

    @property
    def plain(self):
        if self.type != self.CREDS_TYPE_PLAIN:
            raise AttributeError('Wrong value for credentials type: ' + self.type)
        return self._unsecure

    def get(self):
        if self.type == self.CREDS_TYPE_SECURE:
            self.user = keyring.get_password(self.alias, self.KWD_UID)
            self.password = keyring.get_password(self.user, self.KWD_PWD)
        elif self.type == self.CREDS_TYPE_PLAIN:
            self._unsecure.get_from_file()
            t = self._unsecure.contents[self.alias]
            self.user = t[self.KWD_UID]
            self.password = t[self.KWD_PWD]
        else:
            raise ValueError('Could not detemine credentials type.')
