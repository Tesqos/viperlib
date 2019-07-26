from ..src.jsd import jsondata
from ..src.misc import dir_get
import os

def test_jsd():
    fname = 'person'
    newname = fname + 'new'
    location = 'data'
    os.chdir(dir_get(__file__))
    x = jsondata()
    x.filename = fname
    x.location = location
    assert x.is_empty(), 'Expected empty contents.'
    assert x.file_exists(), 'Expected file to exist.'
    x.get_from_file()
    assert not x.is_empty(), 'Expected non-empty contents.'
    assert x.contents['first name'] == 'Pat', 'Wrong first name.'
    assert x.contents['last name'] == 'Metheny', 'Wrong last name.'
    assert x.contents['occupation'] == 'musician', 'Wrong occupation.'
    assert x.contents['country of origin'] == 'USA', 'Wrong country.'
    x.contents.update({'country of origin': 'Egypt'})
    x.filename = newname
    x.save_to_file()
    x.clear()
    assert x.is_empty(), 'Expected empty contents.'
    y = jsondata()
    y.filename = x.filename
    y.location = x.location
    del x
    y.get_from_file()
    assert y.contents['country of origin'] == 'Egypt', 'Wrong country.'
    y.destroy()
    assert not y.file_exists(), 'File not destroyed.'
    assert y.filename == newname + '.json', 'Expected filename to be retained.'
    assert y.location == location, 'Expected location to be retained.'
    y.reset()
    assert y.filename is None, 'Expected empty filename.'
    assert y.location is None, 'Expected empty location.'
