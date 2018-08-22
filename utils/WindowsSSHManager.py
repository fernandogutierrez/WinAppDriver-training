from paramiko import *
import re


class WindowsSSHManager(object):
    TIMEOUT = 10
    client = None

    @staticmethod
    def execute(command, **kwargs):
        stdin, stdout, stderr = WindowsSSHManager.client.exec_command(command, **kwargs)
        return {'out': stdout.readlines(),
                'err': stderr.readlines(),
                'retval': stdout.channel.recv_exit_status()}

    @staticmethod
    def connect(connection_string):
        conn_str = re.split(":", connection_string)

        if WindowsSSHManager.client is None:
            WindowsSSHManager.client = SSHClient()
            WindowsSSHManager.client.set_missing_host_key_policy(AutoAddPolicy())
            WindowsSSHManager.client.connect(conn_str[2], 22, username=conn_str[0], password=conn_str[1],
                                             timeout=WindowsSSHManager.TIMEOUT, look_for_keys=False, allow_agent=False)
