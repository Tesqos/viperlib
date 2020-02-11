import os
import pytest
from viperlib.src.misc import *

this_dir = os.path.dirname(__file__)

def test_dir_get():
    from viperlib import tests as parent
    # test for this module's directory
    assert dir_get(__file__) == this_dir
    # test for this module's parent's directory
    assert dir_get(os.path.dirname(parent.__file__)) == dir_get(this_dir)

def test_parent_module_name_get():
    assert parent_module_name_get() == 'viperlib.src' #
    assert parent_module_name_get('root.whatever.whichever') == 'root.whatever'
    assert parent_module_name_get('') == ''
    with pytest.raises(ValueError):
        parent_module_name_get('aaa bbb')

def test_strdigit_normalize():
    assert strdigit_normalize('00')  == '00'
    assert strdigit_normalize('0')   == '00'
    assert strdigit_normalize('1')   == '01'
    assert strdigit_normalize('9')   == '09'
    assert strdigit_normalize('10')  == '10'
    assert strdigit_normalize('11')  == '11'
    assert strdigit_normalize('99')  == '99'
    assert strdigit_normalize('100') == '100'
    with pytest.raises(AssertionError):
        strdigit_normalize(0)
    with pytest.raises(AssertionError):
        strdigit_normalize(5)
    with pytest.raises(AssertionError):
        strdigit_normalize(9)
    with pytest.raises(AssertionError):
        strdigit_normalize(0.1)
    with pytest.raises(AssertionError):
        strdigit_normalize(1.1)
    with pytest.raises(AssertionError):
        strdigit_normalize(-1)
    with pytest.raises(AssertionError):
        strdigit_normalize('-1')
    with pytest.raises(AssertionError):
        strdigit_normalize('-11')

def test_list_of_files_with_extension_get():
    os.chdir(dir_get(__file__))
    dir = ''.join('data' + os.sep + 'byext')
    expjson = ['a.json', 'b.json', 'c.json', 'd.json', 'json.json']
    exptxt = ['e.txt', 'f.txt']
    explog = ['g.abc']
    assert list_of_files_with_extension_get(dir, 'json') == expjson, '.json files: wrong list.'
    assert list_of_files_with_extension_get(dir, 'txt') == exptxt, '.txt files: wrong list.'
    assert list_of_files_with_extension_get(dir, 'abc') == explog, '.abc files: wrong list.'
    assert list_of_files_with_extension_get(dir, 'none') == [], 'No files: not an empty list returned.'
    assert list_of_files_with_extension_get(dir, '') == [], 'No extension: not an empty list returned.'

def test_months():
    assert months() == ['', 'January', 'February', 'March', 'April', 'May', \
                        'June', 'July', 'August', 'September', 'October', 'November', 'December'], 'Not expected list of strings.'
                        
def test_isProcessRunning():
    assert isProcessRunning('python')
