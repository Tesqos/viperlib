from viperlib.src.jsd import jsondata
from viperlib.src.misc import dir_get
import os

os.chdir(dir_get(__file__))

fname = 'person'
newname = fname + 'new'
location = 'data'

class Test_jsd():

    x = jsondata()
    x.filename = fname
    x.location = location
    y = jsondata()

    def test_is_empty(self):
        assert self.x.is_empty(), 'Expected empty contents.'

    def test_file_exists(self):
        assert self.x.file_exists(), 'Expected file to exist.'

    def test_get_from_file_1(self):
        self.x.get_from_file()
        assert not self.x.is_empty(), 'Expected non-empty contents.'
        assert self.x.contents['first name'] == 'Pat', 'Wrong first name.'
        assert self.x.contents['last name'] == 'Metheny', 'Wrong last name.'
        assert self.x.contents['occupation'] == 'musician', 'Wrong occupation.'
        assert self.x.contents['country of origin'] == 'USA', 'Wrong country.'

    def test_save_to_file_must_NOT_save(self):
        self.x.mustsave = False
        self.x.contents.update({'country of origin': 'Egypt'})
        self.x.filename = newname
        self.x.save_to_file()
        assert not self.x.file_exists(), 'Expected file to NOT exist.'

    def test_save_to_file_must_save(self):
        self.x.mustsave = True
        self.x.contents.update({'country of origin': 'Egypt'})
        self.x.filename = newname
        self.x.save_to_file()
        assert self.x.file_exists(), 'Expected file to exist.'
        self.y.filename = self.x.filename # new one
        self.y.location = self.x.location
        self.y.get_from_file()
        assert self.y.contents['country of origin'] == 'Egypt', 'Wrong country.'

    def test_clear(self):
        self.x.clear()
        assert self.x.is_empty(), 'Expected empty contents.'

    def test_destroy_must_NOT_delete(self):
        self.y.mustdelete = False
        self.y.destroy()
        assert self.y.file_exists(), 'Expected file to be retained.'

    def test_destroy_must_delete(self):
        self.y.mustdelete = True
        self.y.destroy()
        assert not self.y.file_exists(), 'Expected file to be deleted.'

    def test_reset(self):
        self.y.reset()
        assert self.y.filename is None, 'Expected empty filename.'
        assert self.y.location is None, 'Expected empty location.'
