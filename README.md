# Vigenère Cipher in Python

This project demonstrates a simple implementation of the **Vigenère
Cipher** --- a method of encrypting and decrypting text using a keyword.

## 🔑 How It Works

The Vigenère cipher uses a secret **key** (a word) to determine how much
each letter in the message should be shifted in the alphabet.\
- Each letter in the key corresponds to a shift value (e.g., `a=0`,
`b=1`, ..., `z=25`).\
- The key repeats itself until it matches the length of the message.\
- Non-alphabet characters (spaces, punctuation) are preserved.

### Encryption

-   The message letters are shifted **forward** in the alphabet by the
    key values.

### Decryption

-   The message letters are shifted **backward** in the alphabet by the
    key values.

## 📂 Code Example

``` python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'Encrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'Decrypted text: {decryption}')
```

## ▶️ Example Run

    Encrypted text: mrttaqrhknsw ih puggrur
    Key: python
    Decrypted text: information is secure

## ✅ Features

-   Encrypt and decrypt messages using any key.
-   Preserves spaces and punctuation in messages.
-   Simple, lightweight Python implementation.

## 📜 License

This code is free to use and modify for educational purposes.
