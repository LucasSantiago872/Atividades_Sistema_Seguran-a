# Importando bibliotecas necessárias
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import hashlib

print("=== CRIPTOGRAFIA SIMÉTRICA ===")

# Gerar chave
chave_simetrica = Fernet.generate_key()
fernet = Fernet(chave_simetrica)

mensagem = "Segurança é importante!"

# Criptografar
mensagem_criptografada = fernet.encrypt(mensagem.encode())

# Descriptografar
mensagem_original = fernet.decrypt(mensagem_criptografada).decode()

print("Chave:", chave_simetrica)
print("Mensagem criptografada:", mensagem_criptografada)
print("Mensagem original:", mensagem_original)
