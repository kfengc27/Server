# echo-server.py

import socket
import rsa

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
                        # the encrypted message can be decrypted
            # with ras.decrypt method and private key
            # decrypt method returns encoded byte string,
            # use decode method to convert it to string
            # public key cannot be used for decryption
            decMessage = rsa.decrypt(encMessage, privateKey).decode()
            if not data:
                break
            conn.sendall(data)