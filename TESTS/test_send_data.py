import paramiko
import os
import configparser
from datetime import datetime

# Useful directories
home_dir = os.path.expanduser('~')
ground_dir = os.path.join(home_dir,'Documents','Vicinity','GROUND')

cfg_dir = os.path.join(ground_dir,'DATA','CFG')
input_dir = os.path.join(ground_dir,'DATA','Input')
log_dir = os.path.join(ground_dir,'DATA','log')

if not os.path.exists(input_dir):
    os.mkdir(input_dir)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)


#Save all paramiko activity in a log file
curr_time = datetime.today().strftime('%Y%m%d_%H%M%S')
log_name = 'log_paramiko_' + curr_time + '.log'
log_file = os.path.join(log_dir,log_name)
paramiko.util.log_to_file(log_file)

# Initialise configuration files
config = configparser.ConfigParser()
config.read( os.path.join(cfg_dir,'sat_network.ini') )

################################################

# Start an SSH client
ssh_client = paramiko.SSHClient()

# Establish default policy to find local host key
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Establish SSH connection
net_cfg = dict( config['Vicinity_network_settings'] )
ssh_client.connect(**net_cfg)

# Open SFTPClient object
sftp = ssh_client.open_sftp()

# Go to data directory
directory = '/home/pi/Documents/Vicinity'
sftp.chdir(directory)
files = sftp.listdir()

# File transmission
for file in files:
    if '.csv' in file:
        remote_file = os.path.join(directory,file)
        sftp.get(remote_file, os.path.join(input_dir,file))

# Close SSH Connection
sftp.close()
ssh_client.close()