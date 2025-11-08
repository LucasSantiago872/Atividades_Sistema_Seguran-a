import hashlib

print("=== FUNÇÃO HASH ===")


texto = "senha"

hash_gerado = hashlib.sha256(texto.encode()).hexdigest()

print("Texto original:", texto)
print("Hash gerado:", hash_gerado)


texto2 = "senha"
hash2 = hashlib.sha256(texto2.encode()).hexdigest()

print("\nTexto alterado:", texto2)
print("Novo hash:", hash2)

print("\nFim do programa!")