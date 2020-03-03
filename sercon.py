import paramiko
import json
import os

class Server(object):

    def __init__(self, command, hostname, username, password):
        self.command = command
        self.hostname = hostname
        self.username = username
        self.password = password


    def executeCommand(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname=self.hostname, port=22, username=self.username, password=self.password)

        stdin, stdout, stderr = ssh.exec_command(self.command)
        result = stdout.read()
        print(result)
        print('Execute successful!!')

        ssh.close()

    def server2dict(self):
        return{
            'command':self.command,
            'hostname':self.hostname,
            'username':self.username,
            'password':self.password
        }


def main():

    if os.path.exists('config.json'):
        f = open('config.json', 'rb')
        t = json.load(f)
        test = Server(t[3], t[0], t[1], t[2])
        f.close()
    
    else:


        hostname = input('Please input your hostname:\n')
        username = input('Please input your username:\n')
        password = input('Please input your password:\n')
        command = input('Please input your command；\n')

        test = Server(command, hostname, username, password)
        d = [hostname, username, password, command]
        f = open('config.json', 'w')
        json.dump(d, f)
        f.close()

    test.executeCommand()



    
if __name__ == "__main__":
    main()