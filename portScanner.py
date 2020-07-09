######################################################
# IMPORT MODULES
######################################################
from socket import *
from time import *
######################################################

######################################################
# ENTER TARGET IP
######################################################
target = input('Enter the host to be scanned: ')
targetIP = gethostbyname(target)
######################################################

######################################################
# ENTER RANGE OF PORT
######################################################
port = input('Enter the range to be scanned (Eg: 1-10): ')

portF = int(port.split('-')[0])
portS = int(port.split('-')[1])
if portF > 65535:
    print("the total number of ports are 65535 can't use greater values")
    print('Setting default starting port (1)')
    portS = 1
if portS > 65535:
    print("the total number of ports are 65535 can't use greater values")
    print('Setting default final port (65535)')
    portS = 65535
######################################################
print('Starting scan on host: ', targetIP)


tStart = time()  # TIME OF THE SCAN STARTED

######################################################
#  STARTING THE SCANNING
######################################################
for i in range(portF, portS+1):

    s = socket(AF_INET, SOCK_STREAM)  # SOCKET CREATED TO CONNECT
    conn = s.connect_ex((targetIP, i))  # CONNECT TO THE HOST BY GIVEN PORT

    if not conn:
        print('Port %d: OPEN' % i)
        s.close()
    if conn:
        print('Port %d: CLOSED' % i)
        s.close()

print('Time taken:', time() - tStart)  # TOTAL TIME TO GET SCANNED
