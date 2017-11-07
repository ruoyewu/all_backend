import base64

from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

random_generator = Random.new().read

file = open('private_rsa.pem')
content = file.read()
file.close()

private_key = RSA.importKey(content)


def decrypt_rsa(secret):
    cipher = PKCS1_v1_5.new(private_key)
    text = cipher.decrypt(base64.b64decode(secret), random_generator)
    return text.decode()