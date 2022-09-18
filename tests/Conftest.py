from connect_remote import connect_host
import pytest


@pytest.fixture(autouse=True)
def vm_setup():
    return connect_host()
