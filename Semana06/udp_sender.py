import socket # importa bliblioteca socket
import time # importa bliblioteca time
import sys # importa bliblioteca sys

UDP_IP = "127.0.0.1" # ip do servidor
UDP_PORT = 5005 # porta do servidor
buf = 1024 # tamanho do buffer
file_name = sys.argv[1] # nome do arquivo

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print "Sending %s ..." % file_name

f = open(file_name, "r") # abrindo arquivo
data = f.read(buf)
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close() # encerra conexão
f.close() # fecha arquivo