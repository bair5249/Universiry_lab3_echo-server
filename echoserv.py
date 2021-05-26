import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024).decode("utf-8")
    print(data)
    if not data:
        break
    conn.send(data.upper().encode("utf-8"))
    break
conn.close()
