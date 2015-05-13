import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 5050))
print "Web server running..."
server_sock.listen(10)

while True:
    client_sock, addr = server_sock.accept()
    print 'We have opened a socket!'
    output = client_sock.recv(100)  # these are the incoming headers
    output = output.split()
    print(output)

    if output[1] == ('/kittens'):
        with open('kittens.html') as f:
            output = f.read()
    else: output[4] == ('localhost:5050'):
        with open('file.html') as f:
            output = f.read()


    client_sock.send("HTTP/1.1 404 Not Found\n")
    client_sock.send("Content length: "+str(len(output)))
    client_sock.send("Content-Type: text/html\n\n")

    client_sock.send(output)
    client_sock.close()


