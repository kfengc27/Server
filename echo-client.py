# echo-client.py

import socket
import rsa

# Source: https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)

# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method

passport = 'PO'

encMessage = rsa.encrypt(passport.encode(),
                         publicKey)

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello World")
    data = s.recv(1024)

print(f"Received {data!r}")