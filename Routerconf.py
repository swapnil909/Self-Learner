from typing import TextIO

from netmiko import ConnectHandler
import getpass
import sys
import time


##initialising device
device = {
    'device_type': 'cisco_ios',
    'ip': '10.100.250.80',
    'username': 'username',
    'password': 'password',
    'secret':'password'
    }
##opening IP file
f=open("iplist.txt")
print ("Please enter your credential")
device['username']=input("User name ")
device['password']=getpass.getpass()
print("Enter enable password: ")
device['secret']=getpass.getpass()

for line in f:
    try:
     fields=line.split()
     field1=fields[0]
     field2=fields[1]
     device['ip']=field1
     print("\n\nConnecting Device " ,field1)
     net_connect = ConnectHandler(**device)
     net_connect.enable()
     time.sleep(1)
     print ("writing configuration... ")
     print('ip dhcp excluded-adress' ,field2)
     #net_connect.config_mode()
     config_commands=['ip dhcp excluded-address'+field2]
     net_connect.send_config_set('config_commands')
     net_connect.send_command_expect('write mem')
     #net_connect.save_config()
     #net_connect.send_command('write mem')
     time.sleep(3)
     net_connect.disconnect()
     print("Configuration done for" ,field1)
    except:
      print("Access to " + device['ip'] + " failed,configuration did not done")

f.close()
print("\nAll device configuration completed")
