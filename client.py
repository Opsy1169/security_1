import io
import socket
import ssl

from PIL import Image

try:
    sock = ssl.wrap_socket(socket.socket())
    sock.connect(('localhost', 9093))
    print('Подключен')
    file = open("picture.png", 'rb').read()
    image = Image.open(io.BytesIO(file))
    bytes_len = len(file).to_bytes(4, byteorder='big')
    sock.send(bytes_len)
    sock.send(file)


except ConnectionRefusedError:
    print('Подключение не установлено')
