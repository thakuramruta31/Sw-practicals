import hashlib
password = input("Enter password: ")
password_hash = hashlib.sha256(password.encode()).hexdigest()
print("Password hash:", password_hash)

