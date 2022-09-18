import pytest


def test_percent_disk():
    """
    """
    # obj = connect_host()
    with open('ParshuramVM.txt') as f:
        line = eval(f.read())
        disk_used_percent = line.get('disk_used_percent')

    assert disk_used_percent <= 90
