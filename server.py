import io
import socket
import ssl

from PIL import Image

sock = ssl.wrap_socket(socket.socket(), 'server.key', 'server.crt', True)
sock.bind(('localhost', 9093))
sock.listen(1)
many_bytes = 4096

while 1:
    conn, addr = sock.accept()
    print('Клиент подключен: ', addr[0])
    image_size_bytes = conn.recv(4)
    size = int.from_bytes(image_size_bytes, "big")
    data = b''
    while True:
        part = conn.recv(many_bytes)
        data += part
        if len(part) < many_bytes:
            break
    image = Image.open(io.BytesIO(data))
    image.show()
