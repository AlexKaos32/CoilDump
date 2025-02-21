#!/usr/bin/env python3

import sys
import time
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

# This is the ip of the remote machine running modbus, you pass this to the tool at runtime
ip = sys.argv[1]

# Passes IP and port number to ModbusTcpClient/ModbusClient, sets that to a var named client
client = ModbusClient(ip, port=502)

# Connects to remote machine on port 502
client.connect()
# while statement is going to run until stopped with ctrl+c or an error is reached
while True:
    request = client.read_coils(address=0, count=10)
    if request.isError():
           print('Modbus Error:', request)
    else:
        result = request.bits
        print(result)
# time.sleep is providing a waiting period before checking again
    time.sleep(1)
