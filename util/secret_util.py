from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

random_generator = Random.new().read


def decrypt_rsa(secret):
    with open('/home/ubuntu/project/all/all_test/all_python/util/private_rsa.pem') as file:
        private_key = RSA.importKey(file.read())
        cipher = PKCS1_v1_5.new(private_key)
        text = cipher.decrypt(base64.b64decode(secret), random_generator)
        return text.decode('utf-8')


if __name__ == "__main__":
    message = 'xviaum2UGVRtLBAeHVYUlft/82K2WoIFxDcKT4FnbRZ2ptEISX3D+yRQcuYg5DOQEeE3MeTbQ04r\ny436cpnqjeq6qPvVEVvejEmNoTosvwp0AVvMBaYNj6TkGL78GoleUcFxTA6p7w9SP1Vsc0bRcpi7\nF1qUfFXQBliUFY5UEaI='
    print(decrypt_rsa(message))