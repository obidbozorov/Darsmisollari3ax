from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_OAEP
def rsa_encrypt_decrypt():
    key = RSA.generate(2048)
    private_key = key.export_key('PEM')
    public_key = key.publickey().exportKey('PEM')
    #print(public_key)
    message = input('Ochiq matnni kiriting:')
    message = str.encode(message)
    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)
    print('Shifrma`lumot: {}'.format(encrypted_text))
    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text)
    print('Deshifrlangan ma`lumot : {}'.format(decrypted_text))
rsa_encrypt_decrypt()