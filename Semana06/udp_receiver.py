import socket # importa a bliblioteca socket
import select # importa a bliblioteca select

UDP_IP = "127.0.0.1" # ip do servidor
IN_PORT = 5005 # porta do servidor
timeout = 3 # tempo de esgotamento

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print "File name:", data
        file_name = data.strip()

    f = open(file_name, 'wb') # abrindo arquivo

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            print "%s Finish!" % file_name # printa na tela o nome do arquivo que a escrita foi finalizada
            f.close() # fechando o arquivo
            break