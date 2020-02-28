import paramiko

class Server(object):

    def __init__(self, commandStr, hostname, username, password):
        self.commandStr = commandStr
        self.hostname = hostname
        self.username = username
        self.password = password


    def executeCommand(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname=self.hostname, port=22, username=self.username, password=self.password)

        stdin, stdout, stderr = ssh.exec_command(self.commandStr)
        result = stdout.read()
        print(result)
        print('Execute successful!!')

        ssh.close()

def main():
    hostname = input('Please input your hostname:\n')
    username = input('Please input your username:\n')
    password = input('Please input your password:\n')
    command = input('Please input your command；\n')

    test = Server(command, hostname, username, password)

    test.executeCommand()

if __name__ == "__main__":
    main()