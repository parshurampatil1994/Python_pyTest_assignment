import pytest


def test_percent_CPU():
    """
    """
    # obj = connect_host()
    with open('ParshuramVM.txt') as f:
        line = eval(f.read())
        cpu_usage = line.get('cpu_usage')

    assert cpu_usage <= 90
