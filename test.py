import base64
from time import time

from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5

random_generator = Random.new().read

print(int(time()))
public_key = open('public_rsa.pem').read()
private_key = open('private_rsa.pem').read()
public_key = RSA.importKey(public_key)
cipher = PKCS1_v1_5.new(public_key)
text = base64.b64encode(cipher.encrypt("I am nana".encode('ascii')))
# print(text.decode())
message = 'xviaum2UGVRtLBAeHVYUlft/82K2WoIFxDcKT4FnbRZ2ptEISX3D+yRQcuYg5DOQEeE3MeTbQ04r\ny436cpnqjeq6qPvVEVvejEmNoTosvwp0AVvMBaYNj6TkGL78GoleUcFxTA6p7w9SP1Vsc0bRcpi7\nF1qUfFXQBliUFY5UEaI='
private_key = RSA.importKey(private_key)
cipher = PKCS1_v1_5.new(private_key)
text = cipher.decrypt(base64.b64decode(message), random_generator)
print(text.decode())