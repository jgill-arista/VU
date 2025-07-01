#!/usr/local/bin/python3
import pyeapi
import os

pyeapi.load_config('eapi.conf')

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

switches = ['mhd367', 'mhd368', 'mhd369', 'mrvp307', 'mrvp350', 'mrvp360', 'mrvp361', 'cdv566', 'cdv584', 'ghb284', 'ghb285', 'upp428', 'upp429']

for switch in switches:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    path = directory+'/'+switch+'.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")
