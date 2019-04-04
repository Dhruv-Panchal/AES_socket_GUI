# AES_socket_GUI
This repo contains 2 codes for encryption and decryption using AES.

Encryptor takes in message and key and port number and encrypts it. A socket client starts on local host with the input port.
Decryptor is a socket server that listens to open servers with given port number.
Encryptor sends encrypted message to decryptor that then decrypts its using the key that you will have to input.

Run in this order.
1.python3 decrptor.py
2.input port
3.start server
4.python3 excryptor.py
5.input message, key
6.press encrypt
7.enter port
8.press send
9.then on decryptor enter key and press decrypt






