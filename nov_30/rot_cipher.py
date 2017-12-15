def rot_cipher_encrypt(text, rotation):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rotated = alpha[rotation-1:]+alpha[0:rotation-1]
    cipher_table = "a".maketrans(alpha,rotated)
    return(text.translate(cipher_table))

def rot_cipher_decrypt(text, rotation):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rotated = alpha[rotation-1:]+alpha[0:rotation-1]
    cipher_table = "a".maketrans(rotated, alpha)
    return(text.translate(cipher_table))

def rot_cipher_interface():
    encrypt_decrypt = input('Would you like to encrypt or decrypt your message? ').lower()
    if encrypt_decrypt == 'encrypt':
        text, rotation = (input('What is your message? ').lower(), int(input('What rotation would you like? ')))
        print(rot_cipher_encrypt(text, rotation))
    else:
        text, rotation = (input('What is your message? ').lower(), int(input('What rotation would you like? ')))
        print(rot_cipher_decrypt(text, rotation))

    another_message = input('Do you have another message? y/n: ').lower()
    if another_message in 'yes':
        return rot_cipher_interface()
    else:
        return 'Translation ended.'

print(rot_cipher_interface())
