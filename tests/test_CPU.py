import pytest
import logging


@pytest.mark.cli
def test_CPU():
    logging.getLogger().info('Log inside a test_CPU function!')

    with open('ParshuramVM.txt') as f:
        line = eval(f.read())
        cpu_usage = line.get('cpu_usage')

    assert cpu_usage <= 90


