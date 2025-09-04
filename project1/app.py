# Given encrypted text
text = 'mrttaqrhknsw ih puggrur'

# Custom key to use for encryption/decryption
custom_key = 'python'


# Core function for Vigenère cipher
def vigenere(message, key, direction=1):
    """
    Implements the Vigenère cipher algorithm.
    - message: text to encrypt or decrypt
    - key: the secret word used to shift letters
    - direction: +1 for encryption, -1 for decryption
    """
    
    key_index = 0                           # Keeps track of the position in the key
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # Allowed characters for encryption
    final_message = ''                      # Store the result (encrypted/decrypted text)

    # Process each character in the message
    for char in message.lower():            # Convert message to lowercase for consistency

        # If the character is NOT a letter (e.g., space, punctuation), keep it unchanged
        if not char.isalpha():
            final_message += char

        else:
            # Get the current key character (cycles through key repeatedly)
            key_char = key[key_index % len(key)]
            key_index += 1                  # Move to the next position in the key

            # Find how much to shift using the key character
            offset = alphabet.index(key_char)

            # Find the position of the current message character
            index = alphabet.find(char)

            # Calculate new position depending on encryption (+1) or decryption (-1)
            new_index = (index + offset * direction) % len(alphabet)

            # Add the shifted letter to the final message
            final_message += alphabet[new_index]
    
    return final_message


# Helper function: Encrypt a message with the given key
def encrypt(message, key):
    return vigenere(message, key)           # Calls vigenere with direction=+1 (default)


# Helper function: Decrypt a message with the given key
def decrypt(message, key):
    return vigenere(message, key, -1)       # Calls vigenere with direction=-1


# --- Program Execution ---

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

# Decrypt the given encrypted text using the key
decryption = decrypt(text, custom_key)

print(f'\nDecrypted text: {decryption}\n')
