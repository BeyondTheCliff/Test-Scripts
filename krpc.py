import socket
rpc_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rpc_conn.connect(('25.187.234.75', 50000))
# Send the 12 byte hello message
rpc_conn.sendall(b'\x48\x45\x4C\x4C\x4F\x2D\x52\x50\x43\x00\x00\x00')
# Send the 32 byte client name 'Jeb' padded with zeroes
name = 'Jeb'.encode('utf-8')
name += (b'\x00' * (32-len(name)))
rpc_conn.sendall(name)
# Receive the 16 byte client identifier
identifier = b''
while len(identifier) < 16:
    identifier += rpc_conn.recv(16 - len(identifier))
# Connection successful. Print out a message along with the client identifier.
identifier = ''.join('%02x' % ord(c) for c in identifier)
print 'Connected to RPC server, client idenfitier = %s' % identifier

import krpc
vessel = rpc_conn.space_center.active_vessel
vessel.control.throttle = 1