#Send UDP broadcast packets

MYPORT = 20000

import sys, time
from socket import *

ip = None
bcast = None

for line in sys.stdin:
    if "inet addr" in line:
        ip = line.split(':')[1].split()[0]
        bcast = line.split(':')[2].split()[0]
        break

if not ip or not bcast:
    print "ERROR: no ip or broadcast address for eth0"
    sys.exit(1)
else:
    print "Minnow Broadcast: ", ip, "/", bcast

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    data = "minnowboard_ip:%s" % ip
    s.sendto(data, (bcast, MYPORT))
    time.sleep(5)

