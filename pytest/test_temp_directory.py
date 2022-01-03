
import os
#import pytest

def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    print(os.listdir(d))

    assert 1
