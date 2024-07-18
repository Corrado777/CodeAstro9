import os
import sys
# change dir to folder above file using abs path
os.chdir(r"/Users/cieraguest/Documents/GitHub/CodeAstro9")
sys.path.append(os.path.abspath(os.curdir))
from src.timetools import get_julian_date

def test_get_julian_date():
    # Test the get_julian_date function
    assert get_julian_date("2023-04-01 12:00:00") == 2460036.0
    assert get_julian_date("2023-04-02 12:00:00") == 2460037.0
    assert get_julian_date("2023-04-03 12:00:00") == 2460038.0

if __name__ == '__main__':
    test_get_julian_date()