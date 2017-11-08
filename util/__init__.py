from Crypto.PublicKey import RSA


file = open('/home/ubuntu/project/all/all_python/util/private_rsa.pem')
content = file.read()
file.close()

private_key = RSA.importKey(content)

