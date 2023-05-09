# Add path for CI/CD tool
import sys
import os
sys.path.append(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../src/")
)

import plus

def test_is_plus():
    a = plus.plus_twovar(2,2)
    assert a==4