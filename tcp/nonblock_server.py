import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8888))
sock.listen(5)
# sock.setblocking(True)
# sock.settimeout(5)
# sock.settimeout(0) -> sock.blocking(False)
sock.settimeout(None) # -> sock.blocking(True)


try:
    client, addr = sock.accept()
except socket.error:
    print('No connection')
# except socket.timeout:
#    print('Timed off')
else:
    result = client.recv(1024)
    client.close()
    print('Message', result.decode('utf-8'))
