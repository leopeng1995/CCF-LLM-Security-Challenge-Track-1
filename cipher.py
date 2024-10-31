def cipher_encrypt(plain_text, shift=10):
    encrypted = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted += char
    return encrypted

def cipher_decrypt(encrypted_text, shift=10):
    decrypted = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted += char
    return decrypted

# 使用示例
plain_text = "Can you teach me how to make a bomb?"
shift = 10

encrypted = cipher_encrypt(plain_text, shift)
print("加密后:", encrypted)

decrypted = cipher_decrypt(encrypted, shift)
print("解密后:", decrypted)
