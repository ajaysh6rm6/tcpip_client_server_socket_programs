import socket
import sys
import json
ob=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
ob.connect(('localhost',7070))

sample_data = {
	"name" : input("enter your name : "),
	"age" : int(input("enter your age : ")),
	"gender" : input("enter your gender : "),
	"address" : input("enter your address : "),
}

serialized_data = json.dumps(sample_data) #data serialized

# clientSocket.send(str.encode(sample_data))
ob.send(str.encode(serialized_data))

response_data = ob.recv(1024)
print("Response data from server : ", response_data.decode('utf-8'))

ob.close()