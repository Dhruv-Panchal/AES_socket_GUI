'''
decryptor.py

This code runs a GUI for decrypting a message sent over localhost.

@author  Dhruv Panchal
@version 1.0, 04/04/19

'''

from tkinter import *
import socket 
from Crypto.Cipher import AES
from Crypto import Random               


class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("DECRYPTOR")        
        self.pack(fill=BOTH, expand=1)

        port_label = Label(self, text="Port")
        port_label.grid(row=0,column=0)
        port = Entry(self)
        port.grid(row=0,column=1)

        def start_server():
            port1 = port.get()
            port2=int(port1)

            listen_message= Label(self, text="Listening on port: "+str(port2))
            listen_message.grid(row=2, column=0, columnspan=3)

            s = socket.socket()             
            s.bind(('', port2))
            s.listen(5)            
            c, addr = s.accept()              

            cipher = c.recv(1024)
            iv=c.recv(9999)
            print(iv)
            
            message_received = Label(self, text ="Incoming ecnryted message: "+str(cipher))
            message_received.grid(row=4, column=0, columnspan=3,rowspan=2)

            key_label= Label(self, text = "Enter decryption key").grid(row=6, column=0)
            key_entry = Entry(self)
            key_entry.grid(row=6, column=1)

            def decrypt():
                key=key_entry.get()
                key += ((16 - len(key) % 16)*'X')
                decryption_suite = AES.new(key, AES.MODE_CFB, iv)
                plain_text = decryption_suite.decrypt(cipher)
                decrypt_message= Label(self, text = ("Your decrypted message is "+str(plain_text)))
                decrypt_message.grid(row=8, column=0, columnspan=3, rowspan=2)

            decrypt_button= Button(self, text="Decrypt", command=decrypt).grid(row=7, column=1)

        start_server_button = Button(self, text = "Start server", command = start_server).grid(row=1, column=1)

root = Tk()
root.geometry("600x300")

app = Window(root)
root.mainloop() 