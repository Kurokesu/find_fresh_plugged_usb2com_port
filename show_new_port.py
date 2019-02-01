# Full blog post: https://www.kurokesu.com/main/2019/02/01/which-usb-to-com-port-is-the-most-recent-one/

import sys, re
import subprocess
import time
import serial.tools.list_ports

def grep(regexp):
    for port, desc, hwid in serial.tools.list_ports.comports():
        if re.search(regexp, port, re.I) or re.search(regexp, desc) or re.search(regexp, hwid):
            yield port, desc, hwid

# Discover all COM ports and show them
port_list_initial = serial.tools.list_ports.comports()
for port, desc, hwid in port_list_initial:
    print('-', port, desc)

print('\nWaiting for new USB to SERIAL device to be plugged in...\n')

# Wait for new device to be plugged in and show it
while True:
    port_list_poll = serial.tools.list_ports.comports()

    for p in port_list_poll:
        if p not in port_list_initial:
            print('-', p)
            input('\nAll done, press enter to quit')
            sys.exit(1)
        else:
            time.sleep(0.5) # Don't poll too often 
