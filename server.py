import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 5050))
print "Web server running..."
server_sock.listen(10)

while True:
    client_sock, addr = server_sock.accept()
    print 'We have opened a socket!'
    request_headers = client_sock.recv(100)  # these are the incoming request_headers
    request_headers = request_headers.split()
    print(request_headers)

    if len(request_headers) < 2:
        continue
        
    # default status
    response_status = '200 OK'

    if request_headers[1] == '/kittens':
        with open('kittens.html') as f:
            response_body = f.read()
    elif request_headers[1] == '/':
        with open('file.html') as f:
            response_body = f.read()
    else:
        response_status = '404 Not Found'
        with open('file.html') as f:
            response_body = f.read()


    client_sock.send("HTTP/1.1 " + response_status + "\n")
    client_sock.send("Content length: "+str(len(response_body)))
    client_sock.send("Content-Type: text/html\n\n")

    client_sock.send(response_body)
    client_sock.close()
