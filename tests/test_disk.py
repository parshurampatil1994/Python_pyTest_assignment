import pytest
import logging


@pytest.mark.cli
def test_disk():
    logging.getLogger().info('Log inside a test_disk function!')

    with open('ParshuramVM.txt') as f:
        line = eval(f.read())
        disk_used_percent = line.get('disk_used_percent')

    assert disk_used_percent <= 90
