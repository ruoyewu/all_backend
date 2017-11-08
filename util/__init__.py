from Crypto.PublicKey import RSA


file = open('private_rsa.pem')
content = file.read()
file.close()

private_key = RSA.importKey(content)

