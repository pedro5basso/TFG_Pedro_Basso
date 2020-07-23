# import socket

# mi_socket = socket.socket()
# mi_socket.connect(('localhost', 8000))

# mi_socket.send('Hola desde el cliente!')
# respuesta = mi_socket.recv(1024)

# print(respuesta)
# mi_socket.close()

from _thread import *
import socket,time
import webbrowser

def client():
    print("Thread starts")
    time.sleep(1)
    print("Thread connects")
    sock=socket.create_connection((socket.gethostname(),8888))
    #sock=socket.create_connection(("localhost",8888))
    print("Thread after connect")
    sock.sendall(b"Hello from client")
    sock.close()
    print("Thread ends")

serv=socket.socket()
serv.bind((socket.gethostname(),8888))
#serv.bind(("localhost",8888))
#serv.bind(("0.0.0.0",8888))
#serv.bind(("",8888))

serv.listen(10)
# while True:

start_new_thread(client,())
print("Before accept")

s,c=serv.accept()
print("After accept "+ str(c[1]))
url_ = 'localhost::'+str(c[1])
webbrowser.open(url_,new=2)
print("Message: "+s.recv(1024).decode("ASCII"))
s.close()
serv.close()