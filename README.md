# AES_socket_GUI
This repo contains 2 codes for encryption and decryption using AES.

Encryptor takes in message and key and port number and encrypts it. A socket client starts on local host with the input port.
Decryptor is a socket server that listens to open servers with given port number.
Encryptor sends encrypted message to decryptor that then decrypts its using the key that you will have to input.

Run in this order.
1.python3 decrptor.py
2.input port
3.python3 excryptor.py
4.input message, key
5.press encrypt
6.enter port
7.press send
8.then on decryptor enter key and press decrypt






