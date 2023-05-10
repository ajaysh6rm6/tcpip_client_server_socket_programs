import socket

ob=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
ob.connect(('localhost',7070))

ob.send(b'hi this is client')


response_data = ob.recv(1024)
print("Response data from server : ", response_data.decode('utf-8'))

ob.close()