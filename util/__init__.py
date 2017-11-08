from Crypto.PublicKey import RSA


# file = open('/Users/wuruoye/Documents/python/all_app/util/private_rsa.pem')
file = open('/home/ubuntu/project/all/all_python/util/private_rsa.pem')
content = file.read()
file.close()

private_key = RSA.importKey(content)

