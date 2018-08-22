from paramiko import *
import re


class WindowsSSHManager:
    TIMEOUT = 10

    def __init__(self, connection_string, **kwargs):
        results = re.split(":", connection_string)
        self.__key = kwargs.pop("key", None)
        self.client = kwargs.pop("client", None)
        self.__port = 22
        self.__username = results[0]
        self.__password = results[1]
        self.__host = results[2]
        self.connect(self.__host, self.__port, self.__username, self.__password, self.__key)

    def execute(self, command, **kwargs):
        stdin, stdout, stderr = self.client.exec_command(command, **kwargs)
        result = {'out': stdout.readlines(),
                  'err': stderr.readlines(),
                  'retval': stdout.channel.recv_exit_status()}
        return result

    def connect(self, host, port, username, password, key=None):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.connect(host, port, username=username, password=password, pkey=key,
                            timeout=self.TIMEOUT, look_for_keys=False, allow_agent=False)
