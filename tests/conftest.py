import pytest
import paramiko
import logging


@pytest.fixture(autouse = True)
def connect_host():
    try:
        hostname = '192.168.0.4'
        port = 22
        username = 'parshuram22'
        password = '123@Pp'

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)

        cmd = 'python3 Desktop/check_system_data.py'
        stdin, stdout, stderr = client.exec_command(cmd)

        with open('ParshuramVM.txt', 'w') as file1:
            for i in stdout:
                file1.write(i)
                logging.getLogger().info('info: ' + str(i))

        client.close()

    except Exception as e:
         return e
