
def rot_cipher_encrypt(text, rotation):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rotated = alpha[rotation-1:]+alpha[0:rotation-1]
    cipher_table = "".maketrans(alpha,rotated)
    return(text.translate(cipher_table))

def rot_cipher_decrypt(text, rotation):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rotated = alpha[rotation-1:]+alpha[0:rotation-1]
    cipher_table = "".maketrans(rotated, alpha)
    return(text.translate(cipher_table))

def moving_shift(s, shift):
    charlist = []
    for char in s:
        charlist.append(rot_cipher_encrypt(char,shift))
        shift += 1
    return ''.join(charlist)

def demoving_shift(s, shift):
    charlist = []
    for char in s:
        charlist.append(rot_cipher_decrypt(char,shift))
        shift += 1
    return ''.join(charlist)
