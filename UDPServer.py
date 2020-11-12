import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.0.206', 59696)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address) 
message = '$GPGGA,080440.00,5046.9197,N,00602.7938,E,1,08,1.4,226.91,M,46.50,M,,*60'

print('\nwaiting to receive message')
data, address = sock.recvfrom(4096)
        
if data:
    for x in range(1,10):
        sent = sock.sendto(message.encode(), address)
        print ('sent %s bytes back to %s' % (sent, address))
        time.sleep(1)
        