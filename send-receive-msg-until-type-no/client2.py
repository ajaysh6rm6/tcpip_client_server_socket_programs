import socket
ob=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
ob.connect(('127.0.0.1',7070))
print("hello this is first client")

conn=True
while conn:
    msg=input("enter your msg : ")
    ob.send(msg.encode('utf-8'))
    if msg=='no':
        conn=False
        ob.close() 




