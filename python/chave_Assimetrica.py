from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("=== CRIPTOGRAFIA ASSIMÉTRICA ===")

# Gerar chaves (privada e pública)
chave_privada = RSA.generate(2048)
chave_publica = chave_privada.publickey()

# Criar objeto de cifra para criptografar e descriptografar
cifra_publica = PKCS1_OAEP.new(chave_publica)
cifra_privada = PKCS1_OAEP.new(chave_privada)

mensagem2 = "Mensagem secreta com chaves diferentes"

# chave pública
mensagem_cripto = cifra_publica.encrypt(mensagem2.encode())

# chave privada
mensagem_decripto = cifra_privada.decrypt(mensagem_cripto).decode()

# resultado
print("Mensagem criptografada:", mensagem_cripto[:50], "...")  # mostra só o começo
print("Mensagem original:", mensagem_decripto)

print("\n-------------------------------------------\n")
