import socket
ob=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
ob.bind(('127.0.0.1',7070))
ob.listen(3)
clientobject,add=ob.accept()
print("server ready to accept connect")
print("connected with this address",add)

conn=True
while conn:
    gotmsg=clientobject.recv(1024)
    gotmsg.decode('utf-8')
    print(gotmsg)
    if len(gotmsg)==0:
        conn=False
        ob.close()



