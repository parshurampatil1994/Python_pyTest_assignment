import pytest


def test_percent_memory():
    """
    """
    # obj = connect_host()
    with open('ParshuramVM.txt') as f:
        line = eval(f.read())
        memory_used_percent = line.get('memory_used_percent')

    assert memory_used_percent <= 90
