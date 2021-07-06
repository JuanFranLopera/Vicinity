import paramiko
import os

ground_dir = '/home/pi/Documents/GroundControl/data'



#Save all paramiko activity
paramiko.util.log_to_file('paramiko.log')

# Start an SSH client
ssh_client = paramiko.SSHClient()

# Establish default policy to find local host key
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Establish connection
ip = '192.168.1.146'
username = 'pi'
password = 'raspberry'
ssh_client.connect(ip, username=username, password=password)

# Open SFTPClient object
sftp = ssh_client.open_sftp()

#Go to data directory
directory = '/home/pi/Documents/Vicinity'
sftp.chdir(directory)
files = sftp.listdir()


for file in files:
    if '.csv' in file:
        remote_file = os.path.join(directory,file)
        sftp.get(remote_file, os.path.join(ground_dir,file))

sftp.close()
ssh_client.close()