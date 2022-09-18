import pytest
import logging


@pytest.mark.cli
def test_memory(caplog):
    caplog.set_level(logging.INFO)
    logging.getLogger().info('Log inside a test_memory function!')

    with open('ParshuramVM.txt') as f:
        line = eval(f.read())
        memory_used_percent = line.get('memory_used_percent')

    assert memory_used_percent <= 90
