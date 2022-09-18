import paramiko


def connect_host():
    try:
        hostname = '192.168.0.5'
        port = 22
        username = 'parshuram22'
        password = '123@Pp'

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)

        cmd = 'python3 Desktop/check_system_data.py'
        stdin, stdout, stderr = client.exec_command(cmd)

        with open('ParshuramVM.txt', 'w') as f:
            for i in stdout:
                f.write(i)

        client.close()

    except Exception as e:
         return e


connect_host()













