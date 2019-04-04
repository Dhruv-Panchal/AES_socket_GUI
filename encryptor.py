'''
encryptor.py

This code runs a GUI for encrypting a message with a key 
using AES and send it to a decryptor over localhost.

@author  Dhruv Panchal
@version 1.0, 04/04/19

'''
 
 from tkinter import *
from Crypto.Cipher import AES
from Crypto import Random
import socket                


class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("ENCRYPTOR")
        self.pack(fill=BOTH, expand=1)

        message_label = Label(self, text="Enter Message").grid(row=0)
        message = Entry(self)

        key_label = Label(self, text="Enter Key").grid(row=1)        
        key = Entry(self)        

        port_label = Label(self, text ="Enter Port no").grid(row=5)
        port = Entry(self)         

        def encrypt():
            output_message = Label(self, text = ("Your message is  :"+ message.get()))
            output_message.grid(row=3, column=0, columnspan = 3)
            key1=key.get()
            key1 += ((16 - len(key1) % 16)*'X')
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(key1, AES.MODE_CFB, iv)
            cipher_txt = cipher.encrypt(message.get())
            output_cipher = Label(self, text = ("Your cipher message is : "+ str(cipher_txt)))
            output_cipher.grid(row=4, column=0, columnspan=3)

        show_button = Button(self, text="Encrypt", command=encrypt)  

        def send():
            s = socket.socket()
            port1 = port.get() 
            port_get = int(port1)
            s.connect(('127.0.0.1', port_get))
            conecting_message = Label(self, text = ("Connecting to 127.0.0.1 at port "+ str(port_get))) 
            conecting_message.grid(row=7, column=0, columnspan=3) 
            key1=key.get()
            key1 += ((16 - len(key1) % 16)*'X')
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(key1, AES.MODE_CFB, iv)
            cipher_txt = cipher.encrypt(message.get()) 
            print(iv)
            s.send(cipher_txt)
            s.send(iv)            

        send_button = Button(self, text = "Send", command=send)

        message.grid(row=0, column=1)
        key.grid(row=1, column=1)
        show_button.grid(row=2, column=1)
        port.grid(row=5, column=1)
        send_button.grid(row=6, column=1)        

root = Tk()
root.geometry("600x300")

app = Window(root)
root.mainloop()
